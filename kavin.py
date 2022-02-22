import tkinter as tk
from tkinter import *
import wikipedia
import speech_recognition as sr
import wolframalpha

class karl( Frame ):
    def __init__( self ):
        tk.Frame.__init__(self)
        self.pack()
        self.master.title("WIKI BOT")
     #   self.photo = PhotoImage(file = r"E:\wi.png")
     

        self.button1 = Button( self, text = "VOICE", width = 25,fg="red",
                               command = self.new_window )
        self.button1.grid( row = 0, column = 1, columnspan = 2)
        self.button2 = Button( self, text = "TEXT", width = 25, fg="red",
                               command = self.text_window )
        self.button2.grid( row = 1, column = 0, columnspan = 2)
    def new_window(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("hi say something")
            audio = r.listen(source)
            r.adjust_for_ambient_noise(source)
            print("text:" +r.recognize_google(audio))
            try:
                #wolframalpha
                app_id = "TE4XTA-9UQ7W89U3R"
                client = wolframalpha.Client(app_id)
                res = client.query(r.recognize_google(audio))
                answer = next(res.results).text
                print (answer)
               
            except:
                #wikipedia
                print(wikipedia.summary(r.recognize_google(audio),sentences=2))
    def text_window(self):
        try:
            #wolframalpha
            print("ask me something:")
            q=input("Q:")
            app_id = "TE4XTA-9UQ7W89U3R"
            client = wolframalpha.Client(app_id)
            res = client.query(q)
            answer = next(res.results).text
            print (answer)
               
        except:
            #wikipedia
                   
            print (wikipedia.summary(q,sentences=2))
           
         
       
       
       
def main():
    karl().mainloop()
if __name__ == '__main__':
    main()