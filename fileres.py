class SimulationSettings:

    def __init__(self):

        self.emitterName=[]
        self.voltageDrive=[]
        self.voltageValue=[]


#residual Gas - title 
#pressure - title
#emitter 

#voltage


class SimulationData:

    def __init__(self):
        self.firstIterationData=[]
        self.lastIterationData=[]

class FileRes:     
    fileExtension=".res"
    recognitionVoltage=["      VOLTAGE"]
    recognitionTitle=["    User title:"]
    recognitionEmitter=[" Emitter:"]
    recognitionEmitterData = [" Primary Emitter ", " Secondary Emitter"]
    recognitionIterationNumer=[" Nonlinear iteration "]

    def __init__(self, filePath,fileName):
        self.inFile=filePath+fileName+self.fileExtension

    def readFile(self):

        self.simSettings=SimulationSettings()        
        self.file = open(self.inFile,'r')
        iterationCounter=0   
        while True:

            line = self.file.readline()

            if line == '':
                break
            else:
                if line.startswith(self.recognitionTitle[0]):
                    self.simSettings.pressure=float(self.file.readline().split(":")[1])
                    self.simSettings.residualGas=self.file.readline().split(":")[1]
                elif line.startswith(self.recognitionVoltage[0]):
                    self.simSettings.voltageDrive.append(line)
                elif line.startswith(self.recognitionEmitter[0]):
                    emitter=line.split()[1]
                    self.simSettings.emitterName.append(emitter)
                elif line.startswith(self.recognitionIterationNumer[0]):
                    iterationCounter=iterationCounter+1

        self.simSettings.emitterNumber=len(self.simSettings.emitterName)
        self.simSettings.iterationNumber=int(iterationCounter/2)

        self.file.close()


        self.simData=SimulationData()
        tmpPrimaryEmitterData=[]
        tmpSecondaryEmitter=[]
        tmpData=[]
        primaryEmitterNumber=0

        with open(self.inFile, "r") as file:

            for line in file:
                if line.startswith(self.recognitionEmitterData[0]):
                    primaryEmitterNumber=primaryEmitterNumber+1
                    lineSpl = line.split("=")
                    val = float(lineSpl[1])
                    tmpData.append(val)                     

                elif line.startswith(self.recognitionEmitterData[1]):
                    lineSpl = line.split(",")
                    val_in=float(lineSpl[1].split("=")[1])
                    val_out=float(lineSpl[2].split("=")[1])
                    tmpData.append(val_in)
                    tmpData.append(val_out)

        self.simSettings.primaryEmitterNumber=int(primaryEmitterNumber/self.simSettings.iterationNumber)
        dataNumber=self.simSettings.emitterNumber*2-self.simSettings.primaryEmitterNumber

        self.simData.firstIterationData=[tmpData[i] for i in range(0,dataNumber)]
        self.simData.lastIterationData=[tmpData[i] for i in range((self.simSettings.iterationNumber-1)*dataNumber,len(tmpData))]



           