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

#include "DataFormats/EcalDigi/interface/EcalDigiCollections.h"
#include "DataFormats/HcalDigi/interface/HcalDigiCollections.h"
#include "DataFormats/L1CaloTrigger/interface/L1CaloCollections.h"
#include "DataFormats/L1CaloTrigger/interface/L1CaloRegion.h"
#include "DataFormats/L1CaloTrigger/interface/CICADA.h"
#include "DataFormats/VertexReco/interface/Vertex.h"

#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "TTree.h"

#include <string>

class L1TCaloSummaryTestNtuplizer : public edm::one::EDAnalyzer< edm::one::SharedResources >
{
public:
  explicit L1TCaloSummaryTestNtuplizer(const edm::ParameterSet&);
  ~L1TCaloSummaryTestNtuplizer() override;

private:
  void beginJob() override {};
  void analyze(const edm::Event&, const edm::EventSetup&) override;
  void endJob() override {};
  
  //Just some stuff to let us actually ntuplize everything
  edm::EDGetTokenT< l1t::CICADABxCollection > anomalyToken;

  edm::EDGetTokenT<std::vector<reco::Vertex>> vertexToken;
  float anomalyScore;

  edm::EDGetTokenT<EcalTrigPrimDigiCollection> ecalTPSource;
  edm::EDGetTokenT<HcalTrigPrimDigiCollection> hcalTPSource;
  unsigned short int regional_ecalTPData[18][14];
  unsigned short int regional_hcalTPData[18][14];

  unsigned short int modelInput[18][14];



  //Stuff pulled from the emulator region collection
  edm::EDGetTokenT<L1CaloRegionCollection> emuRegionsToken;
  bool tauBits[18][14];
  bool egBits[18][14];

  edm::Service<TFileService> theFileService;
  TTree* triggerTree;
  unsigned int run;
  unsigned int lumi;
  unsigned int evt;
  bool includePUInfo;
  int npv = 0;
  
  bool verboseDebug;

  std::string outputScoreName;
};

L1TCaloSummaryTestNtuplizer::L1TCaloSummaryTestNtuplizer(const edm::ParameterSet& iConfig):
  anomalyToken( consumes< l1t::CICADABxCollection >(iConfig.getParameter<edm::InputTag>("scoreSource")) ),
  vertexToken( consumes<std::vector<reco::Vertex>>(iConfig.getParameter<edm::InputTag>("pvSrc"))),
  ecalTPSource(consumes<EcalTrigPrimDigiCollection>(iConfig.getParameter<edm::InputTag>("ecalToken"))),
  hcalTPSource(consumes<HcalTrigPrimDigiCollection>(iConfig.getParameter<edm::InputTag>("hcalToken"))),
  emuRegionsToken(consumes<L1CaloRegionCollection>(iConfig.getParameter<edm::InputTag>("emuRegionsToken")))
{
  usesResource("TFileService");
  verboseDebug  = iConfig.exists("verboseDebug") ? iConfig.getParameter<bool>("verboseDebug"): false;
  includePUInfo = iConfig.exists("includePUInfo") ? iConfig.getParameter<bool>("includePUInfo"): false;
  outputScoreName = iConfig.exists("outputScoreName") ? iConfig.getParameter<std::string>("outputScoreName"): "anomalyScore";

  //We need to reserve space for the vectors so that the tree 
  //Properly spaces out the entries.

  //create some ntuplization brickwork
  triggerTree = theFileService->make< TTree >("L1TCaloSummaryOutput","(emulator) L1CaloSummary information");
  triggerTree -> Branch("run",  &run);
  triggerTree -> Branch("lumi", &lumi);
  triggerTree -> Branch("evt",  &evt);
  if(includePUInfo) triggerTree -> Branch("npv",  &npv);
  triggerTree -> Branch(outputScoreName.c_str(), &anomalyScore);
  // triggerTree -> Branch("ecalRegionalTPs", &regional_ecalTPData, "ecalRegionalTPs[18][14]/s");
  // triggerTree -> Branch("hcalRegionalTPs", &regional_hcalTPData, "hcalRegionalTPs[18][14]/s");
  triggerTree -> Branch("modelInput", &modelInput, "modelInput[18][14]/s");
  // triggerTree -> Branch("tauBits", &tauBits, "tauBits[18][14]/O");
  // triggerTree -> Branch("egBits", &egBits, "tauBits[18][14]/O");
}

L1TCaloSummaryTestNtuplizer::~L1TCaloSummaryTestNtuplizer()

{
}

