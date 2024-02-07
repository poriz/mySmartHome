import speech_recognition as sr
import TextToSpeech

class SpeechToText1:
    def __init__(self):
        self.r = sr.Recognizer()
        with sr.Microphone() as source:
            self.audio = self.r.listen(source)
        
    def return1(self):
        try:
            return self.r.recognize_google(self.audio)
        except sr.UnknownValueError:
            TextToSpeech.ttSpeech("can't understand")
            return ("can't understand")
        except sr.RequestError as e:
            TextToSpeech.ttSpeech("RequestError, please say again")
            return ("RequestError: {0}".format(e))