import time
import serial
from predecir import *
import os

#Función para tomar foto y guardarla
def foto():
	print("foto")
	os.system('fswebcam -r 840x420 -S 30 --jpeg 95 --save /home/pi/Recon/image.jpg')
	
# mostrar cuando el modelo y peso ya estan cargados y todo esta listo para funcionar 
print("Modelo cargado")
print("Pesos cargado")
print("Reconocimiento listo...")
print(" Todo listo...")

#un pequeño tiempo de descanso por la carga del modelo y peso para que se refresque del proceso  
time.sleep(3)

arduino = serial.Serial('/dev/ttyACM0',9600, timeout=3.0) #se abre la comunicación serial con arduino
time.sleep(2) # otro descanso para que se estabilice 

#bucle que va leer lo que arduino envíe 
while True:
        txt=''
	txt += str(arduino.read(4)) #se lee lo que arduino envia y lo captura en la variable txt 
	
	#hasta que lo recibido sea igual a b'foto' comienza el proceso de tomar la foto y analizarla 
	if txt == "b'foto'":
		foto() #se captura la foto y la guarda
		
		# se le pasa la imagen anteriormente capturada para que sea reconocido lo hay delante
		# y se guarda la respuesta en la variable 'respuesta'
		respuesta = predict('/home/pi/Recon/image.jpg') 
		print(respuesta)
		
		arduino = serial.Serial('/dev/ttyACM0',9600, timeout=3.0) #se abre la comunicación serial
		time.sleep(2)

		# la respuesta va ser el número que más porcentaje
		# que haya tenido despues que la IA haya analizado la foto
		# ------Nota: los números seran del 0 al 11 porque en el dataset se le pusieron 12 etiquetas
		# ------ 12 carpetas con fotos
		
		if respuesta == 0:
			#-- 0 = bolsa
			arduino.write(str.encode('P')) #se le manda una varible al arduino para que posicioné el clasificador
			print('Esto es => Plastico')
			respuesta='' #la variable respuesta de pone en estado inicial vaciando lo que contiene 
		
		elif respuesta == 1:
			#-- 1 = botella
			arduino.write(str.encode('P')) #se le manda una varible al arduino para que posicioné el clasificador
			print('Esto es => Plastico')
			respuesta='' #la variable respuesta de pone en estado inicial vaciando lo que contiene 
			
		elif respuesta == 2:
			#-- 2 = galleta piknic
			arduino.write(str.encode('P')) #se le manda una varible al arduino para que posicioné el clasificador
			print('Esto es => Plastico')
			respuesta='' #la variable respuesta de pone en estado inicial vaciando lo que contiene 
			
		elif respuesta == 3:
			#-- 3 = casacara de guineo
			arduino.write(str.encode('O')) #se le manda una varible al arduino para que posicioné el clasificador
			print('Esto es => Organico')
			respuesta='' #la variable respuesta de pone en estado inicial vaciando lo que contiene 
			
		elif  respuesta == 4:
			#-- 4 = hoja
			arduino.write(str.encode('O')) #se le manda una varible al arduino para que posicioné el clasificador
			print('Esto es => Organico')
			respuesta='' #la variable respuesta de pone en estado inicial vaciando lo que contiene 
		
		elif respuesta == 5:
			#-- 5 = METAL
			arduino.write(str.encode('M')) #se le manda una varible al arduino para que posicioné el clasificador
			print('Esto es => metal')
			respuesta='' #la variable respuesta de pone en estado inicial vaciando lo que contiene 
			
		elif respuesta == 6:
			#-- 6 = Casacara de naranja
			arduino.write(str.encode('O')) #se le manda una varible al arduino para que posicioné el clasificador
			print('Esto es => Organico')
			respuesta='' #la variable respuesta de pone en estado inicial vaciando lo que contiene 
			
		elif respuesta == 7:
			#-- 7 = PAPEL
			arduino.write(str.encode('p')) #se le manda una varible al arduino para que posicioné el clasificador
			print('Esto es => Papel')
			respuesta='' #la variable respuesta de pone en estado inicial vaciando lo que contiene 
			
		elif respuesta == 8:
			#-- 8 = plato
			arduino.write(str.encode('P')) #se le manda una varible al arduino para que posicioné el clasificador
			print('Esto es un => Plastico')
			respuesta='' #la variable respuesta de pone en estado inicial vaciando lo que contiene 
			
		elif respuesta == 9:
			#-- 9 = tenedor desechable
			arduino.write(str.encode('P')) #se le manda una varible al arduino para que posicioné el clasificador
			print('Esto es un => Plastico')
			respuesta='' #la variable respuesta de pone en estado inicial vaciando lo que contiene 
			
		elif respuesta == 10:
			#-- 10 = VACIO
			arduino.write(str.encode('V')) #se le manda una varible al arduino para que posicioné el clasificador
			print('Esto está =>Vacio')
			respuesta='' #la variable respuesta de pone en estado inicial vaciando lo que contiene 
			
		elif respuesta == 11:
			#-- 11 = vaso
			arduino.write(str.encode('P')) #se le manda una varible al arduino para que posicioné el clasificador
			print('Esto es un => Plastico')
			respuesta='' #la variable respuesta de pone en estado inicial vaciando lo que contiene

			#--Nota: luego de haber reconocido y envíado la variable pasará a esperar que lo leído sea igual a b'foto' para comenzar
			# el proceso desde tomar foto. --- Por eso el bucle (while True) 

		
