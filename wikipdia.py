import wikipedia
import pyttsx3
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
while True:
 srch = input("enter what you want to search on wikipedia:")
 if srch == "stop":
     print("ending your wikipedia searching...")
     speak("ending your wikipedia searching...")
     break
 else:
   try:
       print("Searching wikipedia...")
       speak("searching wikipedia!")
       result = wikipedia.summary(srch, sentences=2)
       print("According to wikipedia!")
       speak("according to wikipedia!!")
       print(result)
       speak(result)
       print()
       speak("if you want to see full details enter 1")
       a = int(input("if you want to see full details enter 1: "))
       if a == 1:
          url = "https://en.wikipedia.org/wiki/"
          webbrowser.open(url+srch)
          
   except:
       print("Couldn't find on wikipedia searching on google")
       speak("Couldn't find on wikipedia searching on google")
       url = "https://www.google.com/search?client=firefox-b-d&q="
       webbrowser.open(url+srch)