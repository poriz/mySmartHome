import tkinter
import SpeechToText 
import TextToSpeech
import CommandModule
import RPi.GPIO as GPIO

global data
data = ""

root = tkinter.Tk()


def changeOri():
     cc = c.create_oval(50,50,150,150,fill="white")
     label['text']="Press the button and tell me your requirements"
     GPIO.cleanup()
     global data
     data =""
     cmd = CommandModule.Command(data)
     cmd.chooseCommand("clear")
     
     
def changeblue():
    cc = c.create_oval(50,50,150,150,fill="blue")
    label['text']="Complete!"

def click():
    global data
    data1 = SpeechToText.SpeechToText1()
    data = data1.return1()
    cmd = CommandModule.Command(data)
    cmd.chooseCommand(data)
    print(data)
    
    
    
c= tkinter.Canvas(root,width=200,height=200)

button1 = tkinter.Button(root,text='Record',command = lambda:[click(),changeblue()])
clearbutton = tkinter.Button(root,text='clear',command = changeOri)
label = tkinter.Label(root,text='Press the button and tell me your requirements')
cc = c.create_oval(50,50,150,150,fill="")


button1.pack()
clearbutton.pack()
c.pack()
label.pack(side="bottom")

root.mainloop()

