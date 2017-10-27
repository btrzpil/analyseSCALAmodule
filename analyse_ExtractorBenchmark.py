import matplotlib.pyplot as plt
import numpy as np
from fileres import FileRes
from parameters import Parameters
from graphs import Graphs
from filedat import FileDat
from filetracks import FileTracks
from parameterstrackparticle import ParametersTrackParticles
from parameterstrackparticle import Volume
from parameterstrackparticle import Cylinder
from parameterstrackparticle import Cuboid
import time
#analyse ExtractorGauge Benchmark


#parse file .track
#filePath="E:\\btrzpil\\EMPIR\\Works\\Sim\\extractor\\result"
#numberCase=16
#for i in range(1,numberCase+1):
#	fileName="\\ex_pH2_100eV_i3_"+str(i) 
#	tracks = FileTracks(filePath,fileName)
#	tracks.parseFile()
#	time.sleep(30)





filePath="E:\\btrzpil\\EMPIR\\Works\\Sim\\extractor\\result"
fileName="\\Benchmark_Extractor_pH2_100eV_i"
fileNameTrack="\\ex_pH2_100eV_i2_i"
numberFile=3
numberCase=16

lineLabel=[]
pressureData=[]
yieldData=[]

meanPathLengthPrimaryParticlesData=[] #theory, calculation from res file
stepLengthNSTEPData=[] #calculation from tracks file, NSTEP*stepLength
meanPathLengthElectronsData=[] #calculation from tracks file, vector
for i in range(1,numberFile+1):
	res = FileRes(filePath,fileName+str(i))
	res.readFile()
	pressure=res.valueTitle
	pressureData.append(pressure)
	stepLengthNSTEP=[]
	meanPathLengthElectrons=[]
	param=Parameters(res.lastIterationDataSimulation,res.nameEmitter,res.numberEmitter,res.numberSimulation,pressure)
	param.calculateYield()
	yieldData.append(param.yieldCalculation)
	param.calculateMeanPathLengthPrimaryParticles()
	meanPathLengthPrimaryParticlesData.append(param.meanPathLengthPrimaryParticles)

	for j in range(1,numberCase+1):
		fileNameTrack="\\ex_pH2_100eV_i"+str(i)+"_"+str(j)
		tracks = FileTracks(filePath,fileNameTrack)
		tracks.readFile()
		param=ParametersTrackParticles(tracks.trajectories)
		param.calculateStepLengthNSTEP()
		stepLengthNSTEP.append(param.stepLengthNSTEP)
		param.calculateMeanPathLengthElectrons()
		meanPathLengthElectrons.append(param.meanPathLengthElectrons)

	stepLengthNSTEPData.append(stepLengthNSTEP)	
	meanPathLengthElectronsData.append(meanPathLengthElectrons)

	lineLabel.append(str(i))



xData=pressureData
graphTitle=fileName
legendTitle="Emission current [mA]"
xAxLabel='Pressure [mbar]'

#yData=meanPathLengthPrimaryParticlesData
#graphPath="E:\\btrzpil\\EMPIR\\Works\\Results\\BenchmarkSimulation\\meanPathLengthPrimaryParticle\\res"
#graphs=Graphs(graphTitle)
#graphs.plotMeanPathLengthPrimaryParticles(xData,yData,xAxLabel,lineLabel,legendTitle,graphPath)

yData=yieldData
graphPath="E:\\btrzpil\\EMPIR\\Works\\Results\\BenchmarkSimulation\\yield"
graphs=Graphs(graphTitle)
graphs.plotYield(xData,yData,xAxLabel,lineLabel,legendTitle,graphPath)

#yData=stepLengthNSTEPData
#graphPath="E:\\btrzpil\\EMPIR\\Works\\Results\\BenchmarkSimulation\\meanPathLengthPrimaryParticle\\track_mean_step"
#graphs=Graphs(graphTitle)
#graphs.plotMeanPathLengthPrimaryParticles(xData,yData,xAxLabel,lineLabel,legendTitle,graphPath)

#yData=meanPathLengthElectronsData
#graphPath="E:\\btrzpil\\EMPIR\\Works\\Results\\BenchmarkSimulation\\meanPathLengthPrimaryParticle\\track_vector"
#graphs=Graphs(graphTitle)
#graphs.plotMeanPathLengthPrimaryParticles(xData,yData,xAxLabel,lineLabel,legendTitle,graphPath)




