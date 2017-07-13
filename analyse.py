import matplotlib.pyplot as plt
import numpy as np
from fileres import FileRes
from parameters import Parameters
from graphs import Graphs
from filetracks import FileTracks

######analyse file - pressure 
##filePath="E:\\btrzpil\\OperaSimulations\\simulation Helmer Gauge\\res file\\research - pressure"
##fileName="\\helmer_database"
##numberFile=4
##pressureData=[10**i for i in range(-13, 0, 1)]
##sensitivityData=[]
##for i in range(numberFile):
##
##    res = FileRes(filePath,fileName+str(i))
##    res.readFile()
##    param=Parameters()
##    param.setDataResFile(res.lastIterationDataSimulation,res.nameEmitter,res.numberEmitter,res.numberSimulation)
##    param.setPressure(pressureData)
##    param.calculateSensitivity()
##    sensitivityData.append(param.sensitivityData)
##
##    
##graphTitle="\\pressure"
##graphPath="E:\\btrzpil\\Result\\Graph\\Helmer"
##labelLegend=["l","a","b","e","l"]
##
##graphs=Graphs()
##graphs.setGraphLabel(labelLegend)
##graphs.setGraphTitle(graphTitle)
##graphs.setGraphPath(graphPath)
##graphs.plotSensitivityVsPressure(sensitivityData,pressureData)

######analyse file - voltage
##filePath="E:\\btrzpil\\OperaSimulations\\simulation Helmer Gauge\\res file\\research - deflector, grid, filament, suppressor\\current_density0.0015"
##fileName="\\helmer_database-"
##numberFile=5
##pressureData=[1e-10 for i in range(10)]
##sensitivityData=[]
##for i in range(1,numberFile):
##
##    res = FileRes(filePath,fileName+str(i))
##    res.readFile()
##    param=Parameters()
##    param.setDataResFile(res.lastIterationDataSimulation,res.nameEmitter,res.numberEmitter,res.numberSimulation)
##    param.setPressure(pressureData)
##    param.calculateSensitivity()
##    sensitivityData.append(param.sensitivityData)
##
##    
##graphTitle="\\voltage"
##graphPath="E:\\btrzpil\\Result\\Graph\\Helmer"
##labelLegend=["l","a","b","e","l"]
##voltageData=[(x + 1) * 100 for x in range(10)]
##graphs=Graphs()
##graphs.setGraphLabel(labelLegend)
##graphs.setGraphTitle(graphTitle)
##graphs.setGraphPath(graphPath)
##graphs.plotSensitivityVsVoltage(sensitivityData,voltageData)


######analyse file - current
##filePath="E:\\btrzpil\\OperaSimulations\\simulation Helmer Gauge\\res file\\research - current\\new"
##fileName="\\helmer_database"
##numberFile=6
##pressureData=[1e-10 for i in range(10)]
##sensitivityData=[]
##currentData=[]
##for i in range(1,numberFile):
##
##    res = FileRes(filePath,fileName+str(i))
##    res.readFile()
##    param=Parameters()
##    param.setDataResFile(res.lastIterationDataSimulation,res.nameEmitter,res.numberEmitter,res.numberSimulation)
##    param.setPressure(pressureData)
##    param.calculateSensitivity()
##    sensitivityData.append(param.sensitivityData)
##    currentData.append(param.currentEmitterData)
##
##
##graphTitle="\\current"
##graphPath="E:\\btrzpil\\Result\\Graph\\Helmer"
##labelLegend=["l","a","b","e","l","l","o","n","g"]
##
##graphs=Graphs()
##graphs.setGraphLabel(labelLegend)
##graphs.setGraphTitle(graphTitle)
##graphs.setGraphPath(graphPath)
##graphs.plotSenistivityVsCurrent(sensitivityData,currentData)




##
##filePath="E:\\btrzpil"
##fileName="\\helmer"
filePath="E:\\btrzpil\\OperaSimulations\\simulation Helmer Gauge\\research\\research - pressure\\result"
fileName="\\helmer_database0_1"
programPath="C:\\Program Files\\Vector Fields\\Opera 18R2 x64\\code\\bin"

tracks = FileTracks()
tracks.setFilePath(filePath)
tracks.setFileName(fileName)
tracks.setReadtrackPath(programPath)
tracks.parseFile()
##tracks.readFile()
##
##
##param=Parameters()
##param.setTracksInformation(tracks.tracksInformation,tracks.startPositionTrack)
##param.calculateMeanPathPrimaryParticles()
##
##graphs=Graphs()
##
##graphs.plot2D(param.xPositionIons,param.zPositionIons,param.currentIons)

