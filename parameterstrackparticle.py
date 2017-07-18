class ParametersTrackParticles:





	def setTracksInformation(self, tracksInformation,postionTrack):
        
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
        print(emitterInd)


    def calculateMeanPathPrimaryParticles(self):
        sumLenPathPrimaryParticles=0
        nParticle=self.emitterInd[1]
        for step in range (self.emitterInd[0],self.emitterInd[1]):
            lenPathParticle=self.tracksInformationNSTEP[step]*self.tracksInformationStepLength[step]
            sumLenPathPrimaryParticles=sumLenPathPrimaryParticles+lenPathParticle
               
        meanPathPrimaryParticles=sumLenPathPrimaryParticles/nParticle
        return meanPathPrimaryParticles

    def calculatePositionIons(self):
        self.xPositionIons=self.XPositionTracks[self.emitterInd[1]:self.emitterInd[2]]
        self.yPositionIons=self.YPositionTracks[self.emitterInd[1]:self.emitterInd[2]]
        self.zPositionIons=self.ZPositionTracks[self.emitterInd[1]:self.emitterInd[2]]
        self.currentIons=self.tracksInformationCurrent[self.emitterInd[1]:self.emitterInd[2]]


    def calculateIonCollectionEfficency(self):
        print(self.calculateMeanPathPrimaryParticles)
