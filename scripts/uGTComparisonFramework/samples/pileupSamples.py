from .sample import sample
import os

listOfFiles = []

EZBPaths = (
    '/hdfs/store/user/aloelige/EphemeralZeroBias1/CICADA_EphemeralZeroBias1_Feb2023/230217_183452/0000/',
    '/hdfs/store/user/aloelige/EphemeralZeroBias2/CICADA_EphemeralZeroBias2_Feb2023/230217_183512/0000/',
    '/hdfs/store/user/aloelige/EphemeralZeroBias2/CICADA_EphemeralZeroBias2_Feb2023/230217_183512/0001/',
    '/hdfs/store/user/aloelige/EphemeralZeroBias2/CICADA_EphemeralZeroBias2_Feb2023/230217_183512/0002/',
    '/hdfs/store/user/aloelige/EphemeralZeroBias3/CICADA_EphemeralZeroBias3_Feb2023/230217_183532/0000/',
    '/hdfs/store/user/aloelige/EphemeralZeroBias3/CICADA_EphemeralZeroBias3_Feb2023/230217_183532/0001/',
    '/hdfs/store/user/aloelige/EphemeralZeroBias3/CICADA_EphemeralZeroBias3_Feb2023/230217_183532/0002/',
    '/hdfs/store/user/aloelige/EphemeralZeroBias5/CICADA_EphemeralZeroBias5_Feb2023/230217_183613/0000/',
    '/hdfs/store/user/aloelige/EphemeralZeroBias6/CICADA_EphemeralZeroBias6_Feb2023/230217_183633/0000/',
    '/hdfs/store/user/aloelige/EphemeralZeroBias6/CICADA_EphemeralZeroBias6_Feb2023/230217_183633/0001/',
    '/hdfs/store/user/aloelige/EphemeralZeroBias7/CICADA_EphemeralZeroBias71_Feb2023/230217_183653/0000/',
)

for path in EZBPaths:
    for fileName in [path+x for x in os.listdir(path)]:
        listOfFiles.append(fileName)

pileupSample = sample(listOfFiles)