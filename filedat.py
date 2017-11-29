class FileDat:
   

    fileExtension=".dat"
    
    def __init__(self, filePath,fileName):
        self.inFile=filePath+fileName+self.fileExtension

    def readFile(self):

        self.distanceData=[]
        self.potentialData=[]

        self.file = open(self.inFile,'r')

        self.readLines(6)
        while True:

            line = self.file.readline()

            if line == '':

                break
            else:

                self.distanceData.append(float(line.split()[0]))
                self.potentialData.append(float(line.split()[3]))

        self.file.close()


    def readLines(self,numberLines):
        for i in range(numberLines):
            self.file.readline()