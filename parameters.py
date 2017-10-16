
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
        self.currentCollectorIn= [self.dataSimulation[i][id*2-1] for i in range(len(self.dataSimulation))]
        self.currentCollectorOut = [self.dataSimulation[i][id*2] for i in range(len(self.dataSimulation))]

        
        id=self.nameEmitter.index("ionisation")
        self.currentIonIn = [self.dataSimulation[i][id*2-1] for i in range(len(self.dataSimulation))]
        self.currentIonOut = [self.dataSimulation[i][id*2] for i in range(len(self.dataSimulation))]

        id=self.nameEmitter.index("thermionic output current ")
        self.currentEmitter = [self.dataSimulation[i][id] for i in range(len(self.dataSimulation))]


    def calculateMeanPathLengthPrimaryParticles(self):
        #theory
        #"unit' [cm]
        self.meanPathLengthPrimaryParticles=[]
        for i in range(0, len(self.currentIonIn)):    
            pathLength=abs(self.currentIonIn[i]/self.currentEmitter[i])
            self.meanPathLengthPrimaryParticles.append(pathLength)        


    def calculateYield(self):
        #'unit' [1/cm]
        self.yieldCalculation=[]
        for i in range(0, len(self.currentIonIn)):    
            yieldValue=abs(self.currentIonOut[i]/self.currentIonIn[i])
            self.yieldCalculation.append(yieldValue)
        

        
        
    def calculateSensitivity(self):

        self.sensitivityData=[]
        for i in range(0, len(self.pressureData)):    
            sensitivity=abs(self.currentCollectorIn[i]/(self.currentEmitter[i]*self.pressureData[i]))
            self.sensitivityData.append(sensitivity)


        
    