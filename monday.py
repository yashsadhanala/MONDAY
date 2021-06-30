import time
import pyautogui
import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
import requests
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys
import pyjokes

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening sir....')
        r.pause_threshold = 1
        audio = r.listen(source, timeout=1, phrase_time_limit=5)

    try:
        print('Recognizing....')
        query = r.recognize_google(audio, language="en-in")
        print(f'user said :{query}')
    except Exception as e:
        speak('say that again sir!...')
        return "none"
    return query


def wish():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")
    if hour >= 0 and hour <= 12:
        speak('good morning sir...' + "tt")
    elif hour > 11 and hour < 15:

        speak('good afternoon sir...' + "tt")
    elif hour >= 15 and hour <= 18:
        speak("good evening sir!.." + "tt")
    else:
        speak("have a great evening sir!....")


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('saiyaswanth.sadhanala@gmail.com', 'saiyaswanth')
    server.sendmail('saiyaswanth.sadhanala@gmail.com', to, content)
    server.close()


def news():
    main_url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=3fa10ad5b710455fac3664e5c4e5183f"
    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    head = []
    day = ["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        speak(f"today's {day[i]} news is : {head[i]}")


def screenshot():
    img = pyautogui.screenshot()
    img.save("E:\\Python\\ss.png")


def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at' + usage, 'xx')
    battery = psutil.sensors_battery()
    speak('battery is at', 'xx')
    speak(battery.percent, "xx")

if __name__ == '__main__':
    wish()
    speak("This is MONDAY." + "," + "How can i help you sir")
while True:

    query = takecommand().lower()

    # logic building for tasks  on monday
    if "open notepad" in query:
        npath = "C:\\WINDOWS\\system32\\notepad.exe"
        os.startfile(npath)


    elif "open adobe reader" in query:
        apath = "C:\\Program Files (x86)\\Adobe\\Acrobat Reader DC\\Reader\\AcroRd32.exe"
        os.startfile(apath)


    elif "open command prompt" in query:
        os.system("start cmd")


    elif "open camera" in query:
        cap = cv2.VideoCapture(0)
        while True:
            ret, img = cap.read()
            cv2.imshow('webcm', img)
            k = cv2.waitKey(50)
            if k == 27:
                break;
        cap.release()
        cv2.destroyAllWindows()


    elif "play music" in query:
        music_dir = "E:\\music"
        songs = os.listdir(music_dir)
        rd = random.choice(songs)
        for song in songs:
            if song.endswith('.mp3'):
                os.startfile(os.path.join(music_dir, rd))

    elif "ip address" in query:
        ip = get('https://api.ipify.org').text
        print(ip)
        speak(f"your IP ADDRESS is {ip}")


    elif "wikipedia" in query:
        speak("searching wikipedia...")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        print(results)
        speak('acording to wikipedia')
        speak(results)


    elif "open youtube" in query:
        webbrowser.open("www.youtube.com")


    elif "open facebook" in query:
        webbrowser.open("www.facebook.com")


    elif "open stack overflow" in query:
        webbrowser.open("www.stackoverflow.com")


    elif "open whatsapp" in query:
        webbrowser.open("web.whatsapp.com")


    elif "monday search for" in query:
        speak("sir,what can i search for you")
        cm = takecommand().lower()
        results = webbrowser.open(f"{cm}")
        webbrowser.open(f"{cm}")
        print(results)


    elif "send message" in query:
        kit.sendwhatmsg("+919032231895", "This is a testing protocal....your mobile is gonna crash now", 22,36)
        time.sleep(50)
        speak("message has been sent")


    # yutube video
    elif "play youtube" in query:
        kit.playonyt("telugu songs")


    elif "turn off" in query:
        speak("visit again sir..have a good day!")
        sys.exit()


    elif "close notepad" in query:
        speak("okay sir closing notepad")
        os.system("taskkill /f /im notepad.exe")

    elif "set alarm" in query:

        nn = int(datetime.datetime.now().hour)
        if nn == 22:
            music_dir = "E:\\music"
            rd = random.choice(songs)
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, rd))


    elif "tell me a joke" in query:
        joke = pyjokes.get_joke()
        speak(joke)

    elif "shut down" in query:
        os.system("shutdown /s /t 5")

    elif "restart" in query:
        os.system("shutdown /r /t 5")

    elif "sleep" in query:
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")


    elif "switch the window" in query:
        pyautogui.keyDown("alt")
        pyautogui.press("tab")
        time.sleep(1)
        pyautogui.keyUp("alt")


    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir, the time is {strTime}")


    elif "search news" in query:
        speak("please wait sir , fetching the latest news")
        news()

        # mail
    elif 'send a mail' in query:
        speak("sir,what should i send?")
        query= takecommand().lower()
        if "send a file" in query :
            email = "saiyaswanth.sadhanala@gmail.com"
            password = "saiyaswanth"
            send_to_email= "saiyaswanth.sadhanala@gmail.com"
            speak("okay sir!what is the subject?")
            query = takecommand().lower()
            subject = query
            speak("okay sir!what is the message for this email?")
            query2 = takecommand().lower()
            message = query2
            speak( " sir please! enter the correct path of the file into the shell")
            file_location = input("please enter the path here :")

            speak("please wait sir sending the email...")

            msg = MIMEMultipart()
            msg["From"] = email
            msg["To"] = send_to_email
            msg["subject"]= subject

            msg.attach(MIMEText(message,"plain"))

            filename = os.path.basename(file_location)
            attachment = open(file_location,"rb")
            part = MIMEBase("application","octet-stream")
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header("Content-Disposition","attachment; file name = %s" % filename)

            msg.attach(part)

            server = smtplib.SMTP("smtp.gmail.com",587)
            server.starttls()
            server.login(email,password)
            text = msg.as_string()
            server.sendmail(email,send_to_email,text)
            server.quit()
            speak("email has been sent to him sir")
        else:
            email = "saiyaswanth.sadhanala@gmail.com"
            password = "saiyaswanth"
            send_to_email = "saiyaswanth.sadhanala@gmail.com"
            message = query

            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(email, password)
            server.sendmail(email, send_to_email,message)
            server.quit()
            speak("email has been sent to him sir")


    elif 'remember monday' in query:
        speak("What should I remember ?")
        data = takecommand()
        speak("YOU said me to remember " + data)
        remember = open('data.txt', 'w')
        remember.write(data)
        remember.close()

    elif 'what"s the plan today' in query:
        remember = open('data.txt', 'r')
        x = 'you told me to remember that' + remember.read()
        speak(x)

    elif 'screenshot' in query:
        screenshot()
        speak("Done !")




# else:
        #     print("sir..do you have any other work")
        #     speak("sir..do you have any other work")"""