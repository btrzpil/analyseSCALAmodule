from filetracks import FileTracks
from filetracks import Trajectories
from filetracks import Position


class Shape:
	def __init__(self,x1,y1,z1,x2,y2,z2):	
		if x1>x2:
			self.xmin=x2
			self.xmax=x1
		else:
			self.xmin=x1
			self.xmax=x2

		if y1>y2:
			self.ymin=y2
			self.ymax=y1
		else:
			self.ymin=y1
			self.ymax=y2

		if z1>z2:
			self.zmin=z2
			self.zmax=z1
		else:
			self.zmin=z1
			self.zmax=z2


class SolidShape:
	def __init__(self):
		self.shape="SolidShape"

class Cylinder(SolidShape):
	def __init__(self,x,y,z1,z2,r):
		self.x=x
		self.y=y
		self.r=r
		if z1>z2:
			self.zmin=z2
			self.zmax=z1
		else:
			self.zmin=z1
			self.zmax=z2		



class Cuboid(SolidShape):
	def __init__(x1,y1,z1,x2,y2,z2):	
		if x1>x2:
			self.xmin=x2
			self.xmax=x1
		else:
			self.xmin=x1
			self.xmax=x2

		if y1>y2:
			self.ymin=y2
			self.ymax=y1
		else:
			self.ymin=y1
			self.ymax=y2

		if z1>z2:
			self.zmin=z2
			self.zmax=z1
		else:
			self.zmin=z1
			self.zmax=z2




