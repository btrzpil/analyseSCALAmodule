import matplotlib.pyplot as plt
import numpy as np
import scipy as scipy
from scipy import interpolate



class Graphs:

    contrastingColors = ["#bf0000", "#f29979", "#ffa640", "#b2aa2d", "#e6f2b6", "#829973", "#00736b", "#164c59", 
                        "#00294d", "#80a2ff", "#6d00cc", "#3d004d", "#ff00ee", "#992645", "#660000", "#e55c00", 
                        "#7f5320", "#e2f200", "#354020", "#008033", "#3df2e6", "#739199", "#b6cef2", "#000033", 
                        "#d580ff", "#944d99", "#ff40a6", "#400009", "#403230", "#662900", "#33210d", "#475900", 
                        "#74d900", "#3df285", "#00c2f2", "#0080bf", "#3056bf", "#504d66", "#eabfff", "#322633", 
                        "#ff0044", "#d9a3aa"];

    def __init__(self,graphName):

        self.graphName=graphName



 
    def setFigure(self,xAxLabel,yAxLabel):
        fig, ax = plt.subplots( nrows=1, ncols=1)
        plt.grid(True)
        plt.xlabel(xAxLabel)
        plt.ylabel(yAxLabel)
        return fig, ax
    
    def setLineLabel(self,lineLabel):
        self.lineLabel=lineLabel

    def setLegend(self,fig, ax, legendTitle):                
        legend = ax.legend(loc='lower left',title=legendTitle)
        frame = legend.get_frame()
        frame.set_facecolor('1')

    def saveFigure(self,fig,graphPath):
        self.graphPath=graphPath
        fig.savefig(self.graphPath+self.graphName+".png")# save the figure to file        

    def plotLine(self,xData,yData,ax,lineColor,lineLabel):

        ax.plot(xData, yData,marker='.',linestyle='-',color=lineColor,label=lineLabel)
        return min(xData),max(xData),min(yData),max(yData)


    def plotGraph(self,xData, yData,xAxLabel,yAxLabel,lineLabel,legendTitle,graphPath):
     
        fig, ax = self.setFigure(xAxLabel,yAxLabel)
        self.setLineLabel(lineLabel)


        numberFile=len(yData)

        lenM = np.shape(xData)
        if len(lenM) == 1:
            x=xData
            y=yData
            self.plotLine(x,y,ax,self.contrastingColors[0],self.lineLabel) 

        elif len(lenM) == 2:
            numberFile=len(yData)

            for counterFile in range(numberFile):
                x=[xData[counterFile][i] for i in range(len(xData[counterFile]))]
                y=[yData[counterFile][i] for i in range(len(yData[counterFile]))]
                self.plotLine(x,y,ax,self.contrastingColors[counterFile],self.lineLabel[counterFile]) 
                self.setLegend(fig, ax,legendTitle)
        darrx=np.array(x)

        if darrx.min()==0:
            x_state=darrx.max()-darrx.min()
            print(darrx.max())
            print(darrx.min())
        else:
            x_state=darrx.max()/darrx.min()

        darry=np.array(y)   
        if darry.min()==0:
            y_state=darry.max()-darry.min()
        else:
            y_state=darry.max()/darry.min()           

        

        if x_state>100:
            ax.set_xscale('log')
        if y_state>500:
            ax.set_yscale('log')
   
        
        self.saveFigure(fig,graphPath)

    def plotMeanPathLengthPrimaryParticles(self,xData,meanPathLengthPrimaryParticlesData,xAxLabel,lineLabel,legendTitle,graphPath):
        yAxLabel='Mean Path Length Primary Particles [cm]'
        self.plotGraph(xData, meanPathLengthPrimaryParticlesData,xAxLabel,yAxLabel,lineLabel,legendTitle,graphPath)

    def plotIonEfficency(self,xData,ionEfficencyData,xAxLabel,lineLabel,legendTitle,graphPath):
        yAxLabel='Ion Efficency $[\%]$'
        self.plotGraph(xData, ionEfficencyData,xAxLabel,yAxLabel,lineLabel,legendTitle,graphPath)

    def plotPotentialProfile(self,distanceData,potentialData,lineLabel,legendTitle,graphPath):

        xAxLabel='Distance [mm]'
        yAxLabel='Electric potential [V]'
        self.plotGraph(distanceData, potentialData,xAxLabel,yAxLabel,lineLabel,legendTitle,graphPath)

    def plotSensitivity(self,xData,sensitivityData,xAxLabel,lineLabel,legendTitle,graphPath):
        yAxLabel='Sensitivity $[mbar^{-1}]$'
        self.plotGraph(xData, sensitivityData,xAxLabel,yAxLabel,lineLabel,legendTitle,graphPath)

    def plotYield(self,xData,yieldData,xAxLabel,lineLabel,legendTitle,graphPath):
        yAxLabel='Yiled $[cm^{-1}]$'
        self.plotGraph(xData, yieldData,xAxLabel,yAxLabel,lineLabel,legendTitle,graphPath)

    def plotTransmissionEfficency(self,xData,transEfficencyData,xAxLabel,lineLabel,legendTitle,graphPath):
        yAxLabel='Electron Transmission Efficency $[\%]$'
        self.plotGraph(xData, transEfficencyData,xAxLabel,yAxLabel,lineLabel,legendTitle,graphPath)



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



        

