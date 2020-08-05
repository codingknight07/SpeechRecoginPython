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

        
        

