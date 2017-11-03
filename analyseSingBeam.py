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
from graphs import Graphs

import time


gauge=ModelGauge()

gauge.addEmitter(IonCollector('I_coll'))
gauge.addEmitter(ElectronEmitter(['E_fil_prim','E_fil_back']))
gauge.addEmitter(ElectronFaradayCup('E_cage_O'))

filePath="E:\\btrzpil\\EMPIR\\Works\\Sim\\proposal2\\sBeam04res"
fileName="\\c_0_1_2_1_0"




for i in range(0,10):
	res=FileRes(filePath,fileName)
	res.readFile()
	param=ParametersGauge(gauge.emitters,gauge.boundaryConditions,res.simSettings, res.simData)
	param.