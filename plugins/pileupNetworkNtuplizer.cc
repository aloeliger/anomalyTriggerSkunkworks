#include <memory>
#include <iostream>

#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "FWCore/ServiceRegistry/interface/Service.h"

#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "TTree.h"

#include <string>

class pileupNetworkNtuplizer : public edm::one::EDAnalyzer<edm::one::SharedResources>
{
    public:
        explicit pileupNetworkNtuplizer(const edm::ParameterSet&);
        ~pileupNetworkNtuplizer() override {};
    
    private:
        void analyze(const edm::Event&, const edm::EventSetup&) override;

        edm::EDGetTokenT<float> pileupToken;

        float pileupPrediction;
        edm::Service<TFileService> theFileService;
        TTree* pileupTree;
};

pileupNetworkNtuplizer::pileupNetworkNtuplizer(const edm::ParameterSet& iConfig):
    pileupToken(consumes<float>(iConfig.getParameter<edm::InputTag>("pileupSource")))
{
    usesResource("TFileService");
    pileupTree = theFileService->make<TTree>("pileupTree", "Tree for the pileup prediction network output");
    pileupTree->Branch("pileupPrediction", &pileupPrediction);
}

void pileupNetworkNtuplizer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
    using namespace edm;
    
    Handle<float> pileupHandle;
    iEvent.getByToken(pileupToken, pileupHandle);

    pileupPrediction = *pileupHandle;

    pileupTree->Fill();
}

DEFINE_FWK_MODULE(pileupNetworkNtuplizer);