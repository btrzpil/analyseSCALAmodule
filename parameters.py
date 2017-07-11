
class Parameters:

    currentCollectorData=[]
    currentEmitterData=[]

    sensitivityData=[]
    
    dataSimulation=[]
    nameEmitter=[]
    numberEmitter=[]
    numberSimulation=[]
    pressureData=[]

    def setPressure(self,pressureData):
        self.pressureData=pressureData
        

    def setDataResFile(self, dataSimulation,nameEmitter,numberEmitter,numberSimulation):
        self.dataSimulation=dataSimulation
        self.nameEmitter=nameEmitter
        self.numberEmitter=numberEmitter
        self.numberSimulation=numberSimulation
        
        id=self.nameEmitter.index("ion_collec")
        self.currentCollectorData = [self.dataSimulation[i][id*2-1] for i in range(len(self.dataSimulation))]


        id=self.nameEmitter.index("thermionic output current ")
        self.currentEmitterData = [self.dataSimulation[i][id] for i in range(len(self.dataSimulation))]



        
        
    def calculateSensitivity(self):

        self.sensitivityData=[]
        for i in range(0, len(self.pressureData)):    
            sensitivity=abs(self.currentCollectorData[i]/(self.currentEmitterData[i]*self.pressureData[i]))
            self.sensitivityData.append(sensitivity)

        
    def setTracksEmitter(self, tracksInformation,postionTrack):
        
        self.tracksInformationEmitters=[tracksInformation[i][2] for i in range(len(tracksInformation))]
        self.XPositionTracks=[postionTrack[i][1] for i in range(len(postionTrack))]
        self.YPositionTracks=[postionTrack[i][2] for i in range(len(postionTrack))]
        self.ZPositionTracks=[postionTrack[i][3] for i in range(len(postionTrack))]
        self.currentTracks=[postionTrack[i][7] for i in range(len(postionTrack))]

        
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


    def setTrackInformationEmitter(self,emitter):

        xPositionData=self.XPositionTracks[self.emitterInd[i]:self.emitterInd[i+1]]
        yPositionData=self.YPositionTracks[self.emitterInd[i]:self.emitterInd[i+1]]
        zPositionData=self.ZPositionTracks[self.emitterInd[i]:self.emitterInd[i+1]]
        self.currentTracks[self.emitterInd[i]:self.emitterInd[i+1]]



      ##def calculateIonCollectionEfficency(self):
##        
##
##        print(len(tracksInformationEmitter[emitterInd[0]:emitterInd[1]]))
##
##        print(len(tracksInformationEmitter[emitterInd[1]:emitterInd[2]]))
##
##        for i in range(0,len(emitterInd)-1):
##            print(len(tracksInformationEmitter[emitterInd[i]:emitterInd[i+1]]))

        
    
      


    
