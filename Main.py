import pyttsx3
import pywhatkit
import speech_recognition as sr
from datetime import date
from datetime import datetime
import wikipedia
import psutil



bot = pyttsx3.init()
bot.setProperty('rate', 160)  

def battery():
    

# function returning time in hh:mm:ss
    def convertTime(seconds):
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        return "%d:%02d:%02d" % (hours, minutes, seconds)
  
# returns a tuple
    battery = psutil.sensors_battery()
  
    bot.say("Battery percentage : "+ str(battery.percent))
    bot.say("Power plugged in : "+ str(battery.power_plugged))

    bot.say("Battery left : "+ convertTime(battery.secsleft))

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak Anything :")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print(text)
    except:
        print("Sorry could not recognize what you said")
        
    if 'hello' in text:
        bot.say("Hello Master Rishabh, How can I help you")
    elif 'date' in text:
        today = date.today()
        d2 = today.strftime("%B %d, %Y")
        bot.say("Today's date is "+ d2 )
    elif "time" in text:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        bot.say("The time is" + current_time)
    elif "play" in text:
        pywhatkit.playonyt(text.replace("play", ''))
    elif "search" in text:
        pywhatkit.search(text.replace("search", ''))
    elif "who is " in text:
        info = wikipedia.summary(text.replace("who is", ""),1)
        bot.say(info)
    elif "battery" in text:
        battery()

    bot.runAndWait()
