import os as os
import subprocess as subprocess

class Trajectories:
    def __init__(self):
        self.TrajectoriesCoordinates=[]
        self.TrajectoriesParameters=[]
        self.TrajectoriesStartPosition=[]
        self.TrajectoriesEndPosition=[]

class Position:
    def __init__(self):
        self.position=[]

class FileTracks:
    
    fileExtensionTxt=".txt"
    fileExtensionTracks=".tracks"
    recognitionText = ["                   Writing track number:"]
    programName="readtrac.exe "
    programArgument=" B "

  
    def __init__(self,filePath,fileName):

        self.setFilePath(filePath)
        self.setFileName(fileName)
        self.setFile()


    def setFilePath(self,filePath):

        self.filePath=filePath

    def setFileName(self,fileName):

        self.fileName=fileName

    def setFile(self):

        self.fileTracks=self.filePath+self.fileName+self.fileExtensionTracks
        self.fileTxt=self.filePath+self.fileName+self.fileExtensionTxt
        
        
    def parseFile(self):

        commandExecuteProgram = self.programName + self.fileTracks + self.programArgument + self.fileTxt
        subprocess.Popen(commandExecuteProgram)
        

    
    def readFile(self):

        self.trackCounter=0
        self.trajectories=Trajectories()    
        self.file = open(self.fileTxt,'r')
            
        while True:

            line = self.file.readline()

            if line == '':
                print("file finished")
                break
            else:
                if line.startswith(self.recognitionText[0]):
                    self.trackCounter = self.trackCounter+1
                        
                    ITRAK=self.file.readline().split()
                    self.readLines(3)    
                    RTRACK=self.file.readline().split()
                    self.readLines(3) 
                    #header
                    self.readLines(1)
                    self.addTrajectoriesParameters(ITRAK,RTRACK)   
                    self.addTrajectoriesCoordinates()

        self.file.close()


    def addTrajectoriesCoordinates(self):
        pos=Position()
        NSTEP=self.trajectories.TrajectoriesParameters[self.trackCounter-1][1]
        for step in range(NSTEP):
            tabStr=self.file.readline().split()[1:4]
            tabFloat = [float(s) for s in tabStr]
            pos.position.append(tabFloat)

                
        startPosition=[pos.position[0][i] for i in range(3)]
        endPosition=[pos.position[NSTEP-1][i] for i in range(3)]

        self.trajectories.TrajectoriesCoordinates.append(pos.position)
        self.trajectories.TrajectoriesStartPosition.append(startPosition)
        self.trajectories.TrajectoriesEndPosition.append(endPosition)       

    def addTrajectoriesParameters(self,ITRAK,RTRACK):
        trackInformation=[]
        trackCounter=self.trackCounter
        NSTEP=int(ITRAK[0])
        emitterNumber=int(ITRAK[2])
        currentTrack=float(RTRACK[0])
        mass=float(RTRACK[1])
        charge=float(RTRACK[2])
        stepLength=float(RTRACK[3])


        trackInformation.append(trackCounter)
        trackInformation.append(NSTEP)
        trackInformation.append(emitterNumber)
        trackInformation.append(currentTrack)
        trackInformation.append(mass)
        trackInformation.append(charge)
        trackInformation.append(stepLength)

        self.trajectories.TrajectoriesParameters.append(trackInformation)                

    def readLines(self,numberLines):
        for i in range(numberLines):
            self.file.readline()

    # def debugTracks(self,numberTrack):
    #     print(self.tracksInformation[numberTrack])
    #     print(self.startPositionTrack[numberTrack])
    #     print(self.endPositionTrack[numberTrack])
    #     print(self.header)





        



