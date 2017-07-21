import os as os
import subprocess as subprocess

class FileTracks:
    
    fileExtensionTxt=".txt"
    fileExtensionTracks=".tracks"
    recognitionText = ["                   Writing track number:"]
    programName="readtrac.exe "
    programArgument=" B "

  
    def __init__(self,filePath,fileName):
        self.tracksInformation=[]
        self.startPositionTrack=[]
        self.endPositionTrack=[]
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


		#subprocess.Popen("readtrac.exe E:\\btrzpil\\helmer_database0_1.tracks B E:\\btrzpil\\helmer_database0_1.txt")

        commandExecuteProgram = self.programName + self.fileTracks + self.programArgument + self.fileTxt
        subprocess.Popen(commandExecuteProgram)
        

    
    def readFile(self):
        sumIon=0
        sumIonCollected=0
        trackCounter=0
        inFile=self.fileTxt
        with open(inFile, "r") as file:
            
            while True:
                trackInformation=[]

                line = file.readline()

                if line == '':
                    print("file finished")
                    break
                else:
                    if line.startswith(self.recognitionText[0]):
                        trackCounter = trackCounter+1
                        
                        lineITRAK = file.readline()
                        ITRAK=lineITRAK.split()
                        
                        NSTEP=int(ITRAK[0])

                        emitterNumber=int(ITRAK[2])
                        file.readline()
                        file.readline()
                        file.readline()
                        
                        RTRACK=file.readline().split()

                        currentTrack=float(RTRACK[0])
                        mass=float(RTRACK[1])
                        charge=float(RTRACK[2])
                        stepLength=float(RTRACK[3])
                        file.readline()
                        file.readline()
                        file.readline()

                        if (trackCounter==1):
                            self.header = file.readline()#header
                        else:
                            file.readline()


                        position=[]

                        for step in range(NSTEP):
                            position.append(file.readline().split()[1:4])
                        if charge==-1:
                        else:
                            sumIon=sumIon+1
                            for step in position:
                                if (-1<=float(step[0])<=2.4)and(-2.75<=float(step[1])<=2.5)and(-1.55<=float(step[2])<=1):
                                    sumIonCollected=sumIonCollected+1
                                    break

                        trackInformation.append(trackCounter)
                        trackInformation.append(NSTEP)
                        trackInformation.append(emitterNumber)
                        trackInformation.append(currentTrack)
                        trackInformation.append(mass)
                        trackInformation.append(charge)
                        trackInformation.append(stepLength)
                        self.tracksInformation.append(trackInformation)


                        startPosition=[position[0][i] for i in range(3)]
                        endPosition=[position[NSTEP-1][i] for i in range(3)]

                        self.startPositionTrack.append(startPosition)
                        self.endPositionTrack.append(endPosition)
        print(sumIonCollected)
        print(sumIon)

                        

    def debugTracks(self,numberTrack):
        print(self.tracksInformation[numberTrack])
        print(self.startPositionTrack[numberTrack])
        print(self.endPositionTrack[numberTrack])
        print(self.header)



