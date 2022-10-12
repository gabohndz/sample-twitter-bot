# Primeramente para que el bot funcione se debe instalar Python en la consola
#Algunos servicios ofrecen instalarlo automáticamente, instalan Python Primero
#Segundamente deben instalar las librerias que van a utilizar en el servidor
# Se hace en la consola Bash donde se alojará el bot y se escribe lo siguiente:
# pip install tweepy       /o/       pip install git+https://github.com/tweepy/tweepy.git
# pip install schedule         / (Esto es para programar trabajos)
import tweepy   #(La base principal de bots de twitter en python)
import time    #(Para programar tiempos y poner pausas)
import random   #(Por si necesitas elegir algo de forma random)
import schedule  #(Para programar tareas cada cierto tiempo)

#Antes de comenzar, también debes pedir estas apis en el portal de developer de Twittter

ACCESS_KEY = 'Tu llave de acceso'
ACCESS_SECRET = 'Tu clave secreta de acceso'
CONSUMER_KEY = 'Tu llave de cliente'
CONSUMER_SECRET = 'Tu clave secreta de cliente'

#Esta es mi propia forma de usar el bot: "client" para buscar tweets y "client1" para hacer acciones

client = tweepy.Client("Tu Barrear Token")
client1 = tweepy.Client(
    consumer_key=CONSUMER_KEY,
    consumer_secret=CONSUMER_SECRET,
    access_token=ACCESS_KEY,
    access_token_secret=ACCESS_SECRET
)

#Este es el código que uso para buscar el id de las cuentas, debes colocar entre comillas el usuario
def buscaruser():
    users = client.get_users(usernames=['GaboLatam'])
    for user in users:
    	print(user)

user_id = 'Tu Id por si lo necesitas'
user_id_cuenta = 'Id de la cuenta que vas a reaccionar'

# Definimos la función de reacción a la cuenta
def tweets_cuenta():
    #Lo primero siempre es buscar los tweets sobre los que vas a trabajar
    #con la linea de abajo obtienes los ultimos 5 tweets de la cuenta que reaccionaras
    tweets = client.get_users_tweets(id=user_id_cuenta,max_results=5)
    #Básicamente para cada tweet que consiga, vamos a buscar si tiene la palabra clave
    #Luego vamos a darle like y Retweet a cada tweet o retweet que cumpla con la especificacion	
    for tweet in tweets.data:
        if '#NFTGiveaway' in tweet.text:
            print('Likeable') #(Para saber si hará la accion o no)
            client1.like(tweet.id) #(Para dar like al tweet)
            client1.retweet(tweet.id) #(Para retweetear el tweet)
            
#Definimos los procesos que va a correr
def main():

    #Cada 600 segundos/10minutos va a correr la función que definimos antes
    schedule.every(600).seconds.do(tweets_cuenta)

    #Aqui definimos el lop infinito para que siempre este haciendo la tarea
    while True:
            try:
                schedule.run_pending()
                time.sleep(2)
            except tweepy.TweepError as e:
                raise e

#Con esto evitamos errores por si importan el código, es una costumbre en Python
if __name__ == "__main__":
    main()         
