import matplotlib.pyplot as plt
import numpy as np
from fileres import FileRes
from parameters import Parameters
from graphs import Graphs



######analyse file - pressure - sensitivity
filePath="E:\\btrzpil\\EMPIR\\Works\\OperaSimulation\\ExtractorBenchmarkSimulation\\N2"
fileName="\\Benchmark_Extractor_pN2_i"
numberFile=3
pressureData=[10**i for i in range(-10, -1, 1)]
sensitivityData=[]

for i in range(1,numberFile+1):

	res = FileRes(filePath,fileName+str(i))
	res.readFile()
	param=Parameters()
	param.setDataResFile(res.lastIterationDataSimulation,res.nameEmitter,res.numberEmitter,res.numberSimulation)
	param.setPressure(pressureData)
	param.calculateSensitivity()
	sensitivityData.append(param.sensitivityData)
	
	param=Parameters()
	param.setDataResFile(res.firstIterationDataSimulation,res.nameEmitter,res.numberEmitter,res.numberSimulation)
	param.setPressure(pressureData)
	param.calculateSensitivity()
	sensitivityData.append(param.sensitivityData)

graphTitle=fileName
graphPath="E:\\btrzpil\\EMPIR\\Works\\Results\\BenchmarkSimulation"
labelLine=["last iteration, current1","first iteration, current1","last iteration, current2","first iteration, current2","last iteration, current3","first iteration, current3"]
graphs=Graphs(graphTitle,graphPath)
graphs.plotSensitivity(sensitivityData,pressureData,'Pressure [mbar]',labelLine)























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
##labelLine=["l","a","b","e","l"]
##voltageData=[(x + 1) * 100 for x in range(10)]
##graphs=Graphs(graphTitle,graphPath)
##graphs.plotSensitivity(sensitivityData,voltageData'Voltage [V]',labelLine)








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
##labelLine=["l","a","b","e","l"]
##graphs=Graphs(graphTitle,graphPath)

##graphs.plotSensitivity(sensitivityData,currentData'Current [A]',labelLine)

