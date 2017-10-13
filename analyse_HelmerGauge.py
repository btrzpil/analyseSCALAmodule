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

from filetracks import FileTracks
from parameterstrackparticle import ParametersTrackParticles
import time



filePath="E:\\btrzpil\\OperaSimulations\\shg\\sim\\deflector-h"
for i in range(0,10):
	fileName="\\model_helmer_database_"+str(i+1) 
	tracks = FileTracks(filePath,fileName)
	tracks.parseFile()
	time.sleep(30)


	
modelGauge=Cylinder("cylinder",[0,0,-4.0,6.0,4.0])
modelCollector=Cuboid("cuboid",[2.4,-1.0,-2.75,2.5,1.0,-1.55])
modelReflaction=Cylinder("cylinder",[0,0,-0.1,0.1,0.3])
filePath="E:\\btrzpil\\OperaSimulations\\shg\\sim\\pressure-h\\result"
pressureData=[10**i for i in range(-13, 0, 1)]
xData=pressureData
xlabelText='Pressure [mbar]'
meanPathPrimaryParticles=[]
ionCollectionEfficency=[]
ionReflactionEfficency=[]
ionVolumeEfficency=[]
for i in range(0,13):
	fileName="\\helmer_database0_"+str(i+1) 
	tracks = FileTracks(filePath,fileName)
	tracks.readFile()
	param=ParametersTrackParticles(tracks.trajectories)
	MeanPathPrimaryParticles=param.calculateMeanPathPrimaryParticles()
	meanPathPrimaryParticles.append(MeanPathPrimaryParticles)

	# IonCollectionEfficency=param.calculateIonCollectionEfficency(modelCollector)
	# ionCollectionEfficency.append(IonCollectionEfficency)

	# IonReflactionEfficency=param.calculateIonVolumeEfficency(modelReflaction,modelGauge)
	# ionReflactionEfficency.append(IonReflactionEfficency)

	# IonVolumeEfficency=param.calculateIonVolumeEfficency(modelCollector,modelReflaction)
	# ionVolumeEfficency.append(IonVolumeEfficency)
    def plotMeanPathPrimaryParticles(self,xData,meanPathPrimaryParticlesData,xAxLabel,lineLabel,legendTitle,graphPath):

graphPath="E:\\btrzpil\\Result\\Graph\\Helmer\\Track"
graphTitle="\\pressure_h_meanPathPrimaryParticles"
graphMeanPath=Graphs(graphTitle,graphPath)
graphMeanPath.plotMeanPathPrimaryParticles(xData,meanPathPrimaryParticles,xlabelText)

# graphPath="E:\\btrzpil\\Result\\Graph\\Helmer\\Track"
# graphTitle="\\pressure_h_ionCollectionEfficency"
# graphMeanPath=Graphs(graphTitle,graphPath)
# graphMeanPath.plotIonEfficency(xData,ionCollectionEfficency,xlabelText)

# graphPath="E:\\btrzpil\\Result\\Graph\\Helmer\\Track"
# graphTitle="\\pressure_h_ionReflactionEfficency"
# graphMeanPath=Graphs(graphTitle,graphPath)
# graphMeanPath.plotIonEfficency(xData,ionReflactionEfficency,xlabelText)

# graphPath="E:\\btrzpil\\Result\\Graph\\Helmer\\Track"
# graphTitle="\\pressure_h_ionVolumeEfficency"
# graphMeanPath=Graphs(graphTitle,graphPath)
# graphMeanPath.plotIonEfficency(xData,ionVolumeEfficency,xlabelText)
