//this is an new python library
import pyttsx3
import pyautogui
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am Zukaari Sir ,Please tell me how may i help you") 
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold=1
        audio = r.listen(source)
    try:
        print("REcognising")
        query = r.recognize_google(audio,language=='en-in')
        print(f"user said:{query}\n")
    except Exception as e:
        print("Say that gagin please...")
        return "None"
def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('your gmail','your password')
    server.sendmail('your mail',to,content)
    server.close()
def takescreenshoot():
    img = pyautogui.screenshot()
    img.save(f"E:\\webpage programmming\\screenshot{random.randint(0,4854658)}.png")
    speak('screenshot taken and saved to decribed location') 
    
if __name__=='__main__':
    wishMe()
    while True:
        query=takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace('wikipedia','')
            results=wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube ' in query:
            webbrowser.open("youtube.com")
        elif 'open google ' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow ' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            music_dir='.....music directory'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir the time is{strTime}")
        elif 'take screenshot' in query:
            takescreenshoot() 
        elif 'quit buddy' in query:
            speak('quitting myself')
            exit()
        elif 'email to pranesh' in query:
            try:
                speak("what should i say?")
                content=takeCommand()
                to="email to whom yur are sending"
                sendEmail(to,content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("soory my friend pranesh, ia m not able to sent email")





