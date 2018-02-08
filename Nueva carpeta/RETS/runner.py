"""
Reglas de conversion
Notas: G A B C D E F#
		 S1   S2   S3	
	S -> gN | aN | bN
	N -> gG | aA | bB | cC | dD | eE | fF
	G -> gG | aA | bB
	A -> aA | gG | bB | cC
	B -> bB | gG | aA | cC | dD
	C -> cC | aA | bB | dD | eE
	D -> dD | bB | cC | eE | fF
	E -> eE | cC | dD | fF 
	F -> fF | dD | eE 

	------------------------------------
	G -> G | B | D 
	A -> C | A | E | F#
	B -> B | G | D | E | F#
	C -> C | G | B | E
	D -> G | A | D | F#
	E -> G | B | C | E
	F# -> G | A | B | D | F#     
"""
import winsound
import random
import turtle
import time
from tkinter import *
master = Tk()
Label(master, text="# of notes").grid(row=0)
Label(master, text="Color Hue").grid(row=1)
Label(master, text="Input file name (with .txt)").grid(row=2)
Label(master, text="Note duration (in seconds)").grid(row=3)
Label(master, text="Stroke angle").grid(row=4)
Label(master, text="Stroke spread").grid(row=5)
Savefile = IntVar()
c = Checkbutton(master, text="Save File?", variable= Savefile).grid(row=6, sticky=W)

e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)
e4 = Entry(master)
e5 = Entry(master)
e6 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)
e5.grid(row=4, column=1)
e6.grid(row=5, column=1)

e1.insert(0,"100")
e2.insert(0,"1")
e3.insert(0,"rules.txt")
e4.insert(0,".2")
e5.insert(0,"70.0")
e6.insert(0,"150")
Button(master, text='Start', command=master.quit).grid(row=7, column=0, sticky=W, pady=4)

master.mainloop()
"""
print(e1.get())
print(e2.get())
print(e3.get())
print(e4.get())
print(e5.get())
print(e6.get())
"""
Alfa = Savefile.get()
Save = False
if Alfa ==1:
	Save = True
random.seed()
file = open(e3.get(), "r")
imprimir = file.read()
GScale = {}
count = 0
ArrStr = []
str0 = ""
"""este for es para sacar los renglones"""
while count<len(imprimir):
    if imprimir[count]== '\n':
        ArrStr.append(str0)
        str0 = ""
    else:
        str0 = str0+imprimir[count]
    count = count +1
loop = 0
while loop<len(ArrStr):
	row = ArrStr[loop].split("=")
	key = row[0] 
	row.pop(0)
	x = 0
	Provitional = []
	row = "".join(row).split("|")
	while x < len(row):
		Provitional.append(row[x])
		x = x+1
	loop = loop + 1
	GScale[key]=Provitional
print(GScale)
"""
GScale = {
		('S1',) : 'gN',
		('S2',) : 'aN',
		('S3',) : 'bN',
		('N1','G1','B2','C2','D1','E1','F1') : 'gG',
		('N2','A1','D2','F2') : 'aA',

		('N3','G2','B1','C3','E2','F3') : 'bB',
		('N4','A2','C1','D3','E3') : 'cC',
		('N5','G3','B3','F2','D3','F4') : 'dD',
		('N6','A3','B4','C4','E4') : 'eE',
		('N7','A4','B5','D4','F5') : 'fF'
	}
"""

