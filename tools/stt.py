import speech_recognition as sr

class SpeechToText:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def transcribe(self, audio_path):
        with sr.AudioFile(audio_path) as source:
            audio = self.recognizer.record(source)
        return self.recognizer.recognize_google(audio)