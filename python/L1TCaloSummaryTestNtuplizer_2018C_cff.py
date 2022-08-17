import FWCore.ParameterSet.Config as cms

process = cms.Process("L1TCaloSummaryTest")

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.RawToDigi_Data_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '112X_dataRun2_v7', '')

process.load('L1Trigger.Configuration.CaloTriggerPrimitives_cff')

process.load('EventFilter.L1TXRawToDigi.caloLayer1Stage2Digis_cfi')

process.load('L1Trigger.L1TCaloLayer1.simCaloStage2Layer1Digis_cfi')
process.simCaloStage2Layer1Digis.ecalToken = cms.InputTag("l1tCaloLayer1Digis")
process.simCaloStage2Layer1Digis.hcalToken = cms.InputTag("l1tCaloLayer1Digis")

process.load('L1Trigger.L1TCaloLayer1.uct2016EmulatorDigis_cfi')

process.load("L1Trigger.Run3Ntuplizer.l1BoostedJetStudies_cfi")

process.load("L1Trigger.anomalyTriggerSkunkworks.L1TCaloSummaryTestNtuplizer_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(100000) )
#process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(10000) )

process.MessageLogger.cerr.FwkReport.reportEvery = 100

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
                                #'/store/data/Run2018C/ZeroBias/MINIAOD/PromptReco-v3/000/319/826/00000/C07242E4-8A8B-E811-BF44-FA163E9626F3.root', #45868 events
                                #'/store/data/Run2018C/ZeroBias/MINIAOD/PromptReco-v3/000/319/830/00000/78531080-928B-E811-9C4C-02163E014ABA.root', #15988 events
                                #'/store/data/Run2018C/ZeroBias/MINIAOD/PromptReco-v3/000/319/835/00000/C0F9273D-9D8B-E811-9EC0-FA163E56FC29.root', #12293 events
                                #'/store/data/Run2018C/ZeroBias/MINIAOD/PromptReco-v3/000/319/838/00000/DA8749B2-A48B-E811-8595-FA163ED8CFD8.root', #20407 events
                                '/store/data/Run2018C/ZeroBias/MINIAOD/PromptReco-v3/000/319/910/00000/3A309C66-258D-E811-8115-FA163E942E01.root',
                                '/store/data/Run2018C/ZeroBias/MINIAOD/PromptReco-v3/000/319/910/00000/3430C82C-2A8D-E811-ADF5-FA163ECF8ABB.root',
                                '/store/data/Run2018C/ZeroBias/MINIAOD/PromptReco-v3/000/319/910/00000/18A59B3F-318D-E811-B3F1-FA163E8D7B5B.root',
                                '/store/data/Run2018C/ZeroBias/MINIAOD/PromptReco-v3/000/319/910/00000/22366BEC-378D-E811-9D53-FA163EA6C8AF.root',
                                '/store/data/Run2018C/ZeroBias/MINIAOD/PromptReco-v3/000/319/910/00000/BC897FE1-278D-E811-B65F-FA163E0C6510.root',
                                '/store/data/Run2018C/ZeroBias/MINIAOD/PromptReco-v3/000/319/910/00000/A602DFFC-2B8D-E811-8053-FA163EED2B0A.root',
                                '/store/data/Run2018C/ZeroBias/MINIAOD/PromptReco-v3/000/319/910/00000/BEEB3F7B-2D8D-E811-8E86-FA163E605311.root',
                                '/store/data/Run2018C/ZeroBias/MINIAOD/PromptReco-v3/000/319/910/00000/7254AEC4-268D-E811-B799-FA163EAB8290.root',
                                '/store/data/Run2018C/ZeroBias/MINIAOD/PromptReco-v3/000/319/910/00000/BE9E7270-438D-E811-B7CA-FA163E96DBF1.root',
                                '/store/data/Run2018C/ZeroBias/MINIAOD/PromptReco-v3/000/319/910/00000/7CD504D8-548D-E811-955D-FA163E2F358B.root',
                                '/store/data/Run2018C/ZeroBias/MINIAOD/PromptReco-v3/000/319/910/00000/72830FB8-208D-E811-83B3-02163E013E9C.root',
                                '/store/data/Run2018C/ZeroBias/MINIAOD/PromptReco-v3/000/319/910/00000/94F1CF87-288D-E811-BBFB-FA163EA57599.root',
                                '/store/data/Run2018C/ZeroBias/MINIAOD/PromptReco-v3/000/319/910/00000/F20A73F9-238D-E811-8B0C-FA163ED10FA7.root',
                                '/store/data/Run2018C/ZeroBias/MINIAOD/PromptReco-v3/000/319/910/00000/0CFECDA3-2F8D-E811-87D6-FA163EF6611E.root',
                                '/store/data/Run2018C/ZeroBias/MINIAOD/PromptReco-v3/000/319/910/00000/4271D931-338D-E811-9125-02163E010C16.root',
                            ),
                            secondaryFileNames = cms.untracked.vstring(
                                #'/store/data/Run2018C/ZeroBias/RAW/v1/000/319/826/00000/D02DDFC9-028A-E811-B730-02163E00CDEC.root',
                                #'/store/data/Run2018C/ZeroBias/RAW/v1/000/319/830/00000/C05EBE88-028A-E811-9E1C-FA163EDFA1F1.root',
                                #'/store/data/Run2018C/ZeroBias/RAW/v1/000/319/835/00000/FE4F885D-168A-E811-8A67-FA163E46E568.root',
                                #'/store/data/Run2018C/ZeroBias/RAW/v1/000/319/838/00000/EC0B0241-198A-E811-A957-FA163E9CA336.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/8CB1B3A0-028B-E811-B43A-FA163E170C07.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/80234205-048B-E811-B9BC-02163E01A048.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/9A816C65-068B-E811-AD62-FA163E22408B.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/94524260-068B-E811-9ABA-FA163E04BE64.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/8C02A63C-058B-E811-9B45-FA163E1E8D3A.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/3619F6A5-038B-E811-97F9-02163E012DC5.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/1470C0AB-088B-E811-AEDE-FA163E22408B.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/8203FB63-0A8B-E811-B747-FA163E1AB09F.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/9EB016BC-098B-E811-8F6E-FA163E792D18.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/72CB1130-0B8B-E811-9488-02163E017F0F.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/F2C1A6DB-0D8B-E811-BF6B-FA163E1A09D0.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/287E10BC-0D8B-E811-9687-FA163ED190E5.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/725BE6E4-0F8B-E811-8961-FA163EDE2360.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/F2D3BDF6-0F8B-E811-89CE-FA163E82CF22.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/BE83225B-118B-E811-8BD5-FA163E0E2C94.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/F622E6BE-128B-E811-8B29-FA163ECBD601.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/98586644-128B-E811-90D7-02163E010BD4.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/9CFD73DD-178B-E811-98BD-FA163E5897CC.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/A85FD365-1C8B-E811-B2A0-FA163E0A33E8.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/D493FF93-1B8B-E811-BA38-02163E01A05B.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/8E82D6DD-1F8B-E811-87B3-FA163E283070.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/F4425CDC-1F8B-E811-9FB1-FA163E517117.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/0AE0ED3B-218B-E811-AEC5-FA163E74B46D.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/9E8B338C-1E8B-E811-BDD2-FA163E22AFFD.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/C4F1B254-228B-E811-87E2-FA163EE08300.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/08521033-248B-E811-B760-FA163EA45FDA.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/0C5946DB-2B8B-E811-9604-FA163EDE9AD6.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/1E158DF8-2B8B-E811-A55A-FA163E086D3D.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/4CE4AB9F-2C8B-E811-89EF-02163E01A082.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/B02653C4-2D8B-E811-8EAE-FA163E94857D.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/F2385B26-2E8B-E811-9005-FA163E1D8104.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/D2DA123B-308B-E811-8C05-FA163E6EBF69.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/56F12EE9-2F8B-E811-B490-02163E019FC3.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/0260F0B5-318B-E811-A228-FA163E06C52E.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/AC60D7BB-308B-E811-8CD2-FA163E87213F.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/8A6C6FAE-348B-E811-849C-FA163EE0B264.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/54BECAAF-348B-E811-AF72-02163E01A0AB.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/CA983151-368B-E811-B7A5-FA163EAFF551.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/8AF5DEC8-038B-E811-9F69-FA163E066FBC.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/C68A43DE-038B-E811-982B-FA163EE723F8.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/8260B74F-058B-E811-87FF-02163E01A0CF.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/BAC99E70-068B-E811-BF51-02163E010CC6.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/7CF02B9C-058B-E811-BD10-FA163EC732FD.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/2895FAB1-078B-E811-8B49-FA163E1E616C.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/9085E432-088B-E811-8585-FA163E200265.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/7E6B3D4E-0B8B-E811-8D64-02163E019FF9.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/6E1524C2-0C8B-E811-92BB-FA163E08D4C1.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/D0DA514A-0C8B-E811-9E24-FA163EAE0640.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/C87087BE-108B-E811-909D-FA163EB98709.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/267CFBE2-138B-E811-86BA-FA163E6F0B5B.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/BE3119E0-148B-E811-9F02-FA163E3559D6.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/C8F57E4B-168B-E811-B032-FA163E687348.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/362E3C4C-168B-E811-9B34-FA163EFC186C.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/F0A014AB-168B-E811-9C1C-FA163E337911.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/04B4847C-178B-E811-8968-02163E019F75.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/EADBDD24-178B-E811-893F-FA163E5819DC.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/06659C6D-1A8B-E811-8C9B-FA163EFAEF42.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/D6BDACC5-1A8B-E811-B07B-FA163E4830E6.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/C6E4B138-1D8B-E811-8FCC-FA163EDFE462.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/32E85543-1D8B-E811-83FC-FA163E56B2A1.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/1E1E7446-208B-E811-AB30-FA163ECE7C6A.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/0AAE4FF1-228B-E811-A702-FA163E1C7049.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/ECA26FE0-238B-E811-9A27-FA163ECE7C6A.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/98B6F079-218B-E811-87DA-FA163EE8C7E8.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/286D0999-258B-E811-B495-FA163EFBD74B.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/5A6EE65E-278B-E811-8703-FA163E283070.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/EAC1D239-278B-E811-86B9-FA163E5EF417.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/385692AD-2F8B-E811-8486-FA163E2C529F.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/763F4929-308B-E811-9CF6-FA163E684D4D.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/042B4A9F-308B-E811-80B1-FA163E176422.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/6EB3DBAB-318B-E811-8A2D-FA163EF186AA.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/C6FD30A2-2F8B-E811-AC65-FA163EB9D708.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/A639CDD8-318B-E811-B29C-02163E010CC6.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/E842AA9A-338B-E811-8073-A4BF012CB7F9.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/C2C0A6B8-348B-E811-BCE0-FA163E7A7521.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/709F00BD-358B-E811-8E15-FA163ECDE73F.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/78334E09-378B-E811-B1B2-FA163EE7A04A.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/26CA6165-378B-E811-9991-FA163E6586F8.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/781128C1-038B-E811-B439-02163E019FC5.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/2E915D3B-058B-E811-A22A-FA163E946480.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/6E51085F-098B-E811-9563-FA163EE9C997.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/3CA0CAB6-098B-E811-A9D3-FA163ED39CC9.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/447484AB-0B8B-E811-97DF-FA163E46F35D.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/6EC77B45-0C8B-E811-8DC2-FA163EC18BC6.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/28558346-0C8B-E811-BF59-FA163EEB45BD.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/1AA37A73-0C8B-E811-9ADB-02163E019FC3.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/BC2E514D-108B-E811-8F6E-FA163EE9CF16.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/44AE7B31-0E8B-E811-8B4E-02163E014F48.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/8417FBCE-108B-E811-9833-FA163EB8FB10.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/FE41857A-138B-E811-93D1-FA163EC5ED06.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/2E637FA5-108B-E811-9269-FA163EB43663.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/9EA113F5-148B-E811-8067-FA163EFF9EA7.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/80C2B719-178B-E811-BDF6-A4BF01277567.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/B6A8022A-188B-E811-A764-FA163E9ED5E5.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/3266216B-1A8B-E811-ABD1-FA163E5BAF7F.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/2C41BCC3-1A8B-E811-AE6B-FA163E199928.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/F45CF843-1B8B-E811-B10C-FA163E3E7C16.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/80E51A11-1C8B-E811-A199-FA163ED39CC9.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/56F3EF14-1E8B-E811-B616-02163E01A040.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/24576086-1E8B-E811-8FBE-FA163E47A72B.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/36173017-1E8B-E811-BB08-FA163E2EAD2D.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/86161A16-228B-E811-8274-FA163E8ED26E.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/E4D29713-238B-E811-903A-FA163E77A6A7.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/9A6A45DB-238B-E811-8F6A-FA163EEC6C65.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/F66CD617-258B-E811-A475-FA163ED5C76A.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/160FDE85-1F8B-E811-9C35-02163E00B650.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/D262CD3B-298B-E811-A900-FA163EB07619.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/7A997A99-2B8B-E811-8FAC-FA163E7A9BB1.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/E2A0A7AE-2E8B-E811-AC41-FA163E6D1BE2.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/1074E545-358B-E811-9921-FA163E981033.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/AA01DE8C-1E8B-E811-949B-02163E012F16.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/50A5524D-048B-E811-8B20-FA163E1A09D0.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/A6C145B1-038B-E811-82D1-FA163E7CF385.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/0A6EA8C5-038B-E811-A05E-FA163E4F6754.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/8AF4E457-068B-E811-A668-FA163E529D85.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/F67BF561-078B-E811-97E2-02163E019FB4.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/D265D308-088B-E811-949E-FA163E4317BA.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/70FF6268-098B-E811-BCC9-FA163E47D9B8.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/3012DE95-068B-E811-9964-FA163EECAC76.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/74508FF8-0B8B-E811-A80E-FA163E0CAA0D.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/A4ACB8A8-0A8B-E811-8338-FA163ECDA888.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/46BCB6C4-0C8B-E811-B4B3-02163E017649.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/2E70243B-0F8B-E811-B576-FA163EF67044.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/C2C1D364-0F8B-E811-B2E8-FA163E990568.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/7E9BADDF-108B-E811-9F9A-FA163EBC5A2D.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/F0A430CC-118B-E811-9965-FA163E405DB4.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/B0DD8212-128B-E811-8CA5-FA163EE723F8.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/543BCB68-128B-E811-B26C-FA163E12F63B.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/AE2CB1A8-148B-E811-9598-FA163E74E2D2.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/6A265225-148B-E811-9561-FA163ECFB179.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/3AE69640-158B-E811-A5FA-FA163EFE4E9E.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/1EF5BBC2-118B-E811-8F83-FA163EC3C021.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/32367653-1C8B-E811-BFAA-FA163EB7EA75.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/C24237DE-1F8B-E811-A6E6-FA163E60BC85.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/86045411-228B-E811-9233-A4BF01277567.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/B07C722B-248B-E811-98E5-FA163E13304E.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/64A7ED99-248B-E811-9E4E-FA163EC60790.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/7066E01C-258B-E811-A467-FA163E85E28C.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/E23F3FF9-258B-E811-BE47-FA163E74B46D.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/F68FEECF-278B-E811-97D2-FA163E1D0D20.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/0E4EEF43-288B-E811-BD1D-FA163E41C42D.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/36C8E233-2A8B-E811-81C8-FA163E4F9F51.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/8E65A857-2D8B-E811-BED7-FA163E0E08DF.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/F8AF6F88-2B8B-E811-A32B-FA163E3BC51E.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/D6DBC60D-318B-E811-959A-FA163E7D392D.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/A230C6C3-328B-E811-BFE6-02163E01A035.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/0C475C2F-338B-E811-9973-FA163EA85F8C.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/5C983DAB-028B-E811-8313-02163E017C35.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/FE2A4E10-088B-E811-83EF-FA163E8A2E19.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/42863C54-048B-E811-9B56-02163E015295.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/6C01915F-098B-E811-9CFA-FA163EBF2E80.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/8ABB8CC3-088B-E811-83A4-FA163E52FDA7.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/CA09F96B-0B8B-E811-A35C-A4BF01277792.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/920A693D-0B8B-E811-8A37-FA163E359971.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/421C383C-0D8B-E811-9C5F-FA163E25EBE2.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/ACAE6304-0E8B-E811-9B48-FA163EA84D75.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/3EE603D1-0E8B-E811-9585-FA163E5A3118.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/FC657491-0E8B-E811-B595-FA163E12F63B.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/58B9C4EA-0F8B-E811-A8D0-FA163E62C5A6.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/6AC686F9-108B-E811-A1F5-FA163E712D83.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/6C728B5B-158B-E811-AA0A-FA163E8DC187.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/90B367C8-168B-E811-B9D8-02163E017F29.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/D40A0624-188B-E811-806C-FA163E6BAD4B.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/D00C8D01-1A8B-E811-A278-FA163E9D9FC9.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/745D2186-1B8B-E811-B983-A4BF01277567.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/72457846-288B-E811-B39D-FA163EC65D0D.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/98C312D5-288B-E811-9804-FA163E90EB49.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/E4CB102D-298B-E811-9E2F-FA163ECD532B.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/E0056C63-2A8B-E811-9998-FA163E5B30F8.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/A417DCDA-2B8B-E811-A418-FA163E492CEB.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/F2BFFDBC-2C8B-E811-B297-FA163E06C52E.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/B2D8F8AE-2F8B-E811-AB03-FA163E492CEB.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/248E86C2-2F8B-E811-8C9A-FA163E2890BA.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/04C818C1-2F8B-E811-A848-02163E00B00D.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/54FD6666-348B-E811-BB00-FA163E44F377.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/944E2150-048B-E811-832E-FA163E8D6DD8.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/9AE46A9B-058B-E811-962B-02163E01A0CF.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/EE74D74A-058B-E811-AC20-02163E01A040.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/90E7D81A-068B-E811-9394-FA163E177DDE.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/548C1EE4-068B-E811-AB90-02163E01A066.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/BE219E05-078B-E811-9D40-FA163EEAE4D8.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/AA923B1E-088B-E811-BD8D-FA163ECFB179.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/C61A9081-0B8B-E811-A920-FA163E64B36A.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/88982B6F-0B8B-E811-85F7-FA163E3E7C16.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/7C1A4A16-118B-E811-BDCE-02163E01A16C.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/E622CBBC-128B-E811-B509-FA163E8BA09F.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/F862A3D8-128B-E811-8191-FA163E4BB802.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/747625EE-138B-E811-A90E-FA163EF8E1C0.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/266DD9A3-158B-E811-9A55-FA163E8CE6BD.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/B69B122F-158B-E811-9399-FA163E29DB10.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/BE037FFC-158B-E811-BE47-FA163E2B06F2.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/1069954C-168B-E811-B388-FA163E6314D2.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/EA2D9A7F-178B-E811-B617-FA163E9F10B7.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/56BF00AC-188B-E811-A5C1-FA163E29DB10.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/02A216D5-188B-E811-8071-FA163E4A6585.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/EE172810-1A8B-E811-AA2F-FA163E3D0CE3.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/1080CE2C-1D8B-E811-BE0B-FA163E0A8099.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/12D2A1F1-268B-E811-BC0D-FA163EF3E48B.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/E2A098E3-268B-E811-A95E-FA163E6D9F0E.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/CEBF9369-278B-E811-95E2-FA163E658888.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/7E4038E5-268B-E811-A41C-FA163E5BCB73.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/A8AE18E1-2A8B-E811-99C6-FA163E38F35E.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/28754719-328B-E811-9767-FA163E4D3C24.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/CE90558E-338B-E811-A4D7-FA163E4959A4.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/48CF9617-338B-E811-9D6F-FA163E3C37D4.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/E4F19C36-368B-E811-BE83-FA163EE3D13F.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/705895BF-358B-E811-8077-FA163E9E8E7B.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/FE08572D-138B-E811-A151-FA163EDE7D03.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/3CD5A03C-058B-E811-97EE-A4BF01277792.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/3612AD04-048B-E811-9D72-FA163ECDA888.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/C0055C44-0B8B-E811-AE37-FA163E507A6F.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/468DDD35-0D8B-E811-BBA4-FA163E800141.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/1A22851B-0D8B-E811-8B9D-FA163E250820.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/78C677B6-0E8B-E811-96BF-FA163EF5EC59.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/1AC505BC-118B-E811-A3CF-FA163E3275C8.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/6C48F620-148B-E811-9039-02163E01A0E8.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/0A910A48-158B-E811-B9C0-FA163EF7922D.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/70668535-178B-E811-8A61-FA163E3E7C16.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/F061E831-198B-E811-9DB2-FA163E1D90F2.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/0E506B2A-198B-E811-9B75-FA163E5DF416.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/38B8BF63-1C8B-E811-A108-FA163E58351A.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/BC5625FC-1E8B-E811-AA9D-FA163EB615BD.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/14C70F80-1F8B-E811-8509-FA163E6C4A2C.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/0A20C34F-208B-E811-9E5C-FA163EC4066E.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/AC6135B3-208B-E811-AC39-FA163E7A7521.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/700B4610-228B-E811-B4E3-FA163EAC6FC3.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/821A0438-1B8B-E811-8CB8-FA163EECAC76.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/C6E2FE8D-228B-E811-94D9-FA163E1A0ED3.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/30C7A06A-238B-E811-B1A2-02163E019F7C.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/3E556BF2-258B-E811-A2AE-FA163EFA0B3E.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/FAF1D89B-248B-E811-A6BD-FA163EA2B1EA.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/E8691FBE-288B-E811-B287-FA163E2ECFBA.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/0EDF2DBE-298B-E811-BF22-FA163E8B92D3.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/0E51C288-2B8B-E811-8874-FA163E11135C.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/BC613BE8-2A8B-E811-B44D-FA163E74AC81.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/F4686866-2C8B-E811-856E-FA163ED3FFC7.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/2EDF6EC8-2C8B-E811-9E21-FA163E52FDA7.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/129F9AB6-2D8B-E811-A57D-FA163EC8B7BD.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/F202B543-2E8B-E811-86EA-02163E01A106.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/A8F3AC19-328B-E811-B7C1-FA163EA274D0.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/82DAA7F3-328B-E811-9F5B-FA163ED141EE.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/E833B8F8-028C-E811-9002-FA163EAD3FD0.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/3660A94B-048B-E811-9E25-FA163E3B5CA1.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/4C1D72C9-038B-E811-B847-FA163E200265.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/76836443-078B-E811-8114-FA163EACD9E0.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/265A2659-088B-E811-8C27-A4BF0112DB74.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/02018801-088B-E811-9A28-FA163ED3FFC7.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/92F28218-068B-E811-B7E1-FA163E274745.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/6428475D-098B-E811-9E25-FA163E0CDCE5.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/22CCD73B-0B8B-E811-8DD9-FA163E8BA09F.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/68B8F408-0D8B-E811-94C7-FA163E464BE8.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/244E9290-0E8B-E811-9F3A-FA163E54C32E.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/2E8C6647-0E8B-E811-AE45-02163E017F7B.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/D06F0DF1-0F8B-E811-ADEE-02163E019FF2.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/FEAA2667-128B-E811-AC6B-FA163E1D90F2.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/C6082181-148B-E811-AC87-FA163EC375AA.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/B06093D0-068B-E811-9C87-02163E013A22.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/809BC510-168B-E811-BA87-FA163E4BB802.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/5677E082-188B-E811-9C1C-FA163E36351C.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/FE06964A-188B-E811-B2EF-FA163EFF9EA7.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/E8C45221-198B-E811-8782-FA163E64B36A.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/DA1AA21A-1A8B-E811-82DE-FA163E3FD493.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/EC1830F2-1C8B-E811-8A1F-FA163EB005BF.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/8EFB5D11-1E8B-E811-B8EF-FA163E96DEEE.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/32429595-228B-E811-884A-FA163EC375AA.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/E44FFDEA-228B-E811-A4CE-FA163E41C42D.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/64AA8C9F-228B-E811-8B89-FA163E405DB4.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/F214B99F-258B-E811-8A8D-FA163E1E3B31.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/44F2D461-278B-E811-8BD6-FA163E8CA177.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/54FB8C57-298B-E811-BA7A-FA163E5962DD.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/E80638B2-298B-E811-94DD-02163E019F7C.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/2E219976-2B8B-E811-AD96-FA163E3AFBF6.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/B8E07BB1-2D8B-E811-B79F-FA163E05FE96.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/E68D3F3E-348B-E811-8B62-02163E01A040.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/28A98A42-378B-E811-A9D1-FA163E9C6DAA.root',
                            ),
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step2 nevts:1'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)


#Output
process.TFileService = cms.Service(
	"TFileService",
	fileName = cms.string("l1TNtuple-ZeroBias-2018C.root")
)

process.L1TRawToDigi_Stage2 = cms.Task(process.caloLayer1Digis, process.caloStage2Digis)
process.RawToDigi_short = cms.Sequence(process.L1TRawToDigi_Stage2)
process.p = cms.Path(process.RawToDigi_short * 
                     process.l1tCaloLayer1Digis *
                     process.simCaloStage2Layer1Digis * 
                     process.uct2016EmulatorDigis * 
                     #process.l1NtupleProducer
                     process.L1TCaloSummaryTestNtuplizer
)
#process.e = cms.EndPath(process.out)

#process.schedule = cms.Schedule(process.p,process.e)
process.schedule = cms.Schedule(process.p)

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)

# Multi-threading
process.options.numberOfThreads=cms.untracked.uint32(8)
process.options.numberOfStreams=cms.untracked.uint32(0)

