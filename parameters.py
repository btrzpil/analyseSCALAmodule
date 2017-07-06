

class Parameters:

    currentCollectorData=[]
    currentEmitterData=[]

    sensitivityData=[]
    
    dataSimulation=[]
    nameEmitter=[]
    numberEmitter=[]
    numberSimulation=[]

    def __init__(self, dataSimulation,nameEmitter,numberEmitter,numberSimulation):
        self.dataSimulation=dataSimulation
        self.nameEmitter=nameEmitter
        self.numberEmitter=numberEmitter
        self.numberSimulation=numberSimulation
        
        id=self.nameEmitter.index("ion_collec")
        self.currentCollectorData = [self.dataSimulation[i][id*2-1] for i in range(len(self.dataSimulation))]


        id=self.nameEmitter.index("thermionic output current ")
        self.currentEmitterData = [self.dataSimulation[i][id] for i in range(len(self.dataSimulation))]



     


        
        
    def calculateSensitivity(self,pressureData):

        self.sensitivityData=[]
        for i in range(0, len(pressureData)):    
            sensitivity=abs(self.currentCollectorData[i]/(self.currentEmitterData[i]*pressureData[i]))
            self.sensitivityData.append(sensitivity)


        
        


    
