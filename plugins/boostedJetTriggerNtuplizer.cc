// system include files
#include <memory>
#include <iostream>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "FWCore/ServiceRegistry/interface/Service.h"

#include "DataFormats/L1Trigger/interface/L1JetParticle.h"
#include "DataFormats/L1Trigger/interface/L1JetParticleFwd.h"

#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "TTree.h"

#include <string>

class boostedJetTriggerNtuplizer : public edm::one::EDAnalyzer< edm::one::SharedResources >
{
public:
  explicit boostedJetTriggerNtuplizer(const edm::ParameterSet&);
  ~boostedJetTriggerNtuplizer() override;

private:
  void beginJob() override {};
  void analyze(const edm::Event&, const edm::EventSetup&) override;
  void endJob() override{};

  edm::EDGetTokenT< l1extra::L1JetParticleCollection > boostedJetCollection;
  bool verboseDebug;
  

  edm::Service<TFileService> theFileService;
  TTree* boostedJetTree;
  
  int numberOfJets;
  bool triggerFires;
  
  std::vector<float> jetPts;
  std::vector<float> jetEtas;
  std::vector<float> jetPhis;

  unsigned int run;
  unsigned int lumi;
  unsigned int evt;
};

boostedJetTriggerNtuplizer::boostedJetTriggerNtuplizer(const edm::ParameterSet& iConfig):
  boostedJetCollection( consumes< l1extra::L1JetParticleCollection >(iConfig.getParameter<edm::InputTag>("boostedJetCollection")) )
{
  usesResource("TFileService");
  verboseDebug  = iConfig.exists("verboseDebug") ? iConfig.getParameter<bool>("verboseDebug"): false;

  boostedJetTree = theFileService->make< TTree >("boostedJetTrigger", "Output of the L1TCaloSummary boosted jet process");
  boostedJetTree -> Branch("run", &run);
  boostedJetTree -> Branch("lumi", &lumi);
  boostedJetTree -> Branch("evt", &evt);
  boostedJetTree -> Branch("numberOfJets", &numberOfJets);
  boostedJetTree -> Branch("triggerFires", &triggerFires);
  boostedJetTree -> Branch("jetPts", &jetPts);
  boostedJetTree -> Branch("jetEtas", &jetEtas);
  boostedJetTree -> Branch("jetPhis", &jetPhis);
}

boostedJetTriggerNtuplizer::~boostedJetTriggerNtuplizer()
{
}

void boostedJetTriggerNtuplizer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  using namespace edm;

  run  = iEvent.id().run();
  lumi = iEvent.id().luminosityBlock();
  evt  = iEvent.id().event();

  edm::Handle<l1extra::L1JetParticleCollection> boostedJetCollectionHandle;
  iEvent.getByToken(boostedJetCollection, boostedJetCollectionHandle);

  triggerFires = false;

  numberOfJets = boostedJetCollectionHandle->size();
  for(const l1extra::L1JetParticle& theJet: *boostedJetCollectionHandle)
    {
      //If highest pt jet is above 120 then the trigger fires
      if(theJet.pt() > 120.0) triggerFires=true;
      jetPts.push_back(theJet.pt());
      jetEtas.push_back(theJet.eta());
      jetPhis.push_back(theJet.phi());
    }
  
  if (verboseDebug)
    {
      std::cout<<"Number of boosted jets: "<<numberOfJets<<std::endl;
      std::cout<<"boosted jet trigger fired? "<<triggerFires<<std::endl;
    }

  boostedJetTree->Fill();
  jetPts.clear();
  jetEtas.clear();
  jetPhis.clear();
  triggerFires=false;
}

DEFINE_FWK_MODULE(boostedJetTriggerNtuplizer);
