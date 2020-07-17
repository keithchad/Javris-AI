import pyttsx3 # pip install pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os

engine = pyttsx3.init()
def speak(audio):
    engine.say(audio) #Speaks what is in the brackets
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S") 
    speak("the current time is")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("the current date is")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("Welcome Back Sir!")
    time()
    date()
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Goodmorning sir!")
    elif hour >= 12 and hour < 18:
        speak("Goodafternoon sir!")
    elif hour >= 18 and hour < 24:
        speak("Goodevining sir!")
    else :
        speak("Goodnight sir!")

    speak("Jarvis at your service!")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recongnizing...")
        query = r.recognize_google(audio, language='en-in')
        print(query)

    except Exception as e:
        print (e)
        speak("Say that again")

        return"None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls
    server.login('chaddev10@gmail.com', '0718265385')
    server.sendmail('chadev10@gmail.com', to , content)
    server.close()


if __name__ == "__main__":
    wishme()
    while True :
        query = takeCommand().lower()

        if 'time' in query:
            time()
        elif 'date' in query:
            date()
        elif 'wikipedia' in query:
            speak("Searching...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)
        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "joykinya02@gmail.com"
                sendEmail(to, content)
                speak("Email successfully sent!")
            except Exception as e:
                    print(e)
                    speak("Unable to send Email") 
        elif 'search in chrome' in query:
            speak("What should i Search?")
            chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            search = takeCommand().lower
            wb.get(chromepath).open_new_tab(search+'.com')

        elif 'logout' in query:
            os.system("shutdown -1")

        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")

        elif 'restart' in query:
            os.system("shutdown /r /t 1")
            
        elif 'offline' in query:
            quit()

        takeCommand()