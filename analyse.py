import matplotlib.pyplot as plt
import numpy as np
from fileres import FileRes
from parameters import Parameters
from graphs import Graphs
from filetracks import FileTracks
##filePath="E:\\btrzpil\\OperaSimulations\\simulation Helmer Gauge\\res file"
##fileName="\\helmer_database"
##fileExtension=".res"


###t = [10e-10 for i in range(10)]

##numberFile=1
##sensitivityData=[]
##pressureData=[10**i for i in range(-13, 0, 1)]
##graphs=Graphs(["k","l","p","o"])
##graphs.setPressureData(pressureData)
##
##for i in range(numberFile):
##    inFile=filePath+fileName+str(i)+fileExtension
##    res = FileRes (inFile)
##    res.readFile()
##    param=Parameters(res.firstIterationDataSimulation,res.nameEmitter,res.numberEmitter,res.numberSimulation)
##    pressureData=[10**i for i in range(-13, 0, 1)]
##    print(len(param.sensitivityData))
##    param.calculateSensitivity(pressureData)
##    sensitivityData.append(param.sensitivityData)
##    print(i)
##
##
##
##
##graphs.plotSensitivityVsPressure(sensitivityData,pressureData)
    

filePath="E:\\btrzpil"
fileName="\\helmer"



tracks = FileTracks(filePath,fileName)

tracks.readFile()
tracks.debugTracks(3)
