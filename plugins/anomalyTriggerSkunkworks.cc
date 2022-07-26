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

  edm::EDGetTokenT<L1CaloRegionCollection> regionCollection;
  edm::EDGetTokenT<EcalTrigPrimDigiCollection> ecalCollection;
  edm::EDGetTokenT<HcalTrigPrimDigiCollection> hcalCollection;

  // ----------member data ---------------------------
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
}

anomalyTriggerSkunkworks::~anomalyTriggerSkunkworks() {
  // do anything here that needs to be done at desctruction time
  // (e.g. close files, deallocate resources etc.)
  //
  // please remove this method altogether if it would be left empty
}

//
// member functions
//

// ------------ method called for each event  ------------
void anomalyTriggerSkunkworks::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup) {
  using namespace edm;

}

// ------------ method called once each job just before starting event loop  ------------
void anomalyTriggerSkunkworks::beginJob() {
  // please remove this method if not needed
  std::cout<<"beginning anomaly trigger skunkworks"<<std::endl;
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
