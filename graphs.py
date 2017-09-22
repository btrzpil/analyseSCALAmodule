import matplotlib.pyplot as plt
import numpy as np
import scipy as scipy
from scipy import interpolate



class Graphs:
#b : blue.
#g : green.
#r : red.
#c : cyan.
#m : magenta.
#y : yellow.
#k : black.
#w : white.


    def __init__(self,graphTitle,graphPath):
        self.lineType=['r-*', 'b-*', 'k-*', 'g-*','c-*','m-*']
        self.graphTitle=graphTitle
        self.graphPath=graphPath

    def setLabelLine(self,labelLine):
        self.labelLine=labelLine
 
    def setFigure(self,xlabelText,ylabelText):
        fig, ax = plt.subplots( nrows=1, ncols=1)
        plt.grid(True)
        plt.xlabel(xlabelText)
        plt.ylabel(ylabelText)
        return fig, ax
    
    def setLegend(self,fig, ax):                
        #plt.axis([0,maxPressureData, 0, maxSensitivityData+5])
        legend = ax.legend(loc='lower left')
        frame = legend.get_frame()
        frame.set_facecolor('1')      
        
    def saveFigure(self,fig):
        fig.savefig(self.graphPath+self.graphTitle+".png")# save the figure to file        

    def plotLine(self,xData,yData,ax,line,labelLine):
        ax.plot(xData, yData,line,label=labelLine)
        return min(xData),max(xData),min(yData),max(yData)

    def plotMeanPathPrimaryParticles(self,xData,meanPathPrimaryParticles,xlabelText):

        ylabelText='Mean Path Primary Particles [mm]'
        fig, ax = self.setFigure(xlabelText,ylabelText)
        labelLine=xlabelText
        self.plotLine(xData,meanPathPrimaryParticles,ax,self.lineType[0],labelLine)
        if xlabelText=='Pressure [mbar]':
            ax.set_xscale('log')
        self.saveFigure(fig)


    def plotIonEfficency(self,xData,ionEfficency,xlabelText):

        ylabelText='Ion Efficency'
        fig, ax = self.setFigure(xlabelText,ylabelText)
        labelLine=xlabelText
        self.plotLine(xData,ionEfficency,ax,self.lineType[0],labelLine)
        if xlabelText=='Pressure [mbar]':
            ax.set_xscale('log')

        self.saveFigure(fig)

    def plotSensitivity(self,sensitivityData,xData,xlabelText,labelLine):
        self.setLabelLine(labelLine)
        ylabelText='Sensitivity $[mbar^{-1}]$'
        fig, ax = self.setFigure(xlabelText,ylabelText)

        numberFile=len(sensitivityData)

        for counterFile in range(numberFile):
            yData=[sensitivityData[counterFile][i] for i in range(len(sensitivityData[counterFile]))]
            self.plotLine(xData,yData,ax,self.lineType[counterFile],self.labelLine[counterFile]) 
        
        if xlabelText=='Pressure [mbar]':
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

        xi = linspace(min(x), max(x), resX)
        yi = linspace(min(y), max(y), resY)
        Z = griddata(x, y, z, xi, yi)
        X, Y = meshgrid(xi, yi)
        return X, Y, Z        



        

