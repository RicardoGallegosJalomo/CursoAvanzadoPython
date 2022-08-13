import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

# opciones de voz

id1 = 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_ES-MX_SABINA_11.0'
id2 = 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_ES-ES_HELENA_11.0'
id3 = 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_ES-US_ZIRA_11.0'

# Escuchar nuestro microfono y devuelve el audio como texto

def transformar_audio_en_texto():

	# almacenar el reconocedor en una variable

	r = sr.Recognizer()

	# configurar el microfono
	with sr.Microphone() as origen: # se guarda el microfono en origen

		# tiempo de espera

		r.pause_threshold = 0.8 

		# informar que comenzo la grabacion

		print("ya puedes hablar")

		# guardar lo que escuche como audio

		audio = r.listen(origen)

		try:
			# buscar en google lo que haya escuchado

			pedido = r.recognize_google(audio, languaje = "es-mx")

			# prueba de que pudo ingresar

			print("Dijiste: " + pedido)

			# devolver a pedido

			return pedido
			
			# en caso de que no comprenda el audio

		except sr.UnknownValueError:

			# prueba de que no comprendio el audio

			print("ups no entendi")

			# devolver error

			return "sigo esprando"

			# en caso de no resolver el pedido

		except sr.RequestError:

			# prueba de que no comprendio el audio

			print("ups no hay servicio")

			# devolver error

			return "sigo esprando"

			#error inesperado

		except:

			# prueba de que no comprendio el audio

			print("ups algo salio mal")

			# devolver error

			return "sigo esprando"

			#error inesperado


# funcion para que el asistente pueda ser escuchado

def hablar(mensaje):

	# encender el motor de pyttsx3

	engine = pyttsx3.init()
	engine.setProperty('voice',id1)

	#pronunciar mensaje

	engine.say(mensaje)
	engine.runAndWait()

# informar el dia de la semana

def pedir_dia():

	#crear la variable con datos de hoy

	dia = datetime.date.today()

	print(dia)

	#crear una variable para el dia de la semana

	dia_semana = dia.weekday()

	print(dia_semana)

	# diccionario de los nombres de los dias

	calendario = {0:'Lunes',
				  1:'Martes',
				  2:'Miércoles',
				  3:'Jueves',
				  4:'Viernes',
				  5:'Sábado',
				  6:'Domingo'}

	# decir el dia de la semana

	hablar(f'Hoy es {calendario[dia_semana]}')


# informar la hora

def pedir_hora():

	# crear una variable con datos de la hora

	hora = datetime.datetime.now()
	hora = f'En este momento son las {hora.hour} horas con {hora.minute} minutos'
	print(hora)

	# decir la hora

	hablar(hora)


# saludo inicial
def saludo_inicial():

	# crear variable con datos de hora

	hora = datetime.datetime.now()
	if hora.hour < 6 or hora.hour > 20:
		momento = 'Buenas Noches'
	elif hora.hour > 6 and hora.hour < 12:
		momento = 'Buen Día'
	else:
		momento = 'Buenas Tardes'

	#decir el saludo

	hablar(f'{momento}, soy Lupita, su asistente personal. Por favor, digame en que le puedo ayudar Señor')


# funcion central del asistente

def pedir_cosas():

	# activar el saludo inicial

	saludo_inicial()

	# variable de corte
	comenzar = True 

	while comenzar:

		# activar el microfono y guardar el pedido en un string

		pedido = transformar_audio_en_texto().lower()

		if 'abre youtube' in pedido:
			hablar('Con gusto, estoy abriendo youTube')
			webbrowser.open('https://www.youtube.com')
			continue

		elif 'abre  el navegador' in pedido:
			hablar('Habriendo el navegador')
			webbrowser.open('https://www.google.com')
			continue
		elif 'abre github' in pedido:
			hablar('Abriendo Git Hub')
			webbrowser.open('https://www.github.com')
			continue
		elif 'que dia es hoy' in pedido:
			pedir_dia()
			continue
		elif 'que hora es' in pedido:
			pedir_hora()
			continue
		elif 'busca en wikipedia' in pedido:
			hablar('Buscando lo que pediste en wikipedia')
			pedido = pedido.replace('busca en wikipedia','')
			wikipedia.set_lang('es')
			resultado = wikipedia.summary(pedido, sentences=1)
			hablar('Wikipedia dice lo siguiente: ')
			hablar(resultado)
			continue
		elif 'busca en internet' in pedido:
			hablar('Buscando en internet')
			pedido = pedido.replace('busca en internet','')
			pywhatkit.search(pedido)
			hablar('Esto fue lo que encontre')
			continue
		elif 'reproducir' in pedido:
			hablar('Buena idea lo reprodusco')
			pywhatkit.playonyt(pedido)
			continue
		elif 'chiste' in pedido:
			hablar(pyjokes.get_joke('es'))
			continue
		elif 'precio de las acciones' in pedido:
			accion = pedido.split('de')[-1].strip()
			cartera = {'apple':'APPL',
						'amazon':'AMZN',
						'google':'GOOGL'}
			try:
				accion_buscada = cartera[accion]
				accion_buscada = yf.Ticker(accion_buscada)
				precio_actual = accion_buscada.info['regularMarketPrice']
				hablar(f'La encontre, el precio de {accion} es {precio_actual}')
				continue
			except:
				hablar('Perdon no encontre nada')
				continue
		elif 'Adiós' in pedido:
			hablar('Me voy a descansar, cualquier cosa me avisa')
			break

pedir_cosas()