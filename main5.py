# -*- coding: utf-8 -*-
import sys
import time
import tkinter
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
from tkinter import filedialog
import psutil
import requests
from AiUi import Ui_MainWindow
from PyQt5 import QtGui , QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QTimer , QTime , QDate
from PyQt5.QtWidgets import QApplication
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import speech_recognition as sr
import datetime
import pyttsx3
import os
import sys
import datetime
import webbrowser
import urllib.parse
import urllib.request
import re
import urllib
import wikipedia
import requests
import pyttsx3
import subprocess as sp
import pyjokes
#import logging
import keyboard
import openai
import tkinter as tk
from tkinter import filedialog
import requests
import wikipedia

# API key for OpenWeatherMap
# API key for OpenWeatherMap
weather_api_key = os.getenv("WEATHER_API_KEY")
# API key for OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")
# API key for News
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
# API key for latest movies
TMDB_API_KEY = os.getenv("TMDB_API_KEY")

conversation = ""
user_name = ""
bot_name=""

# Initialize pyttsx3
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():  # sourcery skip: remove-unnecessary-cast
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   
    else:
        speak("Good Evening!")  
    #speak("I am your assistant. Please tell me how may I help you")

def takeCommand():
    # It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    r.energy_threshold = 144  # set energy threshold to 144 dB
    while True:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=0.5)  # reduce ambient noise
            r.pause_threshold = 0.3  # set pause threshold
            r.non_speaking_duration = 0.2  # set non-speaking duration
            print("Speak now...")
            try:
                audio = r.listen(source, timeout=5)  # set a timeout for listening
                print("Recognizing...")
                query = r.recognize_google(audio)
                print(f"User said: {query}\n")
                return query.lower()
            except sr.WaitTimeoutError:
                print("Timeout occurred, try again...")
            except sr.UnknownValueError:
                print("Could not understand audio, try again...")


