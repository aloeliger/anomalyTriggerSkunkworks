from L1Trigger.anomalyTriggerSkunkworks.L1TComparisonConfigs.comparison_base_cff import process
import FWCore.ParameterSet.Config as cms

import FWCore.ParameterSet.VarParsing as VarParsing
options = VarParsing.VarParsing ('analysis')
options.parseArguments()

process.source.fileNames = cms.untracked.vstring(options.inputFiles)
process.source.secondaryFileNames = cms.untracked.vstring(
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/38F33749-7594-E811-99D6-FA163EFF4C41.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/927AE5A7-6994-E811-91B5-FA163E108BAA.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/B260F21B-6A94-E811-842D-FA163EBDA163.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/B4262E99-6B94-E811-AF86-FA163E7B13F7.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/04041029-6D94-E811-AB49-FA163E9CD469.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/049D3492-6E94-E811-AE65-FA163E78828E.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/22420D83-6E94-E811-870D-FA163EE4471D.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/06DBDBAF-6E94-E811-A774-FA163E947408.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/165EB9FC-6F94-E811-8C32-FA163EE96112.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/FE88B073-7194-E811-BEDE-FA163E42078D.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/DC0BF10F-7094-E811-B67A-FA163EF670D6.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/4CC82D79-7094-E811-89AC-FA163EC82D11.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/26980541-7294-E811-821A-FA163E646B29.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/1AE9CCCE-7394-E811-8A1A-FA163E292099.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/2401D730-7294-E811-8758-FA163E7737A2.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/A83CF3CB-7394-E811-9BA2-FA163E150D9F.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/9EA9C4E2-7394-E811-83EF-FA163E38DF6F.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/F4031985-7294-E811-8557-FA163E44EA47.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/FA1BB4ED-7394-E811-A0EF-02163E01A04B.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/AC61E96D-7694-E811-823E-FA163E947408.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/70B6B359-7594-E811-9849-FA163E58F6C6.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/144A8444-6E94-E811-93CB-02163E00B3EB.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/FABD229C-6994-E811-ABBC-FA163E6FE197.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/F007F925-6A94-E811-BEC3-FA163E617121.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/06B4BFBE-6B94-E811-9649-02163E019FF6.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/D46BCB91-6B94-E811-A844-02163E01A048.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/5CD4B994-6B94-E811-B71D-FA163E85B308.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/5A76C334-6D94-E811-BE3C-FA163E943C2A.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/48A6F804-6D94-E811-B736-FA163E227A27.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/76771C7C-6E94-E811-8FCF-FA163EDF0BCA.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/DAE7F690-6E94-E811-B470-FA163E605DD6.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/10B6E814-6D94-E811-9E53-02163E01A16E.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/08486288-6E94-E811-9EC4-02163E010C5E.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/222145CB-6E94-E811-A270-02163E010CC6.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/581A0898-6E94-E811-ADD7-FA163E376DA0.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/0E974A93-7194-E811-8758-FA163E05C2A9.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/4ABF5E61-7194-E811-838E-02163E01A021.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/DE378C8B-7194-E811-9D93-FA163E44D80B.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/A2321C88-7194-E811-8B23-FA163EBE6C67.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/A49D9EAB-7294-E811-9EE2-FA163E5DCFC1.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/8A4DB31F-7294-E811-AB38-FA163E8290E1.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/B6BD2C97-7194-E811-9230-FA163EDE0EA3.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/7485B375-7294-E811-9CBB-FA163EBAEAC5.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/E431658E-7294-E811-BA7D-FA163EDA3EDC.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/284AB29D-7394-E811-A785-FA163E292099.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/50C48210-7094-E811-9EFC-FA163E06F2FD.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/4251D284-7394-E811-807B-FA163E047E67.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/D492982A-7594-E811-828A-FA163EB1CCFA.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/D6571519-7594-E811-B031-FA163EC2BBB1.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/508CD8F8-7394-E811-A61E-FA163E90D34B.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/96751B49-7594-E811-A87D-02163E010EA9.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/7E57D893-7694-E811-B04C-FA163EDCAD2D.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/60052FDB-7594-E811-A7E3-FA163EAFF426.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/8A197B14-7694-E811-8E70-FA163E5C63BB.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/36321E7B-7594-E811-8A21-FA163E3FA786.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/A214AEB4-7694-E811-B435-FA163E44D80B.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/B4C14640-7594-E811-9934-FA163EB35AAD.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/6C450C20-7694-E811-9FCC-FA163E53A37E.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/0CAF9E83-7194-E811-81E3-02163E015E99.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/808D105F-7294-E811-9B59-FA163EF673CF.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/664CA5BA-6994-E811-BF60-02163E013AB2.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/4E41BC2C-6894-E811-97EE-FA163E877AD3.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/1260F21B-6A94-E811-B873-FA163EBDA163.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/DCB8229C-6994-E811-B56D-FA163E6FE197.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/C2C70EAA-6B94-E811-B44A-FA163EF673CF.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/224FF488-6A94-E811-90AC-02163E017611.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/A09235BC-6B94-E811-8DE5-FA163E79B8E4.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/6089670E-6D94-E811-A6CB-FA163E111C08.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/8A084180-6E94-E811-AFB4-FA163EAD6CEB.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/F8162404-6D94-E811-A4DF-FA163E58F6C6.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/1C682884-6E94-E811-972C-FA163E150D9F.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/38EC03A4-6E94-E811-8F91-FA163E21FCC0.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/888538F3-6F94-E811-841C-FA163EE723F8.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/8882C72A-7094-E811-8AB0-FA163E85B308.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/D073F275-7094-E811-B1B7-FA163E626839.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/90815D5F-7194-E811-B333-FA163E5DCFC1.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/DA38E7B9-7294-E811-991E-FA163EDCAD2D.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/30BAB078-7294-E811-909E-FA163ECF0643.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/6E9B9712-7394-E811-860A-FA163E943C2A.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/B6F42D91-7194-E811-9869-FA163E78589E.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/C66DDFB5-7194-E811-A219-FA163E111C08.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/AA75D487-7394-E811-873F-FA163EC40DE1.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/B6847A20-7494-E811-B6CB-FA163E18D82B.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/8A97F86A-7494-E811-8EB2-FA163EE0025D.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/20B157AD-7394-E811-8E7B-FA163E097568.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/2CAFF85F-7594-E811-B683-FA163EF21D25.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/E200C5CC-7594-E811-A815-FA163E42078D.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/42DCEC6E-7594-E811-A586-FA163E6DCA6C.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/8EF018BE-7694-E811-9FD1-FA163EE007AE.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/0C699D1B-7694-E811-8985-FA163E3F3CC0.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/083C896B-3895-E811-8279-FA163E16E69A.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/96988B9C-6B94-E811-A466-02163E0164F8.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/2AE4A8A1-6994-E811-8B7B-FA163E05C2A9.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/BC5F7E36-6A94-E811-A10E-FA163E3FD732.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/2067612E-6A94-E811-B8B2-FA163E1F3FE7.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/4C3B0E94-6B94-E811-A919-FA163EA00566.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/B0FB2F06-6D94-E811-B394-FA163EEAD43D.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/46ECF790-6B94-E811-9AB4-FA163E09A6AB.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/62846513-6D94-E811-A4A8-FA163E6B4001.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/14B6680E-6D94-E811-9C87-FA163E44D80B.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/5E184485-6E94-E811-A855-FA163EFDD7AF.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/10439F7F-6E94-E811-B7EB-FA163EDF63C4.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/5E7E3385-6E94-E811-B2B9-FA163EC40DE1.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/D6B144EF-6F94-E811-A193-FA163E292099.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/D69AF548-6894-E811-A932-FA163E264A72.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/74C56B25-7094-E811-8228-FA163EB75CE4.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/CEE1F181-7194-E811-A8F1-FA163E7B13F7.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/14E5C605-7094-E811-9132-02163E0164F8.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/B2C64FD3-7194-E811-9C77-FA163E8A2E19.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/F6E78D4F-7094-E811-9838-FA163E033F78.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/AAF511BB-6994-E811-A9C0-02163E016096.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/C8227AA9-7294-E811-8162-FA163EEFC25A.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/647FB1FE-6F94-E811-BD0F-FA163E20F4EA.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/3E97CE23-7394-E811-82DD-FA163EAAFDDB.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/8ADA3F87-7394-E811-82DC-FA163EF68D36.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/C29164E6-7394-E811-9C78-FA163E29B158.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/68CAC802-7494-E811-B11D-FA163E581BC1.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/362DEC28-6D94-E811-A165-FA163E826FAC.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/8E97EE9D-7494-E811-A7B9-FA163EAB91EC.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/5683A064-7594-E811-9F62-FA163E004F02.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/50AF44A1-6994-E811-B48B-FA163E355523.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/70C56249-6894-E811-AB6D-02163E010CCE.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/705BF52F-6894-E811-87BF-FA163E9EF305.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/C60DDE19-6A94-E811-85D4-FA163E298876.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/32CCBE8F-6B94-E811-9401-FA163EB2E79E.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/964EA86B-6A94-E811-8EED-02163E010CF7.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/F6130791-6B94-E811-A37E-FA163EF68D36.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/A803813C-6894-E811-A0B2-FA163EB9CE9F.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/26F95A91-6B94-E811-A430-FA163E19F6BD.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/4CB49C91-6B94-E811-AC00-FA163E19F6BD.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/8ADA0D94-6B94-E811-9F79-FA163E5FB1EE.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/E2976CBB-6B94-E811-AE53-FA163EBB9798.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/1E3DF90A-6D94-E811-9072-FA163E793AC1.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/DA679C84-6E94-E811-A5B7-FA163E87B737.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/26AC840D-6D94-E811-ACA7-FA163E96DEEE.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/3207D7B9-6B94-E811-B548-FA163E5BCB73.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/8C16250B-6D94-E811-A31C-FA163ED49149.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/10F6EE9A-6E94-E811-83FA-FA163E8BC3ED.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/C2BEB0F8-6F94-E811-99FB-FA163EB9C3AA.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/6A761636-6D94-E811-8025-FA163E448F1D.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/16858D5F-7194-E811-A01B-FA163E551B8E.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/F0D57E61-7194-E811-A34C-FA163E385185.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/668BCAF5-6F94-E811-A3DD-FA163EABD261.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/B87ECA12-6D94-E811-A3E1-FA163E959DBF.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/DABA9A94-7194-E811-A685-FA163E337D5D.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/0CD49C0C-7094-E811-9E8E-FA163E3FA786.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/86361D76-7294-E811-B762-FA163E337D5D.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/2645923D-7394-E811-988B-02163E016579.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/CEA30CA4-7294-E811-A8B3-FA163EA79D8C.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/0AF1B6A6-7394-E811-B764-FA163EA65232.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/7238C791-7394-E811-A543-FA163E3B2308.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/9E1532FF-7394-E811-9A26-FA163E21FCC0.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/02F116FE-7394-E811-BC91-FA163EF653A5.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/06200B79-7294-E811-924A-FA163E2746DB.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/4CE74507-7494-E811-893C-02163E010C3F.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/E8BEC016-7694-E811-9F12-FA163E6E9B93.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/0499B1FE-6F94-E811-9D51-FA163E20F4EA.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/FC3BA717-7694-E811-B0C6-FA163EE79646.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/AE04F2A6-7694-E811-8F6E-02163E017F10.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/86AA279F-7594-E811-AC28-FA163E020EAE.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/A0E0D2FA-6E94-E811-9BD5-02163E01483F.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/D2ED11AC-7694-E811-9461-FA163E6C63D4.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/EA500E81-7594-E811-BC12-FA163EBB9798.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/1613BDA4-6994-E811-801A-FA163E2750FC.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/E4A0765E-6D94-E811-BBA8-FA163E8290E1.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/CCBCA57F-6E94-E811-B6AE-02163E019FF6.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/CAA8374B-6D94-E811-BDC2-FA163EEFC25A.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/9EE31D94-6B94-E811-97A4-FA163EF6EF83.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/9E9353F5-6F94-E811-88FE-FA163EBAEB5B.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/86585E10-7094-E811-9524-FA163EBDF294.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/8AA79C34-6A94-E811-BAF7-02163E016035.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/567F2CF1-6F94-E811-8039-FA163E525955.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/444D63E7-6D94-E811-99DB-FA163E46B98A.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/166833C3-6B94-E811-B20E-FA163E820483.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/4EBE2200-7094-E811-AE5A-FA163E890C5B.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/26F5E00A-7094-E811-97AE-FA163E646B29.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/D85432FD-6F94-E811-A520-FA163E95D558.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/26F36D60-7194-E811-9D7F-FA163E14A572.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/DEB202FB-6F94-E811-B770-FA163E6DCA6C.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/261710FB-6F94-E811-A0CE-FA163EC38ED5.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/7221A792-7294-E811-8320-FA163E27069D.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/E0BED81E-7294-E811-92F9-FA163EB0AC13.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/EAE72C7F-7194-E811-9D11-FA163E937ABD.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/A660287B-7294-E811-BAB7-FA163E376DA0.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/FC737DED-7394-E811-9E5C-FA163E79B8E4.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/76746DC3-7494-E811-9ED7-02163E010C96.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/1630925B-7594-E811-B6A5-FA163EDDAD9B.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/CE14F35D-7594-E811-B020-FA163E6AE23B.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/5A51C22D-6D94-E811-BF63-FA163E264A72.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/364F7EAC-7694-E811-8193-FA163E605DD6.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/FE64E04F-7594-E811-BE78-FA163EB330ED.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/76379FB9-6694-E811-8D22-FA163EF6F61C.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/76FF9030-6894-E811-A56F-FA163E7DCDDC.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/AA01E2C0-6994-E811-8AE6-FA163E020EAE.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/26ABE798-6B94-E811-AEC0-FA163E3F3CC0.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/CA416298-6B94-E811-89CC-FA163EC94C64.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/8E87E0F8-6994-E811-9770-FA163EE15E55.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/08E67906-6D94-E811-8D76-FA163EFDD7AF.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/7E763F9B-6B94-E811-8CF1-02163E019FAC.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/56636191-6B94-E811-8C8A-FA163E09A6AB.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/048C0C9E-6994-E811-936B-02163E016067.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/286EC738-6D94-E811-8D3E-FA163EC4A708.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/D05BD19C-6E94-E811-848B-FA163EAAFDDB.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/BA1B2D88-6E94-E811-B28E-02163E010F87.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/8891C98E-6E94-E811-9B59-FA163EC2EA88.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/C836F186-6E94-E811-A179-FA163EBC06F8.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/041811F3-6F94-E811-B723-FA163EDA3EDC.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/1CBBF101-7094-E811-8BD4-FA163EEC74A2.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/3AF986F7-6F94-E811-BACB-FA163E4636FB.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/AC63D561-7194-E811-8728-FA163E2E7215.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/84AA423B-7094-E811-A254-02163E017611.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/62E27E89-7094-E811-869F-FA163E342326.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/28B0CEBB-7394-E811-99A0-FA163E166081.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/8E577ECC-7394-E811-9DB7-FA163EBAEB5B.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/5CD0E8B3-7194-E811-B9F4-FA163E3A08F6.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/ACC16E3E-7594-E811-BB38-FA163E05C2A9.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/A8363E9F-7494-E811-AD24-FA163E3464F5.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/34DD1161-7594-E811-9272-FA163E793AC1.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/4053212A-7594-E811-9F2D-FA163E4B7072.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/2AA28564-7594-E811-B914-FA163E4636FB.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/38F0EAA9-6E94-E811-BEB9-FA163E9FF645.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/66BBEC75-7594-E811-9FBE-FA163EA7752A.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/3A09C2C3-7694-E811-8B5D-FA163E2750FC.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/0063B4C0-7694-E811-979E-02163E010EC5.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/68225F94-7694-E811-99AB-02163E019FAC.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/AC068EE2-7694-E811-BF32-FA163EF670D6.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/D0E10ED1-7694-E811-9462-FA163E937ABD.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/AC24EE4A-6D94-E811-8956-02163E00BCAD.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/DA3C6C68-3595-E811-B00E-FA163E6B091B.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/CC237D2B-3895-E811-91EE-FA163EE048DE.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/9A35B207-4295-E811-90AD-FA163E7ECD23.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/90F87DA2-6994-E811-A16D-FA163E18D82B.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/D44D0423-6A94-E811-8183-FA163EBAEAC5.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/FECF5394-6B94-E811-A5E2-FA163E337D5D.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/5E72A0A6-6994-E811-9B5C-FA163E4B7072.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/2EE173A1-6B94-E811-B8C1-02163E019F48.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/5697DB92-6B94-E811-806A-02163E016598.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/D81E9238-6A94-E811-8384-FA163E90D34B.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/8EAA7907-6D94-E811-A234-02163E01A0FB.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/2E95CA84-6E94-E811-A81D-FA163EED9E90.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/C6C8E584-6E94-E811-9462-FA163E047E67.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/865A2184-6E94-E811-8A29-FA163EC1819D.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/C894B508-7094-E811-A0C5-FA163EC78217.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/167DA8F3-6F94-E811-8D16-FA163E7FB452.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/1CBEAB96-6E94-E811-9382-FA163E3B5CA1.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/BA02C9FE-6F94-E811-882E-FA163E695ADD.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/BA125EA1-6994-E811-A865-02163E01493B.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/9693C764-7194-E811-BB4E-FA163E7A3564.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/DE6A9472-7294-E811-8C24-FA163EFA3CEB.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/F24C4884-7094-E811-8E96-FA163E885D87.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/FE1D4C24-7294-E811-90F9-FA163EDF60BF.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/20F59A7D-7194-E811-B65A-02163E0164F8.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/ECF1190A-7094-E811-94BD-02163E010C51.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/5ED16976-7194-E811-9AF5-FA163E8BC3ED.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/48BBDCB6-7194-E811-84CE-FA163EC7FEDF.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/4213627B-7194-E811-9822-FA163EF8D9AB.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/74CB9DBC-7394-E811-88A3-FA163E5FB1EE.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/422AA0E8-7294-E811-889A-FA163E852154.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/DA76F2DC-7494-E811-A646-FA163E3FE3C5.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/3C5468D9-6894-E811-A9FB-02163E00AEE9.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/1C30C94A-7694-E811-8A22-FA163EDF0BCA.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/6A6945BA-7694-E811-9E1A-FA163E033F78.root",
    "/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/A6CDEBE5-3A95-E811-96A9-FA163E880BF2.root",
)

process.TFileService.fileName = cms.string(options.ouputFile)
#process.TFileService.fileName = cms.string("l1TNtuple_TriggerBitsComparison_2018D_320569.root")