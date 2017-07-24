from filetracks import FileTracks
from filetracks import Trajectories
from filetracks import Position
class ShapeArea:

	def __init__(self, x1,y1,z1,x2,y2,z2):
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
		print(len(TrajectoriesCoordinatesIon))
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
        #print(TrajectoriesCoordinates[0])
  #       startPosition=[pos.position[0][i] for i in range(3)]
  #       endPosition=[pos.position[NSTEP-1][i] for i in range(3)]

		# self.X=[postionTrack[i][0] for i in range(len(postionTrack))]
		# self.Y=[postionTrack[i][1] for i in range(len(postionTrack))]
		# self.Z=[postionTrack[i][2] for i in range(len(postionTrack))]

		# self.calculatePositionIons()


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


	# def calculatePositionIons(self):
	# 	self.xPositionIons=self.XPositionTracks[self.emitterInd[1]:self.emitterInd[2]]
	# 	self.yPositionIons=self.YPositionTracks[self.emitterInd[1]:self.emitterInd[2]]
	# 	self.zPositionIons=self.ZPositionTracks[self.emitterInd[1]:self.emitterInd[2]]





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




	def calculateIonCollectionEfficency(self,x1,y1,z1,x2,y2,z2):

		rec=ShapeArea(x1,y1,z1,x2,y2,z2)
		TrajectoriesCoordinatesDestinationIons=self.getTrajectoriesCoordinatesDestinationIons()
		print(len(TrajectoriesCoordinatesDestinationIons))
	 	xPositionIons=TrajectoriesCoordinatesDestinationIons[0]
	 	yPositionIons=TrajectoriesCoordinatesDestinationIons[1]
	 	zPositionIons=TrajectoriesCoordinatesDestinationIons[2]

	 	sumIon=0
	 	sumIonCollected=0
	 	for step in range (self.emitterInd[2]-self.emitterInd[1]):

	 	 	sumIon=sumIon+1
	 	 	if (rec.xmin<=self.xPositionIons[step]<=rec.xmax)and(rec.ymin<=self.yPositionIons[step]<=rec.ymax)and(rec.zmin<=self.zPositionIons[step]<=rec.zmax):
	 	 		sumIonCollected=sumIonCollected+1
		
	 	self.ionCollectionEfficency=sumIonCollected/sumIon	
	 	print(self.ionCollectionEfficency)









