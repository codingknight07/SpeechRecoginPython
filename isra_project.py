import speech_recognition as sr
import time
import webbrowser
import sys
import playsound
from gtts import gTTS
import os
import random
import threading
#import tkinter
from tkinter import *
from tkinter.ttk import *

#instance of recogniser class
r=sr.Recognizer()
#list acting as global variable
l=[0]


#ret_speech invokes mic gets input convert to text and returns
def ret_speech() :
    with sr.Microphone() as src : 
        audio=r.listen(src,timeout=5.0)
        audio_text=''
        try : 
            #recognize_sphinx(): CMU Sphinx - requires installing PocketSphinx-works offline
            audio_text=r.recognize_google(audio)
        except sr.UnknownValueError :
            #if couldn't recognize audio
            pass
            #text_speech("Sorry I couldn't get that mic off")
            
             #change button state function to off
        except sr.RequestError : #if google didnt respond
            text_speech("Either you are not connected or Service is currently down ")
        except sr.WaitTimeoutError : 
            text_speech('Timeout try again')
        return audio_text 
    
#fn to convert text to speech    
def text_speech(tex) : 
    tts=gTTS(text=tex,lang='en')
    r=random.randint(1,100000)
    audio_file='audio-'+str(r)+'.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    os.remove(audio_file)
    
#tells what it can do(to be added at last)    
def tell_what() : 
    pass
#fn to do task as required    
def respond(audio_data) :
    got=0
    if 'exit'  in audio_data.lower() : 
        text_speech('Bye! Have a nice Day')
        mic_button.configure(image = _offmic)
        return 0
         #change button state function to off      
    if 'is your name' in audio_data.lower() : 
        text_speech('My name is isra')
        got=1
        tmp=0
        return 1
    elif 'search web for' in audio_data.lower() : 
        tmp=audio_data.find('web for')
        got=1
        url='https://www.google.co.in/search?q='+audio_data[(tmp+7):]
        text_speech('Searching, Web')
        mic_button.configure(image = _offmic)
        try :
            webbrowser.open_new_tab(url)
            
        except : 
            text_speech('cannot find a browser')
        return 0    
       #change button state function to off      
    elif 'search' in audio_data.lower() : 
        tmp=audio_data.find('search')
        got=1
        
        url='https://www.google.co.in/search?q='+audio_data[(tmp+7):]
        text_speech('Searching Web')
        mic_button.configure(image = _onmic)
        try :
            webbrowser.open_new_tab(url)
            
        except : 
            text_speech('cannot find a browser')
            mic_button.configure(image = _offmic)
        return 0    #change button state function to off
         
    elif 'what can you do' in audio_data.lower() : 
        tell_what()
        got=1
    elif ('is the time' in audio_data ) or ('time is it' in audio_data) : 
        got=1
        text_speech(time.strftime("%H:%M:%S",time.localtime()))
        return 1
    
    elif 'about yourself' in audio_data.lower() : 
        got=1
        text_speech('I am ISRA developed by Varun')
        return 1
    if got==0 :
       text_speech("Sorry,I don't know how to respond to this Would you like me to search web")
       return 0
       url='https://www.google.co.in/search?q='+audio_data
       text_speech('Searching Web')
        
       try :
            webbrowser.open_new_tab(url)
            
       except : 
            text_speech('cannot find a browser')
#Main window dimensions
_root = Tk()
_root.title('ISRA')
_root.iconbitmap('ISRA LOGO.ico')
_root.geometry('430x500')
_root.resizable(height = False, width=False)

def _about():
        about = Tk()
        about.title('ISRA')
        about.iconbitmap('ISRA LOGO.ico')
        about.geometry('300x200')
        ab = Label(about, text='Indian Speech Recognition Assistant')
        ab.place(anchor = CENTER, rely=0.15, relx=0.5)
        v = Label(about, text ='Version v1.0 beta')
        v.place(anchor = CENTER ,relx=0.5,rely=0.25)
        c = Label(about, text='Creators: Varun Bhatnagar and Tushar Garg')
        c.place(anchor = CENTER,relx=0.5,rely=0.75)
        
def _help():
        help = Tk()
        help.title('ISRA')
        help.iconbitmap('ISRA LOGO.ico')
        help.geometry('300x50')
        h = Label(help, text='It is a simple program so there is no need for help.')
        h.pack()
        
 #adding assistant text area
        
ass_text = Text(_root, height = 18 , width=48)
ass_text.place(anchor = CENTER, relx=0.48,rely=0.49)
scroll = Scrollbar(_root)
scroll.pack(side = RIGHT, fill = Y)
ass_text.config(yscrollcommand = scroll.set)
scroll.config(command = ass_text.yview)

#Web search entry
search_lab = Label(_root, text = 'Search Web: ', font = ("Times New Roman", 10, "bold"))
search_lab.place(relx=0.1 , rely = 0.85, anchor = CENTER)
search_entry = Entry(_root)
search_entry.config(width = 53)
search_entry.place(relx=0.56,rely=0.85,anchor=CENTER)

#hear fn invoked as thread after you Activate mic
def hear(): 
    text_speech('Hi!,How may, I help you?')  
    ass_text.insert(END,'\nHi, I am ISRA how may I help you?') 

    while(l[0]) : #exit button GUI 
        ass_text.insert(END,'\nListening...')
        if l[0]==0 : 
            break
        audio_data=ret_speech()
        if l[0]==0 : 
            break
        ass_text.insert(END,'\n'+audio_data)#create update user text widget fn
        l[0]=respond(audio_data)
    
 #changing state(on/off) of mic using global list variable

onmic = PhotoImage(file = 'MIC.png')
_onmic = onmic.subsample(4,4)

offmic = PhotoImage(file = 'offmic.png')
_offmic = offmic.subsample(4,4)
        
def change_state(i) :
    if i==0 :
        l[0]=1
        threading.Thread(target=hear).start()
        l[0]=1
        mic_button.configure(image = _onmic)
    else : 
        l[0]=0
        text_speech('mic off')
        mic_button.configure(image = _offmic)
#making menus
my_menu = Menu(_root)

_root.config(menu = my_menu)

my_menu.add_cascade(label = 'Settings')

options = Menu(my_menu, tearoff = 0)
my_menu.add_cascade(label = 'Account', menu = options)
options.add_command(label = 'General')
options.add_command(label = 'Privacy and Security')
options.add_separator()
options.add_command(label = 'Sign Out')

my_menu.add_cascade(label = 'Help', command = _help)

my_menu.add_cascade(label = 'About', command = _about)

    #Making Exit button
#Making Exit button
style = Style()
style.configure('Exit.TButton', font =('Showcard Gothic', 10))

exit_button = Button(_root, text='Exit', style = 'Exit.TButton', command = _root.destroy)
exit_button.place(relx=0.5, rely=0.95, anchor = CENTER)
exit_button.config( width = 25)

    #Making Mic button

#mic photo not working have to fix
mic_button = Button(_root, image = _offmic, command=lambda:change_state(l[0]))#mic_button = Button(_root, image = _photo,command=hear)
mic_button.place(relx=0.5, rely=0.1, anchor = CENTER)

_root.mainloop()