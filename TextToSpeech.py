from gtts import gTTS
import pygame

class TextToSpeech:
    def __init__(text):
        tts=gTTS(text=text,lang='en')
        tts.save('returnVoice.mp3')
        
    def Play(self):
        pygame.mixer.init()
        pygame.mixer.music.load('/home/pi/final_project/test.mp3')
        pygame.mixer.music.play()


