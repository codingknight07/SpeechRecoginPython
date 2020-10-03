import speech_recognition as sr
import time
import webbrowser
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import sys
import playsound
from gtts import gTTS
import os
import random
import threading
from tkinter import *
from tkinter.ttk import *

#instance of recogniser class
r=sr.Recognizer()
#list acting as global variable
l=[0]
social_media=['facebook','instagram','twitter','whatsapp','gmail','google']


#ret_speech invokes mic gets input convert to text and returns
def ret_speech() :
    with sr.Microphone() as src : 
        audio=r.listen(src,timeout=3.0)
        audio_text=''
        try : 
            #recognize_sphinx(): CMU Sphinx - requires installing PocketSphinx-works offline
            audio_text=r.recognize_google(audio)
        except sr.UnknownValueError :
            #if couldn't recognize audio
            text_speech('sorry please repeat?')
            audio_text=ret_speech()
            #text_speech("Sorry I couldn't get that mic off")
            
             #change button state function to off
        except sr.RequestError : #if google didnt respond
            text_speech("Either you are not connected or Service is currently down ")
        except sr.WaitTimeoutError : 
            audio_text=ret_speech()
            #text_speech('Timeout try again')
        return audio_text 
    
#fn to convert text to speech    
def text_speech(tex) : 
    tts=gTTS(text=tex,lang='en')
    r=random.randint(1,100000)
    audio_file='audio-'+str(r)+'.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    os.remove(audio_file)
    ass_text.insert(END,'\n'+'ISRA -'+tex)
    
#tells what it can do(to be added at last)    
def social_log(action,soc_media) :
    topost=''
    

            
    if soc_media=='facebook' :
        if action==2 : 
            text_speech('Do you want to post only text? answer in yes or no')
            ass_text.insert(END,'\n'+'say(yes/no)')
            ans=ret_speech()
            ass_text.insert(END,'\n'+ans)
            if ans=='yes' : 
                text_speech('what you want to post?')
                topost=ret_speech()
                ass_text.insert(END,'\n'+'TEXT TO POST-'+'"'+topost+'"')
                
                text_speech('Do you want to post the text displayed? answer in yes or no')
                ass_text.insert(END,'\n'+'say (yes/no)')
                ans=''
                ans=ret_speech()
                ass_text.insert(END,'\n'+ans)
                if ans=='no' : 
                         
                      
                         text_speech('would you like to say it again?')
                         ans2=ret_speech()
                        
                         if ans2=='yes' : 
                             text_speech('what you want to post?')

                             topost=ret_speech()
                             ass_text.insert(END,'\n'+'TEXT TO POST-'+'"'+topost+'"')
                             text_speech('Do you want to post the text displayed? answer in yes or no')
                             ass_text.insert(END,'\n'+'say (yes/no)')
                             ans2=ret_speech()
                             ass_text.insert(END,'\n'+'yes')

    
            else : 
                text_speech('Do you want to post image? answer in yes or no')
                ans=ret_speech()
                #complete this
                
                    #caption           
        text_speech('loging in to face book')
        driver=webdriver.Chrome()
        driver.get('https://facebook.com/login/')
        userid_fb='##enter user id here'
        soc_media=''
        emailelement=driver.find_element(By.XPATH,'.//*[@id="email"]')
        emailelement.send_keys(userid_fb)
        passelement=driver.find_element(By.XPATH,'.//*[@id="pass"]')
        passelement.send_keys('##enter pwd here')
        signin=driver.find_element_by_id("loginbutton")
        signin.click()
        time.sleep(3)
        driver.find_element_by_css_selector('div._3ixn').click()
        home_button=driver.find_element(By.XPATH,'//*[@id="u_0_c"]/a')
        home_button.click()
        time.sleep(3)
        try:
            driver.find_element_by_css_selector('div._3ixn').click()
        except:
            pass    
        time.sleep(2)
        if action==1 : 
            pass#sending message on facebook also include broadcast
        elif action==2 : 
            statuselem=driver.find_element_by_tag_name('textarea')
            statuselem.click()
            
           
            statuselem.send_keys(topost)
            time.sleep(10)
            try:
                driver.find_elements_by_css_selector('button')[2].click()
                time.sleep(5)
                
            except:
                time.sleep(5)    
                driver.close()
    elif soc_media=='instagram' : 
        driver=webdriver.Chrome()
        driver.get('https://www.instagram.com/accounts/login/')
        userid_insta='##enter userid'
        time.sleep(1)
        emailelement=driver.find_element_by_name('username')
        
        emailelement.send_keys(userid_insta)
        passelement=driver.find_element(By.XPATH,'.//*[@id="loginForm"]/div/div[2]/div/label/input')
        passelement.send_keys('##enter pwd')
        time.sleep(1)
        signin=driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]/button/div')
        signin.click()
            
        time.sleep(3)
        
        try:
            home=driver.find_element_by_css_selector('svg._8-yf5 ')#(By.XPATH,'//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[1]/div/a/svg')
            home.click()
            time.sleep(2)
        except:
            pass    
        
        try:
            driver.find_element(By.XPATH,'/html/body/div[4]/div/div/div/div[3]/button[2]').click()
           
            
        except:
            pass    
        time.sleep(2)
        
        
        
