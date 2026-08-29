from gtts import gTTS

text=input("enter the text :")
tts=gTTS(text=text,lang='en')
tts.save("audio.mp3")
print("audio saved!")
