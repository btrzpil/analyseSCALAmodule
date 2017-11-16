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
		self.setCollectorCondition()
		self.setFilamentCondition()
		self.setFaradayCupCondition()
		self.setFaradayCollectorCondition()
		self.setWehneltCondition()
		


	def getBoundaryConditionValue(self,name):

		id=self.simulationSettings.voltageDrive.index(name)
		BoundaryConditionValue= self.simulationSettings.voltageValue[id]
		return BoundaryConditionValue

	def setCollectorCondition(self):
		if "Collector" in self.boundaryConditions:
			nameCollector=self.boundaryConditions["Collector"]
			CollectorCondition=self.getBoundaryConditionValue(nameCollector)
		else:
			CollectorCondition=0
		self.CollectorCondition=CollectorCondition


	def setFilamentCondition(self):
		if "Filament" in self.boundaryConditions:
			FilamentCondition=self.getBoundaryConditionValue(self.boundaryConditions["Filament"])
		else:
			FilamentCondition=0
		self.FilamentCondition=FilamentCondition

	def setFaradayCupCondition(self):
		if "FaradayCup" in self.boundaryConditions:
			FaradayCupCondition=self.getBoundaryConditionValue(self.boundaryConditions["FaradayCup"])
		else:
			FaradayCupCondition=0
		self.FaradayCupCondition=FaradayCupCondition

	def setFaradayCollectorCondition(self):
		if "FaradayCollector" in self.boundaryConditions:
			FaradayCollectorCondition=self.getBoundaryConditionValue(self.boundaryConditions["FaradayCollector"])
		else:
			FaradayCollectorCondition=0
		self.FaradayCollectorCondition=FaradayCollectorCondition

	def setWehneltCondition(self):
		if "Wehnelt" in self.boundaryConditions:
			WehneltCondition=self.getBoundaryConditionValue(self.boundaryConditions["Wehnelt"])
		else:
			WehneltCondition=0
		self.WehneltCondition=WehneltCondition



	def getSecondaryEmitterCurrent(self,name):
		id=self.simulationSettings.secondaryEmittersName.index(name)
		inCurrent= self.simulationData.secondaryEmitterData[id*2]
		outCurrent = self.simulationData.secondaryEmitterData[id*2+1]
		return inCurrent,outCurrent

	def getPrimaryEmitterCurrent(self,name):
	
		id=self.simulationSettings.primaryEmittersName.index(name)
		outCurrent = self.simulationData.primaryEmitterData[id]
		return outCurrent
#set value

	def setPressure(self):
		self.pressure=self.simulationSettings.pressure

	def setIonCollectorCurrent(self):
		if "IonCollector" in self.emitters:
			nameIonCollectorCurrent=self.emitters["IonCollector"]
			[inCurrent,outCurrent]=self.getSecondaryEmitterCurrent(nameIonCollectorCurrent)
			ionCollectorCurrent=inCurrent
		else:
			ionCollectorCurrent=0
		self.ionCollectorCurrent=ionCollectorCurrent

		
 

	def setElectronEmitterCurrent(self):
		if "ElectronEmitter" in self.emitters:
			nameElectronEmitterCurrent=self.emitters["ElectronEmitter"]
			[inCurrent,outCurrent]=self.getSecondaryEmitterCurrent(nameElectronEmitterCurrent[1])	
			outCurrent=self.getPrimaryEmitterCurrent(nameElectronEmitterCurrent[0])
			electronEmitterCurrent=inCurrent-outCurrent
		else:
			electronEmitterCurrent=0
		self.electronEmitterCurrent=electronEmitterCurrent

	def setElectronFaradayCupCurrent(self):
		if "ElectronFaradayCup" in self.emitters:
			nameElectronFaradayCupCurrent=self.emitters["ElectronFaradayCup"]
			[inCurrent,outCurrent]=self.getSecondaryEmitterCurrent(nameElectronFaradayCupCurrent)
			electronFaradayCupCurrent=inCurrent
		else:
			electronFaradayCupCurrent=0	
		self.electronFaradayCupCurrent=electronFaradayCupCurrent	



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
		return self.sensitivity

	def calculateSensitivityBenchmark(self):
		#unit [1/mbar if pressure[mbar]]		
		self.sensitivityBenchmark=abs(self.ionCollectorCurrent/(self.electronFaradayCupCurrent*self.pressure))
		return self.sensitivityBenchmark
	def calculateYield(self):
		#unit [1/cm]
		self.yieldValue=abs(self.ionVacuumCurrentOut/self.ionVacuumCurrentIn)
		print(self.yieldValue)
		return self.yieldValue
	def calculateTheoryMeanPathLengthPrimaryParticles(self):
		#unit [cm]
		self.theoryMeanPathLengthPrimaryParticles=abs(self.ionVacuumCurrentIn/self.electronEmitterCurrent)
		return self.theoryMeanPathLengthPrimaryParticles
	def calculateIonCollectionEfficency(self):
		#unit [%]
		self.ionCollectionEfficency=abs(self.ionCollectorCurrent/self.ionVacuumCurrentOut)*100
		return self.ionCollectionEfficency

	def calculateElectronTransmissionEfficency(self):
		#unit [%]	
		self.electronTransmissionEfficency=abs(self.electronFaradayCupCurrent/self.electronEmitterCurrent)*100
		return self.electronTransmissionEfficency