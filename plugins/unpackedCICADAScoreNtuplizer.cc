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
  void fillBX(float& bx_score, const edm::Handle<l1t::CICADABxCollection>& vector, const int bx);

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

  fillBX(BXMinusTwoScore, cicadaScores, -2);
  fillBX(BXMinusOneScore, cicadaScores, -1);
  fillBX(BXZeroScore, cicadaScores, 0);
  fillBX(BXOneScore, cicadaScores, 1);
  fillBX(BXTwoScore, cicadaScores, 2);

  theTree->Fill();
}

void unpackedCICADAScoreNtuplizer::fillBX(float& bx_score, const edm::Handle<l1t::CICADABxCollection>& vector, const int bx){
  if(vector->isEmpty(bx))
	       bx_score = 0.0;
  else
    bx_score = vector->at(bx, 0);
}

DEFINE_FWK_MODULE(unpackedCICADAScoreNtuplizer);
