import speech_recognition as sr     
import pyttsx3                       
import time                          
from selenium import webdriver       
import pyautogui                     
import google.generativeai as genai  
from googletrans import Translator, LANGUAGES
import os                            
import datetime

r= sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('rate',150)
genai.configure(api_key='YOUR API')
model = genai.GenerativeModel('models/gemini-pro')

def dinle():
    with sr.Microphone() as source:   
        r.adjust_for_ambient_noise(source)
        ses = r.listen(source)
        global sonuc
        sonuc = r.recognize_google(ses,language = "eng-US")
        print(f"Siz: {sonuc}")

def cevapla(cevap):
    engine.say(cevap)
    engine.runAndWait()

chat = model.start_chat()

while True:      
    try:       
        dinle()       

        response = chat.send_message(sonuc)         
  
        print(f"CEVAP: {response.text}")   

        cevapla(response.text)    

    except sr.UnknownValueError as hata:
        print("while sonu hata ",hata)
    except Exception as hata2:
        print("while sonu hata ",hata2)
        continue
