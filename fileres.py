class SimulationSettings:

    def __init__(self):

        self.emitterLabel=[]
        self.voltageLabel=[]
        self.voltageValue=[]
        self.pressure=[]
        self.residualGas=[]
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

    def __init__(self, filePath,fileName):
        self.inFile=filePath+fileName+self.fileExtension

    def readFile(self):




        self.setSimulationSettings()

        self.setSimulationData()




    def setSimulationSettings(self):
        simSettings=SimulationSettings()        
        self.file = open(self.inFile,'r')
            
        while True:

            line = self.file.readline()

            if line == '':
                break
            else:
                if line.startswith(self.recognitionTitle[0]):
                    pressure=self.file.readline().split(":")[1]
                    residualGas=self.file.readline().split(":")[1]
                    simSettings.pressure.append(float(pressure))
                    simSettings.residualGas.append(residualGas)


                elif line.startswith(self.recognitionVoltage[0]):
                    print(line)


                elif line.startswith(self.recognitionEmitter[0]):
                    emitter=line.split()[1]
                    simSettings.emitterLabel.append(emitter)

        self.file.close()


    def setSimulationData(self):    
        simData=SimulationData()
        iterationCounter=0

        with open(self.inFile, "r") as file:

            for line in file:
                if line.startswith(self.recognitionEmitterData[0]):
                    lineSpl = line.split("=")
                    val = float(lineSpl[1])
                    print(val)
                elif line.startswith(self.recognitionEmitterData[1]):
                    lineSpl = line.split(",")
                    val_in=float(lineSpl[1].split("=")[1])
                    val_out=float(lineSpl[2].split("=")[1])
                    print(val_in)
                    print(val_out)
