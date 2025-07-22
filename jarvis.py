import pyttsx3
import speech_recognition as sr
import random
import webbrowser
import datetime
from plyer import notification
import pyautogui  #used for open any application in pc which is already installed
import wikipedia
import pywhatkit
import mistral_ai as ai
import image_form


engine= pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def command():
    content = " "
    while content == " ":
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)

        try:
            content = r.recognize_google(audio,language = 'en-in')
            print(" you said that: " + content)
        except Exception as e:
            print("try once again")
        return content

def main_process():
    while True:
        request = command().lower()
        if "hello" in request:
            speak("hi, how can i help u")
        elif "play music" in request:
            speak("Playing music")
            song = random.randint(1,3)
            if song ==1:
                webbrowser.open("https://youtu.be/iJVtxex6HIk?si=tCUwLqrbeTsd0eoj")
            elif song ==2:
                webbrowser.open("https://youtu.be/SkQz6OzT85w?si=wg2gyE_c-pIuwkEk")
            else:
                webbrowser.open("https://youtu.be/gXKEaJXDmek?si=3WSc3gpQZTgnOjvO")
        elif "sat shri akaal" in request:
            speak("sat shri akaal ji, kidda help kra mai tuhadi")
        elif "tell time" in request:
            now_time= datetime.datetime.now().strftime("%H:%M")
            speak("current time is" + str(now_time))
        elif "tell date" in request:
            now_date = datetime.datetime.now().strftime("%m:%h:%y")
            speak("Today is" + str(now_date))
        elif "add task" in request:
            task = request.replace("add task", " ")
            task = task.strip()
            if task !=" ":
                speak("adding task"+ task)
                with open("todo.txt", "a") as file:
                    file.write(task + "\n")
        elif "speak task" in request:
            with open("todo.txt", "r") as file:
                speak("In todo there is" + file.read())
        
        elif "show task" in request:
            with open("todo.txt", "r") as file:
                task = file.read()
                notification.notify(
                    title = "messages are",
                    message = task
                )
        elif "open" in request:
            query = request.replace("open", "")
            pyautogui.press("super")   #super is window button and press is click on that button which is under quotations
            pyautogui.typewrite(query)
            pyautogui.sleep(2)
            pyautogui.press("enter")

        elif "search google" in request:
       
            request = request.replace("search google", "").strip()
            speak("we r searching for" + request)
           
            webbrowser.open(f"https://www.google.com/search?q={request}")
            # speak(f"searching in google for {request}")
        elif "send whatsapp" in request:
            # pywhatkit.sendwhatmsg("+916398442272" , "ki haal ne puttr" ,13, 58,15 )
            pywhatkit.sendwhatmsg_instantly("+916398442272" , "ki haal ne puttr", 15)

        elif "ask ai" in request:
            request = request.replace("ask ai", "").strip()
            print(request)
            response = ai.send_request(request)
            print(response)
            speak(response)
        elif "create image" in request:
            request = request.replace("create image", "").strip()
            print(request)
            speak("creating image of " + request)
            respnse1 = image_form.generate_and_open_image(request)
            


        elif "bye" in request:
            speak("good bye, have a nice day")
            break
    
        # print(request)
# speak("Sat shri akaal ji")
main_process()