import argparse
import re
import nmap
import csv
import os
import shutil
from openpyxl import Workbook
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import subprocess
import pickle
from Wappalyzer import Wappalyzer, WebPage
import logging
import time
import requests
import json
#
#Creo una lista con los argumentos validos para cada parámetro
valid_nmap = ['txt','csv','xlsx']
valid_hash = ['y','Y']
valid_correo = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')


os.mkdir('Reporte')
z=1

def ValidatePath(thePath):
    #Valida si la ruta existe
    if not os.path.exists(thePath):
        raise argparse.ArgumentTypeError('Path does not exist')

    #Valida si se puede leer la ruta
    if os.access(thePath, os.R_OK):
        return thePath
    else:
        raise argparse.ArgumentTypeError('Path is not readable')



parser = argparse.ArgumentParser(description="A program wih many Cibersecurity tools")

parser.add_argument('-i', '--ipadress', type=str, help='ip address of the host', required=True)
parser.add_argument('-s', '--start',       type = int, required = True, help="Specify the beginning of the range to scan")
parser.add_argument('-e', '--end',       type = int, required = True, help="Specify the end of the range to scan") 
parser.add_argument('-o', '--output',        required=True, default= 'txt',help="Specify the output file for the scanning")
parser.add_argument('-b', '--baseline',   required=True,
                    help="Specify the resulting baseline file")
parser.add_argument('-p', '--Path',       type= ValidatePath,
                    required=True, help="Specify the target folder to baseline")
parser.add_argument('-t', '--tmp',        required=True,
                    help="Specify a temporary result file for the PowerShell Script")
#
parser.add_argument('-hs', '--hash', dest='p_hash', help='Genera el valor hash del archivo de escaneo')

parser.add_argument('-d', '--destino', help='Correo al cual se enviará la información')
parser.add_argument('-r', '--ruta', help="Ruta de la carpeta que se enviará por correo")
parser.add_argument('-url', '--url', help = 'Ingresa la url del sitio web', type= str,  default = '')
args = parser.parse_args()
url = args.url  

#---------------------------------------------------------------
if (args.output in valid_nmap):
    # instantiate a PortScanner object
    scanner = nmap.PortScanner()

    #Crear el directorio
    #os.mkdir('Reporte')
    target = args.ipadress
    begin = args.start
    end = args.end
    output  = args.output

    wb = Workbook() 
    ws = wb.active
    j= 1
    for i in range(begin,end+1):
    
        # scan the target port
        res = scanner.scan(target,str(i))
    
        # the result is a dictionary containing 
        # several information we only need to
        # check if the port is opened or closed
        # so we will access only that information 
        # in the dictionary
        res = res['scan'][target]['tcp'][i]['state']

        if args.output == "xlsx":
            #Exporting data to Excel
            if res == "open":
                A = str(f'{target} port {i} is "open"')
                ws['A' + str(j)] = A
                j+=1

        elif args.output == "csv":   
            #Crear archivo .csv
            with open('reporte_puertos.csv', 'a+', newline='') as puertos:
                respuesta = csv.writer(puertos, delimiter=' ',
                                        quotechar='_', quoting=csv.QUOTE_MINIMAL)
                if res == "open":
                    #print(f'{target} port {i} is "open"')
                    respuesta.writerow(f'{target} port {i} is "open"')

        elif args.output == "txt":
            #crear archivo txt
            with open('reporte_puertos.txt', 'a') as f:
                    if res == "open":
                        #print(f'{target} port {i} is "open"')
                        f.write(f'{target} port {i} is "open"')
                        f.write("\n")
                        f.close()

    # guardar archivo xlsx
    if args.output == "xlsx":
        wb.save('reporte_puertos.xlsx')

    #Mover el archivo
    if args.output == "xlsx":
        shutil.move("reporte_puertos.xlsx","Reporte")
    elif args.output == "csv":
        shutil.move("reporte_puertos.csv","Reporte")
    else:
        shutil.move("reporte_puertos.txt","Reporte")
    pass

