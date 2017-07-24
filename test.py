##
##graphs=Graphs()
##
##graphs.plot2D(param.xPositionIons,param.zPositionIons,param.currentIons)
                        # if charge==-1:
                        # else:
                        #     sumIon=sumIon+1
                        #     for step in position:
                        #         if (-1<=float(step[0])<=2.4)and(-2.75<=float(step[1])<=2.5)and(-1.55<=float(step[2])<=1):
                        #             sumIonCollected=sumIonCollected+1
                        #             break
import subprocess



subprocess.Popen("readtrac.exe E:\\btrzpil\\helmer_database0_1.tracks B E:\\btrzpil\\helmer_database0_1.txt")




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


    def setPressureData(self,pressureData):
        self.pressureData=pressureData
        
    def setVoltageData(self,voltageData):
        self.voltageData=voltageData
        
    def setCurrentData(self,currentData):
        self.currentData=currentData

def plotSensitivityVsVoltage(self,sensitivityData,voltageData):
        self.setVoltageData(voltageData)
        
        xlabelText='Voltage [V]'
        ylabelText='Sensitivity $[mbar^{-1}]$'
        
        fig, ax = self.setFigure(xlabelText,ylabelText)
        
        numberFile=len(sensitivityData)

        for counterFile in range(numberFile):
            yData=[sensitivityData[counterFile][i] for i in range(len(sensitivityData[counterFile]))]
            self.plotLine(self.voltageData,yData,ax,self.lineType[counterFile],self.labelName[counterFile])

        self.setLegend(fig, ax)
        self.saveFigure(fig)




        
    def plotSenistivityVsCurrent(self,sensitivityData,currentData):
        self.setCurrentData(currentData)
        xData=[]
        yData=[]
        
        xlabelText='Current [A]'
        ylabelText='Sensitivity $[mbar^{-1}]$'
        
        fig, ax = self.setFigure(xlabelText,ylabelText)


        numberFile=len(sensitivityData)

        for counterFile in range(numberFile):
            yData=[sensitivityData[counterFile][i] for i in range(len(sensitivityData[counterFile]))]
            xData=[currentData[counterFile][i] for i in range(len(currentData[counterFile]))]

            ax.plot(xData, yData,'r-*',label='')


        #self.setLegend(fig, ax)
        self.saveFigure(fig)
        
    def plotSensitivityVsPressure(self,sensitivityData,pressureData):

        self.setPressureData(pressureData)
        
        xlabelText='Pressure [mbar]'
        ylabelText='Sensitivity $[mbar^{-1}]$'
        
        fig, ax = self.setFigure(xlabelText,ylabelText)

        numberFile=len(sensitivityData)

        for counterFile in range(numberFile):
            yData=[sensitivityData[counterFile][i] for i in range(len(sensitivityData[counterFile]))]
            self.plotLine(self.pressureData,yData,ax,self.lineType[counterFile],self.labelName[counterFile])

        ax.set_xscale('log')
        self.setLegend(fig, ax)
        self.saveFigure(fig)