def jarvis(query):
    global conversation
    if "who made you" in query.lower() or "created you" in query.lower():
        speak("I have been created by gpg students")

    elif "who are you" in query.lower():
        speak("I am your assistant. Please tell me how may I help you")

    elif "how are you" in query.lower():
        speak("I am Fine Sir! How can I help you today?")
    
    elif 'open youtube' in query.lower():
        speak('sure')
        webbrowser.open("youtube.com")

    elif 'open camera' in query.lower():
        sp.run('start microsoft.windows.camera:', shell=True)

    elif 'open cmd' in query.lower() or 'open Command Prompt' in query.lower():
        os.system('start cmd')

    elif 'open google' in query.lower():
        speak('sure')
        webbrowser.open("google.com")

    elif 'open stack overflow' in query.lower():
        speak('sure')
        webbrowser.open("stackoverflow.com") 

    elif 'open netflix' in query.lower():
        speak('sure')
        webbrowser.open("netflix.com/in/")

    elif 'open flipkart' in query.lower():
        speak('sure')
        webbrowser.open("flipkart.com")

    elif 'open amazon' in query.lower():
        speak('sure')
        webbrowser.open("amazon.com")

    elif 'open zomato' in query.lower():
        speak('sure')
        webbrowser.open("zomato.com/india")  

    elif 'open swiggy' in query.lower():
        speak('sure')
        webbrowser.open("www.swiggy.com")    

    elif 'open gmail' in query.lower() or 'open email' in query.lower():
        speak('sure')
        webbrowser.open("gmail.com") 

    elif'watch movie' in query.lower():
        webbrowser.open("cineb.net")    
        speak("here you go, you must have VPN connected")

    elif'watch anime' in query.lower():
        webbrowser.open("9anime.vc/home")
        speak("here you go")

    elif 'stocks' in query.lower() or 'tradingview' in query.lower():
        speak("i am opening treadingview for you   ")
        webbrowser.open("www.tradingview.com/")  

    elif 'send email' in query.lower():
        try:
            speak("What should I say?")
            content = takeCommand()
            to = "tanmaypamar18@gmail.com"    
            sendEmail(to, content)
            speak("Email has been sent!")   
        except Exception as e:
            print(e)
            speak("work not done ")  

    elif 'open whatsapp' in query.lower():
        speak('Sure')
        try:
            open_whatsapp()
        except:
            # if WhatsApp application not found, open WhatsApp web in default browser
            webbrowser.open("https://web.whatsapp.com/")
        while True:
            query = takeCommand().lower()
            if 'close it' in query.lower() or 'close whatsapp'  in query.lower():
                keyboard.press_and_release('ctrl+w')
            break

    elif 'open twitter' in query.lower():
        speak('sure')
        webbrowser.open("twitter.com")  
        while True:
            query = takeCommand().lower()
            if 'close it' in query.lower() or 'close twitter'  in query.lower():
                keyboard.press_and_release('ctrl+w')
            break 

    elif 'open facebook' in query.lower():
        speak('sure')
        webbrowser.open("facebook.com") 
        while True:
            query = takeCommand().lower()
            if 'close it' in query.lower() or 'close Facebook'  in query.lower():
                keyboard.press_and_release('ctrl+w')
            break

    elif 'open linkedin' in query.lower():
        speak('sure')
        webbrowser.open("linkedin.com") 
        while True:
            query = takeCommand().lower()
            if 'close it' in query.lower() or 'close linkedin'  in query.lower():
                keyboard.press_and_release('ctrl+w')
            break  

    elif 'open instagram' in query.lower():
        speak('Sure')
        webbrowser.open("instagram.com")
        while True:
            query = takeCommand().lower()
            if 'close it' in query.lower() or 'close Instagram'  in query.lower():
                keyboard.press_and_release('ctrl+w')
            break

    elif 'open google maps' in query.lower():
        webbrowser.open("https://www.google.com/maps")    

    elif 'open github' in query.lower():
        speak('sure')
        webbrowser.open("github.com")  

    elif 'open medium' in query.lower():
        speak('sure')
        webbrowser.open("medium.com")  

    elif 'open website' in query.lower():
        speak('sure')
        webbrowser.open("google.com")  

    elif 'open my website' in query.lower():
        speak('sure')
        webbrowser.open("google.com")  

    elif 'open my blog' in query.lower():
        speak('sure')
        webbrowser.open("google.com")  

    elif 'tell me joke' in query.lower():
        speak(pyjokes.get_joke())
    
    elif 'open notepad' in query.lower():
        speak('sure')
        notepad()
        while True:
            query = takeCommand().lower()
            if 'close it' in query.lower() or 'close Notepad'  in query.lower():
                keyboard.press_and_release('ctrl+w')
            break

    # elif 'add task' in query.lower() or 'tasks' in query.lower() or 'task' in query.lower():
    #     add_task()

    # elif 'add notes' in query.lower() or 'notes' in query.lower() or 'note' in query.lower():
    #     add_notes()

    # elif 'set reminder' in query.lower():
    #     set_reminder()

    elif 'what is time' in query.lower():
        strTime = datetime.datetime.now().strftime("%H:%M:%S")    
        speak(f"Sir, the time is {strTime}")

    elif 'latest news' in query.lower() or 'trending news' in query.lower() or 'current news' in query.lower() or 'current affairs' in query.lower():
            headlines = get_latest_news()
            for headline in headlines:
                print(headline)
                speak(headline)
            speak('This are the few headlines of Latest News')

    elif 'latest movies' in query.lower() or 'trending movies' in query.lower() or 'current movies' in query.lower():
            movies = get_trending_movies()
            for movies in movies:
                print(movies.encode('cp1252', errors='ignore').decode('cp1252'))
                speak(movies)
            speak('This are the few Trending movies Now')

    elif 'play music' in query.lower():
        music_dir = 'C:\\Users\\tanma\\Music\\Resso Music'
        songs = os.listdir(music_dir)
        print(songs)    
        os.startfile(os.path.join(music_dir, songs[0]))

    # elif 'play music' in query.lower():
    #     os.system("spotify")
    #     #time.sleep(10)
    #     keyboard.press_and_release('ctrl+l')
    #     keyboard.write('Aurora', delay=0.1)
    #     for key in ['enter', 'pagedown', 'tab', 'enter', 'enter']:
    #         time.sleep(2)
    #         keyboard.press_and_release(key) 

    elif 'open my code' in query.lower():
        codePath = "C:\\Users\\tanma\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)    
    
    elif"what is today's weather" in query.lower() or "today's weather" in query.lower():
        speak("Sure. Please tell me the name of the city.")
        city = takeCommand().lower()
        weather_report(city)

    elif 'search in chrome' in query.lower() or "search on chrome" in query.lower():
        speak("What should I search?")
        csearch = takeCommand().lower()
        url = f"https://www.google.com/search?q={csearch}"
        webbrowser.open_new_tab(url)

    elif 'search on youtube' in query.lower() or "search in youtube" in query.lower():
        speak("What should I search?")
        search = takeCommand().lower()
        query_string = urllib.parse.urlencode({"search_query" : search})
        html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
        search_result = re.findall(r"watch\?v=(\S{11})",html_content.read().decode())
        video_url = "http://www.youtube.com/watch?v=" + search_result[0]
        webbrowser.open(video_url)

    elif 'search wikipedia' in query.lower():
        speak("what should I search in Wikipedia...")
        query = takeCommand().lower()
        try:
            results = wikipedia.summary(query, sentences = 2)
            print(results.encode(sys.stdout.encoding, errors='ignore'))
            speak(results)
        except Exception as e:
            print(e)
            speak("Sorry, I could not find any results for your query.")

    elif 'shut down' in query.lower():
        speak('Are you sure you want to shut down the system?')
        response = takeCommand().lower()
        if 'yes' in response:
            os.system("taskkill /f /im explorer.exe")  # close all open windows in taskbar
            os.system("shutdown /s /t 1")  # shut down system after 1 second
        else:
            speak('OK, I will not shut down the system.')

    elif 'restart my computer' in query.lower():
        speak('Sure, restarting your computer.')
        response = takeCommand().lower()
        if 'yes' in response:
            os.system("taskkill /f /im explorer.exe")  # close all open windows and files
            os.system("shutdown /r /t 1")  # restart the computer after 1 second delay
        else:
            speak('OK, I will not restart the system.')
    
    elif "close" in query:
        app_name = query.lower().replace("close ", "")
        close_app(app_name)

    elif "exit" in query.lower():
        sys.exit() 

    else:
        query = query
        speak("Searching...")
        prompt = user_name + ":" + query + "\n" + bot_name + ":"
        conversation += prompt
        try:
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=conversation,
                temperature=0.7,
                max_tokens=256,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
                #engine="text-davinci-003",
                #prompt=prompt,
                #max_tokens=4000,
                #n=1,
                #stop=None,
                #temperature=0.5,
            )
            response_str = response["choices"][0]["text"].replace("\n", "")
            response_str = response_str.split(user_name + ":", 1)[0].split(bot_name + ":", 1)[0]
            conversation += response_str + "\n"
            print(response_str)
            speak(response_str)
        except Exception as e:
            print("An error occurred:", e)
            speak('Say that again please...')
        return
