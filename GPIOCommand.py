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
        self.str ="Lamp on!"
        TextToSpeech.ttSpeech(self.str)
        
    def LampOff(self):
        GPIO.output(self.LED,GPIO.LOW)
        self.str ="Lamp off!"
        TextToSpeech.ttSpeech(self.str)
        
    def TakePicture(self):
        with picamera.PiCamera() as camera:
            camera.resolution=(640,480)
            filename=time.strftime("%Y%m%d%H%M%S",time.localtime())
            camera.capture("./%s.jpg"%filename)
            GPIO.cleanup()
        self.str ="Cheese!"
        TextToSpeech.ttSpeech(self.str)
        
    def DoorOpen(self): #6.5 open
        self.p.ChangeDutyCycle(6.5)
        self.str ="Door open"
        TextToSpeech.ttSpeech(self.str)
    def DoorClose(self): #2.5 closed
        self.p.ChangeDutyCycle(2.5)
        self.str ="Door closed!"
        TextToSpeech.ttSpeech(self.str)
    def clear(self):
        GPIO.cleanup()
