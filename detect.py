from pyfann import libfann
from PIL import Image

ann = libfann.neural_net()
ann.create_from_file('fann.data')
imdir="detect_images"
files = ["1.png"]
im = Image.open(imdir+"/"+files[0], 'r')
pix = list(im.getdata(0))
res = ann.run(pix)
print res
if res[0]>0.7:
    print "Train!"
else:
    print "Road clear"