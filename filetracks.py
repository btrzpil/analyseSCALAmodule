import os as os
import subprocess as subprocess

class FileTracks:
    
    fileExtensionTxt=".txt"
    fileExtensionTracks=".tracks"
    recognitionText = ["                   Writing track number:"]
    programName="readtrac.exe "
    programArgument=" B "
    tracksInformation=[]
    startPositionTrack=[]
    endPositionTrack=[]
    
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


		#subprocess.Popen("readtrac.exe E:\\btrzpil\\helmer_database0_1.tracks B E:\\btrzpil\\helmer_database0_1.txt")

        commandExecuteProgram = self.programName + self.fileTracks + self.programArgument + self.fileTxt
        subprocess.Popen(commandExecuteProgram)
        

    
    def readFile(self):

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


                        
                        for step in range(NSTEP):
                            if step == 0:
                                startPosition=file.readline().split()


                            elif step == NSTEP-1:
                                endPosition=file.readline().split()

                            else:
                                file.readline()
                                
                        trackInformation.append(trackCounter)
                        trackInformation.append(NSTEP)
                        trackInformation.append(emitterNumber)
                        trackInformation.append(currentTrack)
                        trackInformation.append(mass)
                        trackInformation.append(charge)
                        trackInformation.append(stepLength)
                        self.tracksInformation.append(trackInformation)
                        

                        self.startPositionTrack.append(startPosition)
                        self.endPositionTrack.append(endPosition)
                        

    def debugTracks(self,numberTrack):
        print(self.tracksInformation[numberTrack])
        print(self.startPositionTrack[numberTrack])
        print(self.endPositionTrack[numberTrack])
        print(self.header)



