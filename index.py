import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
from os import startfile
from pyautogui import click
from keyboard import press
from keyboard import write
from time import sleep
from playsound import playsound
import pywhatkit
from datetime import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# def WhatsAppMsg(name,message):
#     startfile("C:\\Users\\USER\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
#     sleep(7)
#     click(x=239, y=142)
#     sleep(1)
#     write(name)
#     sleep(1)
#     click(x=205, y=295)
#     sleep(1)
#     click(x=634, y=615)
#     sleep(1)
#     write(message)
#     press('enter')

def wishMe():
    hour = int(datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jarvis. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

# def sendEmail(to, content):
#     server = smtplib.SMTP('deepabait26577.gmail.com', 587)
#     server.ehlo()
#     server.starttls()
#     server.login('deepabait26577@gmail.com', 'your-password')
#     server.sendmail('deepabait@gmail.com', to, content)
#     server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")  

        elif 'open google' in query:
            webbrowser.open("google.com")


        elif 'play music' in query:
            playsound("C:\\Users\\USER\\Music\\Post_Malone_-_ft_Ty_Dolla_ign_-_Psycho_Luvmp.com_.mp3")
            # if('stop'):
            #     quit()

        elif 'the time' in query:
            strTime = datetime.now().strftime("%H:%M:%S")    
            print("time",strTime)
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\USER\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'system information' in query:
            webbrowser.open("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Administrative Tools\\System Information.lnk")
        elif 'emergency' in query:
            speak("confirming standard operating protocol ")
            query=takeCommand().lower()
            if 'confirmed' in query:
             speak("Sending Message To Mom")
            #  WhatsAppMsg('Mom','emergency')
             now =datetime.now()
             curr_time_hr=now.strftime("%H")
             curr_time_min=now.strftime("%M")
             pywhatkit.sendwhatmsg("+918425880069","Heyy",int(curr_time_hr),int(curr_time_min)+1)
             quit()
            else:
                speak("Whom should i send message to")
                query=takeCommand().lower()
                
           
       
        elif 'quit' in query:
            speak("Going offline in 3.... 2... 1... ")
            exit()

        # elif 'email to mum' in query:
        #     try:
        #         speak("What should I say?")
        #         content = takeCommand()
        #         to = "deepabait26577@gmail.com"    
        #         sendEmail(to, content)
        #         speak("Email has been sent!")
        #     except Exception as e:
        #         print(e)
        #         speak("Sorry I am not able to send this email")    

