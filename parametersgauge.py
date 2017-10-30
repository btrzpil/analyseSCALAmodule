from fileres import SimulationSettings
from fileres import SimulationData

from modelgauge import BoundaryCondition, Emitter
from modelgauge import ModelGauge
from modelgauge import IonCollector, ElectronEmitter,ElectronFaradayCup,IonVacuumCurrent


class ParametersGauge:
	def __init__(self,emitters,boundaryConditions,simSettings,simData):
		self.emitters=emitters
		self.boundaryConditions=boundaryConditions
		self.simulationSettings=simSettings
		self.simulationData=simData

		self.setPressure()
		self.setIonCollectorCurrent()
		#self.setElectronEmitterCurrent(nameElectronEmitterCurrent)
		#self.setElectronFaradayCupCurrent(nameElectronFaradayCupCurrent)
		#self.setIonVacuumCurrentOut(nameIonVacuumCurrentOut)
		#self.setIonVacuumCurrentIn(nameIonVacuumCurrentIn)

		

#set value

	def setPressure(self):
		self.pressure=self.simulationSettings.pressure

	def setIonCollectorCurrent(self):
		#IonCollectorCurrent=


		id=self.simulationSettings.index(emitters('IonCollector'))
		print(id)
 

	def setElectronEmitterCurrent(self,nameElectronEmitterCurrent):
		self.electronEmitterCurrent=0

	def setElectronFaradayCupCurrent(self,nameElectronFaradayCupCurrent):
		self.electronFaradayCupCurrent=0

	def setIonVacuumCurrentOut(self,nameIonVacuumCurrentOut):
		self.ionVacuumCurrentOut=0

	def setIonVacuumCurrentIn(self,nameIonVacuumCurrentIn):
		self.ionVacuumCurrentIn=1



#calculation
	def calculateSensitivity(self):
		#unit [1/mbar if pressure[mbar]]		
		self.sensitivity=abs(self.ionCollectorCurrent/(self.electronEmitterCurrent*self.pressure))

	def calculateSensitivityBenchmark(self):
		#unit [1/mbar if pressure[mbar]]		
		sensitivityBenchmark=abs(self.ionCollectorCurrent/(self.electronFaradayCupCurrent*self.pressure))

	def calculateYield(self):
		#unit [1/cm]
		self.yieldValue=self.ionVacuumCurrentOut/self.ionVacuumCurrentIn

	def calculateTheoryMeanPathLengthPrimaryParticles(self):
		#unit [cm]
		self.theoryMeanPathLengthPrimaryParticles=abs(self.ionVacuumCurrentIn/self.electronEmitterCurrent)

	def calculateIonCollectionEfficency(self):
		#unit [%]
		self.IonCollectionEfficency=abs(ionCollectorCurrent/ionVacuumCurrentOut)*100

	def calculateElectronTransmissionEfficency(self):
		#unit [%]	
		self.electronTransmissionEfficency=abs(electronFaradayCupCurrent/electronEmitterCurrent)*100
