
class Parameters:


    
    dataSimulation=[]
    nameEmitter=[]
    numberEmitter=[]
    numberSimulation=[]
    pressureData=[]

    def __init__(self,dataSimulation,nameEmitter,numberEmitter,numberSimulation,pressureData ):
        self.pressureData=pressureData
        self.dataSimulation=dataSimulation
        self.nameEmitter=nameEmitter

        self.numberEmitter=numberEmitter
        self.numberSimulation=numberSimulation
        
        id=self.nameEmitter.index("ion_collec")
        self.currentCollectorDataIn = [self.dataSimulation[i][id*2-1] for i in range(len(self.dataSimulation))]
        self.currentCollectorDataOut = [self.dataSimulation[i][id*2] for i in range(len(self.dataSimulation))]

        
        id=self.nameEmitter.index("ionisation")
        self.currentIonIn = [self.dataSimulation[i][id*2-1] for i in range(len(self.dataSimulation))]
        self.currentIonOut = [self.dataSimulation[i][id*2] for i in range(len(self.dataSimulation))]

        id=self.nameEmitter.index("thermionic output current ")
        self.currentEmitterData = [self.dataSimulation[i][id] for i in range(len(self.dataSimulation))]


    def calculateMeanPathLengthPrimaryParticles(self):
        self.meanPathLength=[]
        for i in range(0, len(self.currentIonIn)):    
            pathLength=abs(self.currentIonIn[i]/self.currentEmitterData[i])
            self.meanPathLength.append(pathLength)        
        

    def calculateYield(self):

        self.yieldData=[]
        for i in range(0, len(self.currentIonIn)):    
            yieldValue=abs(self.currentIonIn[i]/self.currentIonOut[i])
            self.yieldData.append(yieldValue)
        

        
        
    def calculateSensitivity(self):

        self.sensitivityData=[]
        for i in range(0, len(self.pressureData)):    
            sensitivity=abs(self.currentCollectorDataIn[i]/(self.currentEmitterData[i]*self.pressureData[i]))
            self.sensitivityData.append(sensitivity)


        
    