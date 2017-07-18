
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

        
    