def email_send() : 
    pass
#fn to do task as required    
def respond(audio_data) :
    got=0
    audio_data=audio_data.lower()
    audio_data1=audio_data.split(' ')
    if audio_data1[0]=='exit' : 
        text_speech('Bye! have a nice day !')
        l[0]=0
        return 0
    elif audio_data1[0]=='what' :
        if audio_data[5:]=='can you do' or audio_data[5:]=='you do' : 
            text_speech('I can, automate your browser, and handle your social media accounts')
        elif audio_data1[1]=='is' :
            if audio_data1[2]=='your':
                if audio_data1[3]=='name' :
                    text_speech('My name is israa')
            elif audio_data[8:]=='the time' or audio_data[8:12]=='time' :
                text_speech(time.strftime("%H:%M:%S",time.localtime()))
    elif audio_data1[0]=='login' :
        if audio_data1[1]=='to' and (audio_data1[2] in social_media) :
            social_log(0,audio_data1[2])
            return 0
            if audio_data1[2]=='my' and (audio_data1[3] in social_media) :
                social_log(0,audio_data1[3])  
                return 0
        elif (audio_data1[1] in social_media) :    
            social_log(0,audio_data1[1])
            return 0
    elif audio_data1[0]=='send' :
        
        if audio_data1[1]=='email'  :
            
            if audio_data1[2]=='to'  :
                conf=1
                tri=0
                
                while(conf or tri>2) :
                    tri+=1
                    text_speech('would you like to use speech to text for message? confirm by saying yes or no')
                    try :
                        ans=ret_speech()
                        if ans=='yes' : 
                            conf=0
                            emailsend(1)
                            
                        elif ans=='no' :
                            emailsend(0)
                            
                            conf=1
                    except :
                        text_speech('cancelling')
                        return 0
                    if conf==1 : 
                        text_speech('sorry something went wrong')
        elif audio_data1[2]=='email'  :
            
            if audio_data1[3]=='to'  :
                conf=1
                tri=0
                
                while(conf or tri>2) :
                    tri+=1
                    text_speech('would you like to use speech to text for message? confirm by saying yes or no')
                    try :
                        ans=ret_speech()
                        if ans=='yes' : 
                            conf=0
                            emailsend(1)
                        elif ans=='no' :
                            emailsend(0)
                            
                            conf=1
                    except :
                        text_speech('cancelling')
                        return 0
                    if conf==1 : 
                        text_speech('sorry something went wrong')  
        elif 'message' in audio_data or 'a message' in audio_data  : 
            for item in social_media : 
                if item in audio_data : 
                    social_log(1,item)#1 means login and send message
                    return 0
                    
    elif audio_data1[0]=='post' : 
        for item in social_media : 
                if item in audio_data : 
                    social_log(2,item)#2 means login and post 
                    return 0
    elif audio_data1[0]=='tell' : 
        if 'about yourself' in audio_data : 
            text_speech('I am israa developed by team Py')
        elif 'time' in audio_data : 
            text_speech((time.strftime("%H:%M:%S",time.localtime())))
    elif audio_data1[0]=='search':         
        if audio_data1[1]=='web' or audio_data1[1]=='internet' :
            if len(audio_data1)==2 :
                try :
                    webbrowser.open_new_tab('https://www.google.co.in/search?q=')
                    return 0
                except : 
                    text_speech('cannot find a browser')
            elif audio_data1[2]== 'for' : 
                try :
                    text_speech('Searching, Web')
                    webbrowser.open_new_tab('https://www.google.co.in/search?q='+audio_data1[3])
                    return 0                 
                except : 
                    text_speech('cannot find a browser')
        elif 'internet for' in audio_data or 'web for' in audio_data: 
            tmp=audio_data.find(' for ')
        
            url='https://www.google.co.in/search?q='+audio_data[(tmp+4):]
            try :
                    text_speech('Searching, Web')
                    webbrowser.open_new_tab(url)
                    return 0
                
            except : 
                    text_speech('cannot find a browser')
    else : 
       
           url='https://www.google.co.in/search?q='+audio_data
           
        
           try :
                webbrowser.open_new_tab(url)
            
           except : 
                text_speech('cannot find a browser')
           return 0
       
    return 1   
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
def signinw():
        lgin = Tk()
        lgin.title('ISRA')
        #root.iconbitmap('C:\ISRA\ISRA LOGO.ico')
        lgin.geometry('350x350')
        lgin.resizable(height = False, width=False)
        
        #first time window
        misc = Label(lgin, text='Login Here!')
        misc.configure(font=("Verdana",20))
        misc.place(relx=0.5, rely=0.1, anchor=CENTER)
        
        un = Label(lgin, text='Username')
        un.configure(font=("Verdana",10))
        un.place(relx=0.5, rely=0.24, anchor=CENTER)
        
        username_var = StringVar()
        
        username_entry = Entry(lgin, textvariable = username_var)
        username_entry.config(width = 35)
        username_entry.place(relx=0.5,rely=0.3,anchor=CENTER)
        
        pw = Label(lgin, text='Password')
        pw.configure(font=("Verdana",10))
        pw.place(relx=0.5, rely=0.4, anchor=CENTER)
        
        password_var = StringVar()
        
        password_entry = Entry(lgin, textvariable = password_var,show="*")
        password_entry.config(width = 35)
        password_entry.place(relx=0.5,rely=0.46,anchor=CENTER)
        
        style = Style()
        style.configure('TButton', font =('Verdana', 10, "bold"))
        login_button = Button(lgin, text='Login', style='TButton', command = lambda : askyesno('Confirmation','Do you want to log in?'))
        
        login_button.place(relx=0.5, rely=0.57, anchor = CENTER)
        login_button.config( width = 15)
        
        signup = Label(lgin, text='New User?')
        signup.configure(font=("Verdana",9))
        signup.place(relx=0.4, rely=0.8, anchor=CENTER)
        
        style.configure('su.TButton', font =('Verdana', 8, "bold"))
        
        signup_button = Button(lgin, text='Sign Up', style='su.TButton')
        signup_button.place(relx=0.6, rely=0.8, anchor = CENTER)
        signup_button.config( width = 7)
        
        
        
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
        try :
            audio_data=ret_speech()
        except : 
            try:
                audio_data=ret_speech()
            except:
                continue
        if l[0]==0 : 
            break
        ass_text.insert(END,'\n'+audio_data)#create update user text widget fn
        try :
            l[0]=respond(audio_data)
        except:
            text_speech('something went wrong')
            l[0]=0
                
        if l[0]==0 : 
            mic_button.configure(image=_offmic)
    
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
options.add_command(label = 'Sign in',command=signinw)
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