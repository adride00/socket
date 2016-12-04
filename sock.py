import socket
import sys
try:
	#crear un AF_INET
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
	print 'Error al crear socket. Error code: ' + str(msg[0]) + ', Mensaje de error: ' + msg[1]
	sys.exit()
print 'Socket creado con exito'	
	
host = 'www.laprensagrafica.com'
puerto=8080
try:
	ip_remota = socket.gethostbyname( host )

except socket.gaierror:
	#no puede resolver el host
	print 'No se puede resolver el host ' +host 	
	sys.exit()

print 'direccion ip de ' + host + ' es ' + ip_remota 

#Conectar con el server
s.connect((ip_remota , puerto))
print 'Socket conectado a ' + host + ' en ip ' + ip_remota

#enviando algun dato al servidor remoto
msg = "GET / HTTP/1.1\r\n\r\n"

try:
	#envio del mensaje
	s.sendall(msg)
except socket.error:
	#el envio fallo
	print 'envio fallo'
	sys.exit()
	
print 'mensaje enviado correctamente'	

#Recibiendo datos desde el server con recv
respuesta = s.recv(4096567)

print respuesta
s.close() #cerramos el socket para que deje de enviar o escuchar	
