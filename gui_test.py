import tkinter as tk
import db
import floor_selection
from PIL import ImageTk, Image

	
def foo(root_parent , user_name):
	try:
		root_parent.destroy()
	except Exception as e:
		print ( e )
	root3 = tk.Tk()
	
	welcome = tk.Label(root3, text = "Welcome "+str(user_name)+',' , font = ('Segoe Script',16,'bold') ,bg ='dark blue', fg ='white')
	exist_plan = tk.Label(root3, text = 'existing plan' , font = ('Arial' , 12 , 'normal'))
	welcome.pack(padx = 50 , pady = 30 )
	welcome.place(x = 150, y = 10 )
	exist_plan.pack()
	exist_plan.place(x = 5, y = 50)
	
	list_plans = ['home' , 'office' , 'hotel']
	x_b = 10
	y_b = 70
	step_b = 40
	for i in list_plans:
		button = tk.Button(root3, text = i , font = ('Arial',13,'normal'))
		button.pack()
		button.place(x = x_b , y = y_b)
		y_b = y_b + step_b
		
	scrollbar = tk.Scrollbar(root3)
	scrollbar.pack(side = tk.RIGHT, padx = 00 , pady = 50, fill = tk.Y)
	
	scrollbar1 = tk.Scrollbar(root3 , orient = tk.HORIZONTAL)
	scrollbar1.pack(side = tk.BOTTOM, padx = 00 , pady = 47, fill = tk.X)
	
	listbox = tk.Listbox(root3, yscrollcommand=scrollbar.set)
	listbox.pack(side = tk.RIGHT, fill = tk.Y, padx = 00 , pady = 50, )
	listbox.scan_dragto(200,00)

# listbox is associated with a scrollbar
	
#	listbox.pack(side = tk.LEFT)
	
#dirlist = os.listdir(os.curdir)
	dirlist = ["kusum","gee","harshu","dhanya"]
	f=open('file1.txt','r')
	a=f.readlines()
	for i in a:
		listbox.insert(tk.END,i)
		
	scrollbar.config(command=listbox.yview)
	scrollbar1.config(command = listbox.xview)

	root3.minsize(600,400)
	root3.mainloop()
	
def logged_in_page(user_t,pass_t,root2):
	flag=False
	if db.check_userid(user_t.get()) : 
		passw = db.check_password(user_t.get())
		label = tk.Label(root2, text = 'Incorrect password' , font = ('Arial',8,'normal'), fg = 'red')
		if pass_t.get() == passw:
			print("logged in")
			label['text'] = ''
			#root2.update_idletasks()
			foo(root2 , user_t.get())
		else:
			label.pack()
			label.place(x = 200, y = 210)
			pass_t.delete(0,len(pass_t.get()))
	else:
		msg = tk.Tk()
		l = tk.Label(msg, text = "Invalid user id!", font = ("Arial", 12, "normal"))
		l.pack()
		msg.mainloop()
	
	#foo(root2)
		
def sign_in():
	print("sign_in")
	
	root.destroy()
	root2 = tk.Tk()
	
	img = ImageTk.PhotoImage(Image.open("image1.jpg"))
	panel = tk.Label(root2, image = img)
	panel.pack()
	panel.place(x = 400)
	
	l1 = tk.Label(root2, text = "SIGN IN " , font = ('Segoe Script',16,'bold') ,bg ='dark blue', fg ='white')
	user_l = tk.Label(root2, text ='USER ID' , font = ('Arial' , 14, 'normal'))
	pass_l = tk.Label(root2, text ='PASSWORD' , font = ('Arial' , 14, 'normal'))
	
	button = tk.Button(root2 , text = "SIGN IN" , command = lambda : logged_in_page(user_t,pass_t,root2))
	button.pack()
	button.place(x=100, y = 250)
	user_t = tk.Entry(root2)
	pass_t = tk.Entry(root2,show = '*')
	
	l1.pack(padx=100)
	user_l.pack()
	pass_l.pack()
	
	user_t.pack()
	pass_t.pack()
	
	l1.place(x=200,y=5)
	user_l.place(x=20,y=100)
	pass_l.place(x=20,y=180)
	
	user_t.place(x=200,y=100)
	pass_t.place(x=200,y=180)
	
	
	root2.minsize(600,300)
	root2.mainloop()
	
