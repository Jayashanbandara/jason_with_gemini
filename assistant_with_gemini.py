import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk  # Install ttkthemes using: pip install ttkthemes
import speech_recognition as sr
import pyttsx3
import pyautogui
import webbrowser
import subprocess

import google.generativeai as genai
G_API_KEY="AIzaSyCQLhzQ9hkE-YM4dTLhU5vQwjEWwCLlsZI"
genai.configure(api_key=G_API_KEY)
model = genai.GenerativeModel('gemini-pro')

tasks = []
listening_to_task = False

def open_notepad():
    try:
        subprocess.Popen(["notepad.exe"])
        respond("Opening Notepad.")
    except Exception as e:
        print(f"Error opening Notepad: {e}")
        respond("Sorry, I encountered an error while trying to open Notepad.")
 
def open_mathlab():
    matlab_path = r"C:\\Program Files\\MATLAB\\R2022b\bin\\matlab.exe"
    try:
        subprocess.Popen(matlab_path, shell=True)
        respond("Opening Matlab.")
    except Exception as e:
        print(f"Error opening matlab: {e}")
        respond("Sorry, I encountered an error while trying to open Matlab.")       
        
        
    
def listen_for_command():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening for commands...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source,timeout=5)

    try:
        command = recognizer.recognize_google(audio)
        command =command.lower()
        print("You said:", command)
        return command
    except sr.UnknownValueError:
        print("Could not understand audio. Please try again.")
        return None
    except sr.RequestError:
        print("Unable to access the Google Speech Recognition API.")
        return None

def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 170)
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def respond(response_text):
    print(response_text)
    speak(response_text)

def take_screenshot():
    pyautogui.screenshot("screenshot.png")
    respond("I took a screenshot for you.")

def open_chrome():
    respond("Opening Chrome.")
    webbrowser.open("https://www.youtube.com/@tronictricks9509/videos")

def list_tasks():
    respond("Sure. Your tasks are:")
    for task in tasks:
        respond(task)


def find_gemini(find_text):
    find_text = find_text.replace('jason find', '')
    response = model.generate_content(find_text)
    
    print(response.text)
    speak(response.text)
    speak('i provided you all the detail i known sir ')


    

def start_listening():
    global tasks
    global listening_to_task
    respond("Welcome to voice assistant Sir")
    
    while True:
        command = listen_for_command()
       
        trigger_keyword = "jason"

        if command and trigger_keyword in command:
            if listening_to_task:
                tasks.append(command)
                listening_to_task = False
                respond("Adding " + command + " to your task list. You have " + str(len(tasks)) +
                         " currently in your list.")
            elif "add task" in command:
                listening_to_task = True
                respond("Sure, what is the task?")
            elif "list tasks" in command:
                list_tasks()
            elif "take a screenshot" in command:
                take_screenshot()
            elif "open chrome" in command:
                open_chrome()
            elif "open notepad" in command:
                open_notepad()
            elif "open matlab" in command:
                open_mathlab()        
            elif "find" in command:
                find_gemini(command)    
            elif "voice exit" in command:
                respond("Exit from the voice assistant")
                break
            else:
                respond("Sorry, I'm not sure how to handle that command.")



def main():
    
    
    
    root = ThemedTk(theme="yaru")  # Use "clearlooks", "equilux", or any other available themes
    root.title("TUTU-AI Assistant")
    root.geometry("400x300")

    style = ttk.Style()
    style.configure("TButton", padding=6, relief="flat", font=("Segoe UI", 10))
    
    label = ttk.Label(root, text="Voice Assistant", font=("Segoe UI", 14))
    label.pack(pady=10)

    button_listen = ttk.Button(root, text="Start Listening", command=start_listening)
    button_listen.pack(pady=10)

    button_screenshot = ttk.Button(root, text="Take Screenshot", command=take_screenshot)
    button_screenshot.pack(pady=10)

    button_open_chrome = ttk.Button(root, text="Open Chrome", command=open_chrome)
    button_open_chrome.pack(pady=10)

    button_list_tasks = ttk.Button(root, text="List Tasks", command=list_tasks)
    button_list_tasks.pack(pady=10)
    
    button_open_notepad = ttk.Button(root, text="Open Notepad", command=open_notepad)
    button_open_notepad.pack(pady=10)
    respond("Hello i am jason voice assistant AI , i was created by jayashan ")
    
    root.mainloop()

    
    
if __name__ == "__main__":
    main()
