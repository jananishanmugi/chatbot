from tkinter import *
#import requests
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
import pyttsx3
import speech_recognition
import threading
#from bs4 import BeautifulSoup


bot = ChatBot('Bot')
trainer = ListTrainer(bot)
for files in os.listdir('data/english'):
    data = open('data/english/'+files,'r',encoding='utf-8').readlines()
    trainer.train(data)


def botReply():
    question = questionField.get()
    question = question.capitalize()
    answer = bot.get_response(question)
    textarea.insert(END,'You:'+question+'\n\n')
    textarea.insert(END,'Bot:'+str(answer)+'\n\n')
    pyttsx3.speak(answer)
    questionField.delete(0,END)
def audiotoText():
    while True:
        sr = speech_recognition.Recognizer()
        try:
            with speech_recognition.Microphone() as m:
                sr.adjust_for_ambient_noise(m,duration=1)
                audio = sr.listen(m)
                query = sr.recognize_google(audio)
                questionField.delete(0,END)
                questionField.insert(0,query)
        except  Exception as e:
            print(e)
#def  webscraping(query):
  #  URL = 'https://www.google.com/search?q='+query
   # page = requests.get(URL)
   # soup = BeautifulSoup





root = Tk()
root.geometry('500x570+100+30')
root.title("chatbot")
root.config(bg='#856ff8')
logoPic = PhotoImage(file='rb.png')
logoPicLabel = Label(root,image=logoPic)
logoPicLabel.pack()
centreFrame = Frame(root)
centreFrame.pack()
scrollbar = Scrollbar(centreFrame)
scrollbar.pack(side=RIGHT)
textarea = Text(centreFrame,font=('times new roman',20,'bold'),height=10,yscrollcommand=scrollbar.set,wrap='word')
textarea.pack(side=LEFT)
scrollbar.config(command=textarea.yview)
questionField = Entry(root,font=('verdana',20,'bold'))
questionField.pack(pady=15,fill=X)
askPic=PhotoImage(file='ask.png')
askButton = Button(root,image=askPic,command=botReply)
askButton.pack()
def click(event):
    askButton.invoke()
root.bind('<Return>',click)
thread = threading.Thread(target=audiotoText)
thread.setDaemon(True)
thread.start()
root.mainloop()
