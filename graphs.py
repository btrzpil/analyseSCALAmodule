import matplotlib.pyplot as plt

class Graphs:
    pressureData=[]
    voltageData=[]
    currentData=[]


    lineType=[]
    labelName=[]


    def __init__(self,labelName):
        self.lineType=['r-*', 'b-*', 'k-*', 'g-*']
        self.labelName=labelName

    def setPressureData(self,pressureData):
        self.pressureData=pressureData
    def setVoltageData(self,voltageData):
        self.voltageData=voltageData
    def setCurrentData(self,currentData):
        self.currentData=currentData




    def plotLine(self,xData,yData,axes,line,textLabel):
        print(xData)
        print(yData)
        axes.plot(xData, yData,line,label=textLabel)
        return min(xData),max(xData),min(yData),max(yData)

    def plotSensitivityVsVoltage(self,sensitivityData,voltageData):
        self.setVoltageData(voltageData)
        
        fig, axes = plt.subplots( nrows=1, ncols=1)
        plt.grid(True)
        plt.xlabel('Voltage [V]')
        plt.ylabel('Sensitivity $[mbar^{-1}]$')

        numberFile=len(sensitivityData)

        for counterFile in range(numberFile):
            yData=[sensitivityData[counterFile][i] for i in range(len(sensitivityData[counterFile]))]
            self.plotLine(self.voltageData,yData,axes,self.lineType[counterFile],self.labelName[counterFile])

        # Now add the legend with some customizations.
        legend = axes.legend(loc='upper left')
        # The frame is matplotlib.patches.Rectangle instance surrounding the legend.
        frame = legend.get_frame()
        frame.set_facecolor('1')

        titleGraph="voltage"
        # plt.show()
        fig.savefig(titleGraph+".png")# save the figure to file

        
    def plotSenistivityVsCurrent(self,sensitivityData,currentData):
        self.setCurrentData(currentData)

        fig, axes = plt.subplots( nrows=1, ncols=1)
        plt.grid(True)
        plt.xlabel('Current [A]')
        plt.ylabel('Sensitivity $[mbar^{-1}]$')
        
        numberFile=len(sensitivityData)


        for counterFile in range(numberFile):
            yData=[sensitivityData[counterFile][i] for i in range(len(sensitivityData[counterFile]))]
            self.plotLine(self.currentData,yData,axes,self.lineType[counterFile],self.labelName[counterFile])

        # Now add the legend with some customizations.
        legend = axes.legend(loc='upper left')
        # The frame is matplotlib.patches.Rectangle instance surrounding the legend.
        frame = legend.get_frame()
        frame.set_facecolor('1')

        titleGraph="current"
        # plt.show()
        fig.savefig(titleGraph+".png")# save the figure to file
        
    def plotSensitivityVsPressure(self,sensitivityData,pressureData):

        self.setPressureData(pressureData)
        
        fig, axes = plt.subplots( nrows=1, ncols=1)
        plt.grid(True)
        plt.xlabel('Pressure [mbar]')
        plt.ylabel('Sensitivity $[mbar^{-1}]$')

        numberFile=len(sensitivityData)


        for counterFile in range(numberFile):
            yData=[sensitivityData[counterFile][i] for i in range(len(sensitivityData[counterFile]))]
            self.plotLine(self.pressureData,yData,axes,self.lineType[counterFile],self.labelName[counterFile])

        axes.set_xscale('log')
            
        #plt.axis([0,maxPressureData, 0, maxSensitivityData+5])
        
        # Now add the legend with some customizations.
        legend = axes.legend(loc='upper left')
        # The frame is matplotlib.patches.Rectangle instance surrounding the legend.
        frame = legend.get_frame()
        frame.set_facecolor('1')

        titleGraph="pressure"
        # plt.show()
        fig.savefig(titleGraph+".png")# save the figure to file
        

