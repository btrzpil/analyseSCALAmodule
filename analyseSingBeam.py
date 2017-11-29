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




# #//////////////////////////////////////////////////////////////////////////////////
# #///////////////////singBeam07/////////////////////////////////////////////////////
# #//////////////////////////////////////////////////////////////////////////////////

# gauge=ModelGauge()

# gauge.addEmitter(IonCollector('I_coll'))
# gauge.addEmitter(ElectronEmitter(['E_fil_prim','E_fil_back']))
# gauge.addEmitter(ElectronFaradayCup('E_far'))
# gauge.addEmitter(IonVacuumCurrent('I_Vac_1'))

# gauge.addBoundaryCondition(FaradayCup('FARADAY'))
# gauge.addBoundaryCondition(FaradayCollector('FARADAY_COLLECTOR'))



# filePath="E:\\btrzpil\\EMPIR\Works\\model2\\MDS\\singBeam07\\result"

# p_i=[]
# sen_i=[]
# eff_i=[]
# trans_i=[]
# path_i=[]
# yield_i=[]

# FaradayCup_i=[]
# FaradayCollector_i=[]

# x_i=[]
# label_i=[]
# baseFileName="\\c_1_"


# for i in range(0,3):

# 	p_j=[]
# 	sen_j=[]
# 	eff_j=[]
# 	trans_j=[]
# 	path_j=[]
# 	yield_j=[]	
	
	
# 	x_j=[]
# 	for j in range(0,4):

# 		fileName=baseFileName+str(2*i)+"_"+str(2*j)
# 		print(fileName)
# 		res=FileRes(filePath,fileName)
# 		res.readFile()
# 		param=ParametersGauge(gauge.emitters,gauge.boundaryConditions,res.simSettings, res.simData)
		
# 		p_j.append(param.pressure)
# 		sen_j.append(param.calculateSensitivityBenchmark())
# 		eff_j.append(param.calculateIonCollectionEfficency())
# 		trans_j.append(param.calculateElectronTransmissionEfficency())
# 		path_j.append(param.calculateTheoryMeanPathLengthPrimaryParticles())
# 		yield_j.append(param.calculateYield())
# 		x_j.append(param.FaradayCollectorCondition)

# 	label_j=param.FaradayCupCondition

# 	p_i.append(p_j)
# 	sen_i.append(sen_j)
# 	eff_i.append(eff_j)
# 	trans_i.append(trans_j)
# 	path_i.append(path_j)
# 	yield_i.append(yield_j)

# 	x_i.append(x_j)
# 	label_i.append(label_j)



# graphPath="E:\\btrzpil\\EMPIR\\Works\\model2\\analysisResult\\singBeam07\\graph"
# xData=x_i

# legendTitle=param.boundaryConditions["FaradayCup"]+' [V] '
# xAxLabel=param.boundaryConditions["FaradayCollector"] + ' [V]'

# graphName=baseFileName
# graphs=Graphs(graphName+'sen')
# graphs.plotSensitivity(xData,sen_i,xAxLabel,label_i,legendTitle,graphPath)

# graphs=Graphs(graphName+'ioneff')
# graphs.plotIonEfficency(xData,eff_i,xAxLabel,label_i,legendTitle,graphPath)

# graphs=Graphs(graphName+'yield')
# graphs.plotYield(xData,yield_i,xAxLabel,label_i,legendTitle,graphPath)

# graphs=Graphs(graphName+'path')
# graphs.plotMeanPathLengthPrimaryParticles(xData,path_i,xAxLabel,label_i,legendTitle,graphPath)

# graphs=Graphs(graphName+'transeff')
# graphs.plotTransmissionEfficency(xData,trans_i,xAxLabel,label_i,legendTitle,graphPath)


# #//////////////////////////////////////////////////////////////////////////////////
# #///////////////////singBeam08/////////////////////////////////////////////////////
# #//////////////////////////////////////////////////////////////////////////////////
# gauge=ModelGauge()

# gauge.addEmitter(IonCollector('I_coll'))
# gauge.addEmitter(ElectronEmitter(['E_fil_prim','E_fil_back']))
# gauge.addEmitter(ElectronFaradayCup('E_far'))
# gauge.addEmitter(IonVacuumCurrent('I_Vac_1'))

# gauge.addBoundaryCondition(FaradayCup('FARADAY'))
# gauge.addBoundaryCondition(FaradayCollector('FARADAY_COLLECTOR'))



# filePath="E:\\btrzpil\\EMPIR\Works\\model2\\MDS\\singBeam08\\result"



# p_i=[]
# sen_i=[]
# eff_i=[]
# trans_i=[]
# path_i=[]
# yield_i=[]

# FaradayCup_i=[]
# FaradayCollector_i=[]

