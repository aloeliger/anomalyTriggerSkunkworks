from L1Trigger.anomalyTriggerSkunkworks.L1TComparisonConfigs.comparison_base_cff import process
import FWCore.ParameterSet.Config as cms

import FWCore.ParameterSet.VarParsing as VarParsing
options = VarParsing.VarParsing ('analysis')
options.parseArguments()

process.source.fileNames = cms.untracked.vstring(options.inputFiles)

process.source.secondaryFileNames = cms.untracked.vstring(
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/321/755/00000/40BA173E-B9A7-E811-9625-02163E019FA9.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/321/755/00000/FA66C472-A8A7-E811-BC1B-02163E01A08F.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/321/755/00000/BC41ABDE-A9A7-E811-A626-FA163E1A5A66.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/321/755/00000/2C5EA74E-A7A7-E811-9AC4-FA163E4B6104.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/321/755/00000/E0EB4E0E-AEA7-E811-9264-FA163E4BC5B5.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/321/755/00000/22A0499E-AFA7-E811-B9C7-02163E019F0B.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/321/755/00000/2416D715-B0A7-E811-8BC9-FA163E63172E.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/321/755/00000/66947D2E-B3A7-E811-8D2D-FA163E4413A6.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/321/755/00000/2EDC15A6-B1A7-E811-B556-FA163EFA689B.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/321/755/00000/9248B765-B2A7-E811-A388-FA163EC92774.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/321/755/00000/D4C4D1C3-B7A7-E811-ADA8-FA163EDE7FEA.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/321/755/00000/60DABCC0-BAA7-E811-ACDD-FA163ED42EAE.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/321/755/00000/1A5F9215-BBA7-E811-8D5B-FA163E212973.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/321/755/00000/ECEB8A18-BBA7-E811-9C5B-FA163E31C0D5.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/321/755/00000/F83D5AE3-A9A7-E811-8C1C-FA163E1C72D5.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/321/755/00000/6E9B50FB-A9A7-E811-89BC-FA163EB27263.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/321/755/00000/B0C74A15-AAA7-E811-8B36-FA163E1347E8.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/321/755/00000/B8582B69-AFA7-E811-9541-FA163E700015.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/321/755/00000/8A2770B5-B4A7-E811-9A44-FA163E462119.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/321/755/00000/7665F0F1-B4A7-E811-9FF6-FA163EA1368E.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/321/755/00000/5A29D3C8-B7A7-E811-A0BB-02163E019F97.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/321/755/00000/143AB405-BBA7-E811-BAB2-FA163E47C8BD.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/321/755/00000/9EFFF973-A8A7-E811-B4BF-FA163EE835E3.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/321/755/00000/861DE8C9-A9A7-E811-A397-FA163EBB9A14.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/321/755/00000/BEC647CF-A9A7-E811-BCA0-FA163EECC3A9.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/321/755/00000/46B50CB1-AAA7-E811-A7E6-FA163E78EBF0.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/321/755/00000/E23B3EE3-ABA7-E811-90E4-FA163E837B72.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/321/755/00000/E8D6550D-B0A7-E811-8BAA-FA163E795CFE.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/321/755/00000/AEC176BC-B1A7-E811-AF63-FA163E1B57DB.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/321/755/00000/F0E5FADD-B4A7-E811-9358-FA163EBEF75C.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/321/755/00000/5AC9D240-B9A7-E811-B95F-FA163EF4E3E9.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/321/755/00000/169DCAC4-B7A7-E811-BBD0-FA163EAB4AB6.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/321/755/00000/381181C6-AAA7-E811-9F0A-FA163E2BB5F1.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/321/755/00000/7AC9C24B-ADA7-E811-AE9C-FA163E1A5A66.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/321/755/00000/568D575E-ACA7-E811-B8DE-FA163EB41A13.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/321/755/00000/E6A30143-B3A7-E811-8AA0-FA163E452D93.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/321/755/00000/F2699C01-B5A7-E811-9F56-FA163EB1CCFA.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/321/755/00000/BA1AE3BA-B4A7-E811-99BA-FA163E60A5FD.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/321/755/00000/54AE932B-B6A7-E811-89E5-02163E019F5F.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/321/755/00000/D22647C6-B7A7-E811-BC35-02163E019ED0.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/321/755/00000/02AFC5CE-AAA7-E811-8E7D-02163E017F64.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/321/755/00000/906BDB20-ADA7-E811-A25B-FA163E57B0C7.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/321/755/00000/0410A2AA-ADA7-E811-9CA5-FA163E427E8F.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/321/755/00000/8A62DF76-ADA7-E811-A1D2-FA163EA85F8C.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/321/755/00000/6890B25A-AEA7-E811-BA01-02163E01A10B.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/321/755/00000/E2AEFE50-B0A7-E811-AB37-FA163E555720.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/321/755/00000/A4C3CCE6-B1A7-E811-B103-FA163EE81CA0.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/321/755/00000/30CD6239-B6A7-E811-8D19-FA163E376102.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/321/755/00000/3C059141-B9A7-E811-9F2C-FA163E010862.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/321/755/00000/C4B37271-A8A7-E811-94FD-FA163E3509C2.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/321/755/00000/7E9CDF09-B5A7-E811-961D-FA163E8DA20D.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/321/755/00000/4AF23CCC-B4A7-E811-A470-FA163EB41A13.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/321/755/00000/4EA8923F-B9A7-E811-8AE7-FA163EE95896.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/321/755/00000/F8D7F6B0-AAA7-E811-B508-FA163EADE699.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/321/755/00000/768D16EE-ABA7-E811-9760-FA163E059BE1.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/321/755/00000/FC164428-ADA7-E811-AE2F-FA163E5F83E7.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/321/755/00000/ACBCDCE2-AEA7-E811-8543-FA163EFCFF2C.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/321/755/00000/66CDB134-B3A7-E811-97D4-FA163EB84E0D.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/321/755/00000/44965C56-B3A7-E811-BA02-FA163E85FA06.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/321/755/00000/A27E71C4-B7A7-E811-A1B0-02163E019ECE.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/321/755/00000/2467893B-B9A7-E811-8BF6-FA163E96591B.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/321/755/00000/7095CFC9-BAA7-E811-95BF-FA163E21086B.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/321/755/00000/44A9FFE3-BAA7-E811-A30E-FA163E493255.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/321/755/00000/64FCBD6F-A8A7-E811-87FD-FA163E030AB8.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/321/755/00000/4810AC08-ACA7-E811-B382-FA163E854178.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/321/755/00000/C82EB10A-ACA7-E811-96F6-FA163E53FDF8.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/321/755/00000/6A85DAFF-ADA7-E811-8A97-FA163E555720.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/321/755/00000/9CB7970F-AFA7-E811-97A4-FA163ECB2D7D.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/321/755/00000/32D663A5-B1A7-E811-A15E-FA163E06876F.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/321/755/00000/96A5BFCA-B1A7-E811-9370-FA163E464EF2.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/321/755/00000/F03D0F2A-B6A7-E811-8945-FA163EEE0E46.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/321/755/00000/FE19AB2B-B6A7-E811-A53E-FA163E455B73.root',
)
process.TFileService.fileName=cms.string(options.outputFile)

#process.TFileService.fileName = cms.string("l1TNtuple_TriggerBitsComparison_2018D_320571.root")