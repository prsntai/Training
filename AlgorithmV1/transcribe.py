import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()

def record_text():
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=0.2)
            audio = r.listen(source)
            text = r.recognize_google(audio)

            return text
    except:
        return ''

if __name__ == "__main__":
    text = ''
    while text.lower() != 'stop':
        text = record_text()
        print(text)
