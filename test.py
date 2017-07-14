
import subprocess

##filePath="E:\\btrzpil\\OperaSimulations\\simulation/ Helmer/ Gauge\\research\\research/ -/ pressure\\result"
##fileName="helmer_database0_1"
##inFile=filePath+fileName+".tracks"
##outFile=filePath+fileName+".txt"
##command = "readtrac.exe "+str(inFile)+" B " +str(outFile)
##print(command)
##subprocess.Popen(command)

subprocess.Popen("readtrac.exe E:\\btrzpil\\helmer_database0_1.tracks B E:\\btrzpil\\h_1.txt")
