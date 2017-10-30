class BoundaryCondition:
	def __init__(self,name, value):
		self.name=name
		self.value=value


class Emitter:
	def __init__(self,name,emitterType):
		self.emitterType=emitterType
		self.name=name

class IonCollector(Emitter):
	def __init__(self,name,emitterType='IonCollector'):
		Emitter.__init__(self,name, emitterType)

class ElectronEmitter(Emitter):
	def __init__(self,name,emitterType='ElectronEmitter'):
		Emitter.__init__(self,name, emitterType)

class ElectronFaradayCup(Emitter):
	def __init__(self,name,emitterType='ElectronFaradayCup'):
		Emitter.__init__(self,name, emitterType)

class IonVacuumCurrent(Emitter):	
	def __init__(self,name,emitterType='IonVacuumCurrent'):
		Emitter.__init__(self,name, emitterType)


class ModelGauge:
	def __init__(self):
		self.boundaryConditions={}
		self.emitters={}

	def addEmitter(self,Emitter):
		self.emitters.update({Emitter.emitterType : Emitter.name})

	def addBoundaryCondition(self,BoundaryCondition):
		#value  - BoundaryCondition - value , name
		self.boundaryConditions.update({BoundaryCondition.name : BoundaryCondition.value})





