# -*- coding: utf-8 -*-

from urllib.request import urlopen
import os
import img2pdf

i=0

os.mkdir("ImgTemp")

'''link preparation '''
link = input("Give link:\n")
if link.startswith("http://"):
	link = link[7:]

if link.endswith("/"):
    link = link[:-1] 

if link.startswith("static."):
	print("Sorry, this type is not implemented. Try some other book :( ")
elif not link.startswith("online."):
	link = "online." + link
link ="http://" + link + "/files/large/"

pagenu = input("Give number of pages:\n")

'''image downloading'''
for bpage in range(1,int(pagenu)+1):
	line = link+str(bpage)+".jpg"
	print("Downloading " + line)
	try: 
		res = urlopen(line)
		imgData = res.read()
		with open("ImgTemp/" + str(i) + ".jpg",'wb') as output:
			output.write(imgData)
	except:
		print("Exception")
		print(i)
	i=i+1

print('completed downloading')

'''pdf creation'''
os.chdir('ImgTemp')

with open("../output.pdf", "wb") as f:
	dList = os.listdir(os.getcwd())
	dList.sort(key=lambda e: int(e.split(".")[0]))
	f.write(img2pdf.convert([i for i in dList if i.endswith(".jpg")]))

for f in os.listdir(os.getcwd()):
	os.remove(f)

os.chdir('../')
os.rmdir("ImgTemp")
