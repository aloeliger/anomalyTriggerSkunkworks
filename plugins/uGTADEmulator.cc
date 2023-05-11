//Quick class to emulate uGT AD emulation
//Andrew Loeliger
//THIS IS TEMPORARY, AND NOT IMPLEMENTED BY THE uGT AD GROUP, NOR IS IT THE OFFICIAL EMULATOR
//THIS SHOULD NOT END UP IN ANY PRODUCTION, ANY OFFICIAL PR, OR ACTUAL USAGE AS THE uGT EMULATOR

#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/stream/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "FWCore/MessageLogger/interface/MessageLogger.h"

#include "DataFormats/L1Trigger/interface/EGamma.h"
#include "DataFormats/L1Trigger/interface/Jet.h"
#include "DataFormats/L1Trigger/interface/Muon.h"
#include "DataFormats/L1Trigger/interface/EtSum.h"

#include "PhysicsTools/TensorFlow/interface/TensorFlow.h"
#include <string>

#include "TLorentzVector.h"

class uGTADEmulator : public edm::stream::EDProducer<> {
    public:
        explicit uGTADEmulator(const edm::ParameterSet&);
        ~uGTADEmulator () override;

        static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

    private:
        //void beginJob() override;
        void produce(edm::Event&, const edm::EventSetup&) override;
        //void endJob() override;

        void beginRun(edm::Run const&, edm::EventSetup const&) override {};
        void print(){};

        const edm::EDGetTokenT<l1t::EGammaBxCollection> egToken_;
        const edm::EDGetTokenT<l1t::JetBxCollection> jetToken_;
        const edm::EDGetTokenT<l1t::EtSumBxCollection> sumToken_;
        const edm::EDGetTokenT<l1t::MuonBxCollection> muonToken_;

        //Used for the auto-encoder/anomaly trigger emulation
        tensorflow::Options options;
        tensorflow::MetaGraphDef* metaGraph;
        tensorflow::Session* session;

        //I'm too lazy to figure out how to properly read the scaling .h5 in a c++/CMSSW context, 
        //so instead we're just going to do this this the hardcoded way.
        //I really should go figure out the c++ hdf5 API, but it looks very confusing
        const float muScaling[57] = {
            -3.133424, // MET X
            -0.7839487, // MET y
            0.0, // MET z
            -0.02530229, //EG 1 X
            0.05055978, // EG 1 Y
            -0.025991749, //EG 1 Z
            -0.024099816, //EG 2 X
            0.023683041, //EG 2 Y
            -0.20707601, //EG 2 Z
            -0.014315786, //EG 3 X
            0.014297869, //EG 3 Y
            0.22515944, //EG 3 Z
            -0.0101828985, //EG 4 x
            0.007027869, //EG 4 y
            -0.11460422, //EG 4 z
            -0.005505146, //mu 1 x
            -0.0014294093, //mu 1 y
            0.0076831942, // mu 1 z
            -0.00040483323, //mu 2 x
            9.667148e-05, //mu 2 y
            -0.0010912959, //mu 2 z
            -1.5248189e-05, // mu 3 x
            -1.23842765e-05, //mu 3 y
            -0.000106199615, //mu 3 z
            -8.719633e-06, //mu 4 x
            -3.239087e-06, //mu 4 y
            -3.709283e-05, //mu 4 z
            0.31337953,
            0.28660685,
            0.9132165,
            0.094598055,
            0.1676287,
            0.330552,
            0.026241334,
            0.11425084,
            0.5235183,
            -0.0027382032,
            0.06306178,
            -0.012866467,
            -0.008411425,
            0.03585502,
            0.25917953,
            -0.0050427443,
            0.01719672,
            0.024919424,
            -0.0022710038,
            0.010573137,
            0.053041805,
            -0.0007368658,
            0.0038358702,
            -0.0036463973,
            -0.00040903385,
            0.0016698425,
            0.014503392,
            -0.00015826985,
            0.00014445762,
            0.00040233973 
        };

