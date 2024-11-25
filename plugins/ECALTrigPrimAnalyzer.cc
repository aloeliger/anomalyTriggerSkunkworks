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

#include "DataFormats/EcalDigi/interface/EcalDigiCollections.h"
#include "DataFormats/HcalDigi/interface/HcalDigiCollections.h"


class ECALTrigPrimAnalyzer : public edm::one::EDAnalyzer<> {
public:
  explicit ECALTrigPrimAnalyzer(const edm::ParameterSet&);

  //static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

private:
  void beginJob() override {};
  void analyze(const edm::Event&, const edm::EventSetup&) override;
  void endJob() override {};

  edm::EDGetTokenT<EcalTrigPrimDigiCollection> ecalTPSource;
  edm::Service<TFileService> theFileService;
  TTree* theTree;

  std::vector<int> trigPrimIEta;
  std::vector<int> trigPrimIPhi;
  std::vector<int> trigPrimET;
};
  
ECALTrigPrimAnalyzer::ECALTrigPrimAnalyzer(const edm::ParameterSet& iConfig):
  ecalTPSource(consumes<EcalTrigPrimDigiCollection>(iConfig.getParameter<edm::InputTag>("ecalTpSource")))
{
  //usesResource("TFileService");

  theTree = theFileService->make<TTree>("ECALTriggerPrimitives","ECAl Trigger Primitives");
  theTree->Branch("trigPrimIEta", &trigPrimIEta);
  theTree->Branch("trigPrimIPhi", &trigPrimIPhi);
  theTree->Branch("trigPrimET", &trigPrimET);
}

void ECALTrigPrimAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  edm::Handle<EcalTrigPrimDigiCollection> EcalTrigPrims;
  iEvent.getByToken(ecalTPSource, EcalTrigPrims);

  trigPrimIEta.clear();
  trigPrimIPhi.clear();
  trigPrimET.clear();

  for(const auto& ecalTp: *EcalTrigPrims) {
    trigPrimIEta.push_back(ecalTp.id().ieta());
    trigPrimIPhi.push_back(ecalTp.id().iphi());
    trigPrimET.push_back(ecalTp.compressedEt());
  }

  theTree->Fill();
}

DEFINE_FWK_MODULE(ECALTrigPrimAnalyzer);
