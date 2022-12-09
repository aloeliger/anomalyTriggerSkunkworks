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

#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "TTree.h"

#include <string>

class uGTModelNtuplizer : public edm::one::EDAnalyzer<edm::one::SharedResources>
{
    public:
        explicit uGTModelNtuplizer(const edm::ParameterSet&);
        ~uGTModelNtuplizer() override {};

    private:
        //void beginJob() override {};
        void analyze(const edm::Event&, const edm::EventSetup&) override;
        //void endJob() override {};

        edm::EDGetTokenT<float> anomalyToken;

        float anomalyScore;

        edm::Service<TFileService> theFileService;
        TTree* triggerTree;
        unsigned int run;
        unsigned int lumi;
        unsigned int evt;
};

uGTModelNtuplizer::uGTModelNtuplizer(const edm::ParameterSet& iConfig):
    anomalyToken( consumes< float >(iConfig.getParameter<edm::InputTag>("scoreSource")) )
{
    triggerTree = theFileService->make< TTree >("uGTModelOutput","custom uGT AD model emulator information");
    triggerTree -> Branch("run", &run);
    triggerTree -> Branch("lumi", &lumi);
    triggerTree -> Branch("evt", &evt);
    triggerTree -> Branch("uGTAnomalyScore", &anomalyScore);
}

void uGTModelNtuplizer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
    using namespace edm;

    edm::Handle< float > anomalyHandle;
    iEvent.getByToken(anomalyToken, anomalyHandle);

    run = iEvent.id().run();
    lumi = iEvent.id().luminosityBlock();
    evt = iEvent.id().event();

    anomalyScore = *anomalyHandle;

    //std::cout<<anomalyScore<<std::endl;

    triggerTree->Fill();
}

DEFINE_FWK_MODULE(uGTModelNtuplizer);