import speech_recognition as sr

r=sr.Recognizer()

with sr.AudioFile("dictée.wav") as source:
    audio = r.record(source)
    audio = r.listen(source)

    
text = r.recognize_google(audio)
for i in text:
    print(i)

