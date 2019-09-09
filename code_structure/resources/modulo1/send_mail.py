#! /usr/bin/python
# from flask import Flask, request, json
# from flask_restful import Resource, Api
from flask import Flask, request
from flask_restful import reqparse,Resource, Api
from flask_cors import CORS
import requests
import json
import datetime

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


Token = "Bearer gM0M1tUWtgdam3B5s76iqRLaHOHtRic+vf87bT1gV13KFZj1CSgm3p4xJnYQuCP6Qg8BNvlcRf3dKpG09NpFK59/tJuFbx0g0YBoES+3nv2XdFYKIwWza97J0AtlMKoTReWStenLjphG6d6hTgofeKZdjZ5x7MjrwDIsR8yTHfKyGH52QbipKyJPhrRiFq+LSFRBxGDPOIPgdHaeGfSIGnln3Hu17XgI1DjZ5Qec9bKpEp5VWBMFgSci2YYcKT4cbJcN/gunEi7l8akOvcycsGzMll6UNpEdkVbBeDL8AhZNU6AepeaFuWPVcMuG3qdG3e+mxL9MFoHFBg4F6sYtntqgxCsOiWsF6iiB8z9XiFEle9axjvPSJsAyqNvN6fyER1mjsnt2vYIX0x2Q96tOFkqJ/CZnI/KxtM8mZKh9pZO6AFzEyrC6br6PU3qM9OFjnxD1EBFUQKdZ/7QJOktNMqaoSKsgaeK7QgL7iGNIOj2nag5ZFo8OTz81En5JaJ7eaQopBK6FKJtW/PTamAoMruQeT2IgF4DOzpEVcgBYYNZvIHN/7QT0lh07G+4Tt+wsYyyWVriPqGpRawskL6KKfOhNrHySKB1k/9RB4BoUL2LLEFPi/FLp6FRWyTCOgcL6mrvID2Ox3EDwBZ4nwPfwMjX7Kzn76vUcBdWyPB6+pv1kP8TfPKyP/dxbQsE+ct0j9LhmLAve2vz3m5K8FTaAaAVghUfWQr4sbdXwcd8hIHg/KZinqltwtjeP+DA1VE5LGvMmC/kZ6sAB63MJlR18VnTdVmGq/sSK0j+1fDLFLWw29uxcN4zN/BTZsUirFDpAhQ4a94ILbI9RVL0ApFzsrVe+1W4/yICG4RPOI/d1fnh2cTubvp2Wa49KN1YjCQK1GzaADVF+8aigQnBbMWE/aLvcOWjsFMzq38rx"
Type = "application/json"
x = datetime.datetime.now()



emisor = "ersanchez@palaceresorts.com"
receptor = "ixicale@palaceresorts.com"
# Create message container - the correct MIME type is multipart/alternative.
    # Crear contenedor de mensajes: el tipo MIME correcto es multiparte / alternativo.
mensage = MIMEMultipart('alternative')
mensage['Subject'] = "mensaje asunto" # Mensaje de asunto
mensage['From'] = emisor    # EMISOR
mensage['To'] = receptor     # RECEPTOR

# Create the body of the message (a plain-text and an HTML version).
#Texto externo para envio del cuerpo del mensaje
text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
#HTML externo para envio del cuerpo del mensaje
html = """\
<html>
  <head></head>
  <body>
    <p>Hi Erick!<br>
       Hello World<br>
       <p>soy un nivel superior a lo esperado</p>
    </p>
  </body>
</html>
"""

# Record the MIME types of both parts - text/plain and text/html.
    # Graba los tipos MIME de ambas partes.
part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

# Attach parts into message container. 
    # Coloque las piezas en el contenedor de mensajes.
# According to RFC 2046, the last part of a multipart message, in this case
    # Según RFC 2046, la última parte de un mensaje multiparte, en este caso
# the HTML message, is best and preferred.
    # El mensaje HTML, es mejor y preferido.
mensage.attach(part1)
mensage.attach(part2)

# Send the message via local SMTP server.
s = smtplib.SMTP('localhost') # LOCAL POR MIENTRAS
# sendmail function takes 3 arguments: sender's address, recipient's address
    # sendmail toma 3 argumentos: dirección del remitente, dirección del destinatario
# and message to send - here it is sent as one string.
    # y mensaje para enviar - aquí se envía como una cadena.
s.sendmail(emisor, receptor, mensage.as_string())
s.quit()

@app.route('/codigo/api/palaceaRuX/lwQmyIjdVFW0/UEHUoYKXMZoIHRoZSBVUkwgUEHUoYKXMZ3MyYW1ldHJvcyBwY0JQDvcnF+Y2UubmV3KHRpdGxlLXJhIGNyZWFyIHJlZ2lzdHGFyhxpiiEYQ6uZ3NdfZ0JQDvcnF+Y2UubmVb2YgdGhlIGBSByZXBsYWNlZCB3aXRoIHRoZSBVUkwgb2YgdGhlBkdXJpbmc=SZCB3aXRoIHRwdWJsaWNgIGZvbGRlciBkdXJpbmc/<post_str>', methods=['POST'])
def post_notificaciones(post_str):
    url = 'http://dev.clever-api-frm.local/notificaciones/notificacion/'+post_str
    values = request.get_json()
    print(url)
    headers = { 'Content-Type': Type, 'Authorization': Token }
    #return(json.dumps(values))
    return (requests.post(url, data=json.dumps(values), headers=headers).text)


if __name__ == '__main__':
    app.run(debug = True)

# """ if __name__ == '__main__':
#     app.run(debug=True) """