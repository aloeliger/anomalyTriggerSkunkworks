# Organized by
# [model version][menu or general][desired rate in khz]
CICADAThresholds = {
    'v_1.0.0': { #original 2018 model
        'general':{ #treated as L1Menu_Collisions2018_v2_0_0
            10: 5.364,
            5: 5.600,
            3: 5.758,
            2: 5.880,
            1: 6.142,
            0.5: 6.474,
        },
        'L1Menu_Collisions2018_v2_0_0':{
            10: 5.364,
            5: 5.600,
            3: 5.758,
            2: 5.880,
            1: 6.142,
            0.5: 6.474,
        },
        'L1Menu_Collisions2018_v2_1_0':{
            10: 5.906,
            5: 6.037,
            3: 6.142,
            2: 6.273,
            1: 6.500,
            0.5: 6.788,
        },
    },
    'v_2.0.0':{ #updated arch 2018 model
        'general':{ #treated as L1Menu_COllisions2018_v_2_0_0
            10: 9.131,
            5: 10.0128,
            3: 10.763,
            2: 11.601,
            1: 13.365,
            0.5: 15.527,
        },
        'L1Menu_Collisions2018_v2_0_0':{
            10: 9.131,
            5: 10.0128,
            3: 10.763,
            2: 11.601,
            1: 13.365,
            0.5: 15.527,
        },
        'L1Menu_Collisions2018_v2_1_0':{
            10: 11.557,
            5: 12.483,
            3: 13.189,
            2: 13.983,
            1: 15.747,
            0.5: 17.820,
        },
    },
    'v_1.1.0':{ #trained for 2023
        'general':{ # default treated as L1Menu_Collisions2023_v1_2_0 for this arch
            10: 5.734,
            5: 5.884,
            3: 5.953,
            2: 6.047,
            1: 6.406,
            0.5: 6.922,
        },
        'L1Menu_Collisions2023_v1_0_0':{
            10: 5.391,
            5: 5.609,
            3: 5.734,
            2: 5.804,
            1: 5.922,
            0.5: 6.156,
        }, 
        'L1Menu_Collisions2023_v1_2_0':{
            10: 5.734,
            5: 5.884,
            3: 5.953,
            2: 6.047,
            1: 6.406,
            0.5: 6.922,
        }, 
        'L1Menu_Collisions2022_v1_4_0':{ #likely bugged by bad stats or overtraining
            10: 0.312,
            5: 0.328,
            3: 0.328,
            2: 0.344,
            1: 0.344,
            0.5: 0.359,
        },
    },
    'v_2.1.0':{ #trained for 2023
        'general':{ # default treated as L1Menu_Collisions2023_v1_2_0 for this arch
            10: 11.356,
            5: 11.983,
            3: 12.477,
            2: 13.371,
            1: 15.707,
            0.5: 18.934,
        },
        'L1Menu_Collisions2023_v1_0_0':{
            10: 10.299,
            5: 11.092,
            3: 11.476,
            2: 12.358,
            1: 13.284,
            0.5: 15.188,
        }, 
        'L1Menu_Collisions2023_v1_2_0':{
            10: 11.356,
            5: 11.983,
            3: 12.477,
            2: 13.371,
            1: 15.707,
            0.5: 18.934,
        }, 
        'L1Menu_Collisions2022_v1_4_0':{ #likely bugged by bad stats or overtraining
            10: 0.809,
            5: 0.836,
            3: 0.852,
            2: 0.883,
            1: 0.914,
            0.5: 0.992,
        },
    },
    'v_1.1.1' :{
        'general':{
            10: 10.910,
            5: 12.082,
            3: 13.170,
            2: 14.231,
            1: 16.575,
            0.5: 18.975,
        },
        'L1Menu_Collisions2023_v1_2_0':{
            10: 10.910,
            5: 12.082,
            3: 13.170,
            2: 14.231,
            1: 16.575,
            0.5: 18.975,
        },
        
    },
    'v_2.1.1' : {
        'general':{
            10: 8.549,
            5: 9.296,
            3: 10.023,
            2: 10.691,
            1: 11.871,
            0.5: 13.856,
        },
        'L1Menu_Collisions2023_v1_2_0':{
            10: 8.549,
            5: 9.296,
            3: 10.023,
            2: 10.691,
            1: 11.871,
            0.5: 13.856,
        },
    },
}