"""
GScale = {
		('S1',) : 'gN',
		('S2',) : 'aN',
		('S3',) : 'bN',
		('N1','G1','A2','B2') : 'gG',
		('N2','G2','A1','B3','C2') : 'aA',

		('N3','G3','A3','B1','C3','D2') : 'bB',
		('N4','A4','B4','C1','D3','E2') : 'cC',
		('N5','B5','C4','D1','E3','F2') : 'dD',
		('N6','C5','D4','E1','F3') : 'eE',
		('N7','D5','E4','F1') : 'fF'
	}
"""
Title1 = {
		'1' : 'Symphony',
		'2' : 'Song',
		'3' : 'Requiem',
		'4' : 'Toccata',
		'5' : 'Sonata',
		'6' : 'Serenade',
		'7' : 'Loud Banging',
		'8' : 'Horrible sounds',
		'9' : 'Opera',
		'10' : 'Soundtrack'	
}
Title2 = {
		'1' : 'for',
		'2' : 'from',
		'3' : 'by',
		'4' : 'to',
		'5' : 'originally intented to be',
		'6' : 'imitating',
		'7' : 'surpasing',
		'8' : 'to kill',
		'9' : 'not really for'
}	
Title3 = {
		'1' : 'Mozart',
		'2' : 'Ivan',
		'3' : 'Chino',
		'4' : 'Heaven',
		'5' : 'Soup',
		'6' : 'a really big sausage',
		'7' : 'a sloppy bar of soap',
		'8' : 'broccoli',
		'9' : 'Manu',
		'10' : 'shoes',
		'11' : 'child youtubers',
		'12' : 'boogers',
		'13' : 'scare away the pain',
		'14' : 'meeting',
		'15' : 'elevator music',
		'16' : 'old people',
		'17' : 'dictatorship',
		'18' : 'playing with yourself',
		'19' : 'anarchy',
		'20' : 'Manus Beard',
		'21' : 'Patys friends',
		'22' : 'Majo',
		'23' : 'Doña Pancha and her friend doña Pelos',
		'24' : 'Samy',
		'25' : 'Mr. Felipe'
}
def getNote(s):
	notes = GScale[s]
	return notes[random.randint(0,(len(notes)-1))]
def buildGScale(notes):
	song = "S"
	pick = 0
	x = 0
	loop = True
	while loop:
		x += 1
		if(x == notes):
			loop = False
		key = ""
		if(song[len(song) -2 ] == '#'):
			key = song[len(song) -3] + song[len(song) -2]
		else:
			key = song[len(song) -2]
		song = song.replace(key,"")
		song = song + getNote(key) + ","
	if(song[len(song)-2] == '#'):
		song = song[:len(song)-3]
	else:
		song = song[:len(song)-2]
	return song
def getSongTitle(s):
	song = s
	value = 0
	x = 0
	while True:
		if(x >= len(song)):
			break
		value = value + ord(song[x]) 
		x = x+1 
	title = Title1[str((value % 10) + 1)] + " " + Title2[str((value % 9) + 1)] + " "+ Title3[str((value % 25) + 1)]
	return title
def stringToColor(s):
	value = 0
	color = []
	x = 0
	loop = True
	while loop:
		if(x >= len(s)-1):
			loop = False
		value = value + ord(s[x]) 
		x = x+1
	value = value * int(float(e2.get()))
	color1 = value % 255
	color.append(color1)
	color1 = (color1 * value) % 255
	color.append(color1)
	color1 = (color1 * value) % 255
	color.append(color1)
	return color
def stringToSound(s):
	x = 0
	loop = True
	angle = float(e5.get())
	tur = turtle.Turtle()
	screen = turtle.Screen()
	title = getSongTitle(s)
	screen.title("Versión 0.1 " + title)
	turtle.colormode(255)
	tur.width(3)
	tur.speed(25)
	song = s.split(",")
	duration = float(e4.get())
	distanceUser = float(e6.get())
	while loop:
		if x >= len(song) -1:
			loop = False
		pause = duration
		distance = distanceUser
		winsound.PlaySound(song[x] + ".wav",winsound.SND_ASYNC)
		color = stringToColor(song[x])
		tur.pencolor(color[0],color[1],color[2])
		tur.right(angle)
		while True:
			if x == len(song) - 1:
				distance = distanceUser * 5
				pause = 5
				break
			if song[x + 1] != song[x]:
				break
			pause += duration
			distance += distanceUser
			x += 1
		x += 1
		tur.forward(distance)
		time.sleep(pause)
	print("Song ended")
	if(Save):
		cv = turtle.getcanvas()
		cv.postscript(file=title + ".ps", colormode='color')
finalSong = buildGScale(int(float(e1.get())))
print(finalSong)
stringToSound(finalSong)