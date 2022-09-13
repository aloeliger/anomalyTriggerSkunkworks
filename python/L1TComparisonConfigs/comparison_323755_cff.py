from L1Trigger.anomalyTriggerSkunkworks.L1TComparisonConfigs.comparison_base_cff import process
import FWCore.ParameterSet.Config as cms

import FWCore.ParameterSet.VarParsing as VarParsing
options = VarParsing.VarParsing ('analysis')
options.parseArguments()

process.source.fileNames = cms.untracked.vstring(options.inputFiles)

process.source.secondaryFileNames = cms.untracked.vstring(
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/323/755/00000/B3255073-70FA-954E-9171-D28733F96373.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/323/755/00000/11FC721B-C288-2342-B356-317FD2457444.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/323/755/00000/F481E165-04F5-4D41-9265-B8D040CDF213.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/323/755/00000/DEA0E01C-DBD0-D544-9962-CFF423A53155.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/323/755/00000/754D20A5-FBCC-1348-9DB5-05300BFDD5FD.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/323/755/00000/DB40597A-1C9E-A045-A9A6-EFA27515DC2B.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/323/755/00000/D760D566-F50C-1C40-AD97-CDF945FA3DE5.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/323/755/00000/38F3D8A6-BD2A-F34E-97CC-9AAD6495C58B.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/323/755/00000/27A80D80-1B6A-814B-A297-8B12A657FA1F.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/323/755/00000/9E0F855B-812F-AD46-99CE-DD57DA35A45E.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/323/755/00000/DCEA489D-78FF-9049-9884-FCC92E134EF1.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/323/755/00000/54518933-3ABC-8C43-8BD2-EFD5B4642AAD.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/323/755/00000/751FD49E-83FB-0347-BCAF-377731807228.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/323/755/00000/CBB6CF24-CDBA-6C40-A6B7-C61B5B0504EB.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/323/755/00000/47DF057A-96D6-484E-83E9-8BA55BADBE55.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/323/755/00000/2B1F8E54-BC0B-AB4F-9AC4-0902B8DA17AF.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/323/755/00000/92641E29-DE74-CD40-B5C2-0D163F467B8E.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/323/755/00000/179A44F0-CFD6-B343-A23A-16A5C6AD0E00.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/323/755/00000/D0D4E8A6-F8C4-3146-A5B2-AD4B7342C5A4.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/323/755/00000/8ED17597-21A9-4A42-A73A-52E72E074B71.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/323/755/00000/D687B966-560F-5847-BECC-17795459B3C7.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/323/755/00000/2C52B8CE-AF9E-9949-BB87-08DECF01A86A.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/323/755/00000/88CA8E4A-0C99-694E-AFDF-D00D6A1B8925.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/323/755/00000/9A218702-7D32-A740-9905-0B451EF43109.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/323/755/00000/19775202-1A92-8A40-8AF7-85D801508CDB.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/323/755/00000/9F5BE94E-9924-594A-B067-918353ECDBB8.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/323/755/00000/5636BC7C-E0A1-8B4A-9514-293E82646367.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/323/755/00000/B1A5F4F6-F567-7448-81F0-813A3FF01883.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/323/755/00000/459AF97A-FF2C-4E49-80E0-BBE93E7F3B69.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/323/755/00000/2BCEDC76-019A-4E43-BB21-3212E0C058A6.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/323/755/00000/616034C1-3EFC-5D43-904F-1806CEA3F833.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/323/755/00000/CDEC125D-AD74-4C40-AD04-72997E813E75.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/323/755/00000/331102C3-ED2D-FA49-9121-FDCD3F8B939A.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/323/755/00000/767DC10E-2E63-E048-BC3B-4E86D6A23C54.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/323/755/00000/B7B130A0-F032-F144-B755-3A2B35E4CE4F.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/323/755/00000/B60698ED-CCF4-C443-8B63-D1C94F6034F2.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/323/755/00000/638B851C-45DB-2947-8C3F-525E23F2574B.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/323/755/00000/990620CA-C6B6-B340-8226-99EEEF5E2AD1.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/323/755/00000/A1431D8B-4F81-B34F-8376-804C55E09ECF.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/323/755/00000/D49EED50-C7BF-CE48-AF38-9139ADE0359B.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/323/755/00000/02506E54-CE47-A649-9F80-117E978DC69E.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/323/755/00000/1507559B-D021-E648-8100-010C4698D4DB.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/323/755/00000/45931E64-B74C-A14E-9A6E-4BE00510DF67.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/323/755/00000/5B4881D3-3417-B14C-91BA-760F78B427B3.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/323/755/00000/08D7B1A7-B8C5-0944-9A69-B698A2BF52EB.root',
)
process.TFileService.fileName=cms.string(options.outputFile)

#process.TFileService.fileName = cms.string("l1TNtuple_TriggerBitsComparison_2018D_320571.root")