        const float sigmaScaling[57] = {
            13.524995,
            13.614131,
            1.0,
            3.705061,
            3.6841729,
            12.948976,
            1.9719172,
            1.9631053,
            6.6368666,
            1.3317548,
            1.3292547,
            4.1831985,
            0.9436624,
            0.94023234,
            3.1721768,
            1.5605977,
            1.6877472,
            6.3551526,
            0.25569826,
            0.24334946,
            1.0024893,
            0.054684065,
            0.05461134,
            0.25722975,
            0.015053494,
            0.014544883,
            0.06906957,
            17.777935,
            17.814259,
            111.96128,
            11.781788,
            11.772849,
            80.822655,
            8.283245,
            8.270007,
            52.487015,
            5.902082,
            5.8872547,
            35.957718,
            4.138977,
            4.126431,
            23.350311,
            2.838793,
            2.820105,
            15.71434,
            1.8876066,
            1.8780094,
            9.973745,
            1.2076207,
            1.2017758,
            6.2937074,
            0.73680884,
            0.73302007,
            3.5713167,
            0.41814741,
            0.41986507,
            2.10403
        };
};

uGTADEmulator::uGTADEmulator (const edm::ParameterSet& iConfig):
    egToken_(consumes<l1t::EGammaBxCollection>(iConfig.getUntrackedParameter<edm::InputTag>("egToken"))),
    jetToken_(consumes<l1t::JetBxCollection>(iConfig.getUntrackedParameter<edm::InputTag>("jetToken"))),
    sumToken_(consumes<l1t::EtSumBxCollection>(iConfig.getUntrackedParameter<edm::InputTag>("sumToken"))),
    muonToken_(consumes<l1t::MuonBxCollection>(iConfig.getUntrackedParameter<edm::InputTag>("muonToken")))
{
    std::string fullPathToModel(std::getenv("CMSSW_BASE"));
    fullPathToModel.append(iConfig.getParameter<string>("anomalyModelLocation"));

    metaGraph = tensorflow::loadMetaGraphDef(fullPathToModel);
    session = tensorflow::createSession(metaGraph, fullPathToModel, options);

    produces<float>("uGTAnomalyScore");
}

uGTADEmulator::~uGTADEmulator()
{
    delete metaGraph;
    metaGraph = nullptr;
    tensorflow::closeSession(session);
    session = nullptr;
}

