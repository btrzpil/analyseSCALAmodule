import matplotlib.pyplot as plt
import numpy as np
from fileres import FileRes
from parameters import Parameters
from graphs import Graphs

#analyse ExtractorGauge Benchmark




######pressure - sensitivity
filePath="E:\\btrzpil\\EMPIR\\Works\\OperaSimulation\\ExtractorBenchmarkSimulation\\newMesh\\H2"
fileName="\\Benchmark_Extractor_pH2_100eV_i"
numberFile=3
pressureData=[(10**(i // 2)) * (5 if abs(i) % 2 else 1) for i in range(-20, -3, 1)]
sensitivityData=[]



for i in range(1,numberFile+1):

	res = FileRes(filePath,fileName+str(i)+"_mesh")
	print(res)
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

graphTitle=fileName+"_mesh"
graphPath="E:\\btrzpil\\EMPIR\\Works\\Results\\BenchmarkSimulation"
labelLine=["last iteration, current1","first iteration, current1","last iteration, current2","first iteration, current2","last iteration, current3","first iteration, current3"]
graphs=Graphs(graphTitle,graphPath)
graphs.plotSensitivity(sensitivityData,pressureData,'Pressure [mbar]',labelLine)