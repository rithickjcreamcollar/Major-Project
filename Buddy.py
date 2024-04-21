import smtplib
import ssl

import keyboard
import qrcode
import speech_recognition as sr
import cv2
import ctypes
from googlesearch import search
import psutil
from plyer import notification
import pyautogui
import pytesseract
import youtube_dl
import time
import tkinter
import datetime
import webbrowser
import os
import pyttsx3
import shutil
from tkinter import filedialog
from tkinter import *



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def send_email(sender_email, receiver_email, password, subject, body):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"

    message = f"""\
    Subject: {subject}

    {body}
    """

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
def shutdown_computer():
    try:
        os.system("shutdown /s /t 1")  # Shutdown command for Windows
        # For Linux/Mac, you can use: os.system("shutdown now")
        print("Shutting down the computer...")
    except Exception as e:
        print(f"Error shutting down the computer: {e}")
def switch_tab(num_tabs_to_switch):
    for _ in range(num_tabs_to_switch):
        pyautogui.hotkey('ctrl', 'tab')

def generate_qr_code(data, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
def sleep_computer_windows():
    try:
        os.system("shutdown /h")  # Command to put Windows into sleep mode
        print("Putting the computer to sleep...")
    except Exception as e:
        print(f"Error putting the computer to sleep: {e}")
def close_chrome():
    os.system("taskkill /f /im chrome.exe")
def open_task_manager():
    os.system("taskmgr")
def minimize_all():
    pyautogui.hotkey('win', 'd')
def open_explorer():
    pyautogui.hotkey('win', 'e')
def incBright():
    pyautogui.hotkey('Fn', 'F6')
def decBright():
    pyautogui.hotkey('Fn', 'F5')
def settings():
    pyautogui.hotkey('win', 'i')
def clipboard():
    pyautogui.hotkey('win', 'v')
def notifyBar():
    pyautogui.hotkey('win', 'a')
def searchBar():
    pyautogui.hotkey('win', 's')
def runn():
    pyautogui.hotkey('win', 'r')
def emoji():
    pyautogui.hotkey('win', '.')


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


speak("Im ready!")

print("")

notification.notify(
    title="Buddy",
    message="Buddy is Ready !",
    timeout=10,
    app_icon="Customization\\jarvis.ico"
)

time.sleep(3)


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir !")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir !")

    else:
        speak("Good Evening Sir !")

    assname = ("BUddy")
    speak("I am your Assistant")
    speak(assname)


def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said : {query}\n")

    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        return "None"

    return query

def sleep_computer_windows():
    try:
        os.system("shutdown /h")  # Command to put Windows into sleep mode
        print("Putting the computer to sleep...")
    except Exception as e:
        print(f"Error putting the computer to sleep: {e}")
def usrname():
    speak("What should i call you Sir")
    uname = takeCommand()

    speak("Welcome" + uname + "Sir.")
    print("Welcome " + uname + " Sir.")
    columns = shutil.get_terminal_size().columns
    speak("How can i Help you, Sir. Please give your queries")

def take_notes():
    try:
        note = input("What do you want to write down?: ")
        with open("notes.txt", "a") as file:
            file.write(note + "\n")
        print("Note saved successfully!")
    except Exception as e:
        print("An error occurred:", str(e))

def take_screenshot():
    try:
        # Take screenshot
        screenshot = pyautogui.screenshot()

        # Save screenshot to a file
        screenshot_path = "screenshot.png"
        screenshot.save(screenshot_path)

        print("Screenshot saved successfully!")
        return screenshot_path
    except Exception as e:
        print("An error occurred:", str(e))
        return None
def google_search(query):
    try:
        # Perform Google search
        results = search(query, num=5, stop=5, pause=2)  # Get top 5 search results

        # Display search results
        for i, result in enumerate(results, start=1):
            print(f"Result {i}: {result}")

    except Exception as e:
        print("An error occurred:", str(e))
