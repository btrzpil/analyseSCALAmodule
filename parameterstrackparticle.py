from filetracks import FileTracks
from filetracks import Trajectories
from filetracks import Position

import math

class Volume:
	def __init__(self,name):
		self.name=name

class Cylinder(Volume):
	def __init__(self,name,parameters):
		Volume.__init__(self, name)
		self.setParameters(parameters)
	def setParameters(self,parameters):
		print(self.name)

		x =parameters[0]
		y =parameters[1]
		z1=parameters[2]
		z2=parameters[3]
		r =parameters[4]

	
		self.x=x
		self.y=y
		self.r=r
		if z1>z2:
			self.zmin=z2
			self.zmax=z1
		else:
			self.zmin=z1
			self.zmax=z2

	def checkPointVolume(self,x,y,z):

		if (((x-self.x)**2+(y-self.y)**2<=(self.r)**2)and(self.zmin<=z<=self.zmax)):
			return True
		else:
			return False


class Cuboid(Volume):

	def __init__(self,name,parameters):
		Volume.__init__(self, name)
		self.setParameters(parameters)
	def setParameters(self,parameters):
		print(self.name)

		x1=parameters[0]
		x2=parameters[1]
		y1=parameters[2]
		y2=parameters[3]
		z1=parameters[4]
		z2=parameters[5]

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

	def checkPointVolume(self,x,y,z):

		if (self.xmin<=x<=self.xmax)and(self.ymin<=y<=self.ymax)and(self.zmin<=z<=self.zmax):
			return True
		else:
			return False

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

	def calculateStepLengthNSTEP(self):
		trackLengthData=0	
		NSTEPdata=self.getTrajectoriesParametersNSTEP()
		StepLengthData=self.getTrajectoriesParametersStepLength()
		for i in range(self.emitterPointer[0],self.emitterPointer[1]):
			trackLength=NSTEPdata[i]*StepLengthData[i]
			trackLengthData=trackLengthData+trackLength

		self.stepLengthNSTEP=(trackLengthData/self.emitterPointer[1])*100 #convert to cm

		

	def calculateMeanPathLengthElectrons(self):
		TrajectoriesCoordinatesElectrons=self.getTrajectoriesCoordinatesElectrons()
		sumPathLengthPrimaryParticles=0
		for electron in TrajectoriesCoordinatesElectrons:
			NSTEP=len(electron)
			lengthPathElectron=0
			for step in range(NSTEP-1):
				lengthStep=math.sqrt((electron[step+1][0]-electron[step][0])**2+(electron[step+1][1]-electron[step][1])**2+(electron[step+1][2]-electron[step][2])**2)
				lengthPathElectron=lengthPathElectron+lengthStep
			sumPathLengthPrimaryParticles=sumPathLengthPrimaryParticles+lengthPathElectron
		#self.meanPathLengthElectrons=(sumPathLengthPrimaryParticles*10)/len(TrajectoriesCoordinatesElectrons) /in cm	
		self.meanPathLengthElectrons=(sumPathLengthPrimaryParticles)/len(TrajectoriesCoordinatesElectrons)	


	def calculateIonCollectionEfficency(self,volume):
		numberIon=len(self.getTrajectoriesCoordinatesIons())		
		numberIonCollected=self.calculateIonCollection(volume)
		ionCollectionEfficency=numberIonCollected/numberIon	
		return ionCollectionEfficency

	def calculateIonCollection(self,volume):

		TrajectoriesCoordinates=self.getTrajectoriesCoordinatesDestinationIons()
		numberIonCollected=0
	
		for particle in TrajectoriesCoordinates:

			if volume.checkPointVolume(particle[0],particle[1],particle[2]):
				numberIonCollected=numberIonCollected+1
				
		return numberIonCollected



	def calculateIonVolumeEfficency(self,volumeSmall,volumeReference):
		numberIon=self.calculateIonVolume(volumeSmall)
		numberIonVolume=self.calculateIonVolume(volumeReference)
		ionVolumeEfficency=numberIonVolume/numberIon
		return ionVolumeEfficency

	def calculateIonVolume(self,volume):
		
		TrajectoriesCoordinates=self.getTrajectoriesCoordinatesIons()
		numberIonVolume=0

		for ion in TrajectoriesCoordinates:

			for step in ion:

				if volume.checkPointVolume(step[0],step[1],step[2]):
					numberIonVolume=numberIonVolume+1
					break


		return numberIonVolume