def new_page(text_labels, root1):
	flag = False
	values=[]
	user_name=text_labels[2].get()
	if user_name not in db.fetch_user_id():
		flag = True
	else:
		msg = tk.Tk()
		l = tk.Label(msg, text = "User id already exists", font = ("Arial", 12, "normal"))
		l.pack()
		msg.mainloop()
	if flag and text_labels[3].get() == text_labels[4].get():
		flag = True
		print("accepted")
		for i in text_labels:
			try:
				print(i,i.get())
				values.append(str(i.get()))
			except Exception as e:
				print(e)
		try:
			root1.destroy()
		except Exception as e:
			print(e)
	else:
		text_labels[3].delete(0,len(text_labels[3].get()))
		text_labels[4].delete(0,len(text_labels[4].get()))
		msg = tk.Tk()
		l = tk.Label(msg, text = "Enter the correct password", font = ("Arial", 12, "normal"))
		#button = tk.Button(msg, text = 'OK', font=('Arial',10,'normal'), command = msg.quit())
		#button.pack()
		l.pack()
		#button.place(x=100 , y=60)
		msg.minsize(150,150)
		msg.mainloop()
	print("new_page")
	print(values)
	db.insert(tuple(values))
	#insert_to _db(values)
	foo(root1,user_name)
	
	
def create_account():
	print("create_account")
	
	root.destroy()
	root1 = tk.Tk()	
	img = ImageTk.PhotoImage(Image.open("image1.jpg"))
	panel = tk.Label(root1, image = img)
	panel.pack()
	panel.place(x = 500)
	label = tk.Label(root1, text = 'CREATE ACCOUNT' , font = ("Segoe Script", 16 ,'bold') ,bg="dark blue", fg ="white")
	label.pack(padx = 100)
	label.place(x = 200,y = 5)
	button = tk.Button(root1 , text = "CREATE" , command = lambda : new_page(text_labels,root1))
	first_l = tk.Label(root1 , text = "First Name *" , font = ("Arial",12,'normal'))
	last_l = tk.Label(root1 , text = "Last Name *" , font = ("Arial",12,'normal'))
	id_l = tk.Label(root1, text = "User ID *", font = ("Arial",12,'normal'))
	pass_l = tk.Label(root1,text = "Password *" , font = ('Arial',12,'normal'))
	conP_l = tk.Label(root1,text = "Confirm Password *" , font = ('Arial',12,'normal'))
	cont_l = tk.Label(root1,text = "Contact Number *" , font = ('Arial',12,'normal'))
	star_l = tk.Label(root1,text = "The fields marked as * are mandatory", font=('Arial',8,'italic'), fg = 'red')
	first_t = tk.Entry(root1)
	last_t = tk.Entry(root1)
	id_t = tk.Entry(root1)
	pass_t = tk.Entry(root1, show="*")
	conP_t = tk.Entry(root1, show="*")
	cont_t = tk.Entry(root1)
	def keyPress(event):
		if event.char not in ['0','1','2','3','4','5','6','7','8','9','-']:
			error = tk.Tk()
			l1 = tk.Label(error,text="Invalid input "+event.char , font = ('Arial',16,'bold'))
			#img = ImageTk.PhotoImage(Image.open("image1.gif"))
			#panel = tk.Label(error, image = img)
			#panel.pack(side = "bottom", fill = "both", expand = "yes")
			l1.pack()
			#panel.pack(side = "bottom", fill = "both", expand = "yes")
			error.minsize(200,150)
			error.mainloop()
		else:
			pass
			

	cont_t.bind('<KeyPress>', keyPress)
	cont_t.pack()
	cont_t.focus()
	first_l.pack()
	last_l.pack()
	id_l.pack()
	pass_l.pack()
	conP_l.pack()
	cont_l.pack()
	star_l.pack()
	
	first_t.pack()
	last_t.pack()
	id_t.pack()
	pass_t.pack()
	conP_t.pack()
	
	button.pack(padx = 200 , pady =50)
	button.place(x=325 , y=350)
	
	first_l.place(x=20,y=100)
	last_l.place(x=20,y=140)
	id_l.place(x=20,y=180)
	pass_l.place(x=20,y=220)
	conP_l.place(x=20,y=260)
	cont_l.place(x=20,y=300)
	star_l.place(x=5,y=370)
	
	first_t.place(x=200,y=100)
	last_t.place(x=200,y=140)
	id_t.place(x=200,y=180)
	pass_t.place(x=200,y=220)
	conP_t.place(x=200,y=260)
	cont_t.place(x=200,y=300)
	flag = False
	
	text_labels = (first_t, last_t, id_t,pass_t, conP_t, cont_t)
	root1.minsize(700,400)
	#l2.place(align = LEFT)
	root1.mainloop()
	
	
root = tk.Tk()
l1 = tk.Label(root, text = "\nWelcome to Design MyHome\n\n", font = ("Times new Roman", 22, "bold"))
l2 = tk.Label(root, text = "Design MyHome helps you to generate a plan for your dream house." , font = ("Times new Roman", 16))
img = ImageTk.PhotoImage(Image.open("image1.gif"))
panel = tk.Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")
button1 = tk.Button(root, text="Sign in" , command = sign_in)
button2 = tk.Button(root, text="Create Account" , command = create_account)

l1.pack()
l2.pack()

button1.pack()
button2.pack()

button1.place(x= 270, y= 450)
button2.place(x= 350, y=450)

root.minsize(700,500)

tk.mainloop()