void uGTADEmulator::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
    using namespace edm;

    std::unique_ptr<float> uGTAnomalyScore(new float);

    edm::Handle<l1t::EGammaBxCollection> eg;
    edm::Handle<l1t::JetBxCollection> jet;
    edm::Handle<l1t::EtSumBxCollection> sums;
    edm::Handle<l1t::MuonBxCollection> muon;

    iEvent.getByToken(egToken_, eg);
    iEvent.getByToken(jetToken_, jet);
    iEvent.getByToken(sumToken_, sums);
    iEvent.getByToken(muonToken_, muon);

    tensorflow::Tensor modelInput(tensorflow::DT_FLOAT, {1, 57});

    //Okay. There's probably a more elegant way to handle this all than this...
    //But we're just going to loop over the individual collections
    //And if we don't get the right amount of objects, we just loop over the remaining
    //And fill those cells with 0's
    //We do this for all the objects that are input into the uGT model

    //TODO: get the scaling back in here properly.

    //start with sums
    for (int ibx = sums->getFirstBX(); ibx <= sums->getLastBX(); ++ibx)
    {
        //We only have to care about BX 0
        if (ibx != 0) continue;
        for(l1t::EtSumBxCollection::const_iterator it = sums->begin(ibx);
            it != sums->end(ibx);
            it++)
            {
                int type = static_cast<int>(it->getType());
                if (type!=2) continue; //we only really care about the MET, which is sum type 2   
                //We can get px py and pz directly from the canidate data format
                modelInput.tensor<float, 2>()(0, 0) = (it->px()-muScaling[0])/sigmaScaling[0];
                modelInput.tensor<float, 2>()(0, 1) = (it->py()-muScaling[1])/sigmaScaling[1];
                modelInput.tensor<float, 2>()(0, 2) = (it->pz()-muScaling[2])/sigmaScaling[2];      
                //std::cout<<"MET"<<std::endl;
                //std::cout<<(it->px()-muScaling[0])/sigmaScaling[0]<<std::endl;
                //std::cout<<(it->py()-muScaling[1])/sigmaScaling[1]<<std::endl;
                //std::cout<<(it->pz()-muScaling[2])/sigmaScaling[2]<<std::endl;
            }
    }
    //We will use this to keep track of where we are in the input tensor
    int indexTracker = 3;
    int nEGs = 0;
    for(int ibx = eg->getFirstBX(); ibx <= eg->getLastBX(); ++ibx)
    {
        if (ibx != 0) continue;
        for(l1t::EGammaBxCollection::const_iterator it = eg->begin(ibx);
            it != eg->end(ibx) && nEGs < 4;
            it++)
            {
                if(it->pt() > 0)
                {
                    nEGs++;
                    modelInput.tensor<float, 2>()(0, indexTracker+0) = (it->px()-muScaling[indexTracker+0])/sigmaScaling[indexTracker+0];
                    modelInput.tensor<float, 2>()(0, indexTracker+1) = (it->py()-muScaling[indexTracker+1])/sigmaScaling[indexTracker+1];
                    modelInput.tensor<float, 2>()(0, indexTracker+2) = (it->pz()-muScaling[indexTracker+2])/sigmaScaling[indexTracker+2];
                    //std::cout<<"EG"<<std::endl;
                    //std::cout<<(it->px()-muScaling[indexTracker+0])/sigmaScaling[indexTracker+0]<<std::endl;
                    //std::cout<<(it->py()-muScaling[indexTracker+1])/sigmaScaling[indexTracker+1]<<std::endl;
                    //std::cout<<(it->pz()-muScaling[indexTracker+2])/sigmaScaling[indexTracker+2]<<std::endl;
                    indexTracker+=3;    
                }
            }
    }
    //If we have less than 4 nEGs
    //explicitly fill remaining indices with 0's
    if(nEGs < 4)
    {
        while (nEGs < 4)
        {
            nEGs++;
            modelInput.tensor<float, 2>()(0, indexTracker+0) = 0.0;
            modelInput.tensor<float, 2>()(0, indexTracker+1) = 0.0;
            modelInput.tensor<float, 2>()(0, indexTracker+2) = 0.0;
            indexTracker+=3;
        }
    }

    //We're now moving on to the muons
    //These start at index 14
    indexTracker = 15;
    int nMuons = 0;
    for (int ibx = muon->getFirstBX(); ibx <= muon->getLastBX(); ++ibx)
    {
        if (ibx != 0) continue;
        for(l1t::MuonBxCollection::const_iterator it = muon->begin(ibx);
            it != muon->end(ibx) && nMuons < 4;
            it++)
            {
                if(it->pt() > 0)
                {
                    nMuons++;
                    modelInput.tensor<float, 2>()(0, indexTracker+0) = (it->px()-muScaling[indexTracker+0])/sigmaScaling[indexTracker+0];
                    modelInput.tensor<float, 2>()(0, indexTracker+1) = (it->py()-muScaling[indexTracker+1])/sigmaScaling[indexTracker+1];
                    modelInput.tensor<float, 2>()(0, indexTracker+2) = (it->pz()-muScaling[indexTracker+2])/sigmaScaling[indexTracker+2];
                    ///std::cout<<"Muon"<<std::endl;
                    ///std::cout<<(it->px()-muScaling[indexTracker+0])/sigmaScaling[indexTracker+0]<<std::endl;
                    ///std::cout<<(it->py()-muScaling[indexTracker+1])/sigmaScaling[indexTracker+1]<<std::endl;
                    ///std::cout<<(it->pz()-muScaling[indexTracker+2])/sigmaScaling[indexTracker+2]<<std::endl;
                    indexTracker+=3;
                    //std::cout<<"mu px: "<<it->px()<<std::endl; 
                    //std::cout<<"mu py: "<<it->py()<<std::endl;
                    //std::cout<<"mu pz: "<<it->pz()<<std::endl; 
                }
            }
    }   

    if(nMuons < 4)
    {
        while (nMuons < 4)
        {
            nMuons++;
            modelInput.tensor<float, 2>()(0, indexTracker+0) = 0.0;
            modelInput.tensor<float, 2>()(0, indexTracker+1) = 0.0;
            modelInput.tensor<float, 2>()(0, indexTracker+2) = 0.0;
            indexTracker+=3;
        }
    }

    indexTracker = 27;
    int nJets = 0;
    for(int ibx = jet->getFirstBX(); ibx <= jet->getLastBX(); ++ibx)
    {
        if(ibx != 0) continue;
        for(l1t::JetBxCollection::const_iterator it = jet->begin(ibx);
            it != jet->end(ibx) && nJets < 10;
            it++)
            {
                if(it->pt() > 0)
                {
                    nJets++;
                    modelInput.tensor<float, 2>()(0, indexTracker+0) = (it->px()-muScaling[indexTracker+0])/sigmaScaling[indexTracker+0];
                    modelInput.tensor<float, 2>()(0, indexTracker+1) = (it->py()-muScaling[indexTracker+1])/sigmaScaling[indexTracker+1];
                    modelInput.tensor<float, 2>()(0, indexTracker+2) = (it->pz()-muScaling[indexTracker+2])/sigmaScaling[indexTracker+2];
                    //std::cout<<"Jet"<<std::endl;
                    //std::cout<<(it->px()-muScaling[indexTracker+0])/sigmaScaling[indexTracker+0]<<std::endl;
                    //std::cout<<(it->py()-muScaling[indexTracker+1])/sigmaScaling[indexTracker+1]<<std::endl;
                    //std::cout<<(it->pz()-muScaling[indexTracker+2])/sigmaScaling[indexTracker+2]<<std::endl;
                    indexTracker+=3;
                }
            }
    }

    if(nJets < 10)
    {
        while (nJets < 10)
        {
            nJets++;
            modelInput.tensor<float, 2>()(0, indexTracker+0) = 0.0;
            modelInput.tensor<float, 2>()(0, indexTracker+1) = 0.0;
            modelInput.tensor<float, 2>()(0, indexTracker+2) = 0.0;
            indexTracker+=3;
        }
    }

    //std::cout<<"< ";
    //for(int i = 0; i<57; ++i) std::cout<<modelInput.tensor<float, 2>()(0, i)<<", ";
    //std::cout<<">"<<std::endl;

    std::vector<tensorflow::Tensor> anomalyOutput;
    tensorflow::run(session, {{"serving_default_input_1:0", modelInput}}, {"StatefulPartitionedCall:0"}, &anomalyOutput);

    //std::cout<<"< ";
    //for (int i = 0; i<13; ++i) std::cout<<anomalyOutput[0].matrix<float>()(0, i)<<", ";
    //std::cout<<">"<<std::endl;
    *uGTAnomalyScore = 0.0;
    for (int i = 0; i < 13; ++i) *uGTAnomalyScore += (anomalyOutput[0].matrix<float>()(0, i) * anomalyOutput[0].matrix<float>()(0, i));

    //std::cout<<"anomalyScore: "<<*uGTAnomalyScore<<std::endl;

    iEvent.put(std::move(uGTAnomalyScore), "uGTAnomalyScore");
}

void uGTADEmulator::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(uGTADEmulator);
