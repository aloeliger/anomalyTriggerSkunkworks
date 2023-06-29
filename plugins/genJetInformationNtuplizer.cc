// system included files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "FWCore/ServiceRegistry/interface/Service.h"

#include "DataFormats/JetReco/interface/GenJet.h"

#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "TTree.h"

class genJetInformationNtuplizer : public edm::one::EDAnalyzer< edm::one::SharedResources >
{
    public:
        explicit genJetInformationNtuplizer(const edm::ParameterSet&);
        ~genJetInformationNtuplizer() override {};

    private:
        void beginJob() override {};
        void analyze(const edm::Event&, const edm::EventSetup&) override;
        void endJob() override {};

        edm::EDGetTokenT< std::vector<reco::GenJet> > genJetToken;

        edm::Service<TFileService> theFileService;

        unsigned int nObjects;
        std::vector<double> ptVector;
        std::vector<double> etaVector;
        std::vector<double> phiVector;
        std::vector<double> massVector;
        std::vector<int> chargeVector;

        TTree* genJetTree;
};

genJetInformationNtuplizer::genJetInformationNtuplizer(const edm::ParameterSet& iConfig):
    genJetToken(consumes<std::vector<reco::GenJet>>(iConfig.getParameter<edm::InputTag>("genJetSrc")))
{
    usesResource("TFileService");

    genJetTree = theFileService->make< TTree >("genJetInformation","MC Truth Jet Information");
    genJetTree -> Branch("genJetNObjects", &nObjects);
    genJetTree -> Branch("genJetPt", &ptVector);
    genJetTree -> Branch("genJetEta", &etaVector);
    genJetTree -> Branch("genJetPhi", &phiVector);
    genJetTree -> Branch("genJetMass", &massVector);
    genJetTree -> Branch("genJetCharge", &chargeVector);
}

void genJetInformationNtuplizer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
    edm::Handle<std::vector<reco::GenJet>> genJetHandle;
    iEvent.getByToken(genJetToken, genJetHandle);

    nObjects = 0;

    for(auto theJet = genJetHandle->begin(); theJet != genJetHandle->end(); theJet++)
    {
        nObjects++;
        ptVector.push_back(theJet->pt());
        etaVector.push_back(theJet->eta());
        phiVector.push_back(theJet->phi());
        massVector.push_back(theJet->mass());
        chargeVector.push_back(theJet->charge());
    }

    genJetTree->Fill();
    ptVector.clear();
    etaVector.clear();
    phiVector.clear();
    massVector.clear();
    chargeVector.clear();
}

DEFINE_FWK_MODULE(genJetInformationNtuplizer);