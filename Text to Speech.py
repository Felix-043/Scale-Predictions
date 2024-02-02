import pyttsx3

# initialize pyttsx3
bot = pyttsx3.init()

# Passing input text string
bot.say("Hello Mercy!")

# run and wait method, will play the audio
bot.runAndWait()