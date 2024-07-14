import gtts
# import os

audio1 = gtts.gTTS(text = "Console Clearing On", lang = "en", slow = False)
audio1.save("consoleclearing.mp3")

audio2 = gtts.gTTS(text = "Coloured Drops On", lang = "en", slow = False)
audio2.save("coloureddrops.mp3")