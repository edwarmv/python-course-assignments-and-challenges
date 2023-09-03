from PIL import Image

mac = Image.open('example.jpg')

# mac.crop((0, 0, 100, 100)).show()

pencils = Image.open('pencils.jpg')

pencils_w = 1950
pencils_h = 1300

x = 0
y = 0

w = int(pencils_w / 3)
h = int(pencils_h / 10)

# pencils.crop((x,y,w,h)).show()


