from nltk.chat.util import Chat, reflections
import requests
import time
from datetime import datetime
pairs = [
    ['my name is (.*)', ['hi %1']],
    ['(hi|hello|hey|holla|halo)', ['hey there', 'hi there', 'haayyy']],
    ['(.*) in (.*) is fun', ['%1 in %2 is indeed fun']],
    ['(.*)(location|city) ?', ['Delhi, California']],
    ['(.*) created you ?', ['vanshaj did using NLTK']],
    ['how is the weather in (.*)', ['the weather in %1 is amazing like always']],
    ['(.*) help (.*)', ['I can help you']],
    ['(.*) your name ?', ['my name is BABA']],
    ['(.*) (personality|actress) ?',['%1 is sunny leone']],
    ['tell me more aabout you',['i am handsome and goodlooking,all you need to know']]
]
print("Hi i am baba,the chatbot,please input in small letters only") 
chat = Chat(pairs,reflections)
chat.converse()

