import FWCore.ParameterSet.Config as cms
from anomalyDetection.anomalyTriggerSkunkworks.newFrameworkNtuplization.ntuplizeSkim_2023_DATA import process

process.source.fileNames = cms.untracked.vstring(
    "/store/user/aloelige/ZeroBias/CICADASkim_2023RunA_ZB_21Jul2023/230721_143242/0000/output_1-1.root",
    "/store/user/aloelige/ZeroBias/CICADASkim_2023RunA_ZB_21Jul2023/230721_143242/0000/output_1.root",
    "/store/user/aloelige/ZeroBias/CICADASkim_2023RunA_ZB_21Jul2023/230721_143242/0000/output_2.root",
    "/store/user/aloelige/ZeroBias/CICADASkim_2023RunA_ZB_21Jul2023/230721_143242/0000/output_3.root",
    "/store/user/aloelige/ZeroBias/CICADASkim_2023RunA_ZB_21Jul2023/230721_143242/0000/output_4.root",
    "/store/user/aloelige/ZeroBias/CICADASkim_2023RunA_ZB_21Jul2023/230721_143242/0000/output_5.root",
    "/store/user/aloelige/ZeroBias/CICADASkim_2023RunA_ZB_21Jul2023/230721_143242/0000/output_6.root",
    "/store/user/aloelige/ZeroBias/CICADASkim_2023RunA_ZB_21Jul2023/230721_143242/0000/output_7.root",
    "/store/user/aloelige/ZeroBias/CICADASkim_2023RunA_ZB_21Jul2023/230721_143242/0000/output_8.root",
)