if __name__ == '__main__':
    clear = lambda: os.system('cls')
    clear()
    wishMe()
    usrname()
    listening = True
    while True:

        a = takeCommand().lower()
        if 'wait wait' in a:
            listening = False  # Pause listening
        elif 'start' in a:
            listening = True  # Resume listening
        elif 'quit' in a:
            speak("Thank you Sir for your time. Have a nice day.")
            break
        elif 'take a note' in a or 'take some note' in a or 'take note' in a or 'take the note' in a:
            take_notes()
        elif 'shutdowm' in a or 'poweroff' in a:
            shutdown_computer()
        elif 'sleep' in a:
            sleep_computer_windows()
        elif 'open taskmanager' in a:
            os.system("taskmgr")
        elif 'minimize all ' in a:
            minimize_all()
        elif 'open explorer' in a:
            open_explorer()
        elif 'increase brightness' in a:
            incBright()
        elif 'decrease brightness' in a:
            decBright()
        elif 'decrease volume' in a:
            speak("Hello Sir. How are you ?")
        elif 'increase volume' in a:
            speak("Hello Sir. How are you ?")
        elif 'open settings' in a:
            settings()
        elif 'open clipboard' in a:
            clipboard()
        elif 'sleep mode' in a:
            sleep_computer_windows()
        elif 'open notify bar' in a:
            notifyBar()
        elif 'open search bar' in a:
            searchBar()
        elif 'open run ' in a:
            runn()
        elif 'open emoji' in a:
            emoji()
        elif 'good morning' in a or 'good morning jarvis' in a:
            speak("Good Morning Sir !")
        elif 'switch tab' in a:
            switch_tab(1)
            speak("Done")
        elif 'close chrome' in a:
            speak("closing Chrome")
            close_chrome()
        elif 'copy' in a:
            speak("copying files")
            pyautogui.hotkey('ctrl', 'c')
        elif 'paste' in a:
            speak("pasting files")
            pyautogui.hotkey('ctrl', 'v')
        elif 'good evening' in a or 'good evening jarvis' in a:
            speak("Good Evening Sir !")

        elif 'search in google' in a or 'google search' in a:
            query = input("What do you want to search for?: ")
            google_search(query)
        elif 'good night' in a or 'good night jarvis' in a:
            speak("Good Night Sir !")

        elif 'open cmd' in a or 'open command prompt' in a or 'open cmd jarvis' in a or 'open command prompt jarvis' in a:
            speak("Opening command prompt")
            os.startfile("C:\\WINDOWS\\system32\\cmd.exe")
        elif 'eject usb' in a:
            speak("Ejecting USB")
            os.startfile("C:\\WINDOWS\\system32\\DeviceEject.exe")
        elif 'open system details' in a:
            speak("Opening SystemInfo")
            os.startfile("C:\\WINDOWS\\system32\\dxdiag.exe")
        elif 'eject usb' in a:
            speak("Ejecting USB")
            os.startfile("C:\\WINDOWS\\system32\\DeviceEject.exe")
        elif 'eject usb' in a:
            speak("Ejecting USB")
            os.startfile("C:\\WINDOWS\\system32\\DeviceEject.exe")
        elif 'play music' in a:
            speak("Playing Music")
            os.startfile("C:\\Program Files\\Windows Media Player\\wmplayer.exe")
        elif 'open word' in a:
            speak("Opening Word")
            os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Word.exe")
        elif 'open powerpoint' in a:
            speak("Opening Powerpoint")
            os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Powerpoint.exe")
        elif 'open excel' in a:
            speak("Opening excel")
            os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Excel.exe")
        elif 'open edge' in a:
            speak("Opening edge")
            os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Edge.exe")
        elif 'take screenshot' in a or 'take a screenshot' in a:
            screenshot_path = take_screenshot()
            if screenshot_path:
                speak("Screenshot taken. Here is your screenshot.")
                os.startfile(screenshot_path)
            else:
                speak("Failed to take a screenshot.")
        elif 'how are you' in a or 'how do you do' in a or 'how are you jarvis' in a or 'how do you do jarvis' in a:
            speak("I am fine Sir. Thank you for asking.")

        elif 'what is your name' in a or 'who are you' in a:
            speak(
                "My name is Jarvis - The virtual assistant cum chatbot. I was created by Mr. Joel Shine on 6th of December on 2020.")

        elif 'wait' in a or 'wait jarvis' in a or 'wait please' in a or 'please wait' in a or 'please wait jarvis' in a or 'wait please jarvis' in a:
            speak("Ok Sir. As you wish ! Waiting till space is pressed !")
            keyboard.wait('space')

        elif 'what is the time' in a or 'what is time' in a or 'say the time' in a or 'say time' in a or 'show time' in a or 'open time' in a:
            now = datetime.datetime.now()
            speak("Sir, the current time is " + now.strftime("%H:%M") + '\n')
            print("Sir, the current time is " + now.strftime("%H:%M") + '\n')

        elif 'get weather' in a or 'get the weather' in a or 'what is the weather' in a or 'give me the weather' in a or 'give me weather' in a:
            import requests, json

            # Enter your API key here
            api_key = "69bf0a590576448ed0bfd804ac2b2694"

            # base_url variable to store url
            base_url = "http://api.openweathermap.org/data/2.5/weather?"

            speak("Sir please give the city name")
            city_name = takeCommand()

            complete_url = base_url + "appid=" + api_key + "&q=" + city_name

            # get method of requests module
            # return response object
            response = requests.get(complete_url)

            # json method of response object
            # convert json format data into
            # python format data
            x = response.json()

            if x["cod"] != "404":

                y = x["main"]

                current_temperature = y["temp"]

                current_pressure = y["pressure"]

                current_humidiy = y["humidity"]

                z = x["weather"]

                weather_description = z[0]["description"]
                celsius = current_temperature - 273.15

                speak("Sir, Temperature in " + city_name + "is" + str(celsius) + " degree celsius")
                print("Temperature in Celsius = " + str(celsius) + " degree celsius")
                print("Temperature in Farenheit = " + str(celsius * 9 / 5 + 32) + " degree farenheit")

                speak("The weather description is " + str(weather_description))
                print("Atmospheric pressure = " + str(current_pressure) + " mb")
                print("Humidity = " + str(current_humidiy) + " %")
                print("Description = " + str(weather_description))
                print("")

            else:
                print(" City Not Found. Please try again.")

        elif 'open google' in a or 'show google' in a:
            speak("Opening google")
            webbrowser.open("www.google.com")

        if 'send email' in a:
             # Assuming the user speaks out the sender's email address
            speak("Give the receiver address")
            receiver_email = input()  # Assuming the user speaks out the receiver's email address
            speak("Give the subject")
            subject = takeCommand().lower()   # Assuming the user speaks out the subject of the email
            speak("Give the body")
            body = takeCommand().lower()  # Assuming the user speaks out the body of the email
            sender_email = "moulidevops@gmail.com"
            password = "Rithickap@19"  # Enter the sender's email password here
            send_email(sender_email, receiver_email, password, subject, body)

        elif 'what is the date' in a or 'what is date' in a or 'show date' in a or 'show the date' in a or 'say the date' in a:
            now = datetime.datetime.now()
            speak("Sir, the Current Date is : " + now.strftime("%d-%m-%Y") + '\n')
            print("Sir, the Current Date is : ")
            print(now.strftime("%d-%m-%Y") + '\n')
            print("")

        elif 'open calendar' in a or 'show calendar' in a:
            speak("Opening Calendar")
            os.startfile("Calendar\\dist\\Calendar\\Calendar.exe")
            print("Opened Calendar")
            print("")

        elif 'open whatsapp' in a or 'show whatsapp' in a:  ##Only if you have whatsapp web.
            speak("Opening Whatsapp")
            webbrowser.open("https://web.whatsapp.com/")

        elif 'open youtube' in a or 'show youtube' in a:
            speak("Opening Youtube")
            webbrowser.open("www.youtube.com")

        elif 'open gmail' in a or 'show gmail' in a or 'open g mail' in a or 'show g mail' in a:
            speak("Opening Gmail")
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")

        elif 'open notepad' in a or 'show notepad' in a:
            speak("Opening Notepad")
            os.startfile("C:\\WINDOWS\\system32\\notepad.exe")

        elif 'open calculator' in a or 'show calculator' in a:
            speak("Opening calculator.")
            os.startfile("Calculator\\dist\\Calculator\\Calculator.exe")

        elif 'take a pic' in a or 'take a picture' in a or 'open camera' in a or 'show camera' in a:
            speak("Preparing to take picture. Press s to save the image.")
            key = cv2.waitKey(1)
            webcam = cv2.VideoCapture(0)
            while True:
                try:
                    check, frame = webcam.read()
                    print(check)  # prints true as long as the webcam is running
                    print(frame)  # prints matrix values of each framecd
                    cv2.imshow("Capturing", frame)
                    key = cv2.waitKey(1)

                    if key == ord('s'):
                        # Assuming 'frame' is your captured image from the webcam
                        cv2.imwrite(filename='images\\saved_img.jpg', img=frame)
                        webcam.release()  # Release the webcam after capturing the image

                        print("Processing image...")
                        img_ = cv2.imread('images\\saved_img.jpg', cv2.IMREAD_ANYCOLOR)  # Read the saved image
                        print("Converting RGB image to grayscale...")
                        gray = cv2.cvtColor(img_, cv2.COLOR_BGR2GRAY)  # Convert RGB image to grayscale
                        print("Resizing image to 28x28 scale...")
                        img_resized = cv2.resize(gray, (28, 28))  # Resize the image to 28x28 pixels
                        print("Image saved!")

                        # Save the resized image
                        cv2.imwrite(filename='images\\saved_img-final.jpg', img=img_resized)

                        break
                    elif key == ord('q'):
                        print("Turning off camera.")
                        webcam.release()
                        print("Camera off.")
                        print("Program ended.")
                        cv2.destroyAllWindows()
                        break

                except(KeyboardInterrupt):
                    print("Turning off camera.")
                    webcam.release()
                    print("Camera off.")
                    print("Program ended.")
                    cv2.destroyAllWindows()
                    break

        elif 'lock the device' in a or 'lock device' in a or 'lock a device' in a or 'lock this device' in a:
            speak("Locking the device")
            ctypes.windll.user32.LockWorkStation()
            break

        elif 'jarvis' in a or 'where are you jarvis' in a:
            speak("At your service Sir !")

        elif 'open webex' in a or 'show webex' in a or 'open cisco webex' in a or 'show cisco webex' in a:
            speak("Opening Cisco Webex")
            webbrowser.open(
                "https://globalpage-prod.webex.com/join?surl=https%3A%2F%2Fsignin.webex.com%2Fcollabs%2F%23%2Fmeetings%2Fjoinbynumber%3F")

        elif 'record jarvis' in a or 'jarvis record' in a or 'open recorder' in a or 'show recorder' in a:
            speak("Opening Voice Recorder")
            os.startfile("Recordingapp\\dist\\Recordingapp\\Recordingapp.exe")

        elif 'download video' in a or 'download a video' in a or 'download the video' in a:

            ydl_opts = {}
            def dwl_vid(video_url):
                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([video_url])
            channel = 1
            while (channel == int(1)):
                speak("Please provide the URL of the YouTube video you want to download.")
                video_url = takeCommand()  # Assuming you have a function takeCommand() for voice input
                zxt = video_url.strip()
                dwl_vid(zxt)
                speak("Enter 1 if you want to download more videos, or Enter 0 if you are done.")
                channel = int(takeCommand())  # Assuming takeCommand() returns the user's voice input

        elif 'ocr' in a or 'extract text from image' in a:
            speak("Opening Optical Character Recognition OCR")
            root = tkinter.Tk()
            root.wm_withdraw()
            root.iconify()

            pytesseract.pytesseract.tesseract_cmd = "C:\\Users\\joels\\AppData\\Local\\Tesseract-OCR\\tesseract.exe"
            image = Image.open(filedialog.askopenfilename())

            image_to_text = pytesseract.image_to_string(image, lang='eng')
            print(image_to_text)

            root.destroy()
            speak("Qr code saved successfully !")
            root.destroy()

        elif 'show battery' in a or 'what is the battery remaining' in a or 'what is the remaining battery' in a:
            battery = psutil.sensors_battery()
            percent = battery.percent
            percentinletters = str(percent)
            speak("Sir, there is " + percentinletters + " percent remaining.")
            print("There is " + percentinletters + " % remaining.")


            class Gsearch_python:
                def __init__(self, name_search):
                    self.name = name_search

                def Gsearch(self):
                    count = 0
                    try:
                        from googlesearch import search
                    except ImportError:
                        print("No Module named 'google' Found")

                    for i in search(query=self.name, tld='co.in', lang='en', num=10, stop=1, pause=2):
                        count += 1
                        print(count)
                        print(i + '\n')


            if __name__ == '__main__':
                gs = Gsearch_python(a)
                gs.Gsearch()
