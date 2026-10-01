import nmap
import csv
import argparse         # argument parsing library
import os
import shutil
from openpyxl import Workbook
   

   
# instantiate a PortScanner object
scanner = nmap.PortScanner()

#Crear el directorio
os.mkdir('Reporte')

parser = argparse.ArgumentParser('File System Baseline Creator with PowerShell- Version 1.0 December 2018')
parser.add_argument('-i', '--ipadress', type=str, help='ip address of the host', required=True)
parser.add_argument('-b', '--start',       type = int, required = True, help="Specify the beginning of the range to scan")
parser.add_argument('-e', '--end',       type = int, required = True, help="Specify the end of the range to scan") 
parser.add_argument('-o', '--output',        required=True, help="Specify the output file for the scanning")

args = parser.parse_args()   

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

    print(f'port {i} is {res}.')

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
                print(f'{target} port {i} is "open"')
                respuesta.writerow(f'{target} port {i} is "open"')

    elif args.output == "txt":
        #crear archivo txt
         with open('reporte_puertos.txt', 'a') as f:
                if res == "open":
                    print(f'{target} port {i} is "open"')
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