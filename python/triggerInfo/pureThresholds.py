# Organized by
# [model version][menu or general][desired rate in khz]
pureCICADAThresholds = {
    'v_1.0.0':{ #2018 model
        'general':{
            'ZeroBias': 0.0,
            5: 5.783,
            3: 5.895,
            2: 5.988,
            1: 6.221,
            0.5: 6.520,
        },
    },
    'v_2.0.0':{ #updated 2018 arch model
        'general':{
            'ZeroBias': 0.0,
            5: 10.630,
            3: 11.336,
            2: 11.953,
            1: 13.365,
            0.5: 15.570,
        },
    },
    'v_1.1.0':{ #2023 model
        'general': { # treated the same as L1Menu Collisions2023_v1_2_0
            'ZeroBias': 0.0,
            10: 5.781,
            5: 5.859,
            3: 5.922,
            2: 5.983,
            1: 6.016,
            0.5: 6.109,
        },
        'L1Menu_Collisions2023_v1_2_0':{
            'ZeroBias': 0.0,
            10: 5.781,
            5: 5.859,
            3: 5.922,
            2: 5.983,
            1: 6.016,
            0.5: 6.109,            
        },
        'L1Menu_Collisions2022_v1_4_0':{
            'ZeroBias':0.0,
            10: 0.312,
            5: 0.328,
            3: 0.344,
            2: 0.344,
            1: 0.344,
            0.5: 0.359,
        }
    },
    'v_2.1.0':{ #2023 model
        'general': { #treated the same as L1Menu_Collisions2023_v1_2_0
            'ZeroBias': 0.0,
            10: 11.555,
            5: 11.947,
            3: 12.252,
            2: 13.528,
            1: 13.277,
            0.5: 14.012,
        },
        'L1Menu_Collisions2023_v1_2_0': {
            'ZeroBias': 0.0,
            10: 11.555,
            5: 11.947,
            3: 12.252,
            2: 12.528,
            1: 13.277,
            0.5: 14.012,            
        },
        'L1Menu_Collisions2022_v1_4_0': { #I suspect this is bugged due to bad Run A Stats?
            'ZeroBias': 0.812,
            10: 0.812,
            5: 0.840,
            3: 0.855,
            2: 0.883,
            1: 0.926,
            0.5: 0.953
        },
    },
    'v_1.1.1':{
        'general': { #treated the same as L1Menu_Collisions2023_v1_2_0
            'ZeroBias': 0.0,
            10: 9.902,
            5: 10.403,
            3: 10.710,
            2: 11.258,
            1: 12.250,
            0.5: 12.969
        },
        'L1Menu_Collisions2023_v1_2_0': {
            'ZeroBias': 0.0,
            10: 9.902,
            5: 10.403,
            3: 10.710,
            2: 11.258,
            1: 12.250,
            0.5: 12.969            
        },
    },
    'v_2.1.1':{
        'general':{
            'ZeroBias': 0.0,
            10: 7.781,
            5: 8.219,
            3: 8.562,
            2: 8.730,
            1: 9.531,
            0.5: 10.719,
        },
        'L1Menu_Collisions2023_v1_2_0':{
            'ZeroBias': 0.0,
            10: 7.781,
            5: 8.219,
            3: 8.562,
            2: 8.730,
            1: 9.531,
            0.5: 10.719,
        }
    }
}