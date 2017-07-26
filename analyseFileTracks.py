import matplotlib.pyplot as plt
import numpy as np
from fileres import FileRes
from parameters import Parameters
from graphs import Graphs
from filetracks import FileTracks
from parameterstrackparticle import ParametersTrackParticles
from volume import Volume
from volume import Cylinder
from volume import Cuboid
import time





modelGauge=Cylinder("cylinder",[0,0,-4.0,6.0,4.0])
modelCollector=Cuboid("cuboid",[2.4,-1.0,-2.75,2.5,1.0,-1.55])
modelReflaction=Cylinder("cylinder",[0,0,-0.1,0.1,0.3])
filePath="E:\\btrzpil\\OperaSimulations\\shg\\sim\\pressure-h\\result"
meanPathPrimaryParticles=[]
ionCollectionEfficency=[]
ionVolumeEfficency=[]
for i in range(0,13):
	fileName="\\helmer_database0_"+str(i+1) 
	tracks = FileTracks(filePath,fileName)
	tracks.readFile()
	param=ParametersTrackParticles(tracks.trajectories)
	MeanPathPrimaryParticles=param.calculateMeanPathPrimaryParticles()
	meanPathPrimaryParticles.append(MeanPathPrimaryParticles)
	IonCollectionEfficency=param.calculateIonCollectionEfficency(modelCollector)
	ionCollectionEfficency.append(IonCollectionEfficency)
	IonVolumeEfficency=param.calculateIonVolumeEfficency(modelCollector,modelReflaction)
	ionVolumeEfficency.append(IonVolumeEfficency)



