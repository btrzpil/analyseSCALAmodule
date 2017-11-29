import matplotlib.pyplot as pltsimData
import numpy as np

from filedat import FileDat
from fileres import FileRes



from filetracks import FileTracks

from parameterstrackparticle import ParametersTrackParticles
from parameterstrackparticle import Volume
from parameterstrackparticle import Cylinder
from parameterstrackparticle import Cuboid

from parametersgauge import ParametersGauge

from modelgauge import BoundaryCondition, Emitter
from modelgauge import ModelGauge
from modelgauge import IonCollector, ElectronEmitter,ElectronFaradayCup,IonVacuumCurrent
from modelgauge import Collector, Filament,FaradayCup,FaradayCollector,Wehnelt
from graphs import Graphs

import time

#//////////////////////////////////////////////////////////////////////////////////
#///////////////////mod1/////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////////
filePath="E:\\btrzpil\\OperaSimulations\\extractorGauge\\MDS\\mod1\\result"
graphPath="E:\\btrzpil\\OperaSimulations\\extractorGauge\\analysisResult\\mod1\\graph"
dataPath="E:\\btrzpil\\OperaSimulations\\extractorGauge\\analysisResult\\mod1\\data"
#//////////////////////////////////////////////////////////////////////////////////
#///////////////////mod2/////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////
# filePath="E:\\btrzpil\\OperaSimulations\\extractorGauge\\MDS\\mod2\\result"
# graphPath="E:\\btrzpil\\OperaSimulations\\extractorGauge\\analysisResult\\mod2\\graph"
# dataPath="E:\\btrzpil\\OperaSimulations\\extractorGauge\\analysisResult\\mod2\\data"
gauge=ModelGauge()

gauge.addEmitter(IonCollector('I_coll'))
gauge.addEmitter(ElectronEmitter(['E_fil_prim','E_fil_back']))
gauge.addEmitter(IonVacuumCurrent('I_Vac'))







baseFileName="\\c_"

p_i=[]
sen_i=[]
eff_i=[]
path_i=[]
yield_i=[]
x_i=[]
label_i=[]


for k in range(0,3):
	p_j=[]
	sen_j=[]
	eff_j=[]
	path_j=[]
	yield_j=[]	
	x_j=[]	
	for i in range(0,9):

		for j in range(1,5):

			fileName=baseFileName+str(k)+"_"+str(i)+"_"+str(2*j-1)
			print(fileName)
			res=FileRes(filePath,fileName)
			res.readFile()
			param=ParametersGauge(gauge.emitters,gauge.boundaryConditions,res.simSettings, res.simData)
		
			p_j.append(param.pressure)
			sen_j.append(param.calculateSensitivity())
			eff_j.append(param.calculateIonCollectionEfficency())
			path_j.append(param.calculateTheoryMeanPathLengthPrimaryParticles())
			yield_j.append(param.calculateYield())
			x_j.append(param.pressure)



	label_i.append("%.2f" % round(param.electronEmitterCurrent*1000,2))

	p_i.append(p_j)
	sen_i.append(sen_j)
	eff_i.append(eff_j)
	path_i.append(path_j)
	yield_i.append(yield_j)
	x_i.append(x_j)



xData=x_i

legendTitle="Emission current [mA]"
xAxLabel='Pressure [mbar]'

graphName=baseFileName
graphs=Graphs(graphName+'sen')
graphs.plotSensitivity(xData,sen_i,xAxLabel,label_i,legendTitle,graphPath)

graphs=Graphs(graphName+'ioneff')
graphs.plotIonEfficency(xData,eff_i,xAxLabel,label_i,legendTitle,graphPath)

graphs=Graphs(graphName+'yield')
graphs.plotYield(xData,yield_i,xAxLabel,label_i,legendTitle,graphPath)

graphs=Graphs(graphName+'path')
graphs.plotMeanPathLengthPrimaryParticles(xData,path_i,xAxLabel,label_i,legendTitle,graphPath)
# //pressure


