
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/stream/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "DataFormats/EcalDigi/interface/EcalDigiCollections.h"
#include "DataFormats/HcalDigi/interface/HcalDigiCollections.h"

#include "DataFormats/L1CaloTrigger/interface/L1CaloCollections.h"
#include "DataFormats/L1CaloTrigger/interface/L1CaloRegion.h"

#include <memory>
#include <string>

#include "PhysicsTools/TensorFlow/interface/TensorFlow.h"

using namespace std;

class pileupNetworkProducer : public edm::stream::EDProducer<>{
    public:
        explicit pileupNetworkProducer(const edm::ParameterSet&);
        ~pileupNetworkProducer() override;

        static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

    private:
        void produce(edm::Event&, const edm::EventSetup&) override;

        //void beginRun(edm::Run const&, edm::EventSetup const&) override;

        edm::EDGetTokenT<L1CaloRegionCollection> regionToken;
  
        tensorflow::Options options;
        tensorflow::MetaGraphDef* metaGraph;
        tensorflow::Session* session;
};

pileupNetworkProducer::pileupNetworkProducer(const edm::ParameterSet& iConfig)
{
    regionToken = consumes<L1CaloRegionCollection>(iConfig.getParameter<edm::InputTag>("regionSource"));

    // regionToken = consumes<L1CaloRegionCollection>(edm::InputTag("simCaloStage2Layer1Digis"));

    std::string pathToModel(std::getenv("CMSSW_BASE"));
    pathToModel.append(iConfig.getParameter<string>("pileupModelLocation"));
    produces<float>("pileupPrediction");

    metaGraph = tensorflow::loadMetaGraphDef(pathToModel);
    session = tensorflow::createSession(metaGraph, pathToModel, options);
}

pileupNetworkProducer::~pileupNetworkProducer()
{
    tensorflow::closeSession(session);
    session = nullptr;
    delete metaGraph;
    metaGraph = nullptr;
}

void pileupNetworkProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
    std::unique_ptr<float> pileupPrediction = std::make_unique<float>();

    edm::Handle<std::vector<L1CaloRegion>> regionCollection;
    iEvent.getByToken(regionToken, regionCollection);
    tensorflow::Tensor modelInput(tensorflow::DT_FLOAT, {1, 18, 14, 1});
    for(const L1CaloRegion& i: *regionCollection)
    {
        modelInput.tensor<float, 4>()(0, i.gctPhi(), i.gctEta()-4, 0) = i.et();
    }
    std::vector<tensorflow::Tensor> pileupOutput;
    tensorflow::run(session, {{"serving_default_input_1:0", modelInput}},{"StatefulPartitionedCall:0"}, &pileupOutput);
    *pileupPrediction = pileupOutput[0].matrix<float>()(0,0);

    iEvent.put(std::move(pileupPrediction), "pileupPrediction");
}

void pileupNetworkProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions)
{
    edm::ParameterSetDescription desc;
    desc.setUnknown();
    descriptions.addDefault(desc);
}

DEFINE_FWK_MODULE(pileupNetworkProducer);
