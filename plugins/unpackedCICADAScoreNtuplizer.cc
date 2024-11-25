#include <memory>

#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "FWCore/ServiceRegistry/interface/Service.h"

#include "DataFormats/L1CaloTrigger/interface/CICADA.h"

#include "TTree.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

class unpackedCICADAScoreNtuplizer : public edm::one::EDAnalyzer< edm::one::SharedResources >
{
public:
  explicit unpackedCICADAScoreNtuplizer(const edm::ParameterSet&);
  ~unpackedCICADAScoreNtuplizer() override = default;

private:
  void beginJob() override {};
  void analyze(const edm::Event&, const edm::EventSetup&) override;
  void endJob() override {};

  edm::EDGetTokenT<l1t::CICADABxCollection> cicadaToken;
  float BXMinusTwoScore;
  float BXMinusOneScore;
  float BXZeroScore;
  float BXOneScore;
  float BXTwoScore;

  edm::Service<TFileService> theFileService;
  TTree* theTree;
};

unpackedCICADAScoreNtuplizer::unpackedCICADAScoreNtuplizer(const edm::ParameterSet& iConfig):
  cicadaToken(consumes<l1t::CICADABxCollection>(iConfig.getParameter<edm::InputTag>("unpackedCICADAScoreSrc")))
{
  usesResource("TFileService");

  theTree = theFileService->make<TTree>("UnpackedCICADAScores", "CICADA scores unpacked over 5BX");
  theTree->Branch("BX_Minus_Two_Score", &BXMinusTwoScore);
  theTree->Branch("BX_Minus_One_Score", &BXMinusOneScore);
  theTree->Branch("BX_Zero_Score", &BXZeroScore);
  theTree->Branch("BX_One_Score", &BXOneScore);
  theTree->Branch("BX_Two_Score", &BXTwoScore);
}

void unpackedCICADAScoreNtuplizer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  edm::Handle<l1t::CICADABxCollection> cicadaScores;
  iEvent.getByToken(cicadaToken, cicadaScores);

  BXMinusTwoScore = cicadaScores->at(-2, 0);
  BXMinusOneScore = cicadaScores->at(-1, 0);
  BXZeroScore = cicadaScores->at(0, 0);
  BXOneScore = cicadaScores->at(1, 0);
  BXTwoScore = cicadaScores->at(2, 0);

  theTree->Fill();
}

DEFINE_FWK_MODULE(unpackedCICADAScoreNtuplizer);