##########################################################################################################################################################
def weather_report(city):
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}"
    response = requests.get(weather_url)
    data = response.json()
    if data["cod"] != "404":
        city_name = data["name"]
        weather_desc = data["weather"][0]["description"]
        current_temp = round(data["main"]["temp"] - 273.15)
        feels_like = round(data["main"]["feels_like"] - 273.15)
        min_temp = round(data["main"]["temp_min"] - 273.15)
        max_temp = round(data["main"]["temp_max"] - 273.15)
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        report = f"Today's weather report for {city_name} is {weather_desc}. The current temperature is {current_temp}°C, but it feels like {feels_like}°C. The minimum temperature is {min_temp}°C and the maximum temperature is {max_temp}°C. The humidity level is {humidity}% and the wind speed is {wind_speed} m/s."
        speak(report)
    else:
        speak("City not found. Please try again.")
##############################################################################################################################################################
#def wolfram_alpha(query):
#    try:
#        res = openai.Completion.create(engine="davinci", prompt=f"Answer the following question:\n\n{query}\n\nAnswer:", max_tokens=1000)
#        result = res.choices[0].text.strip()
#        if result == "":
#            result = "I am sorry, but I could not find an answer to your question."
#            speak(result)
#    except Exception as e:
#        print("Error: ", e)
#        speak("I am sorry, but I could not find an answer to your question.")
#########################################################################################################################################################
def notepad():
    # Create a Tkinter window
    root = tk.Tk()
    root.title("Notepad")
    # Create a text widget
    text = tk.Text(root, wrap="word")
    text.pack(side="top", fill="both", expand=True)
    # Create a menu bar
    menu = tk.Menu(root)
    root.config(menu=menu)
    # Create a file menu
    file_menu = tk.Menu(menu)
    menu.add_cascade(label="File", menu=file_menu)
    def new_file():
        text.delete("1.0", "end")
        root.title("Notepad")
    def open_file():
        file = filedialog.askopenfile(parent=root, mode="rb", title="Open a file")
        if file:
            contents = file.read()
            text.delete("1.0", "end")
            text.insert("1.0", contents)
            file.close()
            root.title(file.name + " - Notepad")
    def save_file():
        file = filedialog.asksaveasfile(mode="w", defaultextension=".txt", filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")])
        if file:
            contents = text.get("1.0", "end")
            file.write(contents)
            file.close()
            root.title(file.name + " - Notepad")
    def quit():
        root.destroy()
    file_menu.add_command(label="New", command=new_file)
    file_menu.add_command(label="Open", command=open_file)
    file_menu.add_command(label="Save", command=save_file)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=quit)
    # Create an edit menu
    edit_menu = tk.Menu(menu)
    menu.add_cascade(label="Edit", menu=edit_menu)
    def cut():
        text.event_generate("<<Cut>>")
    def copy():
        text.event_generate("<<Copy>>")
    def paste():
        text.event_generate("<<Paste>>")
    edit_menu.add_command(label="Cut", command=cut)
    edit_menu.add_command(label="Copy", command=copy)
    edit_menu.add_command(label="Paste", command=paste)
    # Start the mainloop
    root.mainloop()
