from L1Trigger.anomalyTriggerSkunkworks.L1TCaloSummary2018Configs.L1TCaloSummaryTestNtuplizer_2018_Base_cff import process
import FWCore.ParameterSet.Config as cms

process.source.fileNames = fileNames = cms.untracked.vstring(
    '/store/data/Run2018B/ZeroBias/MINIAOD/PromptReco-v1/000/317/511/00000/B6272DB3-5F6B-E811-8B83-02163E019EBE.root'
)

process.source.secondaryFileNames = cms.untracked.vstring(
    '/store/data/Run2018B/ZeroBias/RAW/v1/000/317/511/00000/2C1A98D4-4D6A-E811-8A7F-FA163E4E7FD0.root',
    '/store/data/Run2018B/ZeroBias/RAW/v1/000/317/511/00000/22A599F7-4D6A-E811-8FB2-FA163E9414B2.root',
    '/store/data/Run2018B/ZeroBias/RAW/v1/000/317/511/00000/CE4D37C4-4D6A-E811-AFCB-FA163E78F50B.root',
    '/store/data/Run2018B/ZeroBias/RAW/v1/000/317/511/00000/621852D2-4D6A-E811-A816-FA163E198F4C.root',
    '/store/data/Run2018B/ZeroBias/RAW/v1/000/317/511/00000/884993C6-4D6A-E811-9910-FA163E10052D.root',
    '/store/data/Run2018B/ZeroBias/RAW/v1/000/317/511/00000/3E22E5EA-4D6A-E811-BF9E-FA163E337911.root',
    '/store/data/Run2018B/ZeroBias/RAW/v1/000/317/511/00000/C6AFF2D1-4D6A-E811-8D64-FA163E2640F4.root',
    '/store/data/Run2018B/ZeroBias/RAW/v1/000/317/511/00000/D0916CC6-4D6A-E811-B63B-FA163E279E4C.root',
    '/store/data/Run2018B/ZeroBias/RAW/v1/000/317/511/00000/E267FC11-4E6A-E811-98D6-FA163E0EE1E4.root',
    '/store/data/Run2018B/ZeroBias/RAW/v1/000/317/511/00000/98A5B6D2-4D6A-E811-B675-FA163E4E7FD0.root',
    '/store/data/Run2018B/ZeroBias/RAW/v1/000/317/511/00000/D2B025CE-4D6A-E811-B51E-FA163E631526.root',
    '/store/data/Run2018B/ZeroBias/RAW/v1/000/317/511/00000/525BAFC9-4D6A-E811-84A6-FA163E490F23.root',
    '/store/data/Run2018B/ZeroBias/RAW/v1/000/317/511/00000/82558BC8-4D6A-E811-8D07-FA163E6F4029.root',
    '/store/data/Run2018B/ZeroBias/RAW/v1/000/317/511/00000/CA4D66D5-4D6A-E811-9E95-FA163E5738F8.root',
    '/store/data/Run2018B/ZeroBias/RAW/v1/000/317/511/00000/D28D7ECF-4D6A-E811-8C65-FA163E8F9CBA.root',
    '/store/data/Run2018B/ZeroBias/RAW/v1/000/317/511/00000/B4B812CA-4D6A-E811-A63F-FA163E9ADC84.root',
    '/store/data/Run2018B/ZeroBias/RAW/v1/000/317/511/00000/60435FC9-4D6A-E811-A576-FA163EF4C633.root',
    '/store/data/Run2018B/ZeroBias/RAW/v1/000/317/511/00000/2C1A64F9-4D6A-E811-AC57-FA163E7C479F.root',
    '/store/data/Run2018B/ZeroBias/RAW/v1/000/317/511/00000/9232B1C9-4D6A-E811-A45F-FA163E490F23.root',
    '/store/data/Run2018B/ZeroBias/RAW/v1/000/317/511/00000/60CF23EC-4D6A-E811-B97E-FA163EC27161.root',
    '/store/data/Run2018B/ZeroBias/RAW/v1/000/317/511/00000/B0CE29CE-4D6A-E811-9AAC-FA163E29007B.root',
    '/store/data/Run2018B/ZeroBias/RAW/v1/000/317/511/00000/7088EDC7-4D6A-E811-86D9-FA163E6E9B93.root',
    '/store/data/Run2018B/ZeroBias/RAW/v1/000/317/511/00000/6AF0CED4-4D6A-E811-98FC-FA163E29007B.root',
    '/store/data/Run2018A/ZeroBias/RAW/v1/000/315/420/00000/765A3EAC-0D4D-E811-A382-FA163EEB2BCA.root',
)

process.TFileService.fileName = cms.string("l1TNtuple-ZeroBias-2018B.root")