k=0
for z in range (-10, 31, 10):
	label_i=[]

	distanceData=[]
	potentialData=[]

	for i in range(0,9):

	#for j in range(1,5):
		j=1
		fileName=baseFileName+str(k)+"_"+str(i)+"_"+str(2*j-1)
		print(fileName)
		res=FileRes(filePath,fileName)
		res.readFile()
		param=ParametersGauge(gauge.emitters,gauge.boundaryConditions,res.simSettings, res.simData)

		label_i.append(param.pressure)

		fileDat = FileDat(dataPath,fileName+"_potential_line"+str(z))
		fileDat.readFile()
		distanceData.append(fileDat.distanceData)
		potentialData.append(fileDat.potentialData)

	graphName=baseFileName
	legendTitle='Pressure [mbar]'
	graphs=Graphs(baseFileName+'c_'+str(k)+'_p_potential_line'+str(z))
	graphs.plotPotentialProfile(distanceData,potentialData,label_i,legendTitle,graphPath)
	# //current
for z in range (-10, 31, 10):
	label_i=[]

	distanceData=[]
	potentialData=[]
	for k in range(0,3):

		#for j in range(1,5):
		i=1
		j=1

		fileName=baseFileName+str(k)+"_"+str(i)+"_"+str(2*j-1)
		res=FileRes(filePath,fileName)
		res.readFile()
		param=ParametersGauge(gauge.emitters,gauge.boundaryConditions,res.simSettings, res.simData)
		label_i.append("%.2f" % round(param.electronEmitterCurrent*1000,2))

		fileDat = FileDat(dataPath,fileName+"_potential_line"+str(z))
		fileDat.readFile()
		distanceData.append(fileDat.distanceData)
		potentialData.append(fileDat.potentialData)

	graphName=baseFileName
	legendTitle="Emission current [mA]"
	graphs=Graphs(baseFileName+"p_"+str(i)+"_"+str(2*j-1)+'_c_potential_line'+str(z))
	graphs.plotPotentialProfile(distanceData,potentialData,label_i,legendTitle,graphPath)



# #//////////////////////////////////////////////////////////////////////////////////
# #///////////////////mod3/////////////////////////////////////////////////////
# #//////////////////////////////////////////////////////////////////////////////////

# gauge=ModelGauge()


# gauge.addEmitter(IonCollector('I_coll'))
# gauge.addEmitter(ElectronEmitter(['E_fil_prim','E_fil_back']))
# gauge.addEmitter(IonVacuumCurrent('I_Vac'))




# filePath="E:\\btrzpil\\OperaSimulations\\extractorGauge\\MDS\\mod3\\result"

# p_j=[]
# sen_j=[]
# eff_j=[]
# # trans_i=[]
# path_j=[]
# yield_j=[]


# x_j=[]
# label_j=[]
# baseFileName="\\c_1_"


# for i in range(0,9):

# 	for j in range(1,5):

# 		fileName=baseFileName+str(i)+"_"+str(2*j-1)
# 		res=FileRes(filePath,fileName)
# 		res.readFile()
# 		param=ParametersGauge(gauge.emitters,gauge.boundaryConditions,res.simSettings, res.simData)
		
# 		p_j.append(param.pressure)
# 		sen_i.append(param.calculateSensitivity())
# 		eff_i.append(param.calculateIonCollectionEfficency())
# 		# trans_i.append(param.calculateElectronTransmissionEfficency())
# 		path_i.append(param.calculateTheoryMeanPathLengthPrimaryParticles())
# 		yield_i.append(param.calculateYield())
# 		x_i.append(param.pressure)

# label_i=param.electronEmitterCurrent*1000



# graphPath="E:\\btrzpil\\OperaSimulations\\extractorGauge\\analysisResult\\mod3\\graph"
# xData=x_i

# legendTitle="Emission current [mA]"
# xAxLabel='Pressure [mbar]'

# graphName=baseFileName
# graphs=Graphs(graphName+'sen')
# graphs.plotSensitivity(xData,sen_i,xAxLabel,label_i,legendTitle,graphPath)

# graphs=Graphs(graphName+'ioneff')
# graphs.plotIonEfficency(xData,eff_i,xAxLabel,label_i,legendTitle,graphPath)

# graphs=Graphs(graphName+'yield')
# graphs.plotYield(xData,yield_i,xAxLabel,label_i,legendTitle,graphPath)

# graphs=Graphs(graphName+'path')
# graphs.plotMeanPathLengthPrimaryParticles(xData,path_i,xAxLabel,label_i,legendTitle,graphPath)

# # graphs=Graphs(graphName+'transeff')
# # graphs.plotTransmissionEfficency(xData,trans_i,xAxLabel,label_i,legendTitle,graphPath)
