void L1TCaloSummaryTestNtuplizer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  using namespace edm;

  //little bit wordy, but should function?
  edm::Handle< l1t::CICADABxCollection > anomalyHandle;
  edm::Handle< std::vector< reco::Vertex > > vertexHandle;
  iEvent.getByToken(anomalyToken, anomalyHandle);

  run  = iEvent.id().run();
  lumi = iEvent.id().luminosityBlock();
  evt  = iEvent.id().event();

  anomalyScore = anomalyHandle->at(0, 0);  

  //figure out primary vertices if that's a thing we want to include
  if(includePUInfo)
    {
      iEvent.getByToken(vertexToken, vertexHandle);
      npv  = vertexHandle->size();
    }

  //Sort out TP information and print it
  edm::Handle<EcalTrigPrimDigiCollection> ecalTPs;
  edm::Handle<HcalTrigPrimDigiCollection> hcalTPs;

  for (int i = 0; i < 18; i++)
    for (int j = 0; j < 14; j++)
      {
	      regional_ecalTPData[i][j] = 0;
	      regional_hcalTPData[i][j] = 0;
	      modelInput[i][j] = 0;
      }


  iEvent.getByToken(ecalTPSource, ecalTPs);
  iEvent.getByToken(hcalTPSource, hcalTPs);
	
  //process ecal TPs into usable form
  for(const auto& ecalTP: *ecalTPs)
    {
      int phi = 0;
      int eta = 0;
      uint32_t et = 0;
	    
      phi = ecalTP.id().iphi();
      eta = ecalTP.id().ieta();

      if(std::abs(eta) > 28) continue;

      phi = (phi+2) % 72;
      eta < 0? eta = 28-std::abs(eta): eta+=27;

      ecalTP.compressedEt() > 0xFF? et=0xFF : et = ecalTP.compressedEt();

      regional_ecalTPData[phi/4][eta/4] += et;
    }
  //Do the same for HCAL
  for(const auto& hcalTP: *hcalTPs)
    {
      int phi = 0;
      int eta = 0;
      uint32_t et = 0;
	    
      phi = hcalTP.id().iphi();
      eta = hcalTP.id().ieta();

      if(std::abs(eta) > 28) continue;

      phi = (phi+2) % 72;
      eta < 0? eta = 28-std::abs(eta): eta+=27;

      hcalTP.SOI_compressedEt() > 0xFF? et=0xFF : et = hcalTP.SOI_compressedEt();

      regional_hcalTPData[phi/4][eta/4] += et;
    }

  //Let's sort out the tau bits.
  edm::Handle<std::vector<L1CaloRegion>> emuRegions;
  iEvent.getByToken(emuRegionsToken, emuRegions);
  for(const L1CaloRegion& theRegion: *emuRegions)
    {
      tauBits[theRegion.gctPhi()][theRegion.gctEta()-4] = theRegion.tauVeto();
      egBits[theRegion.gctPhi()][theRegion.gctEta()-4] = theRegion.overFlow(); //This is the EG bit, as define in the L1 Calo Region return ((m_data >> 10) & 0x1) != 0;, 12th bit in the data, which is where this gets stored in the region summary 0x00000400
      modelInput[theRegion.gctPhi()][theRegion.gctEta()-4] = theRegion.et();
    }
  
  //Do event reporting if requested
  if(verboseDebug)
    {
      std::cout<<"Run: "<<run<<std::endl;
      std::cout<<"Lumi: "<<lumi<<std::endl;
      std::cout<<"Event: "<<evt<<std::endl;
      // std::cout<<"Anomaly Score: "<<anomalyScore<<std::endl;
      // std::cout<<"Bit accurate anomaly score: "<<bitAccurateAnomalyScore<<std::endl;
      if(includePUInfo) std::cout<<"NPV: "<<npv<<std::endl;
      std::cout<<"Regional ECAL TPs (No Processing!) at L1TCalosummarytestntuplizer"<<std::endl;
      for(int i =0; i < 18; i++)
      {
        for(int j = 0; j<14; j++)
          {
            std::cout<<regional_ecalTPData[i][j]<<" ";
          }
        std::cout<<std::endl;
      }
      std::cout<<"Regional HCAL TPs (No Processing!) at L1TCalosummarytestntuplizer"<<std::endl;
      for(int i =0; i < 18; i++)
      {
        for(int j = 0; j<14; j++)
          {
            std::cout<<regional_hcalTPData[i][j]<<" ";
          }
        std::cout<<std::endl;
      }
      std::cout<<"Naive summed regional TPs at L1TCalosummarytestntuplizer"<<std::endl;
      for(int i =0; i < 18; i++)
      {
        for(int j = 0; j<14; j++)
          {
            std::cout<<regional_ecalTPData[i][j]+regional_hcalTPData[i][j]<<" ";
          }
        std::cout<<std::endl;
      }
      std::cout<<"Tau bit array from the emulator"<<std::endl;
      for(int i=0; i<18; i++)
      {
        for(int j=0;j<14;j++)
          std::cout<<tauBits[i][j]<<" ";
        std::cout<<std::endl;
      }
      std::cout<<"EG bit array from the emulator"<<std::endl;
      for(int i=0; i<18; i++)
      {
        for(int j=0;j<14;j++)
          std::cout<<egBits[i][j]<<" ";
        std::cout<<std::endl;
      }
      std::cout<<"Direct model input"<<std::endl;
      for(int i =0; i<18; i++)
      {
        for(int j=0; j<14; j++)
          std::cout<<modelInput[i][j]<<" ";
        std::cout<<std::endl;
      }
    }

  triggerTree->Fill();
}

DEFINE_FWK_MODULE(L1TCaloSummaryTestNtuplizer);
