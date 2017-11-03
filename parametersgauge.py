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
		self.setElectronEmitterCurrent()
		self.setElectronFaradayCupCurrent()
		self.setIonVacuumCurrent()


		
	def getSecondaryEmitterCurrent(self,name):
		print(name)
		id=self.simulationSettings.secondaryEmitters.index(name)
		inCurrent= self.simulationData.secondaryEmitterData[id*2]
		outCurrent = self.simulationData.secondaryEmitterData[id*2+1]
		print(inCurrent)
		print(outCurrent)
		return inCurrent,outCurrent

	def getPrimaryEmitterCurrent(self,name):
	
		id=self.simulationSettings.primaryEmitters.index(name)
		outCurrent = self.simulationData.primaryEmitterData[id]
		print(outCurrent)
		return outCurrent
#set value

	def setPressure(self):
		self.pressure=self.simulationSettings.pressure

	def setIonCollectorCurrent(self):

		if "IonCollector" in self.emitters:
			nameIonCollectorCurrent=self.emitters["IonCollector"]
			[inCurrent,outCurrent]=self.getSecondaryEmitterCurrent(nameIonCollectorCurrent)
			IonCollectorCurrent=inCurrent
		else:
			IonCollectorCurrent=0

		
 

	def setElectronEmitterCurrent(self):
		if "ElectronEmitter" in self.emitters:
			nameElectronEmitterCurrent=self.emitters["ElectronEmitter"]



			[inCurrent,outCurrent]=self.getSecondaryEmitterCurrent(nameElectronEmitterCurrent[1])
			
			outCurrent=self.getPrimaryEmitterCurrent(nameElectronEmitterCurrent[0])

			ElectronEmitterCurrent=inCurrent-outCurrent
			print(ElectronEmitterCurrent)

		else:
			ElectronEmitterCurrent=0


	def setElectronFaradayCupCurrent(self):
		if "ElectronFaradayCup" in self.emitters:
			nameElectronFaradayCupCurrent=self.emitters["ElectronFaradayCup"]
			[inCurrent,outCurrent]=self.getSecondaryEmitterCurrent(nameElectronFaradayCupCurrent)
			self.ElectronFaradayCupCurrent=inCurrent
		else:
			self.ElectronFaradayCupCurrent=0		



	def setIonVacuumCurrent(self):
		if "IonVacuumCurrent" in self.emitters:  
			nameIonVacuumCurrent=self.emitters["IonVacuumCurrent"]
			[inCurrent,outCurrent]=self.getSecondaryEmitterCurrent(nameIonVacuumCurrent)
			self.ionVacuumCurrentIn=inCurrent
			self.ionVacuumCurrentOut=outCurrent
		else:
			self.ionVacuumCurrentIn=0
			self.ionVacuumCurrentOut=0



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
