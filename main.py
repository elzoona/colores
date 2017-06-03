import loadassets

print ("lalal")

audio = loadassets.LoadSound('sounds/colores/*.wav').create_list()

cat = loadassets.LoadSprites('img/colores/*.png').create_list()

for item in cat:
    print item


for item in audio:
    print item
