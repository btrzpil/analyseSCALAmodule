class BoundaryCondition:
	#voltage condition
	def __init__(self, nickname, name):
		self.name=name
		self.nickname=nickname

class Collector(BoundaryCondition):
	def __init__(self,nickname, name='Collector'):
		BoundaryCondition.__init__(self,nickname, name)

class Filament(BoundaryCondition):
	def __init__(self,nickname, name='Filament'):
		BoundaryCondition.__init__(self,nickname, name)

class FaradayCup(BoundaryCondition):
	def __init__(self,nickname, name='FaradayCup'):
		BoundaryCondition.__init__(self,nickname, name)

class FaradayCollector(BoundaryCondition):
	def __init__(self,nickname, name='FaradayCollector'):
		BoundaryCondition.__init__(self,nickname, name)

class Wehnelt(BoundaryCondition):
	def __init__(self,nickname, name='Wehnelt'):
		BoundaryCondition.__init__(self,nickname, name)		





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
		self.boundaryConditions.update({BoundaryCondition.name : BoundaryCondition.nickname})
		print(self.boundaryConditions)