# x_i=[]
# label_i=[]
# baseFileName="\\c_0_"


# for i in range(0,7):

# 	p_j=[]
# 	sen_j=[]
# 	eff_j=[]
# 	trans_j=[]
# 	path_j=[]
# 	yield_j=[]	
	
	
# 	x_j=[]
# 	for j in range(0,3):

# 		fileName=baseFileName+str(i)+"_"+str(2*j)
# 		print(fileName)
# 		res=FileRes(filePath,fileName)
# 		res.readFile()
# 		param=ParametersGauge(gauge.emitters,gauge.boundaryConditions,res.simSettings, res.simData)
		
# 		p_j.append(param.pressure)
# 		sen_j.append(param.calculateSensitivityBenchmark())
# 		eff_j.append(param.calculateIonCollectionEfficency())
# 		trans_j.append(param.calculateElectronTransmissionEfficency())
# 		path_j.append(param.calculateTheoryMeanPathLengthPrimaryParticles())
# 		yield_j.append(param.calculateYield())
# 		x_j.append(param.FaradayCollectorCondition)

# 	label_j=param.FaradayCupCondition

# 	p_i.append(p_j)
# 	sen_i.append(sen_j)
# 	eff_i.append(eff_j)
# 	trans_i.append(trans_j)
# 	path_i.append(path_j)
# 	yield_i.append(yield_j)

# 	x_i.append(x_j)
# 	label_i.append(label_j)



# graphPath="E:\\btrzpil\\EMPIR\\Works\\model2\\analysisResult\\singBeam08\\graph"
# xData=x_i

# legendTitle=param.boundaryConditions["FaradayCup"]+' [V] '
# xAxLabel=param.boundaryConditions["FaradayCollector"] + ' [V]'

# graphName=baseFileName

# graphs=Graphs(graphName+'sen')
# graphs.plotSensitivity(xData,sen_i,xAxLabel,label_i,legendTitle,graphPath)

# graphs=Graphs(graphName+'ioneff')
# graphs.plotIonEfficency(xData,eff_i,xAxLabel,label_i,legendTitle,graphPath)
# #wrong 
# graphs=Graphs(graphName+'yield')
# graphs.plotYield(xData,yield_i,xAxLabel,label_i,legendTitle,graphPath)

# graphs=Graphs(graphName+'path')
# graphs.plotMeanPathLengthPrimaryParticles(xData,path_i,xAxLabel,label_i,legendTitle,graphPath)

# graphs=Graphs(graphName+'transeff')
# graphs.plotTransmissionEfficency(xData,trans_i,xAxLabel,label_i,legendTitle,graphPath)


#//////////////////////////////////////////////////////////////////////////////////
#///////////////////singBeam09/////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////////

# gauge=ModelGauge()

# gauge.addEmitter(IonCollector('I_coll'))
# gauge.addEmitter(ElectronEmitter(['E_fil_prim','E_fil_back']))
# gauge.addEmitter(ElectronFaradayCup('E_far'))
# gauge.addEmitter(IonVacuumCurrent('I_Vac_1'))

# gauge.addBoundaryCondition(FaradayCup('FARADAY'))
# gauge.addBoundaryCondition(FaradayCollector('FARADAY_COLLECTOR'))

# filePath="E:\\btrzpil\\EMPIR\\Works\\model2\\MDS\\singBeam09\\result"
# #////////////////////////////////////a///////////////////////////////////////////




# p_i=[]
# sen_i=[]
# eff_i=[]
# trans_i=[]
# path_i=[]
# yield_i=[]

# FaradayCup_i=[]
# FaradayCollector_i=[]

# x_i=[]
# label_i=[]
# baseFileName="\\c_a_"


# for i in range(2,4):


# 	fileName=baseFileName+str(i)
# 	print(fileName)
# 	res=FileRes(filePath,fileName)
# 	res.readFile()
# 	param=ParametersGauge(gauge.emitters,gauge.boundaryConditions,res.simSettings, res.simData)
		
# 	p_i.append(param.pressure)
# 	sen_i.append(param.calculateSensitivityBenchmark())
# 	eff_i.append(param.calculateIonCollectionEfficency())
# 	trans_i.append(param.calculateElectronTransmissionEfficency())
# 	path_i.append(param.calculateTheoryMeanPathLengthPrimaryParticles())
# 	yield_i.append(param.calculateYield())
# 	x_i.append(i)

# label=param.FaradayCupCondition





# graphPath="E:\\btrzpil\\EMPIR\\Works\\model2\\analysisResult\\singBeam09\\graph"
# xData=x_i

# legendTitle=''
# xAxLabel='distance [mm]'

# graphName=baseFileName
# graphs=Graphs(graphName+'sen')
# graphs.plotSensitivity(xData,sen_i,xAxLabel,label,legendTitle,graphPath)