# # ######pressure - sensitivity
# filePath="E:\\btrzpil\\EMPIR\\Works\\Sim\\extractor\\result"
# fileName="\\Benchmark_Extractor_pH2_100eV_i"

# numberFile=3
# sensitivityData=[]
# pressureData=[]
# lineLabel=[]
# for i in range(1,numberFile+1):
	
# 	res = FileRes(filePath,fileName+str(i))
# 	res.readFile()
# 	pressure=res.valueTitle
# 	pressureData.append(pressure)
# 	pressureData.append(pressure)
# 	param=Parameters(res.lastIterationDataSimulation,res.nameEmitter,res.numberEmitter,res.numberSimulation,pressure)
# 	param.calculateSensitivity()
# 	sensitivityData.append(param.sensitivityData)

# 	lineLabel.append(str(i))
# 	lineLabel.append(str(i))	
# 	param=Parameters(res.firstIterationDataSimulation,res.nameEmitter,res.numberEmitter,res.numberSimulation,pressure)
# 	param.calculateSensitivity()
# 	sensitivityData.append(param.sensitivityData)
	

# legendTitle="Emission current [mA]"
# xAxLabel='Pressure [mbar]'
# graphTitle=fileName
# graphPath="E:\\btrzpil\\EMPIR\\Works\\Results\\BenchmarkSimulation\\sensitivity"
# graphs=Graphs(graphTitle)
# graphs.plotSensitivity(pressureData,sensitivityData,xAxLabel,lineLabel,legendTitle,graphPath)







# #potential line
# fileResPath="E:\\btrzpil\\EMPIR\\Works\\Sim\\extractor\\result"
# fileResName="\\Benchmark_Extractor_pH2_100eV_i1"
# fileDatPath="E:\\btrzpil\\EMPIR\\Works\\Results\\BenchmarkSimulation\\data"
# fileDatName="\\Benchmark_Extractor_pH2_100eV_i1_potential_line-10sim_"
# legendTitle="Pressure residual gas [mbar]"
# graphTitle=fileDatName
# graphPath="E:\\btrzpil\\EMPIR\\Works\\Results\\BenchmarkSimulation\\potentialProfile\\graph"

# numberCase=16
# graphs=Graphs(graphTitle)

# res = FileRes(fileResPath,fileResName)
# res.readFile()   
# pressure=res.valueTitle
# lineLabel = [str(p) for p in pressure]
# distanceData=[]
# potentialData=[]
# for i in range(1,numberCase+1):

#     fileDat = FileDat(fileDatPath,fileDatName+str(i))

#     fileDat.readFile()

#     distanceData.append(fileDat.distanceData)
#     potentialData.append(fileDat.potentialData)


# graphs.plotPotentialProfile(distanceData,potentialData,lineLabel,legendTitle,graphPath)



















# numberFile=1
# pressureData=[1e-7 for i in range(6)]
# pressureData.append([1e-7 for i in range(6)])

# sensitivityData=[]

# filePath='E:\\btrzpil\\EMPIR\\Works\\OperaSimulation\\ExtractorBenchmarkSimulation\\Benchmark_Extractor_test\\result\\multithreads\\mol03'
# fileName="\\Benchmark_Extractor_test_manual"



# res = FileRes(filePath,fileName)
# res.readFile()
# param=Parameters()
# param.setDataResFile(res.lastIterationDataSimulation,res.nameEmitter,res.numberEmitter,res.numberSimulation)
# param.setPressure(pressureData)
# param.calculateSensitivity()
# sensitivityData.append(param.sensitivityData)
	
# param=Parameters()
# param.setDataResFile(res.firstIterationDataSimulation,res.nameEmitter,res.numberEmitter,res.numberSimulation)
# param.setPressure(pressureData)
# param.calculateSensitivity()
# sensitivityData.append(param.sensitivityData)

# graphPath="E:\\btrzpil\\EMPIR\\Works\\Results\\BenchmarkSimulation"
# legendTitle=""
# xAxLabel='sim'
# graphTitle=fileName

# lineLabel=["last iteration","first iteration"]

# graphs=Graphs(graphTitle)
# xData=[1,2,3,4,5,6]



# graphs=Graphs(graphTitle)
# graphs.plotSensitivity(xData,sensitivityData,xAxLabel,lineLabel,legendTitle,graphPath)