url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRTpHlpkv4QFjYk81TpM_Gk4nQF3lu63QYD6qV6-0uKqDF3OrmrrUAkywLy'
 
#### using urlretrieve ####
 
import urllib
urllib.urlretrieve(url, "pic2"+".jpg")
 
### using pillow ###
 
from urllib import urlopen
from PIL import Image
import cStringIO
 
imgdata = urlopen(url).read()
img = Image.open(cStringIO.StringIO(imgdata))
img.save("pic1"+".png")