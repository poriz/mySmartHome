import RPi.GPIO as GPIO
import TextToSpeech
import time
class movement:
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        self.LED = 11
        GPIO.setup(self.LED,GPIO.OUT,initial=GPIO.LOW)
        self.str =""
    def LampOn(self):
        GPIO.output(self.LED,True)
        #GPIO.cleanup()
        self.str ="Lamp on!"
        TextToSpeech.ttSpeech(self.str)
    def LampOff(self):
        GPIO.output(self.LED,GPIO.LOW)
        GPIO.cleanup()
        self.str ="Lamp off!"
        TextToSpeech.ttSpeech(self.str)
    #def TakePicture(self):
        
    #def DoorOpen(self):
    
    
    #def DoorClose(self):
    
    def clear(self):
        GPIO.cleanup()
    
    

    
