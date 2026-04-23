# N.O.V.A. – Neural Optimized Virtual Assistant
import pyttsx3
import datetime
from time import sleep
import speech_recognition as sr
import os
import cv2
import random
from requests import get
import requests
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib 
import sys
import time
import pyjokes
import instaloader
import pyautogui
import PyPDF2
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voices', voices[0].id)


#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()
 
#to convert voice into text
def takecommand():
#it takes microphone input from input and returns strring output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said:{query}")

    except Exception as e:
        #print(e)
        print("Say that again please...")
        return "None"
    query = query.lower()
    return query

#to wish
def wishme():
    hour = int(datetime.datetime.now().hour)
    pt = time.strftime("%I:%M %p")
    if hour>=0 and hour<12:
        speak(f"Good morning sir!, its {pt}")

    elif hour>=12 and hour<18:
        speak(f"Good Afternoon sir!, its {pt}")

    else:
        speak(f"Good evening sir!, its {pt}")
    speak("I am NOVA , How can I help you?")

#to send email
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('prathameshhatkar07@gmail.com','ikdt vtzo xxxj kcvj')
    server.sendmail('prathameshhatkar07@gmail.com',to,content)
    server.close()

def pdf_reader():
    pdf = open('Resume.pdf','rb')
    pdfreader = PyPDF2.PdfFileReader(pdf)
    pages = pdfreader.numPages
    speak(f"Total numbers of pages in this pdf are {pages}")
    speak("sir please enter the number of page i have to read.")
    pg = int(input("Please enter the page number: "))
    page = pdfreader.getPage(pg)
    text = page.extractText()
    speak(text)

#start function
def start():
    wishme()
    
    while True:
     #if 1:

        query = takecommand()

#logic building for task
#----------To perform specific tasks----------#
        
        if "open notepad" in query:
            npath = "C:\\Windows\\notepad.exe"
            os.startfile(npath)
            speak("Done sir.")

        elif "close notepad" in query:
            speak("Okay sir, closing notepad")
            os.system("taskkill /f /im notepad.exe")
            speak("Done sir.")
            
        elif "open microsoft word" in query:
            speak("sure sir")
            wpath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.exe"
            os.startfile(wpath)
            speak("Done sir.")

        elif "close microsoft word" in query:
            speak("Okay sir, closing word")
            os.system("taskkill /f /im WINWORD.exe")
            speak("Done sir.")

        elif "open powerpoint" in query:
            speak("sure sir")
            wpath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
            os.startfile(wpath)
            speak("Done sir.")

        elif "close powerpoint" in query:
            speak("Okay sir, closing powerpoint")
            os.system("taskkill /f /im POWERPNT.EXE")
            speak("Done sir.")

        elif "open excel " in query:
            speak("sure sir, opening excel")
            wpath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
            os.startfile(wpath)
            speak("Done sir.")

        elif "close excel" in query:
            speak("Okay sir, closing excel")
            os.system("taskkill /f /im EXCELS.EXE")
            speak("Done sir.")

        elif "take screenshot " in query or "take a screenshot" in query:
            speak("sir,please tell me the name for this screenshot file.")
            name = takecommand().lower()
            speak("please sir hold the screenfor few seconds, i am taking screenshot")
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("i am done sir, the screenshot has been saved in our main folder.")

        #elif "set alarm" in query:
            #nn = int(datetime.datetime.now().hour)
            #if nn==2:
                #music_dir = 'D:\\music'
                #songs = os.listdir(music_dir)
            #os.startfile(os.path.join(music_dir, songs[0]))
            
        elif "open command prompt" in query:
            os.system('start cmd')
            speak("Done sir.")

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam',img)
                k = cv2.waitKey(50)
                if k==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()
            speak("Done sir.")

        elif "close camera" in query:
            pyautogui.press("Esc")
            time.sleep(1)
            speak("Done sir.")

        elif "play music" in query:
            music_dir = "D:\\music"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))
            speak("Done sir.")

        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)

        #elif "close music" in query:
            #speak("Okay sir, closing music")
            #os.system("taskkill /f /im music")

        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your IP address is {ip}")

        elif "wikipedia" in query:
            speak("Searching wikipedia....")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)
            #print(results)