# graphs=Graphs(graphName+'ioneff')
# graphs.plotIonEfficency(xData,eff_i,xAxLabel,label,legendTitle,graphPath)

# graphs=Graphs(graphName+'yield')
# graphs.plotYield(xData,yield_i,xAxLabel,label,legendTitle,graphPath)

# graphs=Graphs(graphName+'path')
# graphs.plotMeanPathLengthPrimaryParticles(xData,path_i,xAxLabel,label,legendTitle,graphPath)

# graphs=Graphs(graphName+'transeff')
# graphs.plotTransmissionEfficency(xData,trans_i,xAxLabel,label,legendTitle,graphPath)


# #////////////////////////////////////a///////////////////////////////////////////


# p_i=[]
# sen_i=[]
# eff_i=[]
# trans_i=[]
# path_i=[]
# yield_i=[]

# FaradayCup_i=[]
# FaradayCollector_i=[]

# x_i=[]
# label_i=[]
# baseFileName="\\c_"


# for i in range(0,4):


# 	fileName=baseFileName+str(i)
# 	print(fileName)
# 	res=FileRes(filePath,fileName)
# 	res.readFile()
# 	param=ParametersGauge(gauge.emitters,gauge.boundaryConditions,res.simSettings, res.simData)
		
# 	p_i.append(param.pressure)
# 	sen_i.append(param.calculateSensitivityBenchmark())
# 	eff_i.append(param.calculateIonCollectionEfficency())
# 	trans_i.append(param.calculateElectronTransmissionEfficency())
# 	path_i.append(param.calculateTheoryMeanPathLengthPrimaryParticles())
# 	yield_i.append(param.calculateYield())
# 	x_i.append(i)

# label=param.FaradayCupCondition





# graphPath="E:\\btrzpil\\EMPIR\\Works\\model2\\analysisResult\\singBeam09\\graph"
# xData=x_i

# legendTitle=''
# xAxLabel='distance [mm]'

# graphName=baseFileName
# graphs=Graphs(graphName+'sen')
# graphs.plotSensitivity(xData,sen_i,xAxLabel,label,legendTitle,graphPath)

# graphs=Graphs(graphName+'ioneff')
# graphs.plotIonEfficency(xData,eff_i,xAxLabel,label,legendTitle,graphPath)

# graphs=Graphs(graphName+'yield')
# graphs.plotYield(xData,yield_i,xAxLabel,label,legendTitle,graphPath)

# graphs=Graphs(graphName+'path')
# graphs.plotMeanPathLengthPrimaryParticles(xData,path_i,xAxLabel,label,legendTitle,graphPath)

# graphs=Graphs(graphName+'transeff')
# graphs.plotTransmissionEfficency(xData,trans_i,xAxLabel,label,legendTitle,graphPath)





# #//////////////////////////////////////////////////////////////////////////////////
# #///////////////////singBeam10/////////////////////////////////////////////////////
# #//////////////////////////////////////////////////////////////////////////////////
# gauge=ModelGauge()

# gauge.addEmitter(IonCollector('I_coll'))
# gauge.addEmitter(ElectronEmitter(['E_fil_prim','E_fil_back']))
# gauge.addEmitter(ElectronFaradayCup('E_far'))
# gauge.addEmitter(IonVacuumCurrent('I_Vac_1'))

# gauge.addBoundaryCondition(FaradayCup('FARADAY'))
# gauge.addBoundaryCondition(FaradayCollector('FARADAY_COLLECTOR'))



# filePath="E:\\btrzpil\\EMPIR\Works\\model2\\MDS\\singBeam10\\result"



# p_i=[]
# sen_i=[]
# eff_i=[]
# trans_i=[]
# path_i=[]
# yield_i=[]

# FaradayCup_i=[]
# FaradayCollector_i=[]

# x_i=[]
# label_i=[]
# baseFileName="\\c_"

# coordinates=["x","y","z"]
# for i in range(0,3):

# 	p_j=[]
# 	sen_j=[]
# 	eff_j=[]
# 	trans_j=[]
# 	path_j=[]
# 	yield_j=[]	
	
	
# 	x_j=[]
# 	for j in range(-2,3):

# 		fileName=baseFileName+str(i)+str(j)
# 		print(fileName)
# 		res=FileRes(filePath,fileName)
# 		res.readFile()
# 		param=ParametersGauge(gauge.emitters,gauge.boundaryConditions,res.simSettings, res.simData)
		
# 		p_j.append(param.pressure)
# 		sen_j.append(param.calculateSensitivityBenchmark())
# 		eff_j.append(param.calculateIonCollectionEfficency())
# 		trans_j.append(param.calculateElectronTransmissionEfficency())
# 		path_j.append(param.calculateTheoryMeanPathLengthPrimaryParticles())
# 		yield_j.append(param.calculateYield())
# 		x_j.append(j)

