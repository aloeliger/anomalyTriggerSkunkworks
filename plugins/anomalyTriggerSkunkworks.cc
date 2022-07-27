// -*- C++ -*-
//
// Package:    L1Trigger/anomalyTriggerSkunkworks
// Class:      anomalyTriggerSkunkworks
//
/**\class anomalyTriggerSkunkworks anomalyTriggerSkunkworks.cc L1Trigger/anomalyTriggerSkunkworks/plugins/anomalyTriggerSkunkworks.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Andrew Loeliger
//         Created:  Thu, 21 Jul 2022 18:53:51 GMT
//
//

// system include files
#include <memory>
#include <iostream>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"

#include "DataFormats/EcalDigi/interface/EcalDigiCollections.h"
#include "DataFormats/HcalDigi/interface/HcalDigiCollections.h"

#include "DataFormats/L1CaloTrigger/interface/L1CaloCollections.h"
#include "DataFormats/L1CaloTrigger/interface/L1CaloRegion.h"

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "PhysicsTools/TensorFlow/interface/TensorFlow.h"

#include "TTree.h"

#include <string>
//
// class declaration
//

// If the analyzer does not use TFileService, please remove
// the template argument to the base class so the class inherits
// from  edm::one::EDAnalyzer<>
// This will improve performance in multithreaded jobs.

class anomalyTriggerSkunkworks : public edm::one::EDAnalyzer<edm::one::SharedResources> {
public:
  explicit anomalyTriggerSkunkworks(const edm::ParameterSet&);
  ~anomalyTriggerSkunkworks() override;

  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

private:
  void beginJob() override;
  void analyze(const edm::Event&, const edm::EventSetup&) override;
  void endJob() override;

  // ----------member data ---------------------------
  edm::EDGetTokenT<L1CaloRegionCollection> regionCollection;
  edm::EDGetTokenT<EcalTrigPrimDigiCollection> ecalCollection;
  edm::EDGetTokenT<HcalTrigPrimDigiCollection> hcalCollection;
  
  //store phi on the first index, eta on the second
  std::vector< std::vector< unsigned > > * GCTEtaPhiETMap;

  //file service
  edm::Service<TFileService> theFileService;
  TTree* triggerTree;
  //tensorflow implements
  tensorflow::MetaGraphDef* metaGraph;
  tensorflow::Session* session;
};

//
// constants, enums and typedefs
//

//
// static data member definitions
//

//
// constructors and destructor
//
anomalyTriggerSkunkworks::anomalyTriggerSkunkworks(const edm::ParameterSet& iConfig):
  regionCollection(consumes< L1CaloRegionCollection >(iConfig.getParameter< edm::InputTag >("regionalInformation"))),
  ecalCollection(consumes< EcalTrigPrimDigiCollection >(iConfig.getParameter< edm::InputTag >("ecalDigis"))),
  hcalCollection(consumes< HcalTrigPrimDigiCollection >(iConfig.getParameter< edm::InputTag >("hcalDigis")))
{
  //now do what ever initialization is needed

  //Okay, this requires some explanation
  //This is going to be our primary ieta/iphi calo region trigger primitive
  //storage device. We need to make this a vector of vectors for 2D storage
  //And we reserve their size for speed, and hopefully to allow these
  //to be of fixed size so that we can write this to a ROOT file.
  GCTEtaPhiETMap = new std::vector< std::vector< unsigned > >;
  int etaDivisions = 14; //14 eta gct/region divisions from 4 to 17
  int phiDivisions = 18; //18 phi gct/region divisions from 0 to 17
  GCTEtaPhiETMap->reserve(phiDivisions); 
  //this reserves the top level eta divisions,
  //now we need to go through and create the vectors along phi
  //and store the actual et/tp values.
  for(int i = 0; i<phiDivisions; ++i)
    {
      std::vector< unsigned > blankVector;
      GCTEtaPhiETMap->push_back(blankVector);
      (*GCTEtaPhiETMap)[i].reserve(etaDivisions);
    }

  //Here's where we get to be INCREDIBLY thankful for the actual computer scientists who
  //work on CMS instead of physicists
  //We load the model on analyzer start
  //char* pathToModel = std::getenv("CMSSW_BASE")+ (char*)"anomalyTriggerSkunkworks/data/qmodel/"
  std::cout<<"Loading model..."<<std::endl;
  
  std::string pathToModel(std::getenv("CMSSW_BASE"));
  pathToModel.append("/src/L1Trigger/anomalyTriggerSkunkworks/data/qmodel/");

  std::cout<<"Reading model from: "<<pathToModel<<" ..."<<std::endl;

  metaGraph = tensorflow::loadMetaGraph(pathToModel);
  //run a tensorflow session here
  session = tensorflow::createSession(metaGraph, pathToModel);

  //TTree for storage of digi information and anomaly scores for validation
  triggerTree = theFileService->make< TTree >("triggerTPInfo", "(emulator) Calo L1 TP information");
  triggerTree -> Branch("GCTEtaPhiETMap", GCTEtaPhiETMap);
}

anomalyTriggerSkunkworks::~anomalyTriggerSkunkworks() {
  // do anything here that needs to be done at desctruction time
  // (e.g. close files, deallocate resources etc.)
  //
  // please remove this method altogether if it would be left empty
  
  //delete the map
  delete GCTEtaPhiETMap;
}

//
// member functions
//

// ------------ method called for each event  ------------
void anomalyTriggerSkunkworks::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup) {
  using namespace edm;
  
  //Okay. Our first job is to go through and make sure we have a record
  //of the regional digies and hcal/ecal digis. We'll save those,
  //to a file to do comparisons on in traditional tf/keras environments later
  //to make sure nothing has gone haywire.
  //We can also compare the code readout digis to traditional modules that do this stuff
  //and hopefully confirm that the input reading procedure is correct
  
  edm::Handle< std::vector< L1CaloRegion > > regionHandle;
  iEvent.getByToken(regionCollection, regionHandle);

  edm::Handle< EcalTrigPrimDigiCollection > ecalTPHandle;
  iEvent.getByToken(ecalCollection, ecalTPHandle);
  
  edm::Handle< HcalTrigPrimDigiCollection > hcalTPHandle;
  iEvent.getByToken(hcalCollection, hcalTPHandle);

  //std::cout<<(*regionHandle).size()<<std::endl;
  //std::cout<<(*ecalTPHandle).size()<<std::endl; //<- this works with source "l1tCaloLayer1Digis"
  //std::cout<<(*hcalTPHandle).size()<<std::endl; //<- this works with source "l1tCaloLayer1Digis"
  
  //We need to create a tensorflow tensor too to serve as input into the model scoring.
  tensorflow::Tensor modelInput(tensorflow::DT_FLOAT, { 1, 18, 14, 1});
  
  for(std::vector< L1CaloRegion >::const_iterator regionIt = regionHandle->begin();
      regionIt != regionHandle->end();
      ++regionIt)
    {
      L1CaloRegion theRegion = *regionIt;
      /*
      std::cout<<"*************************"<<std::endl;
      std::cout<<"regionIt.gctEta(): "<<(*regionIt).gctEta()<<std::endl;
      std::cout<<"regionIt.gctPhi(): "<<(*regionIt).gctPhi()<<std::endl;
      std::cout<<"regionIt.et(): "<<(*regionIt).et()<<std::endl;
      std::cout<<"*************************"<<std::endl;
      */
      //We *always* get 252 regions reporting, so we don't need to worry about clearing the vectors for every event
      //We will just overwrite them
      (*GCTEtaPhiETMap)[theRegion.gctPhi()][theRegion.gctEta()-4] = theRegion.et(); //we take iEta 4 off of either end to account for the removed forward regions(?)
      //modelInput.matrix< float >()(0, theRegion.gctPhi(), theRegion.gctEta()-4, 0) = theRegion.et();
      
    }

  //Of course, the other big important part of the skunkworks will be to actually get the 
  //c++ to interface with the tf/keras model, which is where this gets a bit messy
  //Okay. How do we do this?
  

  //Fill our tree and get out of here
  triggerTree->Fill();
}

// ------------ method called once each job just before starting event loop  ------------
void anomalyTriggerSkunkworks::beginJob() {
  // please remove this method if not needed
  std::cout<<"Initializing anomaly trigger skunkworks..."<<std::endl;
}

// ------------ method called once each job just after ending the event loop  ------------
void anomalyTriggerSkunkworks::endJob() {
  // please remove this method if not needed
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void anomalyTriggerSkunkworks::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);

  //Specify that only 'tracks' is allowed
  //To use, remove the default given above and uncomment below
  //ParameterSetDescription desc;
  //desc.addUntracked<edm::InputTag>("tracks","ctfWithMaterialTracks");
  //descriptions.addWithDefaultLabel(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(anomalyTriggerSkunkworks);
