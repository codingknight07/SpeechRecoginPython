import speech_recognition as sr
import time
import webbrowser
import sys
import playsound
from gtts import gTTS
import os
import random
r=sr.Recognizer()


#chrome_path='C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
#webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path),1)
def ret_speech() :
    with sr.Microphone() as src : 
        audio=r.listen(src,timeout=5.0)
        audio_text=''
        try : 
            #recognize_sphinx(): CMU Sphinx - requires installing PocketSphinx-works offline
            audio_text=r.recognize_google(audio)
        except sr.UnknownValueError : #if couldn't recognize audio
            text_speech("Sorry I couldn't get that")
            sys.exit()
        except sr.RequestError : #if google didnt respond
            text_speech("Either you are not connected or Service is currently down ")
        except sr.WaitTimeoutError : 
            text_speech('Timeout try again')
        return audio_text   
def text_speech(tex) : 
    tts=gTTS(text=tex,lang='en')
    r=random.randint(1,100000)
    audio_file='audio-'+str(r)+'.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    os.remove(audio_file)
    
    
def tell_what() : 
    pass
    
def respond(audio_data) :
    got=0
    if 'exit'  in audio_data.lower() : 
        text_speech('Bye! Have a nice Day')
        sys.exit()
    if 'is your name' in audio_data.lower() : 
        text_speech('My name is isra')
        got=1
        tmp=0
    elif 'search web for' in audio_data.lower() : 
        tmp=audio_data.find('web for')
        got=1
        url='https://www.google.co.in/search?q='+audio_data[(tmp+7):]
        text_speech('Searching, Web')
        
        try :
            webbrowser.open_new_tab(url)
            
        except : 
            text_speech('cannot find a browser')
        sys.exit()        
    elif 'search' in audio_data.lower() : 
        tmp=audio_data.find('search')
        got=1
        
        url='https://www.google.co.in/search?q='+audio_data[(tmp+7):]
        text_speech('Searching Web')
        
        try :
            webbrowser.open_new_tab(url)
            
        except : 
            text_speech('cannot find a browser')
        sys.exit()    
    elif 'what can you do' in audio_data.lower() : 
        tell_what()
        got=1
    elif ('is the time' in audio_data ) or ('time is it' in audio_data) : 
        got=1
        text_speech(time.ctime())
    
    elif 'about yourself' in audio_data.lower() : 
        got=1
        text_speech('I am ISRA developed by Varun')
    if got==0 :
       text_speech("Sorry,I don't know how to respond to this")
       url='https://www.google.co.in/search?q='+audio_data
       text_speech('Searching Web')
        
       try :
            webbrowser.open_new_tab(url)
            
       except : 
            text_speech('cannot find a browser')
    
#Start
text_speech('Hi!,How may, I help you?')       
print('Hi, I am ISRA how may I help you?\nListening...') #ToBeInc.inGUI               
#time.sleep(1)
while(1) : #exit button GUI 
    
    audio_data=ret_speech()
    
    #text_speech('something went wrong try again or say exit
        
    print(audio_data)
    respond(audio_data)
    print('Listening...')
    
    
    

    import tkinter
    from tkinter import *
    from tkinter.ttk import *

    #Main window dimensions
    _root = Tk()
    _root.title('ISRA')
    _root.iconbitmap('C:\ISRA\ISRA LOGO.ico')
    _root.geometry('330x300')


     #defining about
    def _about():
        about = Tk()
        about.title('ISRA')
        about.iconbitmap('C:\ISRA\ISRA LOGO.ico')
        about.geometry('300x200')
        ab = Label(about, text='Indian Speech Recognition Assistant')
        ab.place(anchor = CENTER, rely=0.15, relx=0.5)
        v = Label(about, text ='Version v1.0 beta')
        v.place(anchor = CENTER ,relx=0.5,rely=0.25)
        c = Label(about, text='Creators: Varun Bhatnagar and Tushar Garg')
        c.place(anchor = CENTER,relx=0.5,rely=0.75)


    #defining help
    def _help():
        help = Tk()
        help.title('ISRA')
        help.iconbitmap('C:\ISRA\ISRA LOGO.ico')
        help.geometry('300x50')
        h = Label(help, text='It is a simple program so there is no need for help.')
        h.pack()


    #setting menues
    my_menu = Menu(_root)
    _root.config(menu = my_menu)



    #setting main menu
    options_menu = Menu(my_menu,tearoff = 0)
    my_menu.add_cascade(label ='Menu', menu = options_menu)
    options_menu.add_command(label="Settings")
    options_menu.add_command(label ='Help', command = _help)
    options_menu.add_command(label ='About', command = _about)


    #setting another menu
    options_menu = Menu(my_menu,tearoff = 0)
    my_menu.add_cascade(label ='Account', menu = options_menu)
    options_menu.add_command(label="General")
    options_menu.add_command(label ='Privacy and Security')
    options_menu.add_command(label ='Sign Out')


    #Making Exit button
    exit_button = Button(_root, text='Exit', command = _root.destroy)
    exit_button.place(relx=0.5, rely=0.95, anchor = CENTER)
    exit_button.config(width = 15)


    #Making Mic button

    photo = PhotoImage(file = 'MIC.png')
    _photo = photo.subsample(4,4)
    mic_button = Button(_root, image = _photo)
    mic_button.place(relx=0.5, rely=0.15, anchor = CENTER)

    scroll = Scrollbar(_root)
    scroll.place(relx=0.605, rely=0.6, anchor = CENTER)

    #adding assistant text area
    ass_text = Text(_root, height = 10 , width=35, yscrollcommand = scroll.set)
    ass_text.place(anchor = CENTER, relx=0.5,rely=0.6)
    scroll.config(command = ass_text.yview)



    _root.mainloop()



