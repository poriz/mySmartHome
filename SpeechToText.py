import speech_recognition as sr

class SpeechToText1:
    def __init__(self):
        self.r = sr.Recognizer()
        with sr.Microphone() as source:
            self.audio = self.r.listen(source)
        
    def return1(self):
        try:
            return self.r.recognize_google(self.audio)
        except sr.UnknownValueError:
            return ("can't understand")
        except sr.RequestError as e:
            return ("RequestError: {0}".format(e))