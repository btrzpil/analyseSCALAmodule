import os
import win32com.shell.shell as shell
class FileTracks:
    
    fileExtensionTxt=".txt"
    fileExtensionDat=".txt"
    fileExtensionTracks=".tracks"
    recognitionText = ["                   Writing track number:"]

    tracksInformation=[]
    startPositionTrack=[]
    endPositionTrack=[]
    




    def setFilePath(self, filePath):
        self.filePath=filePath
        
    def setFileName(self, fileName):
        self.fileName=fileName
        
    def setReadtrackPath(self, programPath):
        self.programPath=programPath
        
    def parseFile(self):
        programName="\\readtrac.exe "
        
        inFile=self.filePath+self.fileName+self.fileExtensionTracks
        outFile=self.filePath+self.fileName+self.fileExtensionDat
        command='\"\"'+self.programPath+programName+'\"\"'


        commands = 'echo hi'
        shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe', lpParameters='/c '+commands)
        #.\readtrac.exe E:\btrzpil\helmer.tracks B E:\btrzpil\h.txt
        #.\readtrac.exe E:\btrzpil\helmer.tracks B E:\btrzpil\h.txt
    def readFile(self):
        inFile=self.filePath+self.fileName+self.fileExtensionTxt
        trackCounter=0

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

              
                        
                       

##        with open(inFile, "r") as file:        
##            lineCounter = 0
##
##            #for i, line in enumerate(file):
##            #for line in file:
##            file.seek(lineCounter, 0)   
##            line=file.readline()
##            print(line)
##            if line.startswith(self.recognitionText[0]):
##                lineCounter=lineCounter+1
##                file.seek(lineCounter, 0) 
##                line=file.readline()
##                print(line)



                    



