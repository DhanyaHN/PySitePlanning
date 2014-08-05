#file reading
import turtle, tkinter, math
D = {}
dim = []
init_x = 0
init_y = 0
root = {}
d = []
ratio = 0
def read(file_name):
	global D, dim, init_y, init_x, root, d, ratio
	f = open(file_name,"r")
	f = f.readlines() # reading file into a variable
	dim = f[0].split(":")[1] # stores the site dimension
	D = {} # Dictionary containing site plan
	init_x =0
	init_y=0
	# strips next line in all the lines
	for i in range(0,len(f)):
		f[i] = f[i].strip()

	# to create a dictionary of site plan
	for i in range(1,len(f)):
		ratio = 1.6
		global floor
		global rooms
		if f[i].find("-") < 0 and len(f[i]) > 0:# if it is not "--------" and empty line
			if f[i].find(",") < 0: # it is the floor/partition
				if flag == True: # it is a floor
					floor = f[i].strip()
					D[floor] = {}
				else: # it is a room
					rooms = f[i].strip()
					D[floor][rooms] = {}
			else: # it is the dimensions of the room
				f[i].strip()
				l = f[i].split(",")
				for j in l:
					a = j.split(":")
					D[floor][rooms][a[0].strip()] = float(a[1]) * ratio
			flag = False		
		elif len(f[i]) != 0:# if "---------------" is found then next line is the floor
			flag = True	

	#print(D)
	root = {}
	d = dim.split("*")
	d[0] = float(d[0]) * ratio
	d[1] = float(d[1]) * ratio
def check(flag, init_x, init_y, rooms, l):
	global D
	checked = []
	for i in rooms:
		for j in rooms:
			if i != j:
				x1 = (rooms[i]["left"] - init_x, rooms[i]["left"]+rooms[i]["width"] - init_x)
				y1 = (init_y - rooms[i]["top"], init_y - rooms[i]["top"] - rooms[i]["length"])
				x2 = (rooms[j]["left"] - init_x, rooms[j]["left"] + rooms[j]["width"] - init_x)
				y2 = (init_y - rooms[j]["top"],init_y - rooms[j]["top"] - rooms[j]["length"])
				#print(i,": x1,y1",x1,y1)
				#print(j,": x2,y2",x2,y2)
				#print()
				if x1[0] < x1[1]:
					a = x1[0]
					b = x1[1]
				else:
					a = x1[1]
					b = x1[0]
				if y1[0] < y1[1]:
					c = y1[0]
					d = y1[1]
				else:
					c = y1[1]
					d = y1[0]
				x_cor = (a < x2[0] < b) or (a < x2[1] < b)
				y_cor = (c < y2[0] < d) or (c < y2[1] < d)
				if (x_cor and y_cor) or (x_cor and (y1 == y2)) or (y_cor and (x1 == x2)):
					#print(i,j)
					l.append((i,j))
					flag = True
				checked.append((i,j))
	return flag, l
def draw_door(t,door_dim):
	t.setx(door_dim['left'] + door_dim["width"] - init_x)
	t.sety(init_y - door_dim["top"])
	t.right(180)
	t.color("brown")
	t.forward(door_dim["length"]/3)
	t.pendown()
	t.right(90)
	t.forward(door_dim["width"]/4)
	t.left(90)
	t.forward(door_dim["length"]/3)
	t.left(90)
	t.forward(door_dim["width"]/4)
	#t.color("black")

def right_arrow(t, tri):
	t.begin_fill()
	t.right(45)
	t.forward(tri)
	t.right(135)
	t.forward(10)
	t.right(135)
	t.forward(tri)
	t.right(45)
	t.end_fill()
def left_arrow(t,tri):
	t.begin_fill()
	t.forward(tri)
	t.left(135)
	t.forward(10)
	t.left(135)
	t.forward(tri)
	t.right(45)
	t.end_fill()
def up_arrow(t, tri):
	t.begin_fill()
	t.left(45)
	t.forward(tri)
	t.left(135)
	t.forward(10)
	t.left(135)
	t.forward(tri)
	t.left(45)
	t.end_fill()

def down_arrow(t, tri):
	t.begin_fill()
	t.left(135)
	t.forward(tri)
	t.left(135)
	t.forward(10)
	t.left(135)
	t.forward(tri)
	t.right(45)
	t.end_fill()

def back_to_initial_pos(t, dim):
	t.right(90)
	t.forward(10)
	t.backward(20)
	t.right(90)
	t.penup()
	t.forward(dim["length"])
	t.pendown()
	t.pensize(2)
def write_width(t, dim):
	t.right(90)
	t.forward(dim/2)
	t.color("red")
	t.write(str(dim/ratio),align = "center", font = ("Arial", 8, "bold"))
	t.color("blue")
	t.forward(dim/2 )
	t.left(135)
