from gtts import gTTS
text = "hello everyone welcome to my page"

tts = gTTS (text=text, lang="en")

tts.save("voice.mp3")

print("audio saved succesfully")