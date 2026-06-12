import os
from time import sleep
import pyautogui
import webbrowser
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voices', voices[0].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#to open web
def openweb(query):
    speak("Opening sir.....")
    if ".com" in query or ".in" in query or ".org" in query or  "wikipedia" in query or "openai" in query:
        query = query.replace("open","")
        query = query.replace("jarvis","")
        query = query.replace("launch","")
        query = query.replace(" ","")
        webbrowser.open(f"https://www.{query}.com")
        webbrowser.open(f"http://www.{query}.com")
        webbrowser.open(f"https://www.{query}.in")
        webbrowser.open(f"http://www.{query}.in")
        webbrowser.open(f"https://www.{query}.org")
        webbrowser.open(f"http://www.{query}.org")

#To close any app
def closeappweb(query):
    speak("Closing sir.....")
    if "one tab" in query or "1 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
    elif "two tab" in query or "2 tab " in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        speak("sir, All tabs are closed")
    elif "three tab" in query or "3 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        speak("sir, All tabs are closed")
    elif "four tab" in query or "4 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        speak("sir, All tabs are closed")
    elif "five tab" in query or "5 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        speak("sir, All tabs are closed")
    