#Importar los modulos
import subprocess
import argparse
import os
import pickle
import shutil

hacerlo = "Si"

def ValidatePath(thePath):
    #Valida si la ruta existe
    if not os.path.exists(thePath):
        raise argparse.ArgumentTypeError('Path does not exist')

    #Valida si se puede leer la ruta
    if os.access(thePath, os.R_OK):
        return thePath
    else:
        raise argparse.ArgumentTypeError('Path is not readable')

info = 'File System Baseline Creator with PowerShell- Version 1.0 December 2018'
parser = argparse.ArgumentParser(info)
parser.add_argument('-b', '--baseline',   required=True,
                    help="Specify the resulting baseline file")
parser.add_argument('-p', '--Path',       type= ValidatePath,
                    required=True, help="Specify the target folder to baseline")
parser.add_argument('-t', '--tmp',        required=True,
                    help="Specify a temporary result file for the PowerShell Script")

args = parser.parse_args()   

if hacerlo == "Si":
    baselineFile = args.baseline
    targetPath   = args.Path
    tmpFile      = args.tmp

    if __name__ == '__main__':

        try:
            #Ejecucion de powershell
            print()
            command = "powershell -ExecutionPolicy ByPass -File HashAcquire.ps1 -TargetFolder "+\
                    targetPath + " -ResultFile " + tmpFile 
            print(command)
            powerShellResult = subprocess.run(command, stdout=subprocess.PIPE)
            if powerShellResult.stderr == None:
                input("ya")
            
                #Creacion del diccionario
                baseDict = {}
                
                with open(tmpFile, 'r') as inFile:
                    for eachLine in inFile:
                        lineList = eachLine.split()
                        if len(lineList) == 2:
                            hashValue = lineList[0]
                        else:
                            continue
            
                with open(baselineFile, 'wb') as outFile:
                    pickle.dump(baseDict, outFile)
                    print("Baseline: ", baselineFile, " Created with:",
                        "{:,}".format(len(baseDict)), "Records")
                    print("Script Terminated Successfully")
            else:
                print("PowerShell Error:", p.stderr)
                
        except Exception as err:
            print ("Cannot Create Output File: "+str(err))
            quit()
        
        #Mover el archivo
        shutil.move(tmpFile, targetPath)
        shutil.move(baselineFile, targetPath)
else:
    pass
