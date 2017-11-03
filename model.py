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

class Model:


	def __init__(self,location, name, gauge):
		self.location=location
		self.name=name




	for i in range(0,10):
		res=FileRes(filePath,fileName)
		res.readFile()
		param=ParametersGauge(gauge.emitters,gauge.boundaryConditions,res.simSettings, res.simData)
		param.











param=ParametersGauge(gauge.emitters,gauge.boundaryConditions,res.simSettings, res.simData)



