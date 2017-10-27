import matplotlib.pyplot as plt
import numpy as np
from fileres import FileRes
from parameters import Parameters
from graphs import Graphs
from filedat import FileDat
from filetracks import FileTracks
from parameterstrackparticle import ParametersTrackParticles
from parameterstrackparticle import Volume
from parameterstrackparticle import Cylinder
from parameterstrackparticle import Cuboid
import time

filePath="E:\\btrzpil\\EMPIR\\Works\\Sim\\proposal2\\sBeam04res"
fileName="\\c_0_1_0_0_0"

res=FileRes(filePath,fileName)
res.readFile()