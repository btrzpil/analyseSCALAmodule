import matplotlib.pyplot as plt

import numpy as np
import scipy as scipy

from scipy import interpolate



class Graphs:
    pressureData=[]
    voltageData=[]
    currentData=[]


    lineType=[]
    labelName=[]


    def __init__(self):
        self.lineType=['r-*', 'b-*', 'k-*', 'g-*','k-*']

    def setGraphLabel(self,labelName):
        self.labelName=labelName
        
    def setPressureData(self,pressureData):
        self.pressureData=pressureData
        
    def setVoltageData(self,voltageData):
        self.voltageData=voltageData
        
    def setCurrentData(self,currentData):
        self.currentData=currentData


    def setFigure(self,xlabelText,ylabelText):
        fig, ax = plt.subplots( nrows=1, ncols=1)
        plt.grid(True)
        plt.xlabel(xlabelText)
        plt.ylabel(ylabelText)
        return fig, ax
    
    def setLegend(self,fig, ax):                
        #plt.axis([0,maxPressureData, 0, maxSensitivityData+5])
        legend = ax.legend(loc='upper left')
        frame = legend.get_frame()
        frame.set_facecolor('1')
        
    def setGraphTitle(self,graphTitle):
        self.graphTitle=graphTitle

    def setGraphPath(self,graphPath):
        self.graphPath=graphPath
        
    def saveFigure(self,fig):

        fig.savefig(self.graphPath+self.graphTitle+".png")# save the figure to file        

    def plotLine(self,xData,yData,ax,line,textLabel):
        ax.plot(xData, yData,line,label=textLabel)
        return min(xData),max(xData),min(yData),max(yData)

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

##    def ionCreationMaps(self, xData,yData,zData):
##
##    def ionDestinationMaps(self, xData,yData,zData):

    def plot2D(self, x,y,z):



        # Set up a regular grid of interpolation points
        print(len(x))
        x_min=float(min(x))
        x_max=float(max(x))
        y_min=float(min(y))
        y_max=float(max(y))

        xi, yi = np.linspace(x_min, x_max, 500), np.linspace(y_min, y_max, 500)
        xi, yi = np.meshgrid(xi, yi)

        # Interpolate; there's also method='cubic' for 2-D data such as here
        zi = scipy.interpolate.griddata((x, y), z, (xi, yi), method='cubic')

        plt.imshow(zi, vmin=float(min(z)), vmax=float(max(z)), origin='lower',
           extent=[x_min, x_max, y_min, y_max])
        plt.colorbar()
        plt.show()


    def grid(x, y, z, resX=100, resY=100):
        "Convert 3 column data to matplotlib grid"
        xi = linspace(min(x), max(x), resX)
        yi = linspace(min(y), max(y), resY)
        Z = griddata(x, y, z, xi, yi)
        X, Y = meshgrid(xi, yi)
        return X, Y, Z        



        

