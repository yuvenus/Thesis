from Tkinter import *
from face import change_face

master = Tk()

def default():
	change_face("reg")
	print "default"

def smile():
	change_face("smile")
	print "smile"

def frown():
	change_face("frown")
	print "frown"

def surprise():
	change_face("surprise")
	print "surprised"

def disgust():
	change_face("disgust")
	print "disgusted"

def greet():
	change_face("greet")
	print "greetings!"

def help():
	change_face("help")
	print "help!"

def happy():
	change_face("happy")
	print "happy!"

def sad():
	change_face("sad")
	print "sad..."

def inp(*args):
	text = e.get()
	change_face(text)
	e.delete(0, END)

master.bind('<Return>', inp)

Label(master, text="FACE EXP").grid(row=0, column=0)
Label(master, text="DIALOGUE").grid(row=0, column=1)
Label(master, text="INPUT").grid(row=0, column=2)

default_butt = Button(compound=LEFT, text="default", command=default, width=8)
smile_butt = Button(compound=LEFT, text="smile", command=smile, width=8)
frown_butt = Button(compound=LEFT, text="frown", command=frown, width=8)
surprise_butt = Button(compound=LEFT, text="surprised", command=surprise, width=8)
disgust_butt = Button(compound=LEFT, text="disgusted", command=disgust, width=8)

greet_butt = Button(master, text="greetings", command=greet, width=8)
help_butt = Button(master, text="help me", command=help, width=8)
happy_butt = Button(master, text="helped", command=happy, width=8)
sad_butt = Button(master, text="!helped", command=sad, width=8)

#input_butt = Button(master, text="say", command=inp, width=8)

e = Entry(master)
e.grid(row=1, column=2)
e.focus_set()

default_butt.grid(row=1, column=0)
smile_butt.grid(row=2, column=0)
frown_butt.grid(row=3, column=0)
surprise_butt.grid(row=4, column=0)
disgust_butt.grid(row=5, column=0)

greet_butt.grid(row=1,column=1)
help_butt.grid(row=2,column=1)
happy_butt.grid(row=3,column=1)
sad_butt.grid(row=4,column=1)

#input_butt.grid(row=2,column=2)


mainloop()
