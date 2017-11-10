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






gauge=ModelGauge()

gauge.addEmitter(IonCollector('I_coll'))
gauge.addEmitter(ElectronEmitter(['E_fil_prim','E_fil_back']))
gauge.addEmitter(ElectronFaradayCup('E_far'))
gauge.addEmitter(IonVacuumCurrent('I_Vac_1'))

gauge.addBoundaryCondition(FaradayCup('FARADAY'))
gauge.addBoundaryCondition(FaradayCollector('FARADAY_COLLECTOR'))



filePath="E:\\btrzpil\\EMPIR\\Works\\Sim\\proposal2\\sBeam07res"
lineLabel=[]
pressureData=[]
yieldData=[]

p_i=[]
sen_i=[]
eff_i=[]
trans_i=[]
path_i=[]

FaradayCup_i=[]
FaradayCollector_i=[]
for i in range(0,2):
	p_j=[]
	sen_j=[]
	eff_j=[]
	trans_j=[]
	path_j=[]

	FaradayCup_j=[]
	FaradayCollector_j=[]
	for j in range(0,2):
		fileName="\\c_0_"+str(2*i)+"_"+str(2*j)

		res=FileRes(filePath,fileName)
		res.readFile()
		param=ParametersGauge(gauge.emitters,gauge.boundaryConditions,res.simSettings, res.simData)
		
		p_j.append(param.pressure)
		sen_j.append(param.calculateSensitivityBenchmark())
		eff_j.append(param.calculateIonCollectionEfficency())
		trans_j.append(param.calculateElectronTransmissionEfficency())
		path_j.append(param.calculateTheoryMeanPathLengthPrimaryParticles())

		FaradayCup_j.append(param.FaradayCupCondition)
		FaradayCollector_j.append(param.FaradayCollectorCondition)

	p_i.append(p_j)
	sen_i.append(sen_j)
	eff_i.append(eff_j)
	trans_i.append(trans_j)
	path_i.append(path_j)

	FaradayCup_i.append(FaradayCup_j)
	FaradayCollector_i.append(FaradayCollector_j)

print(FaradayCup_i)
print(FaradayCollector_i)
print(sen_i)
print(eff_i)
print(trans_i)