#----------To check socialmedia----------#
        
        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")
            speak("Done sir.")

        elif "open youtube" in query:
            speak("Sir what would you like to see?")
            yt = takecommand().lower()
            kit.playonyt(f"{yt}")
            speak("Done sir.")

        elif "check instagram profile" in query or "check profile on instagram" in query:
            speak("sir please enter the user name correctly.")
            name = input("Enter username here :")
            webbrowser.open(f"www.instagram.com/{name}")
            speak("Sir here is the user profile of the user {name}")
            time.sleep(5)
            speak("Sir would you like to download profile picture of this account.")
            condition = takecommand().lower()
            if "yes" in condition:
                mod = instaloader.Instaloader() 
                mod.download_profile(name, profile_pic_only=True)
                speak("i am done sir, profile picture is saved in our main folder.")
            else:
                pass

        elif "open stackoverflow" in query:
            webbrowser.open("www.stackoverflow.com")
            speak("Done sir.")

        elif "open google" in query:
            speak("Sir, what would you like to search?")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")
            speak("Done sir.")

        elif "open chrome" in query:
            speak("opening sir")
            apath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(apath)
            speak("Done sir.")
        
        elif "close chrome" in query:
            speak("Okay sir, closing chrome")
            os.system("taskkill /f /im chrome.exe")
            speak("Done sir.")

        elif "send whatsapp message" in query:
            kit.sendwhatmsg("+917666769323","this is testing protocol",4,13)
            time.sleep(120)
            speak("message has been sent")

        elif "switch the window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

        elif "send email" in query:
            try:
                speak("What should I say?")
                content = takecommand().lower()
                to = "patu87422@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent to Prathamesh Succesfully.")
            
            except Exception as e:
                print(e)
                speak("Sorry sir I am not able to send this email.")

        elif "read PDF " in query or "read the pdf" in query:
            pdf_reader()

        elif "open" in query:
            from Dictapp import openweb
            openweb(query)

        elif "close" in query:
            from Dictapp import closeappweb
            closeappweb(query)

#----------pause,play,mute----------#
        elif "pause" in query or "pause video" in query or "pause the video" in query:
            pyautogui.press("k")
            speak("video paused sir")
        elif "play" in query or "play video" in query or "play the video" in query:
            pyautogui.press("k")
            speak("video played sir")
        elif "mute" in query or "mute the video" in query:
            pyautogui.press("m")
            speak("video muted sir")
        elif "unmute" in query or "unmute the video" in query:
            pyautogui.press("m")
            speak("video muted sir")

#----------volume up-down----------#
        elif "volume up" in query:
            from keyboard import volumeup
            speak("Turning volume up sir...")
            volumeup()
        elif "volume down" in query:
            from keyboard import volumedown
            speak("Turning volume down sir...")
            volumedown()

#----------Shutdown,restart or sleepmode----------#

        elif "shutdown the system" in query or "shutdown the machine" in query:
            speak("Okay sir...see you again")
            os.system("shutdown /s /t 5")

        elif "restart the system" in query:
            speak("Sure sir...")
            os.system("shutdown /r /t 5")

        elif "sleep the system" in query:
            speak("Sure sir...")
            os.system("rundll32.exe poweroff.dll,SetSuspenfState 0,1,0")

#----------Greetings----------#

        elif "hello NOVA" in query or "Heyy NOVA" in query:
            speak("Hello sir, Welcome back!")

        elif "how are you" in query or "how r u" in query:
            speak("I'm fine sir, Thanks for asking me, what about you?")

        elif "I am fine" in query or "I m also fine" in query or "I am also fine" in query:
            speak("Sounds great sir.")     

        elif "no thanks" in  query:
            speak("Thanks for using me sir , have a good day.")
            break
        
        elif "thanks" in query or "thank you" in query or "aabhari aahe" in query:
            speak("Its my pleasure sir...")

        elif "you may go now" in  query:
            speak("Thanks for using me sir , have a good day.")
            break

        elif "bye" in query or "by" in query:
            speak("Bye sir, have a great time.")
            break
        
        elif "good night" in query:
            speak("Goodnight sir, have a sweet dreams...")
            sys.exit()
        
#---------To find my location using IP address-----------#
        elif "where are we" in query or "where i am" in query or "where am i" in query:
            speak("wait sir , let me check...")
            try:
                ipAdd = requests.get('https://api.ipify.org').text
                print(ipAdd)
                url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                #print geodata
                city = geo_data['city']
                country = geo_data['country']
                speak(f"sir i am not sure, but i think we are in {city} city of {country} country")
            except Exception as e:
                speak("sorry sir due to network issue i am not able to find where we are.")
                pass
                
#----------To hide files----------#
        elif "hide all files" in query or "hide the folder" in query or "visible for everyone" in query:
            speak("Sir, do you want to hide this folder or make it visible for everyone")
            condition = takecommand().lower()
            if "hide" in condition:
                os.system("attrib +h /s /d")
                speak("Sir, all the files in this folder are hidden now.")

            elif "visible" in condition:
                os.system("attrib -h /s /d")
                speak("Sir, all files from this folder are now visible for everyone. I wish you are taking this decision on your own peace.")
            
            elif "leave it for now" in query or "leave it" in query:
                speak("Okay sir..")
# ----------To open apps from pc ----------#
            # elif "open" in query:
            #     from Dictapp import openweb
            #     openweb(query)
            #     speak("Done sir.")
            
            # elif "close" in query:
            #     from Dictapp import closeappweb
            #     closeappweb(query)
            #     speak("Done sir.")
        #speak("Sir , do you have any other work?")
            
#main function
# if __name__ == '__main__':
start()
#     while True:
#         permission = takecommand()
#         if "wake up" in permission:
#             start()
#         elif "goodbye" in permission or "good bye" in permission or "Good bye" in permission:
#             speak("goodbye sir")
#             sys.exit()
