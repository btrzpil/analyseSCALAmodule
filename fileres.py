class SimulationSettings:

    def __init__(self):

        self.voltageDrive=[]
        self.voltageValue=[]
        self.primaryEmitterNumber=0
        self.secondaryEmitterNumber=0
        self.primaryEmittersName=[]
        self.secondaryEmittersName=[]
        self.iterationNumebr=0 

class SimulationData:

    def __init__(self):
        self.allIterationsOfPrimaryEmitterData=[]
        self.allIterationsOfSecondaryEmitterData=[]

class FileRes:     
    fileExtension=".res"
    recognitionVoltage=["      VOLTAGE"]
    recognitionTitle=["    User title:"]
    recognitionEmitterData = [" Primary Emitter ", " Secondary Emitter"]
    recognitionIterationNumer=[" Nonlinear iteration "]

    



    def __init__(self, filePath,fileName):
        self.inFile=filePath+fileName+self.fileExtension
        self.iterationCounter=0

    def readFile(self):

        self.simSettings=SimulationSettings()        
        self.file = open(self.inFile,'r')
        
  
        while True:

            line = self.file.readline()

            if line == '':
                break
            else:
                if line.startswith(self.recognitionTitle[0]):
                    self.simSettings.pressure=float(self.file.readline().split(":")[1])
                    self.simSettings.residualGas=self.file.readline().split(":")[1]
                elif line.startswith(self.recognitionVoltage[0]):
                    #info after header
                    line=self.file.readline()
                    line = self.file.readline()
                    while len(line.strip()) != 0:

                        self.simSettings.voltageValue.append(float(line.split()[0]))
                        self.simSettings.voltageDrive.append(line.split()[-1])
                        line = self.file.readline()

                elif line.startswith(self.recognitionIterationNumer[0]):
                    self.iterationCounter=self.iterationCounter+1

        self.simSettings.iterationNumber=int(self.iterationCounter/2)

        self.file.close()


        self.simData=SimulationData()




        with open(self.inFile, "r") as file:

            for line in file:
                if line.startswith(self.recognitionEmitterData[0]):
                    self.simSettings.primaryEmitterNumber=self.simSettings.primaryEmitterNumber+1
                    self.simSettings.primaryEmittersName.append(line.split(":")[1].split()[0])   
                    val = float(line.split("=")[1])
                    self.simData.allIterationsOfPrimaryEmitterData.append(val)                    

                elif line.startswith(self.recognitionEmitterData[1]):
                    self.simSettings.secondaryEmitterNumber=self.simSettings.secondaryEmitterNumber+1
                    self.simSettings.secondaryEmittersName.append(line.split(":")[1].split(",")[0].split()[0]) 
                    lineSpl = line.split(",")
                    val_in=float(lineSpl[1].split("=")[1])
                    val_out=float(lineSpl[2].split("=")[1])
                    self.simData.allIterationsOfSecondaryEmitterData.append(val_in)
                    self.simData.allIterationsOfSecondaryEmitterData.append(val_out)



        self.simSettings.primaryEmitterNumber=self.getEmitterNumber(1)
        self.simSettings.secondaryEmitterNumber=self.getEmitterNumber(2)
        
        self.simSettings.primaryEmittersName=self.simSettings.primaryEmittersName[0:self.simSettings.primaryEmitterNumber]
        self.simSettings.secondaryEmittersName=self.simSettings.secondaryEmittersName[0:self.simSettings.secondaryEmitterNumber]
     
   
        self.simData.primaryEmitterData=self.setEmitterData(1)
        self.simData.secondaryEmitterData=self.setEmitterData(2)
        

    def getEmitterNumber(self,typeEmitter):
        if typeEmitter==1:
            emitterNumber=int(self.simSettings.primaryEmitterNumber/self.simSettings.iterationNumber)
        elif typeEmitter==2:
            emitterNumber=int(self.simSettings.secondaryEmitterNumber/self.simSettings.iterationNumber)

        return emitterNumber


    def setEmitterData(self,typeEmitter): 
        if typeEmitter==1:

            lenData=len(self.simData.allIterationsOfPrimaryEmitterData)
            emitterData=self.simData.allIterationsOfPrimaryEmitterData[lenData-self.simSettings.primaryEmitterNumber:]

        elif typeEmitter==2:
            lenData=len(self.simData.allIterationsOfSecondaryEmitterData)
            emitterData=self.simData.allIterationsOfSecondaryEmitterData[lenData-2*self.simSettings.secondaryEmitterNumber:]

        return emitterData