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

class HCALTrigPrimAnalyzer : public edm::one::EDAnalyzer<> {
public:
  explicit HCALTrigPrimAnalyzer(const edm::ParameterSet&);

private:
  void beginJob() override {};
  void analyze(const edm::Event&, const edm::EventSetup&) override;
  void endJob() override {};

  edm::EDGetTokenT<HcalTrigPrimDigiCollection> hcalTPSource;
  edm::Service<TFileService> theFileService;
  TTree* theTree;

  std::vector<int> trigPrimIEta;
  std::vector<int> trigPrimIPhi;
  std::vector<int> trigPrimET;
};

HCALTrigPrimAnalyzer::HCALTrigPrimAnalyzer(const edm::ParameterSet& iConfig):
  hcalTPSource(consumes<HcalTrigPrimDigiCollection>(iConfig.getParameter<edm::InputTag>("hcalTpSource")))
{

  theTree = theFileService->make<TTree>("HCALTriggerPrimitives", "HCAL Trigger Primitives");
  theTree->Branch("trigPrimIEta", &trigPrimIEta);
  theTree->Branch("trigPrimIPhi", &trigPrimIPhi);
  theTree->Branch("trigPrimET", &trigPrimET);
}

void HCALTrigPrimAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  edm::Handle<HcalTrigPrimDigiCollection> HcalTrigPrims;
  iEvent.getByToken(hcalTPSource, HcalTrigPrims);

  trigPrimIEta.clear();
  trigPrimIPhi.clear();
  trigPrimET.clear();

  for(const auto& hcalTp: *HcalTrigPrims) {
    trigPrimIEta.push_back(hcalTp.id().ieta());
    trigPrimIPhi.push_back(hcalTp.id().iphi());
    trigPrimET.push_back(hcalTp.SOI_compressedEt());
  }

  theTree->Fill();  
}


DEFINE_FWK_MODULE(HCALTrigPrimAnalyzer);
