#!/usr/bin/env python
#Version: 10/6/2016

from Tkinter import *
from move_robot import move

master = Tk()
lin = 0
ang = 0
move_type = ""
running = True
count = 0
def scan():
	global lin, ang, move_type, running, count
	if (move_type != "wiggle"):
		if (running and not count > 3000):
			move(lin,ang,move_type)
			count += 1
	elif (move_type == "wiggle"):
		if (running and not count > 600):
			if (count <= 200):
				move(0,-40,move_type)
				count += 1
			else:
				move(0,40,move_type)
				count += 1

	master.after(1, scan)

def forward():
	global lin, ang, move_type, running, count
	lin = 1
	ang = 0
	move_type = "move"
	running = True
	count = 0

def backward():
	global lin, ang, move_type, running, count
	lin = -1
	ang = 0
	move_type = "move"
	running = True
	count = 0

def right():
	global lin, ang, move_type, running, count
	lin = 0
	ang = -40
	move_type = "move"
	running = True
	count = 0

def left():
	global lin, ang, move_type, running, count
	lin = 0
	ang = 40
	move_type = "move"
	running = True
	count = 0

def stop():
	global lin, ang, move_type, running, count
	lin = 0
	ang = 0
	move_type = "stop"
	running = False
	count = 0

def spin():
	global lin, ang, move_type, running, count
	lin = 0.1
	ang = 75
	move_type = "spin"
	running = True
	count = 0

def wiggle():
	global lin, ang, move_type, running, count
	lin = 0
	ang = 20
	move_type = "wiggle"
	running = True
	count = 0


Label(master, text="BASIC MOVES").grid(row=0, column=0)
Label(master, text="NOT AS BASIC").grid(row=0, column=1)

forward_butt = Button(master, text="forward", command=forward, width=8)
backward_butt = Button(master, text="backward", command=backward, width=8)
right_butt = Button(master, text="right", command=right, width=8)
left_butt = Button(master, text="left", command=left, width=8)
stop_butt = Button(master, text="stop", command=stop, width=8)
spin_butt = Button(master, text="spin", command=spin, width=8)
wiggle_butt = Button(master, text="wiggle", command=wiggle, width=8)


forward_butt.grid(row=1, column=0)
backward_butt.grid(row=2,column=0)
right_butt.grid(row=3,column=0)
left_butt.grid(row=4,column=0)
stop_butt.grid(row=5,column=0)
spin_butt.grid(row=1, column=1)
wiggle_butt.grid(row=2, column=1)


master.after(1, scan)
master.mainloop()