###################################################################################################################################################
def get_latest_news():
    news_headlines = []
    res = requests.get(
        f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}&category=general").json()
    articles = res["articles"]
    for article in articles:
        news_headlines.append(article["title"])
    return news_headlines[:5]
####################################################################################################################################################
def get_trending_movies():
    trending_movies = []
    res = requests.get(
        f"https://api.themoviedb.org/3/trending/movie/day?api_key={TMDB_API_KEY}").json()
    results = res["results"]
    for r in results:
        title = r["original_title"]
        trending_movies.append(title)
    return trending_movies[:5]
#####################################################################################################################################################
# def add_task():
# # create a cursor object
#     cursor = connection.cursor()
# # find the maximum value of Tid in the task table
#     cursor.execute("SELECT MAX(Tid) FROM task")
#     result = cursor.fetchone()
#     max_tid = result[0] if result[0] is not None else 0
# # increment the maximum Tid to generate the new Tid for the task
#     new_tid = max_tid + 1
# # prompt the user to enter a task description
#     speak("Enter the task description: ")
#     task_desc = takeCommand().lower()
# # execute an insert query to add the task to the database
#     query = "INSERT INTO task (Tid, task_dec) VALUES (%s, %s)"
#     values = (new_tid, task_desc) 
#     cursor.execute(query, values)
# # commit the changes to the database
#     connection.commit()
# # display the task description
#     print("Task description: " + task_desc)
# # print a message to confirm that the task was added
#     print("Task added successfully!")
# #######################################################################################################################################################
# def add_notes():
# # create a cursor object
#     cursor = connection.cursor()
# # find the maximum value of Tid in the task table
#     cursor.execute("SELECT MAX(Nid) FROM Note")
#     result = cursor.fetchone()
#     max_nid = result[0] if result[0] is not None else 0
# # increment the maximum Tid to generate the new Tid for the task
#     new_nid = max_nid + 1
# # prompt the user to enter a task description
#     speak("What Should I write in Note!! ")
#     Data = takeCommand().lower()
# # execute an insert query to add the task to the database
#     query = "INSERT INTO Note (Nid, Data) VALUES (%s, %s)"
#     values = (new_nid, Data) 
#     cursor.execute(query, values)
# # commit the changes to the database
#     connection.commit()
# # display the task description
#     print("Note description: " + Data)
# # print a message to confirm that the task was added
#     print("Note added successfully!")
##################################################################################################################################################
def close_app(app_name):
    for process in psutil.process_iter():
        try:
            if process.name().lower() == app_name.lower():
                process.kill()
                print(f"{app_name} closed.")
        except:
            pass
