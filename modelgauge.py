class BoundaryCondition:
	def __init__(self,name, value):
		self.name=name
		self.value=value


class Emitter:
	def __init__(self,name,eType):
		self.eType=eType
		self.name=name

class IonCollector(Emitter):
	def __init__(self,name,eType='IonCollector'):
		Emitter.__init__(self,name, eType)

class ElectronEmitter(Emitter):
	def __init__(self,name,eType='ElectronEmitter'):
		Emitter.__init__(self,name, eType)

class ElectronFaradayCup(Emitter):
	def __init__(self,name,eType='ElectronFaradayCup'):
		Emitter.__init__(self,name, eType)

class IonVacuumCurrent(Emitter):	
	def __init__(self,name,eType='IonVacuumCurrent'):
		Emitter.__init__(self,name, eType)


class ModelGauge:
	def __init__(self):
		self.boundaryConditions={}
		self.emitters={}

	def addEmitter(self,Emitter):
		self.emitters.update({Emitter.eType : Emitter.name})

	def addBoundaryCondition(self,BoundaryCondition):
		#value  - BoundaryCondition - value , name
		self.boundaryConditions.update({BoundaryCondition.name : BoundaryCondition.value})





