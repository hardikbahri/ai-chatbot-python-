

import webbrowser
import mysql.connector
import pyttsx3
import wikipedia
from snake1 import *
from gtts import gTTS
import os
from subprocess import Popen
import pygame
from pygame import mixer
import sys
import time
import random
print("ENTER 'code()' to call me")
def code():
    pass1=str(input("Enter mysql password"))
    #entry=str(input("Enter your mysql password"))
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd=pass1)
    cursor=mydb.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS snake ")
    mydb1= mysql.connector.connect(
      host="localhost",
      user="root",
      passwd=pass1,
      database='snake')
    cursor1=mydb1.cursor()
    cursor1.execute("CREATE TABLE IF NOT EXISTS snakegamescores(name VARCHAR(40),score INT)")

    mixer.init()
    mixer.music.load("Wizard - Left the City (Bass Boosted).mp3")
    mixer.music.play()

    pygame.mixer.music.set_volume(0.5)
    engine = pyttsx3.init()
    engine.setProperty('rate','20')

    engine.say('''Enter your desired function
    1) Chat with me
    2)Play a snake game
    3) Surf the web
    4)View game scores ''')

    engine.runAndWait()

    ans = int(input('''Enter your desired function
    1) Chat with me
    2)Play a snake game
    3) Surf the web
    4)View game scores '''))


    if ans==1:
        from nltk.chat.util import Chat, reflections
        import requests
        import time
        pairs = [
            ['my name is (.*)', ['hi %1']],
            ['(hi|hello|hey|holla|halo)(.*)', ['hey there', 'hi there', 'haayyy']],
            ['(how are you|how do you do)(.*)',['I am fine ']],
            ['(.*) in (.*) is fun', ['%1 in %2 is indeed fun']],
            ['(.*)(location|city) ?', ['Delhi, California']],
            ['(.*) created you ?', ['vanshaj did using NLTK']],
            ['how is the weather in (.*)', ['the weather in %1 is amazing like always']],
            ['(.*) help (.*)', ['I can help you']],
            ['(.*) your name ?', ['my name is BABA']],
            ['(.*) (personality|actress) ?',['my %1  is Angelina Jollie']],
            ['tell me more about you',['i am handsome and goodlooking,all you need to know']],
            ['what are your hobbies',[' programming,of course!']],
            ['(.*) like',['i like bananas and money']],
            ['(.*) awesome',['Sure as hell']],
        ]
        print("Hi i am baba,the chatbot,please input in small letters only") 
        chat = Chat(pairs,reflections)
        chat.converse()

    if ans==2:
        snake()
        
    if ans==3:
        engine.say('Press 1 for web search and 2 for looking up data on wikipedia' )
        engine.runAndWait()
        c=int(input('Press 1 for web search and 2 for looking up data on wikipedia' ))
        if c==1:
            webbrowser.open('https://www.google.co.in/')
                            
        if c==2:
            t=str(input('Enter term to be searched for'))
            print(wikipedia.summary(t,sentences=3))

    if ans==4:
        
        cursor1.execute('SELECT * FROM snakegamescores')
        myresult=cursor1.fetchall()

        for x in myresult:
            print(x)
            
                
               
            

                




        
