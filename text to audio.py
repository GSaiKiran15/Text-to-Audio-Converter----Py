from gtts import gTTS
from playsound import playsound

audio = 'speech.mp3'
language = 'en'
text = str(input("Enter the text which is to be converted as audio : "))
sp = gTTS(text=text, lang=language, slow=False)
sp.save(audio)
playsound(audio)
