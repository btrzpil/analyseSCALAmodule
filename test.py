# ##
# ##graphs=Graphs()
# ##
# ##graphs.plot2D(param.xPositionIons,param.zPositionIons,param.currentIons)
#                         # if charge==-1:
#                         # else:
#                         #     sumIon=sumIon+1
#                         #     for step in position:
#                         #         if (-1<=float(step[0])<=2.4)and(-2.75<=float(step[1])<=2.5)and(-1.55<=float(step[2])<=1):
#                         #             sumIonCollected=sumIonCollected+1
#                         #             break





#  filePath="E:\\btrzpil\\OperaSimulations\\shg\\sim\\pressure-h\\result"

# # pressureData=[10**i for i in range(-13, 0, 1)]

# # xlabelText='Pressure [mbar]'

# # meanPathPrimaryParticles=[]
# # ionCollectionEfficency=[]
# # for i in range(0,13):
# #   fileName="\\helmer_database0_"+str(i+1) 

# #   tracks = FileTracks(filePath,fileName)
# #   tracks.readFile()

# #   param=ParametersTrackParticles(tracks.tracksInformation,tracks.endPositionTrack)
# #   param.calculateMeanPathPrimaryParticles()
# #   param.calculateIonCollectionEfficency(2.4,-1.0,-2.75,2.5,1.0,-1.55)
# #   meanPathPrimaryParticles.append(param.meanPathPrimaryParticles)
# #   ionCollectionEfficency.append(param.ionCollectionEfficency)



# # graphPath="E:\\btrzpil\\Result\\Graph\\Helmer"
# # graphTitle="\\pressure_h_meanPathPrimaryParticles"
# # graphsPath=Graphs()
# # graphsPath.setGraphTitle(graphTitle)
# # graphsPath.setGraphPath(graphPath)
# # graphsPath.plotMeanPathPrimaryParticles(pressureData,meanPathPrimaryParticles,xlabelText)

# # graphTitle="\\pressure_h_ionCollectionEfficency"
# # graphsIonCollection=Graphs()
# # graphsIonCollection.setGraphTitle(graphTitle)
# # graphsIonCollection.setGraphPath(graphPath)
# # graphsIonCollection.plotIonCollectionEfficency(pressureData,ionCollectionEfficency,xlabelText)



# # filePath="E:\\btrzpil\\OperaSimulations\\shg\\sim\\current-h\\result"
# # res = FileRes(filePath,"\\helmer_database1")
# # res.readFile()
# # param=Parameters()
# # param.setDataResFile(res.lastIterationDataSimulation,res.nameEmitter,res.numberEmitter,res.numberSimulation)

# # currentData=param.currentEmitterData

# # xlabelText='Voltage [V]'
# # xlabelText='Current [A]'


# # meanPathPrimaryParticles=[]
# # ionCollectionEfficency=[]
# # for i in range(0,10):
# #   fileName="\\helmer_database2_"+str(i+1) 

# #   tracks = FileTracks(filePath,fileName)
# #   tracks.readFile()

# #   param=ParametersTrackParticles(tracks.tracksInformation,tracks.endPositionTrack)
# #   param.calculateMeanPathPrimaryParticles()
# #   param.calculateIonCollectionEfficency(2.4,-1.0,-2.75,2.5,1.0,-1.55)
# #   meanPathPrimaryParticles.append(param.meanPathPrimaryParticles)
# #   ionCollectionEfficency.append(param.ionCollectionEfficency)



# # graphPath="E:\\btrzpil\\Result\\Graph\\Helmer"
# # graphTitle="\\current_h_meanPathPrimaryParticles"
# # graphsPath=Graphs(graphTitle,graphPath)
# # graphsPath.plotMeanPathPrimaryParticles(currentData,meanPathPrimaryParticles,xlabelText)

# # graphTitle="\\current_h_ionCollectionEfficency"
# # graphsIonCollection=Graphs()
# # graphsIonCollection.setGraphTitle(graphTitle)
# # graphsIonCollection.setGraphPath(graphPath)
# # graphsIonCollection.plotIonCollectionEfficency(currentData,ionCollectionEfficency,xlabelText)
















# import subprocess



# subprocess.Popen("readtrac.exe E:\\btrzpil\\helmer_database0_1.tracks B E:\\btrzpil\\helmer_database0_1.txt")




#                         if (trackCounter==1):
#                             self.header = file.readline()#header
#                         else:
#                             file.readline()