class ParametersTrackParticles:

	#FileTracks.trajectories =Trajectories() 

	def __init__(self,trajectories):
		self.trajectories=trajectories
		self.numberTrajectories=len(self.trajectories.TrajectoriesParameters)
		self.emitterPointer=[]
		self.setTrackInformationEmitter()


	def getTrajectoriesParametersNSTEP(self):
		NSTEP=[self.trajectories.TrajectoriesParameters[i][1] for i in range(self.numberTrajectories)]
		return NSTEP

	def getTrajectoriesParametersEmitters(self):
		Emitters=[self.trajectories.TrajectoriesParameters[i][2] for i in range(self.numberTrajectories)]
		return Emitters

	def getTrajectoriesParametersCurrent(self):
		Current=[self.trajectories.TrajectoriesParameters[i][3] for i in range(self.numberTrajectories)]
		return Current

	def getTrajectoriesParametersStepLength(self):
		StepLength=[self.trajectories.TrajectoriesParameters[i][6] for i in range(self.numberTrajectories)]
		return StepLength

	def getTrajectoriesCoordinatesCreationIons(self):
		TrajectoriesCoordinatesIon=self.getTrajectoriesCoordinatesIons()
		CreationIons=[TrajectoriesCoordinatesIon[i][0] for i in range(len(TrajectoriesCoordinatesIon))]	
		return CreationIons

	def getTrajectoriesCoordinatesDestinationIons(self):
		TrajectoriesCoordinatesIon=self.getTrajectoriesCoordinatesIons()
		DestinationIons=[TrajectoriesCoordinatesIon[i][len(TrajectoriesCoordinatesIon[i])-1] for i in range(len(TrajectoriesCoordinatesIon))]
		return DestinationIons
	
	def getTrajectoriesCoordinatesIons(self):
		TrajectoriesCoordinatesIon=[self.trajectories.TrajectoriesCoordinates[i] for i in range(self.emitterPointer[1],self.emitterPointer[2])]
		return TrajectoriesCoordinatesIon

	def getTrajectoriesCoordinatesCreationElectrons(self):
		TrajectoriesCoordinatesElectrons=self.getTrajectoriesCoordinatesIons()
		CreationElectrons=[TrajectoriesCoordinatesElectrons[i][0] for i in range(len(TrajectoriesCoordinatesElectrons))]	
		return CreationElectrons

	def getTrajectoriesCoordinatesDestinationElectrons(self):
		TrajectoriesCoordinatesElectrons=self.getTrajectoriesCoordinatesElectrons()
		DestinationElectrons=[TrajectoriesCoordinatesIon[i][len(TrajectoriesCoordinatesElectrons[i])-1] for i in range(len(TrajectoriesCoordinatesElectrons))]
		return DestinationElectrons

	def getTrajectoriesCoordinatesElectrons(self):
		TrajectoriesCoordinatesElectrons=[self.trajectories.TrajectoriesCoordinates[i] for i in range(self.emitterPointer[0],self.emitterPointer[1])]
		return TrajectoriesCoordinatesElectrons



	def setTrackInformationEmitter(self):
		Emitters=self.getTrajectoriesParametersEmitters()
		emitterPointer=[]
		emitterPointer.append(0)
		counter=0
		emitterTmp=Emitters[0]
		for emitter in Emitters:
			if (emitterTmp!=emitter):
				emitterTmp=Emitters[counter]            
				emitterPointer.append(counter)
			counter=counter+1 
		emitterPointer.append(counter)
		self.emitterPointer=emitterPointer


	def calculateMeanPathPrimaryParticles(self):
		sumLenPathPrimaryParticles=0
		nParticle=self.emitterPointer[1]
		NSTEP=self.getTrajectoriesParametersNSTEP()
		StepLength=self.getTrajectoriesParametersStepLength()
		for step in range (nParticle):
			lenPathParticle=NSTEP[step]*StepLength[step]
			sumLenPathPrimaryParticles=sumLenPathPrimaryParticles+lenPathParticle

		self.meanPathPrimaryParticles=sumLenPathPrimaryParticles/nParticle
		print(self.meanPathPrimaryParticles)

		# TrajectoriesCoordinates=self.getTrajectoriesCoordinatesElectrons()
		

		# for ion in TrajectoriesCoordinates:

		# 	for step in ion:






	def calculateIonCollectionEfficency(self,x1,y1,z1,x2,y2,z2):
		numberIon=len(self.getTrajectoriesCoordinatesIons())		
		numberIonCollected=self.calculateIonCollection(x1,y1,z1,x2,y2,z2)
		ionCollectionEfficency=numberIonCollected/numberIon	
		return ionCollectionEfficency

	def calculateIonCollection(self,x1,y1,z1,x2,y2,z2):
		rec=Shape(x1,y1,z1,x2,y2,z2)
		TrajectoriesCoordinates=self.getTrajectoriesCoordinatesDestinationIons()

		numberIonCollected=0
	
		i=0
		for particle in TrajectoriesCoordinates:
			print(particle)
			if i >10 :
				print(len(particle))
			if (rec.xmin<=particle[0]<=rec.xmax)and(rec.ymin<=particle[1]<=rec.ymax)and(rec.zmin<=particle[3]<=rec.zmax):
				numberIonCollected=numberIonCollected+1
			i=i+1
		return numberIonCollected



	def calculateIonVolumeEfficency(self,x1,y1,z1,x2,y2,z2):
		numberIon=len(self.getTrajectoriesCoordinatesIons())
		numberIonVolume=self.calculateIonVolume(x1,y1,z1,x2,y2,z2)
		ionVolumeEfficency=numberIonVolume/numberIon
		return ionVolumeEfficency

	def calculateIonVolume(self,x1,y1,z1,x2,y2,z2):
		rec=Shape(x1,y1,z1,x2,y2,z2)
		TrajectoriesCoordinates=self.getTrajectoriesCoordinatesIons()
		numberIonVolume=0

		for ion in TrajectoriesCoordinates:

			for step in ion:

				if (rec.xmin<=step[0]<=rec.xmax)and(rec.ymin<=step[1]<=rec.ymax)and(rec.zmin<=step[2]<=rec.zmax):
					numberIonVolume=numberIonVolume+1
					break

		return numberIonVolume










