import speech_recognition  as sr


r = sr.Recognizer()
with sr.Microphone() as source:
    print("say something")
    audio = r.listen(source)
text = r.recognize_google(audio)
try:
   print("You said: {}",format(text))

except:
   print("Sorry I couldn't understand you")


