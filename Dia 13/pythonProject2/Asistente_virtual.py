import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

#escuchar nuestro audio y devolver el audio como texto
def transformar_audio_en_texto():

    #Almacena recognizer en variable
    r = sr.Recognizer()
    #Configurar el microfono
    with sr.Microphone() as origen:

        # tiempo de espera
        r.pause_threshold = 0.8

        # informar que comenzo grabacion
        print('ya pudes hablar')

        # Guardar lo que escuche como audio
        audio = r.listen(origen)

        try:
            #Buscar en google lo pedido
            pedido = r.recognize_google(audio, language='es-CO')

            #prueba de que no pudo ingresar
            print('Dijiste:' + pedido)

            #devolver pedido
            return pedido

        #En caso de que no comprenda el audio
        except sr.UnknownValueError:

            # prueba de que no comproneda el audio
            print('No te entendi')

            #Devolver error
            return ('sigo esperando')
        #en caso de no devolver el pedido
        except sr.RequestError:
            # prueba de que no comproneda el audio
            print('No hay servicio')

            # Devolver error
            return ('sigo esperando')
        #error inesperado
        except :
            # prueba de que no comproneda el audio
            print('Algo anda mal')

            # Devolver error
            return ('sigo esperando')

transformar_audio_en_texto()