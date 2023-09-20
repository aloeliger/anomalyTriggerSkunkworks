import FWCore.ParameterSet.Config as cms
from anomalyDetection.anomalyTriggerSkunkworks.newFrameworkNtuplization.ntuplizeSkim_2023_DATA import process

process.source.fileNames = cms.untracked.vstring(
    "/store/user/aloelige/ZeroBias/CICADASkim_2023RunB_ZB_21Jul2023/230721_143206/0000/output_10.root",
    "/store/user/aloelige/ZeroBias/CICADASkim_2023RunB_ZB_21Jul2023/230721_143206/0000/output_11.root",
    "/store/user/aloelige/ZeroBias/CICADASkim_2023RunB_ZB_21Jul2023/230721_143206/0000/output_12.root",
    "/store/user/aloelige/ZeroBias/CICADASkim_2023RunB_ZB_21Jul2023/230721_143206/0000/output_13.root",
    "/store/user/aloelige/ZeroBias/CICADASkim_2023RunB_ZB_21Jul2023/230721_143206/0000/output_14.root",
    "/store/user/aloelige/ZeroBias/CICADASkim_2023RunB_ZB_21Jul2023/230721_143206/0000/output_15.root",
    "/store/user/aloelige/ZeroBias/CICADASkim_2023RunB_ZB_21Jul2023/230721_143206/0000/output_16.root",
    "/store/user/aloelige/ZeroBias/CICADASkim_2023RunB_ZB_21Jul2023/230721_143206/0000/output_17.root",
    "/store/user/aloelige/ZeroBias/CICADASkim_2023RunB_ZB_21Jul2023/230721_143206/0000/output_18.root",
    "/store/user/aloelige/ZeroBias/CICADASkim_2023RunB_ZB_21Jul2023/230721_143206/0000/output_19.root",
    "/store/user/aloelige/ZeroBias/CICADASkim_2023RunB_ZB_21Jul2023/230721_143206/0000/output_1.root",
    "/store/user/aloelige/ZeroBias/CICADASkim_2023RunB_ZB_21Jul2023/230721_143206/0000/output_20.root",
    "/store/user/aloelige/ZeroBias/CICADASkim_2023RunB_ZB_21Jul2023/230721_143206/0000/output_21.root",
    "/store/user/aloelige/ZeroBias/CICADASkim_2023RunB_ZB_21Jul2023/230721_143206/0000/output_22.root",
    "/store/user/aloelige/ZeroBias/CICADASkim_2023RunB_ZB_21Jul2023/230721_143206/0000/output_23.root",
    "/store/user/aloelige/ZeroBias/CICADASkim_2023RunB_ZB_21Jul2023/230721_143206/0000/output_24.root",
    "/store/user/aloelige/ZeroBias/CICADASkim_2023RunB_ZB_21Jul2023/230721_143206/0000/output_25.root",
    "/store/user/aloelige/ZeroBias/CICADASkim_2023RunB_ZB_21Jul2023/230721_143206/0000/output_26.root",
    "/store/user/aloelige/ZeroBias/CICADASkim_2023RunB_ZB_21Jul2023/230721_143206/0000/output_27.root",
    "/store/user/aloelige/ZeroBias/CICADASkim_2023RunB_ZB_21Jul2023/230721_143206/0000/output_28.root",
    "/store/user/aloelige/ZeroBias/CICADASkim_2023RunB_ZB_21Jul2023/230721_143206/0000/output_29.root",
    "/store/user/aloelige/ZeroBias/CICADASkim_2023RunB_ZB_21Jul2023/230721_143206/0000/output_2.root",
    "/store/user/aloelige/ZeroBias/CICADASkim_2023RunB_ZB_21Jul2023/230721_143206/0000/output_30.root",
    "/store/user/aloelige/ZeroBias/CICADASkim_2023RunB_ZB_21Jul2023/230721_143206/0000/output_31.root",
    "/store/user/aloelige/ZeroBias/CICADASkim_2023RunB_ZB_21Jul2023/230721_143206/0000/output_32.root",
    "/store/user/aloelige/ZeroBias/CICADASkim_2023RunB_ZB_21Jul2023/230721_143206/0000/output_33.root",
    "/store/user/aloelige/ZeroBias/CICADASkim_2023RunB_ZB_21Jul2023/230721_143206/0000/output_34.root",
    "/store/user/aloelige/ZeroBias/CICADASkim_2023RunB_ZB_21Jul2023/230721_143206/0000/output_35.root",
    "/store/user/aloelige/ZeroBias/CICADASkim_2023RunB_ZB_21Jul2023/230721_143206/0000/output_36.root",
    "/store/user/aloelige/ZeroBias/CICADASkim_2023RunB_ZB_21Jul2023/230721_143206/0000/output_37.root",
    "/store/user/aloelige/ZeroBias/CICADASkim_2023RunB_ZB_21Jul2023/230721_143206/0000/output_38.root",
    "/store/user/aloelige/ZeroBias/CICADASkim_2023RunB_ZB_21Jul2023/230721_143206/0000/output_39.root",
    "/store/user/aloelige/ZeroBias/CICADASkim_2023RunB_ZB_21Jul2023/230721_143206/0000/output_3.root",
    "/store/user/aloelige/ZeroBias/CICADASkim_2023RunB_ZB_21Jul2023/230721_143206/0000/output_40.root",
    "/store/user/aloelige/ZeroBias/CICADASkim_2023RunB_ZB_21Jul2023/230721_143206/0000/output_41.root",
    "/store/user/aloelige/ZeroBias/CICADASkim_2023RunB_ZB_21Jul2023/230721_143206/0000/output_42.root",
    "/store/user/aloelige/ZeroBias/CICADASkim_2023RunB_ZB_21Jul2023/230721_143206/0000/output_43.root",
    "/store/user/aloelige/ZeroBias/CICADASkim_2023RunB_ZB_21Jul2023/230721_143206/0000/output_44.root",
    "/store/user/aloelige/ZeroBias/CICADASkim_2023RunB_ZB_21Jul2023/230721_143206/0000/output_4.root",
    "/store/user/aloelige/ZeroBias/CICADASkim_2023RunB_ZB_21Jul2023/230721_143206/0000/output_5.root",
    "/store/user/aloelige/ZeroBias/CICADASkim_2023RunB_ZB_21Jul2023/230721_143206/0000/output_6.root",
    "/store/user/aloelige/ZeroBias/CICADASkim_2023RunB_ZB_21Jul2023/230721_143206/0000/output_7.root",
    "/store/user/aloelige/ZeroBias/CICADASkim_2023RunB_ZB_21Jul2023/230721_143206/0000/output_8.root",
    "/store/user/aloelige/ZeroBias/CICADASkim_2023RunB_ZB_21Jul2023/230721_143206/0000/output_9.root",
)