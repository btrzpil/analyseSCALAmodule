from filetracks import FileTracks
from parameterstrackparticle import ParametersTrackParticles
import time



filePath="E:\\btrzpil\\OperaSimulations\\shg\\sim\\deflector-h"
for i in range(0,10):
	fileName="\\model_helmer_database_"+str(i+1) 
	tracks = FileTracks(filePath,fileName)
	tracks.parseFile()
	time.sleep(30)

