import socket
import sys
import thread
HOST = '' #escucha por todas las interfaces
PORT = 8888 #Uasamos un puerto de numeracion alta para no interderir

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket Creado'

try:
	s.bind((HOST, PORT))
except socket.error , msg:
	print 'Error al crear socket. Error code: ' + str(msg[0]) + ' , Mensaje de error: ' + msg[1]
	sys.exit()

print 'Enlace via socket activo'		

s.listen(5) # encolara un maximo de 5 conexiones
print 'socket escucjando en puerto '+str(PORT)

while True:
	#espera y acepta las conexiones
	conn, addr = s.accept()

	#muestra informacion del cliente
	print 'Conectado con ' + addr[0] + ':' + str(addr[1])

	data = conn.recv(1024)
	print data
	respuesta = 'OK...holaaaa' + data
	if not data:
		break
	conn.sendall(respuesta)
conn.close()
s.close()

def hilo_cliente(conn):
	#enviar un mensaje al cliente cuando se conecte
	conn.send('bienvenidos al server escriba algo y presione enter') 
	#ciclo infinito de escuchas
	while True:
		data = conn.recv(1024)
		respuesta = 'Ok...' + data
		if not data:
			break
		elif data=='q':
			print 'recibi '+ data + ' tome una accion '
		
		conn.sendall(respuesta)
	#cerrar conexion	
	conn.close()		
while 1:
	#espera para acetar conexiones
	conn, adr = s.accept()
	print 'conectado con ' + addr[0] + ':' + str(addr[1])
	
	#inicia un nuevo hilo el cual recive dos parametros el hilo y la conexion
	start_new_thread(hilo_cliente ,(conn,))
s.close()		
	

		
