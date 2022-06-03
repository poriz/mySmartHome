import RPi.GPIO as GPIO
import TextToSpeech
import time
import picamera
GPIO.setwarnings(False)

class movement:
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        self.LED = 11
        self.survo= 12
        self.str =""
        GPIO.setup([self.LED,self.survo],GPIO.OUT)
        self.p=GPIO.PWM(self.survo,50)
        self.p.start(0)
    def LampOn(self):
        GPIO.output(self.LED,True)
        #GPIO.cleanup()
        self.str ="Lamp on!"
        TextToSpeech.ttSpeech(self.str)
        
    def LampOff(self):
        GPIO.output(self.LED,GPIO.LOW)
        #GPIO.cleanup()
        self.str ="Lamp off!"
        TextToSpeech.ttSpeech(self.str)
        
    def TakePicture(self):
        with picamera.PiCamera() as camera:
            camera.resolution=(640,480)
            filename=input(time.localtime())
            camera.capture(filename+'.jpg')
            GPIO.cleanup()
        self.str ="Cheese!"
        TextToSpeech.ttSpeech(self.str)
        
    def DoorOpen(self): #6.5 open
        self.p.ChangeDutyCycle(6.5)
        #self.p.stop()
        self.str ="Door open"
        TextToSpeech.ttSpeech(self.str)
        #GPIO.cleanup()
    def DoorClose(self): #2.5 closed
        self.p.ChangeDutyCycle(2.5)
        #self.p.stop()
        self.str ="Door closed!"
        TextToSpeech.ttSpeech(self.str)
        #GPIO.cleanup()
    def clear(self):
        GPIO.cleanup()
