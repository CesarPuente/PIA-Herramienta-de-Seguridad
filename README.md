# PIA-Herramienta-de-Seguridad
Herramienta de ciberseguridad desarrollada en Python que integra escaneo de puertos con Nmap, generación de hashes para validación de integridad, detección de tecnologías web mediante Wappalyzer y análisis de URLs con VirusTotal. Los resultados son generados en reportes y pueden ser comprimidos y enviados automáticamente por correo electrónico.

 Instrucciones de uso

Requisitos

Para utilizar la herramienta es necesario contar con:

Python 3

Nmap

PowerShell

Las librerías utilizadas por el proyecto:

python-nmap

openpyxl

Wappalyzer

requests

La herramienta funciona principalmente mediante parámetros desde la terminal y permite realizar escaneo de puertos, generación de hashes, detección de tecnologías web, análisis de URLs y generación de reportes.

1. Clonar el repositorio

git clone <URL_DEL_REPOSITORIO>
cd security-tool

2. Instalar las dependencias

pip install python-nmap openpyxl python-Wappalyzer requests

También es necesario tener Nmap instalado en el sistema y disponible desde la terminal.

3. Ejecutar la herramienta

El programa recibe diferentes parámetros:

python importparam.py -i <IP> -s <PUERTO_INICIAL> -e <PUERTO_FINAL> -o <FORMATO> -b <BASELINE> -p <CARPETA> -t <ARCHIVO_TEMPORAL> -hs <Y/N> -d <CORREO> -r <RUTA_REPORTE> -url <URL>

Los principales parámetros disponibles son:

-i → Dirección IP que será analizada.

-s → Puerto inicial del escaneo.

-e → Puerto final del escaneo.

-o → Formato del reporte: txt, csv o xlsx.

-b → Nombre del archivo utilizado para almacenar el baseline.

-p → Ruta de la carpeta utilizada para la generación de hashes.

-t → Archivo temporal utilizado por el script de PowerShell.

-hs → Indica si se ejecutará la generación de hashes.

-d → Dirección de correo electrónico a la que se enviará el reporte.

-r → Ruta de la carpeta que será comprimida para el reporte.

-url → Página web que será analizada.

Ejemplo

python importparam.py -i 192.168.1.10 -s 1 -e 500 -o xlsx -b baseline.dat -p C:\Archivos -t hashes.txt -hs Y -d correo@ejemplo.com -r Reporte -url https://example.com

Al finalizar la ejecución, la herramienta genera una carpeta llamada:

Reporte

En ella se almacenan los diferentes resultados del análisis, como:

Puertos abiertos detectados.

Información de integridad mediante hashes.

Tecnologías utilizadas por el sitio web.

Resultado del análisis de URL.

Archivos de Excel, CSV o TXT generados durante el proceso.

La carpeta también puede comprimirse en formato ZIP y enviarse por correo electrónico.

⚠️ Importante

La herramienta fue desarrollada como un proyecto académico y debe utilizarse únicamente sobre equipos, redes y sitios web propios o sobre los cuales se tenga autorización para realizar pruebas de seguridad.

Antes de utilizar o publicar el proyecto se recomienda eliminar cualquier contraseña, API Key, correo o credencial almacenada directamente dentro del código.
