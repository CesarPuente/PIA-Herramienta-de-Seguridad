import smtplib
import shutil
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

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

#Ejemplos de llamado correcto de funciones
#compresion(r'C:\Users\fermi\Desktop\ignore\carpeta')
#enviar_correo("ferminestradav@gmail.com")