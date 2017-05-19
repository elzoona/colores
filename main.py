import loadaudio

print ("lalal")

audio = loadaudio.LoadSound('sounds/colores/*.wav').create_list()




for item in audio:
    print item
