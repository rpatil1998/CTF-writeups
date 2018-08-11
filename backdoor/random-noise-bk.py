from PIL import Image
im = Image.open('solved.bmp')

pixels = list(im.getdata())
width, height = im.size
string=''
pixels = [pixels[i * width:(i + 1) * width] for i in xrange(height)]
get=pixels[0]
print(get[0])
for i in range(0,799):
	if(get[i]==(0, 0, 0)):
		string=string+'0'
	else:
		string=string+'1'
print(string)
#then i coverted the output binary into ascii using online tools and got the key.		