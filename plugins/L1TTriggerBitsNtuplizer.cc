//system include files
#include <memory>
#include <iostream>

//user includes
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/Framework/interface/ConsumesCollector.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "FWCore/Utilities/interface/ESGetToken.h"
#include "FWCore/ServiceRegistry/interface/Service.h"

#include "CondFormats/DataRecord/interface/L1TUtmTriggerMenuRcd.h"
#include "CondFormats/L1TObjects/interface/L1TUtmTriggerMenu.h"

#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "DataFormats/L1TGlobal/interface/GlobalAlgBlk.h"

#include "TTree.h"

#include <string>

class L1TTriggerBitsNtuplizer : public edm::one::EDAnalyzer< edm::one::SharedResources >
{
public:
  explicit L1TTriggerBitsNtuplizer(const edm::ParameterSet&);
  ~L1TTriggerBitsNtuplizer() override;

private: 
  void beginJob() override {};
  void analyze(const edm::Event&, const edm::EventSetup&) override;
  void endJob() override{};

  edm::Service<TFileService> theFileService;
  TTree* l1BitsTree;
                  
  edm::ESGetToken<L1TUtmTriggerMenu, L1TUtmTriggerMenuRcd> L1TUtmTriggerMenuEventToken;
  const L1TUtmTriggerMenu* l1GtMenu;
  const std::map<std::string, L1TUtmAlgorithm>* algorithmMap;
  std::map<std::string, bool> triggerResults;

  bool verboseDebug;

  // access to the results block from uGT
  edm::EDGetTokenT< BXVector<GlobalAlgBlk> > gtAlgBlkToken;
  edm::Handle< BXVector<GlobalAlgBlk> > gtAlgBlkHandle;
};

L1TTriggerBitsNtuplizer::L1TTriggerBitsNtuplizer(const edm::ParameterSet& iConfig):
  gtAlgBlkToken( consumes< BXVector<GlobalAlgBlk> >(iConfig.getParameter< edm::InputTag >("gtResults")) )
{
  L1TUtmTriggerMenuEventToken = consumesCollector().esConsumes<L1TUtmTriggerMenu, L1TUtmTriggerMenuRcd>();
  
  verboseDebug = iConfig.exists("verboseDebug") ? iConfig.getParameter<bool>("verboseDebug"): false;

  //REALLY need a better way of doing this
  triggerResults ={
    {"L1_SingleMu20", false},
    {"L1_SingleJet120", false},
    {"L1_SingleJet60", false},
  };

  //setup the bits tree
  l1BitsTree = theFileService->make<TTree>("L1TTriggerBits","Emulator L1 Trigger Bits");
  l1BitsTree->Branch("L1_SingleMu20", &triggerResults["L1_SingleMu20"], "L1_SingleMu20/O");
  l1BitsTree->Branch("L1_SingleJet120", &triggerResults["L1_SingleJet120"], "L1_SingleJet120/O");
  l1BitsTree->Branch("L1_SingleJet60", &triggerResults["L1_SingleJet60"], "L1_SingleJet60/O");
  
}

L1TTriggerBitsNtuplizer::~L1TTriggerBitsNtuplizer()
{
}

void L1TTriggerBitsNtuplizer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  using namespace edm;
  //Start the laborious process of accessing the in-event L1 Menu
  auto menuRcd = iSetup.get<L1TUtmTriggerMenuRcd>();
  l1GtMenu = &menuRcd.get(L1TUtmTriggerMenuEventToken);
  algorithmMap = &(l1GtMenu->getAlgorithmMap());

  //REALLY need a better way of doing this
  triggerResults ={
    {"L1_SingleMu20", false},
    {"L1_SingleJet120", false},
    {"L1_SingleJet60", false},
  };


  iEvent.getByToken(gtAlgBlkToken, gtAlgBlkHandle);
  //First we make sure we even have a valid AlgBlk, otherwise we are going nowhere fast
  if(gtAlgBlkHandle.isValid())
    {
      //Want BX0? Event the l1GtUtils doesn't seem sure about this?
      std::vector<GlobalAlgBlk>::const_iterator algBlk = gtAlgBlkHandle->begin(0);
      if(algBlk != gtAlgBlkHandle->end(0))
	{
	  //Now let's see if we can loop over the bits in the path and see if we can print out
	  //The names of the L1 seeds
	  for (std::map<std::string, L1TUtmAlgorithm>::const_iterator itAlgo = algorithmMap->begin();
	       itAlgo != algorithmMap->end();
	       itAlgo++) 
	    {
	      std::string algName = itAlgo->first;
	      int algBit = itAlgo->second.getIndex();
	      bool initialDecision = algBlk->getAlgoDecisionInitial(algBit);
	      bool intermDecision = algBlk->getAlgoDecisionInterm(algBit);
	      bool decisionFinal = algBlk->getAlgoDecisionFinal(algBit);
	      //Not sure if this is dangerous. 
	      //Sure seems like it should be
	      //But I don't want to write specific configuring things
	      //Or do individual cases.
	      try {triggerResults[algName] = decisionFinal;}
	      catch(std::range_error){}
	      if (verboseDebug)
		{
		  std::cout<<"L1 Path: "<<algName<<" Bit: "<<algBit<<" Initial Decision: "<<initialDecision<<" Interm Decision: "<<intermDecision<<" Final Decision: "<<decisionFinal<<std::endl;
		}
	    }

	}
      else
	{
	  std::cout<<"algBlk was found to be the end of the BX vector (empty)!"<<std::endl;
	}
    }
  else
    {
      std::cout<<"Found Invalid AlgBlk!"<<std::endl;
    }
  l1BitsTree->Fill();
}

DEFINE_FWK_MODULE(L1TTriggerBitsNtuplizer);
