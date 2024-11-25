#include <memory>

#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "FWCore/ServiceRegistry/interface/Service.h"

#include "DataFormats/L1TGlobal/interface/GlobalAlgBlk.h"
#include "DataFormats/L1TGlobal/interface/GlobalExtBlk.h"

#include "TTree.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

class unprefirableInformationNtuplizer : public edm::one::EDAnalyzer< edm::one::SharedResources >
{
public:
  explicit unprefirableInformationNtuplizer(const edm::ParameterSet&);
  ~unprefirableInformationNtuplizer() override = default;

private:
  void beginJob() override {};
  void analyze(const edm::Event&, const edm::EventSetup&) override;
  void endJob() override {};
  
  edm::EDGetTokenT<GlobalExtBlkBxCollection> unprefirableToken;

  edm::Service<TFileService> theFileService;
  TTree* theTree;
  bool isUnprefirable = false;
};

unprefirableInformationNtuplizer::unprefirableInformationNtuplizer(const edm::ParameterSet& iConfig):
  unprefirableToken(consumes<GlobalExtBlkBxCollection>(iConfig.getParameter<edm::InputTag>("GlobalExtSrc")))
{
  usesResource("TFileService");
  theTree = theFileService->make<TTree>("UnprefirableInfo", "Unprefirable Info");
  theTree->Branch("isUnprefirable", &isUnprefirable);
}

void unprefirableInformationNtuplizer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  edm::Handle<GlobalExtBlkBxCollection> unprefirableHandle;
  iEvent.getByToken(unprefirableToken, unprefirableHandle);
  if(unprefirableHandle.isValid()) {
    if(unprefirableHandle->size() != 0) {
      isUnprefirable = unprefirableHandle->at(0, 0).getExternalDecision(GlobalExtBlk::maxExternalConditions-1);
    }
    else {
      std::cout<<"Empty external block"<<std::endl;
    }
  }
  else {
    std::cout<<"Invalid external block handle"<<std::endl;    
  }

  theTree->Fill();
}

DEFINE_FWK_MODULE(unprefirableInformationNtuplizer);
