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
  float anomalyScore;

  edm::Service<TFileService> theFileService;
  TTree* triggerTree;
};

L1TCaloSummaryTestNtuplizer::L1TCaloSummaryTestNtuplizer(const edm::ParameterSet& iConfig):
  anomalyToken( consumes< float >(iConfig.getParameter<edm::InputTag>("scoreSource")) )
{
  //create some ntuplization brickwork
  triggerTree = theFileService->make< TTree >("L1TCaloSummaryOutput","(emulator) L1CaloSummary informatione");
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
  iEvent.getByToken(anomalyToken, anomalyHandle);
  anomalyScore = *anomalyHandle;

  triggerTree->Fill();

}

DEFINE_FWK_MODULE(L1TCaloSummaryTestNtuplizer);