#                         position=[]

#                         for step in range(NSTEP):
#                             position.append(file.readline().split()[1:4])
#                         if charge==-1:
#                         else:
#                             sumIon=sumIon+1
#                             for step in position:
#                                 if (-1<=float(step[0])<=2.4)and(-2.75<=float(step[1])<=2.5)and(-1.55<=float(step[2])<=1):
#                                     sumIonCollected=sumIonCollected+1
#                                     break


#     def setPressureData(self,pressureData):
#         self.pressureData=pressureData
        
#     def setVoltageData(self,voltageData):
#         self.voltageData=voltageData
        
#     def setCurrentData(self,currentData):
#         self.currentData=currentData

# def plotSensitivityVsVoltage(self,sensitivityData,voltageData):
#         self.setVoltageData(voltageData)
        
#         xlabelText='Voltage [V]'
#         ylabelText='Sensitivity $[mbar^{-1}]$'
        
#         fig, ax = self.setFigure(xlabelText,ylabelText)
        
#         numberFile=len(sensitivityData)

#         for counterFile in range(numberFile):
#             yData=[sensitivityData[counterFile][i] for i in range(len(sensitivityData[counterFile]))]
#             self.plotLine(self.voltageData,yData,ax,self.lineType[counterFile],self.labelName[counterFile])

#         self.setLegend(fig, ax)
#         self.saveFigure(fig)




        
#     def plotSenistivityVsCurrent(self,sensitivityData,currentData):
#         self.setCurrentData(currentData)
#         xData=[]
#         yData=[]
        
#         xlabelText='Current [A]'
#         ylabelText='Sensitivity $[mbar^{-1}]$'
        
#         fig, ax = self.setFigure(xlabelText,ylabelText)


#         numberFile=len(sensitivityData)

#         for counterFile in range(numberFile):
#             yData=[sensitivityData[counterFile][i] for i in range(len(sensitivityData[counterFile]))]
#             xData=[currentData[counterFile][i] for i in range(len(currentData[counterFile]))]

#             ax.plot(xData, yData,'r-*',label='')


#         #self.setLegend(fig, ax)
#         self.saveFigure(fig)
        
#     def plotSensitivityVsPressure(self,sensitivityData,pressureData):

#         self.setPressureData(pressureData)
        
#         xlabelText='Pressure [mbar]'
#         ylabelText='Sensitivity $[mbar^{-1}]$'
        
#         fig, ax = self.setFigure(xlabelText,ylabelText)

#         numberFile=len(sensitivityData)

#         for counterFile in range(numberFile):
#             yData=[sensitivityData[counterFile][i] for i in range(len(sensitivityData[counterFile]))]
#             self.plotLine(self.pressureData,yData,ax,self.lineType[counterFile],self.labelName[counterFile])

#         ax.set_xscale('log')
#         self.setLegend(fig, ax)
#         self.saveFigure(fig)

import matplotlib.pyplot as plt
import numpy as np
from fileres import FileRes
from parameters import Parameters
from graphs import Graphs
from filedat import FileDat

#analyse ExtractorGauge Benchmark



######pressure - sensitivity
fileResPath="E:\\btrzpil\\EMPIR\\Works\\OperaSimulation\\ExtractorBenchmarkSimulation\\thread\\result"
fileResName="\\Benchmark_Extractor_pH2_100eV_i1"
fileDatPath="E:\\btrzpil\\EMPIR\\Works\\Results\\BenchmarkSimulation\\data"
fileDatName="\\Benchmark_Extractor_pH2_100eV_i1_potential_line-10sim_"
titleLegend="Pressure residual gas [mbar]"
graphTitle=fileDatName
graphPath="E:\\btrzpil\\EMPIR\\Works\\Results\\BenchmarkSimulation\\potentialProfile\\graph"

numberCase=16


graphs=Graphs(graphTitle,graphPath)



res = FileRes(fileResPath,fileResName)
res.readFile()   
pressureData=res.xValue


labelLine = [str(pressure) for pressure in pressureData]

distanceData=[]
potentialData=[]
for i in range(1,numberCase+1):

    fileDat = FileDat(fileDatPath,fileDatName+str(i))

    fileDat.readFile()

    distanceData.append(fileDat.distanceData)
    potentialData.append(fileDat.potentialData)



graphs.plotPotentialProfile(distanceData,potentialData,labelLine,titleLegend)