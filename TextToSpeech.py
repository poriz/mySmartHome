from gtts import gTTS
import pygame

class ttSpeech:
    def __init__(self,text1):
        self.tts=gTTS(text=text1,lang='en')
        self.tts.save('returnVoice.mp3')
        pygame.mixer.init()
        pygame.mixer.music.load('./returnVoice.mp3')
        pygame.mixer.music.play()


