import sys
from PIL import Image
im=Image.open(sys.argv[1])
pix=im.load()
rgb_im = im.convert('RGBA')

block = int(sys.argv[2])

x=int(im.size[0]/block)
y=int(im.size[1]/block)

dim=[x,y]

p=[]
for i in range(x):
    for j in range(y):
        if not rgb_im.getpixel((i*block+block/2,j*block+block/2)) in p:
            p.append(rgb_im.getpixel((i*block+block/2,j*block+block/2)))

colordata=[]
for m in p:
    colordata.append([float(m[0])/255,float(m[1])/255,float(m[2])/255,float(m[3])/255])



'''
for m in p:
    print("UIColor(red:"+str(float(m[0])/255)+",green:"+str(float(m[1])/255)+",blue:"+str(float(m[2])/255)+",alpha:"+str(float(m[3])/255)+"),")
'''


pixeldata=[]
for j in range(y):
    l=[]
    for i in range(x):
        l.append(p.index(rgb_im.getpixel((i*block+block/2,j*block+block/2))))
    pixeldata.append(l)

data={}
data["dim"] = dim
data["colordata"] = colordata
data["pixeldata"] = pixeldata

import json

text_file = open(sys.argv[1]+".json", "w")
text_file.write(json.dumps(data))
text_file.close()





'''
ix=im.crop((0,3,im.size[0]-6,im.size[1]))
#ix.show()
ix.save("image2.png")
a=()
t=0
for x in range(ix.size[1]):
    if not pix[99,x]==a:
        a=pix[99,x]
        print(t)
        t=1
    else:
        t+=1
print(type(im))
print(t)
'''