#---------------------------------------------------------------
if args.p_hash in valid_hash:
    baselineFile = args.baseline
    targetPath   = args.Path
    tmpFile      = args.tmp

    if __name__ == '__main__':

        try:
            #Ejecucion de powershell
            print()
            command = "powershell -ExecutionPolicy ByPass -File HashAcquire.ps1 -TargetFolder "+\
                    targetPath + " -ResultFile " + tmpFile 
            powerShellResult = subprocess.run(command, stdout=subprocess.PIPE)
            if powerShellResult.stderr == None:            
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
                
        except Exception as err:
            quit()
        
        #Mover el archivo
        shutil.move(tmpFile, targetPath)
        shutil.move(baselineFile, targetPath)
else:
    pass


#----------------------------------------------------------
logging.basicConfig(filename='tecnologias.log',level=logging.INFO)
wb = Workbook() 
ws = wb.active

logging.basicConfig(filename='tecnologias.log',level=logging.INFO)
wb = Workbook() 
ws = wb.active
b=1
wap = Wappalyzer.latest()    
logging.info('Datos para ver las tecnologias de la pagina: ')
logging.info(url)
web = WebPage.new_from_url(url)
tecnologias = wap.analyze(web)
for t in tecnologias:
    A = str("Tecnologias detectadas: {}".format(t))
    ws['A' + str(b)] = A
    b+=1


wb.save('Tecnologias.xlsx')
shutil.move("Tecnologias.xlsx","Reporte")
#---------------------------------------------------------------
contador=2
llavesota = '05d18babf615b8c17646aaa1bd1edbb434902aa5d3ead9670e90928c0f89575a'
macizo= url


wb = Workbook() 
ws = wb.active

def verificacion(direccion, APIkey):
    refe = 'https://www.virustotal.com/vtapi/v2/url/report'
    parametros = {'apikey': APIkey, 'resource': direccion}
    response = requests.get(url=refe, params=parametros)
    json_response = json.loads(response.text)
    A = json_response['resource']
    B = json_response['scan_date']
    C = json_response['total']
    D = json_response['positives']
    if D >= 0:
        E = 'Bajo'
    if D >= 3:
        E = 'Medio'
    if D >= 10:
        E = 'Alto'
    time.sleep(30)

    ws['A1'] = 'URL'
    ws['B1'] = 'Fecha de analisis'
    ws['C1'] = 'Total de analisis'
    ws['D1'] = 'Analisis positivos'
    ws['E1'] = 'Clasificacion'
    ws['A' + str(contador)] = A
    ws['B' + str(contador)] = B
    ws['C' + str(contador)] = C
    ws['D' + str(contador)] = D
    ws['E' + str(contador)] = E

    wb.save('reporte_analizador_urls.xlsx')
verificacion(macizo, llavesota)
shutil.move("reporte_analizador_urls.xlsx","Reporte")
#---------------------------------------------------------------
if re.match(valid_correo, args.destino):
    def compresion(ruta_directorio):
        shutil.make_archive("reporte", 'zip', ruta_directorio)

    def enviar_correo(destino):
        origen = "akanthalashay@gmail.com"
        contraseña = "msfqdeahisaammwn"

        zip = open('reporte.zip', 'rb')

        mensaje = MIMEMultipart("alternative")
        mensaje["Subject"] = "Scan report & hashes"
        mensaje["To"] = origen
        mensaje["From"] = destino

        reporte_enviado = MIMEBase('application', 'zip')
        reporte_enviado.set_payload(zip.read())
        encoders.encode_base64(reporte_enviado)
        reporte_enviado.add_header('Content-Disposition', 'attachment', filename = 'reporte.zip')
        mensaje.attach(reporte_enviado)
        mensaje = mensaje.as_string()

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.ehlo()
            server.starttls()
            server.login(origen, contraseña)
            server.sendmail(origen, destino, mensaje)
            server.quit()
    compresion(args.ruta)
    enviar_correo(args.destino)
#