import smtplib
import socket
socket.getaddrinfo('127.0.0.1', 8080)
# from smtplib import SMTP
conn = smtplib.SMTP('smtb.gmail.com',587)
conn.starttls()
conn.login('lotus.training.center.blr@gmail.com', 'Lotus@369')

conn.sendmail('sachinkv14@gmail.com','sachinkv369@gmail.com','Subject: What you like? \n\n Reply Reply Reply')
conn.quit()