# 	label_j=coordinates[i]

# 	p_i.append(p_j)
# 	sen_i.append(sen_j)
# 	eff_i.append(eff_j)
# 	trans_i.append(trans_j)
# 	path_i.append(path_j)
# 	yield_i.append(yield_j)

# 	x_i.append(x_j)
# 	label_i.append(label_j)



# graphPath="E:\\btrzpil\\EMPIR\\Works\\model2\\analysisResult\\singBeam10\\graph"
# xData=x_i

# legendTitle="Coordinates"
# xAxLabel="Distance [mm]"

# graphName=baseFileName

# graphs=Graphs(graphName+'sen')
# graphs.plotSensitivity(xData,sen_i,xAxLabel,label_i,legendTitle,graphPath)

# graphs=Graphs(graphName+'ioneff')
# graphs.plotIonEfficency(xData,eff_i,xAxLabel,label_i,legendTitle,graphPath)

# graphs=Graphs(graphName+'yield')
# graphs.plotYield(xData,yield_i,xAxLabel,label_i,legendTitle,graphPath)

# graphs=Graphs(graphName+'path')
# graphs.plotMeanPathLengthPrimaryParticles(xData,path_i,xAxLabel,label_i,legendTitle,graphPath)

# graphs=Graphs(graphName+'transeff')
# graphs.plotTransmissionEfficency(xData,trans_i,xAxLabel,label_i,legendTitle,graphPath)



#//////////////////////////////////////////////////////////////////////////////////
#///////////////////singBeam11/////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////////
gauge=ModelGauge()

gauge.addEmitter(IonCollector('I_coll'))
gauge.addEmitter(ElectronEmitter(['E_fil_prim','E_fil_back']))
gauge.addEmitter(ElectronFaradayCup('E_far'))
gauge.addEmitter(IonVacuumCurrent('I_Vac_1'))

gauge.addBoundaryCondition(FaradayCup('FARADAY'))
gauge.addBoundaryCondition(FaradayCollector('FARADAY_COLLECTOR'))



filePath="E:\\btrzpil\\EMPIR\Works\\model2\\MDS\\singBeam11\\result"



p_i=[]
sen_i=[]
eff_i=[]
trans_i=[]
path_i=[]
yield_i=[]

FaradayCup_i=[]
FaradayCollector_i=[]

x_i=[]
label_i=[]
baseFileName="\\c_"

coordinates=["x","y","z"]
for i in range(0,3):

	p_j=[]
	sen_j=[]
	eff_j=[]
	trans_j=[]
	path_j=[]
	yield_j=[]	
	
	
	x_j=[]
	for j in range(-2,3):

		fileName=baseFileName+str(i)+str(j)
		print(fileName)
		res=FileRes(filePath,fileName)
		res.readFile()
		param=ParametersGauge(gauge.emitters,gauge.boundaryConditions,res.simSettings, res.simData)
		
		p_j.append(param.pressure)
		sen_j.append(param.calculateSensitivityBenchmark())
		eff_j.append(param.calculateIonCollectionEfficency())
		trans_j.append(param.calculateElectronTransmissionEfficency())
		path_j.append(param.calculateTheoryMeanPathLengthPrimaryParticles())
		yield_j.append(param.calculateYield())
		x_j.append(j)

	label_j=coordinates[i]

	p_i.append(p_j)
	sen_i.append(sen_j)
	eff_i.append(eff_j)
	trans_i.append(trans_j)
	path_i.append(path_j)
	yield_i.append(yield_j)

	x_i.append(x_j)
	label_i.append(label_j)



graphPath="E:\\btrzpil\\EMPIR\\Works\\model2\\analysisResult\\singBeam11\\graph"
xData=x_i

legendTitle="Coordinates"
xAxLabel="Distance [mm]"

graphName=baseFileName

graphs=Graphs(graphName+'sen')
graphs.plotSensitivity(xData,sen_i,xAxLabel,label_i,legendTitle,graphPath)

graphs=Graphs(graphName+'ioneff')
graphs.plotIonEfficency(xData,eff_i,xAxLabel,label_i,legendTitle,graphPath)

graphs=Graphs(graphName+'yield')
graphs.plotYield(xData,yield_i,xAxLabel,label_i,legendTitle,graphPath)

graphs=Graphs(graphName+'path')
graphs.plotMeanPathLengthPrimaryParticles(xData,path_i,xAxLabel,label_i,legendTitle,graphPath)

graphs=Graphs(graphName+'transeff')
graphs.plotTransmissionEfficency(xData,trans_i,xAxLabel,label_i,legendTitle,graphPath)