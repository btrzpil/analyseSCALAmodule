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

	def __init__(self, tracksInformation,postionTrack):
		self.tracksInformationNSTEP=[tracksInformation[i][1] for i in range(len(tracksInformation))]
		self.tracksInformationEmitters=[tracksInformation[i][2] for i in range(len(tracksInformation))]
		self.tracksInformationCurrent=[tracksInformation[i][3] for i in range(len(tracksInformation))]
		self.tracksInformationStepLength=[tracksInformation[i][6] for i in range(len(tracksInformation))]
		self.XPositionTracks=[postionTrack[i][1] for i in range(len(postionTrack))]
		self.YPositionTracks=[postionTrack[i][2] for i in range(len(postionTrack))]
		self.ZPositionTracks=[postionTrack[i][3] for i in range(len(postionTrack))]
		self.setTrackInformationEmitter()
		self.calculatePositionIons()

	def setTrackInformationEmitter(self):

		counter=0
		emitterInd=[]
		emitterInd.append(0)
		emitterTmp=self.tracksInformationEmitters[0]

		for emitter in self.tracksInformationEmitters:
            
			if (emitterTmp!=emitter):
				emitterTmp=self.tracksInformationEmitters[counter]
              
				emitterInd.append(counter)


			counter=counter+1 
              

		emitterInd.append(counter)
		self.emitterInd=emitterInd



	def calculateMeanPathPrimaryParticles(self):
		sumLenPathPrimaryParticles=0
		nParticle=self.emitterInd[1]

		for step in range (self.emitterInd[0],self.emitterInd[1]):
			lenPathParticle=self.tracksInformationNSTEP[step]*self.tracksInformationStepLength[step]
			sumLenPathPrimaryParticles=sumLenPathPrimaryParticles+lenPathParticle

		self.meanPathPrimaryParticles=sumLenPathPrimaryParticles/nParticle
		print(self.meanPathPrimaryParticles)

	def calculatePositionIons(self):
		self.xPositionIons=self.XPositionTracks[self.emitterInd[1]:self.emitterInd[2]]
		self.yPositionIons=self.YPositionTracks[self.emitterInd[1]:self.emitterInd[2]]
		self.zPositionIons=self.ZPositionTracks[self.emitterInd[1]:self.emitterInd[2]]
		self.currentIons=self.tracksInformationCurrent[self.emitterInd[1]:self.emitterInd[2]]


	def calculateIonCollectionEfficency(self,x1,y1,z1,x2,y2,z2):
		rec=ShapeArea(x1,y1,z1,x2,y2,z2)
		
		sumIon=0
		sumIonCollected=0
		for step in range (self.emitterInd[2]-self.emitterInd[1]):

			sumIon=sumIon+1
			if (rec.xmin<=float(self.xPositionIons[step])<=rec.xmax)and(rec.ymin<=float(self.yPositionIons[step])<=rec.ymax)and(rec.zmin<=float(self.zPositionIons[step])<=rec.zmax):
				sumIonCollected=sumIonCollected+1
		self.ionCollectionEfficency=sumIonCollected/sumIon	
		print(self.ionCollectionEfficency)









