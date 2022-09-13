from L1Trigger.anomalyTriggerSkunkworks.L1TComparisonConfigs.comparison_base_cff import process
import FWCore.ParameterSet.Config as cms

import FWCore.ParameterSet.VarParsing as VarParsing
options = VarParsing.VarParsing ('analysis')
options.parseArguments()

process.source.fileNames = cms.untracked.vstring(options.inputFiles)

process.source.secondaryFileNames = cms.untracked.vstring(
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/323/725/00000/2CC49326-F190-8241-B1B1-CD5A49875F4C.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/323/725/00000/A0AA3412-06BB-7D40-95FE-B2DC221E9C7E.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/323/725/00000/019FD57A-6C4E-D741-B361-C8B8537D119E.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/323/725/00000/3E7284D9-CBBF-D44A-AA13-BCD9859276F1.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/323/725/00000/049DE934-A82F-974A-A3EA-A73A79AAC6FF.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/323/725/00000/23E117A5-2993-4B4E-9810-DBB4156F66DC.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/323/725/00000/A76E7819-ADC4-CB45-95D1-EA78FB4AA8F2.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/323/725/00000/BB68ECAA-A0DF-F44B-8C19-DB7283BF0886.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/323/725/00000/877AAD17-0D0F-224E-806B-938033686739.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/323/725/00000/5732DDF6-BDD0-9742-B7F0-770003934BD8.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/323/725/00000/27E5C482-53AC-CF4D-9ECB-1ED7A0ECE56A.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/323/725/00000/2F94EBC6-2C47-844D-971C-80D45A30ED8E.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/323/725/00000/35FF427B-9EA4-4C43-880B-93D7E99190A7.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/323/725/00000/CF7ACB1B-340A-F64C-AC34-A853B1CFFB21.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/323/725/00000/02FDA2FD-A217-D34E-8352-592A7ED11CFD.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/323/725/00000/616951A0-5FA4-304C-8B4C-3A05465C1E16.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/323/725/00000/4625A0B2-7EC3-7F48-B4BB-FD0A9D0B4D8F.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/323/725/00000/4ABABB72-9641-4D45-8F44-040104470149.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/323/725/00000/394126E0-9B59-B04C-9B19-4375062B1EBC.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/323/725/00000/D2692FBF-89EB-F240-A5D2-599D2248C2F5.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/323/725/00000/DC0E05BB-6A84-2F45-8848-EB86987CA270.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/323/725/00000/EAD949F6-E892-6E4C-AB28-CC440B9FFE17.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/323/725/00000/8C60298E-5C1E-2048-A8C7-B71323798EB2.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/323/725/00000/65E975A5-97F3-C043-9E5D-42A480AB5A54.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/323/725/00000/C97B1CDF-66C9-214A-BB72-53FA5778D5B7.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/323/725/00000/5A66114E-D4C2-ED44-9585-363E125A340E.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/323/725/00000/0392BF68-073E-2A41-A6A6-98F3547C1D01.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/323/725/00000/F89AE2AD-5EDE-6F4C-A7B5-4D3965777278.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/323/725/00000/2B287F9E-5428-8F4C-B665-9116A69ED143.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/323/725/00000/EFCA4833-85ED-BD44-B60E-D6B436E0740C.root',
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/323/725/00000/0219DCFA-B7D2-C24D-A59B-33C7CE09330F.root',
)
process.TFileService.fileName=cms.string(options.outputFile)

#process.TFileService.fileName = cms.string("l1TNtuple_TriggerBitsComparison_2018D_320571.root")
