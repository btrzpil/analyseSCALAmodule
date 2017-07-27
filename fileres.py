class SimulationData:

    def __init__(self):
        self.SimulationDataParameters=[]

class FileRes:
   
    recognitionText = [" Primary Emitter ", " Secondary Emitter"]
    lastIterationDataSimulation=[]
    firstIterationDataSimulation=[]
    nameEmitter=[]
    numberSimulation=0
    numberEmitter=0
    fileExtension=".res"
    
    def __init__(self, filePath,fileName):
        self.inFile=filePath+fileName+self.fileExtension
        

    def readFile(self):     
        lastIterationDataSimulation=[]
        firstIterationDataSimulation=[]
        dataSimulation=[]
        nameEmitter=[]
        with open(self.inFile, "r") as file:
                simulationCounter=1
                simulationCounterTmp=simulationCounter
                iterationCounter=0

                for line in file:
        
                    recognitionTextSimulationIndicator = [" Simulation " + str(simulationCounter)+" "]
        
                    if line.startswith(recognitionTextSimulationIndicator[0]):

                        if (simulationCounterTmp==simulationCounter):

                            simulationCounter=simulationCounter+1

                        else:

                            counterColDataFile = len(dataSimulation) // iterationCounter

                            startLastIteration=len(dataSimulation)- counterColDataFile
                            endLastIteration=len(dataSimulation)
                            lastIterationDataSimulation.append(dataSimulation[startLastIteration:endLastIteration])

                            startFirtIteration=0
                            endLastIteration=counterColDataFile
                            firstIterationDataSimulation.append(dataSimulation[startFirtIteration:endLastIteration])

                            dataSimulation=[]
                            simulationCounterTmp=simulationCounter
                            iterationCounter=0



                    if line.startswith(self.recognitionText[0]):
                
                        lineSpl = line.split("=")
                        val = float(lineSpl[1])
                        dataSimulation.append(val)
                        iterationCounter=iterationCounter+1
                        if (iterationCounter==1):

                            nameEmitter.append((lineSpl[0].split(":"))[1])
                        
                
                    elif line.startswith(self.recognitionText[1]):

                        lineSpl = line.split(",")
                        val_in=float(lineSpl[1].split("=")[1])
                        val_out=float(lineSpl[2].split("=")[1])
                        
                        dataSimulation.append(val_in)
                        dataSimulation.append(val_out)
                        if (iterationCounter==1):

                            nameEmitter.append(str(lineSpl[0].split(":")[1]))



                            



                            
                if dataSimulation != []:

                    counterColDataFile = len(dataSimulation)// iterationCounter
                    
                    startLastIteration=len(dataSimulation)- counterColDataFile
                    endLastIteration=len(dataSimulation)
                    
                    lastIterationDataSimulation.append(dataSimulation[startLastIteration:endLastIteration])

                    
                    startFirtIteration=0
                    endLastIteration=counterColDataFile
                    
                    firstIterationDataSimulation.append(dataSimulation[startFirtIteration:endLastIteration])





        self.firstIterationDataSimulation=firstIterationDataSimulation
        self.lastIterationDataSimulation=lastIterationDataSimulation
        
        self.numberEmitter=int(len(nameEmitter)/(simulationCounter-1))

        self.numberSimulation=simulationCounter-1
        self.nameEmitter=nameEmitter[0:self.numberEmitter]

        