#########################################################################################################################################################
def open_whatsapp():
    # WhatsApp URI scheme for Windows
    uri_scheme = "whatsapp://"
    # Open WhatsApp application
    os.system(f"start {uri_scheme}")
####################################################################################################################################################################
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    
    # Get credentials from environment variables
    email_user = os.getenv("EMAIL_USER")
    email_pass = os.getenv("EMAIL_PASS")
    
    server.login(email_user, email_pass)
    server.sendmail(email_user, to, content)
    server.close()
#######################################################################################################################################################
class MainThread(QThread): 
    
    def __init__(self):
        super(MainThread,self).__init__()
        
    def run(self):
        wishMe()
        while True:
            query = takeCommand().lower()
            jarvis(query)
        
startExe = MainThread()     
####################################################################################################################################################################
class Gui_Start(QtWidgets.QMainWindow):
     
    def __init__(self):
        super().__init__()
         
        self.gui = Ui_MainWindow()
        self.gui.setupUi(self)

        self.gui.pb_start.clicked.connect(self.startTask)
        self.gui.pb_exit.clicked.connect(self.close)

        self.startExe = None
         
    def startTask(self):
        
        self.gui.l1 = QtGui.QMovie("GIF//83ec7dae7e76751eecca2adcf0dcfc49.gif")
        self.gui.gif_1.setMovie(self.gui.l1)
        self.gui.l1.start()
        
        self.gui.l2 = QtGui.QMovie("deco//3ab74962b138cb7396156fd96d0f6408.gif")
        self.gui.gif_2.setMovie(self.gui.l2)
        self.gui.l2.start()
        
        self.gui.l3 = QtGui.QMovie("deco//Untitled design (2).gif")
        self.gui.gif_3.setMovie(self.gui.l3)
        self.gui.l3.start()
        
        self.gui.l4 = QtGui.QMovie("deco//01.gif")
        self.gui.gif_4.setMovie(self.gui.l4)
        self.gui.l4.start()
        
        self.gui.l5 = QtGui.QMovie("deco//01.gif")
        self.gui.gif_5.setMovie(self.gui.l5)
        self.gui.l5.start()
        
        timer = QTimer(self)
        timer.timeout.connect(self.showTimeLive)
        timer.start(999)
        
        # Create a new MainThread instance and start it
        self.startExe = MainThread()
        self.startExe.start()
        
    def showTimeLive(self):
        time1=QTime.currentTime()
        time=time1.toString()
        date1=QDate.currentDate()
        date=date1.toString()
        label_t=time
        label_d=date
        
        self.gui.tb_time.setText(label_t)
        self.gui.tb_date.setText(label_d)
        
        
GuiApp=QApplication(sys.argv)
cAiUi = Gui_Start()
cAiUi.show()
exit(GuiApp.exec_()) 
