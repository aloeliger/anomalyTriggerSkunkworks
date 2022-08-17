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

#include "DataFormats/VertexReco/interface/Vertex.h"

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "TTree.h"

#include <string>

class L1TCaloSummaryTestNtuplizer : public edm::one::EDAnalyzer< edm::one::SharedResources >
{
public:
  explicit L1TCaloSummaryTestNtuplizer(const edm::ParameterSet&);
  ~L1TCaloSummaryTestNtuplizer() override;

private:
  void beginJob() override {};
  void analyze(const edm::Event&, const edm::EventSetup&) override;
  void endJob() override {};
  
  //Just some stuff to let us actually ntuplize everything
  edm::EDGetTokenT< float > anomalyToken;
  edm::EDGetTokenT<std::vector<reco::Vertex>> vertexToken;
  float anomalyScore;

  edm::Service<TFileService> theFileService;
  TTree* triggerTree;
  unsigned int run;
  unsigned int lumi;
  unsigned int evt;
  int npv;
};

L1TCaloSummaryTestNtuplizer::L1TCaloSummaryTestNtuplizer(const edm::ParameterSet& iConfig):
  anomalyToken( consumes< float >(iConfig.getParameter<edm::InputTag>("scoreSource")) ),
  vertexToken( consumes<std::vector<reco::Vertex>>(iConfig.getParameter<edm::InputTag>("pvSrc")))
{
  //create some ntuplization brickwork
  triggerTree = theFileService->make< TTree >("L1TCaloSummaryOutput","(emulator) L1CaloSummary informatione");
  triggerTree -> Branch("run",  &run);
  triggerTree -> Branch("lumi", &lumi);
  triggerTree -> Branch("evt",  &evt);
  triggerTree -> Branch("npv",  &npv);
  triggerTree -> Branch("anomalyScore", &anomalyScore);
}

L1TCaloSummaryTestNtuplizer::~L1TCaloSummaryTestNtuplizer()

{
}

void L1TCaloSummaryTestNtuplizer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  using namespace edm;
  
  //little bit wordy, but should function?
  edm::Handle< float > anomalyHandle;
  edm::Handle<std::vector<reco::Vertex>> vertexHandle;
  iEvent.getByToken(anomalyToken, anomalyHandle);
  iEvent.getByToken(vertexToken, vertexHandle);
  
  run  = iEvent.id().run();
  lumi = iEvent.id().luminosityBlock();
  evt  = iEvent.id().event();
  //npv  = iEvent.NPV();
  npv  = vertexHandle->size();

  anomalyScore = *anomalyHandle;

  triggerTree->Fill();

}

DEFINE_FWK_MODULE(L1TCaloSummaryTestNtuplizer);