def write_length(t, dim):
	t.left(90)
	t.forward(dim/3)
	t.color("red")
	t.write(str(dim/ratio),align = "center", font = ("Arial", 8, "bold"))
	t.color("blue")
	t.forward(2 * dim/3)

def write_dim(t, dim):
	t.color("blue")
	t.speed(0)
	t.pensize(1)
	t.pendown()
	t.forward(20)
	t.backward(10)
	tri = 5 * math.sqrt(2) # calculates the side of a triangle(arrow)
	right_arrow(t, tri) # draws right arrow 
	write_width(t, dim["width"])
	left_arrow(t, tri) # draws left arrow
	t.left(90)
	t.forward(10)
	t.backward(20)
	t.left(90)
	t.penup()
	t.forward(dim["width"])
	t.pendown()
	t.forward(20)
	t.backward(10)
	up_arrow(t,tri)	# draws up arrow
	write_length(t,dim["length"])
	down_arrow(t,tri) # draws down arrow
	# step to come back to its initial position
	back_to_initial_pos(t,dim)

def create_screen(m):
	root[m] = tkinter.Tk()
	cv = tkinter.Canvas(root[m], width=float(d[1])+50,height=float(d[0])+50, bg="#ffeeee")
	cv.find_all()
	a = tkinter.Label(root[m],text = m.upper(), font = ("Segoe Script", 20,"bold"))
	a.config(fg = "white", bg = "black")
	a.pack()
	root[m].title(m.upper())
	cv.pack()
	s = turtle.TurtleScreen(cv)
	s.bgcolor("white")
	t = turtle.RawTurtle(s)
	t.ht()
	return t
def set_initials(t):
	t.pensize(2)
	t.speed(0)
	t.color("black", (1, 0.85, 0.85))
	t.penup()
	print("set_initials")
	print(init_x)
	print(init_y)
	t.setx(-init_x)
	t.sety(init_y)
	t.pendown()
def draw_rect(t,l,b):
	t.forward(b)
	t.right(90)
	t.forward(l)
	t.right(90)
	t.forward(b)
	t.right(90)
	t.forward(l)
def write_text(t, j, dim, init_x, init_y):
	st_pos = t.position()
	t.penup()
	t.setx(dim['left'] - init_x +  dim['width']/2)
	t.sety(init_y - dim['top'] - dim['length']/2)
	t.color("blue")
	t.write(j.upper(), True, align = "center", font=("Segoe Script", 10, "italic"))
	t.setx(st_pos[0])
	t.sety(st_pos[1])
def set_x_y(t,init_x,init_y, Dij):
	t.penup()
	t.sety(init_y - Dij['top'])
	t.setx(Dij['left']-init_x)
	t.pendown()

def draw_plan(m,init_x, init_y):
	t = create_screen(m)
	set_initials(t)
	draw_rect(t,float(d[0]),float(d[1]))
	for j in D[m]:
		t.color("black")
		if j != "Stair case":
			t.right(90)
			set_x_y(t, init_x, init_y, D[m][j])
			draw_rect(t, D[m][j]["length"],D[m][j]["width"])
			st_pos = t.position()
			write_text(t,j, D[m][j], init_x, init_y)
			if j == "Entrance":
				draw_door(t,D[m][j])
				t.penup()
				t.setx(st_pos[0])
				t.sety(st_pos[1])
				t.pendown()
				t.left(90)
		else:
			st_pos = t.position()
			steps = D[m][j]['length']/8
			set_x_y(t, init_x, init_y, D[m][j])
			t.color("grey")
			for k in range(8):
				t.right(90)
				draw_rect(t,steps, D[m][j]["width"])
				t.backward(steps)
			write_text(t, j, D[m][j], init_x, init_y)
			t.forward(D[m][j]["length"])
		write_dim(t,D[m][j])
m = 0

def begin(fl):
	global D,d
#fl=input("Enter the choice : " + str(D.keys()))
	#print("D : ",D)
	#read()
	print("D : ",D)
	global init_x
	global init_y
	init_x = float(d[1])/2
	init_y = float(d[0])/2
	flag = False
	l = []
	print("fl : ",fl)
	flag, l = check(flag, init_x,init_y,D[fl], l)
	print(flag)
	if not flag:
		print("hi")
		draw_plan(fl, init_x,init_y)
	else:
		a = tkinter.Tk()
		l = tkinter.Message(a,text = str(fl.upper())+" cannot be drawn because there is a dimension problem in ".upper()+str(l), aspect=400, font=("Segoe Script", 12, "italic"))
		l.config(bg = "black", fg = "white")
		l.pack(expand = tkinter.YES, fill = tkinter.BOTH)
		#print(i,"cannot be drawn because there is a dimension problem in",l)
	tkinter.mainloop()