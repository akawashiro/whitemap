import sys
from PIL import Image

if __name__ == '__main__':
    inp = sys.stdin.readlines()
    xs = list()
    ys = list()
    for i in inp:
        s=i[0:-1].split(",")
        if len(s)==3:
            xs.append(float(s[0]))
            ys.append(float(s[1]))
    mx = min(xs)
    my = min(ys)
    xs = map(lambda x:x-mx,xs)
    ys = map(lambda x:x-my,ys)
    mx = max(xs)
    my = max(ys)
    width = 1000
    height = width/mx*my
    xs = map(lambda x:x*width/mx, xs)
    ys = map(lambda y:y*height/my,ys)
    height = int(height)

    img = Image.new('RGB',(width+10,height+10),(255,255,255))
    for i in range(0,len(xs)):
        img.putpixel((int(xs[i]),height-int(ys[i])+5),(0,0,0))
    img.save("whitemap.png")
