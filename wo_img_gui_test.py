import tkinter as tk
import db
import floor_selection1 as fs
#from PIL import ImageTk, Image

class ScrolledText(tk.Text):
    def __init__(self, master=None, **kw):
        self.frame = tk.Frame(master)
        self.vbar = tk.Scrollbar(self.frame)
        self.vbar.pack(side=tk.RIGHT, fill=tk.Y)

        kw.update({'yscrollcommand': self.vbar.set})
        tk.Text.__init__(self, self.frame, **kw)
        self.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.vbar['command'] = self.yview

        # Copy geometry methods of self.frame without overriding Text
        # methods -- hack!
        text_meths = vars(tk.Text).keys()
        methods = vars(tk.Pack).keys() | vars(tk.Grid).keys() | vars(tk.Place).keys()
        methods = methods.difference(text_meths)

        for m in methods:
            if m[0] != '_' and m != 'config' and m != 'configure':
                setattr(self, m, getattr(self.frame, m))

    def __str__(self):
        print(str(self.frame))
        return str(self.frame)

	
def foo(root_parent , user_name):
	print("inside foo")
	fs.read(db.get_file(user_name))
	try:
		root_parent.destroy()
	except Exception as e:
		print ( e )
	root3 = tk.Tk()
	
	welcome = tk.Label(root3, text = "Welcome "+str(user_name)+',' , font = ('Segoe Script',16,'bold') ,bg ='dark blue', fg ='white')
	welcome.pack(padx = 50 , pady = 30 )
	welcome.place(x = 150, y = 10 )
	
	x_b = 700
	y_b = 70
	step_b = 40
	button = []
	ind = 0
	hell = ''
	
	
	stext = ScrolledText(root3 ,bg='white', height=10)
	print(type(stext))
	f = open(db.get_file(user_name),"r")
	f1 = f.read()
	stext.insert(tk.END, f1)
	f.close()
	stext.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
	stext.focus_set()
	#print(stext.get(0))
	def create_button(i, ind):
		button.append(tk.Button(root3, text = i , font = ("Segoe Script", 10,"bold"),command = lambda:fs.begin(i)))
		button[ind].pack(side=tk.RIGHT)
		button[ind].place(x = x_b, y = y_b)
	for i in fs.D.keys():
		print("fs.D.keyts: ",str(i))
		hell = i
		create_button(i,ind)
		y_b = y_b + step_b
		ind = ind + 1
	run_b = tk.Button(root3, text = "EDITING DONE",font = ("Segoe Script", 10,"bold"), command = lambda: write_into_file(tk.Text.get(stext,"1.0",'end'), user_name))
	run_b.pack(padx = 100, pady = 300) 
	root3.minsize(600,400)
	root3.mainloop()
def write_into_file(text, user_name):
	file_name = db.get_file(user_name)
	f = open(file_name,"w")
	f.write(text)
	f.close()
	fs.read(file_name)
def logged_in_page(user_t,pass_t,root2):
	flag=False
	if db.check_userid(user_t.get()) : 
		passw = db.check_password(user_t.get())
		label = tk.Label(root2, text = 'Incorrect password' , font = ("Segoe Script", 8,"normal"), fg = 'red')
		if pass_t.get() == passw:
			emp_l = tk.Label(root2, text = '')
			print("logged in")
			emp_l.pack()
			label.config(text = "")
			emp_l.place(x = 200, y = 210)
			foo(root2 , user_t.get())
		else:
			label.pack()
			label.place(x = 200, y = 210)
			pass_t.delete(0,len(pass_t.get()))
	else:
		msg = tk.Tk()
		msg.bell()
		l = tk.Message(msg, text = "Invalid user id!", font = ("Segoe Script", 10,"bold"))
		l.pack(expand = True)
		l.config(bg = "black", fg = "white")
		msg.mainloop()
	
	#foo(root2)
		
def sign_in():
	print("sign_in")
	
	root.destroy()
	root2 = tk.Tk()
	
	#img = ImageTk.PhotoImage(Image.open("image1.jpg"))
	panel = tk.Label(root2)
	panel.pack()
	panel.place(x = 400)
	
	l1 = tk.Label(root2, text = "SIGN IN " , font = ('Segoe Script',16,'bold') ,bg ='dark blue', fg ='white')
	user_l = tk.Label(root2, text ='USER ID' , font = ('Segoe Script',14,'normal'))
	pass_l = tk.Label(root2, text ='PASSWORD' , font = ('Segoe Script',14,'normal'))
	
	button = tk.Button(root2 , text = "SIGN IN" ,font = ('Segoe Script',12,'bold'), command = lambda : logged_in_page(user_t,pass_t,root2))
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
		msg.bell()
		l = tk.Label(msg, text = "User id already exists", font = ("Segoe Script", 12, "normal"))
		l.pack()
		l.config(bg = 'black', fg = 'white')
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
		msg.bell()
		l = tk.Label(msg, text = "Enter the correct password", font = ("Segoe Script", 12, "normal"))
		l.pack()
		l.pack(bg = 'black', fg = 'white')
		msg.minsize(150,150)
		msg.mainloop()
	print("new_page")
	print(values)
	db.insert(tuple(values))
	#insert_to _db(values)
	upload = tk.Tk()
	f_name = tk.Label(upload, text = "Enter file name")
	f_name.pack()
	text = tk.Entry(upload)
	text.pack()
	up_b = tk.Button(upload, text = "UPLOAD", font = ("Segoe Script", 12, "normal"), command = lambda:db.upload(upload,user_name,text.get()))
	up_b.pack()
	upload.mainloop()
	foo(root1,user_name)
	
	
def create_account():
	print("create_account")
	
	root.destroy()
	root1 = tk.Tk()	
	#img = ImageTk.PhotoImage(Image.open("image1.jpg"))
	panel = tk.Label(root1)#, image = img)
	panel.pack()
	panel.place(x = 500)
	label = tk.Label(root1, text = 'CREATE ACCOUNT' , font = ("Segoe Script", 16 ,'bold') ,bg="dark blue", fg ="white")
	label.pack(padx = 100)
	label.place(x = 200,y = 5)
	button = tk.Button(root1 , text = "CREATE" , font = ('Segoe Script',16,'bold'),command = lambda : new_page(text_labels,root1))
	first_l = tk.Label(root1 , text = "First Name *" , font = ("Segoe Script",12,'normal'))
	last_l = tk.Label(root1 , text = "Last Name *" , font = ("Segoe Script",12,'normal'))
	id_l = tk.Label(root1, text = "User ID *", font = ("Segoe Script",12,'normal'))
	pass_l = tk.Label(root1,text = "Password *" , font = ('Segoe Script',12,'normal'))
	conP_l = tk.Label(root1,text = "Confirm Password *" , font = ('Segoe Script',12,'normal'))
	cont_l = tk.Label(root1,text = "Contact Number *" , font = ('Segoe Script',12,'normal'))
	star_l = tk.Label(root1,text = "The fields marked as * are mandatory", font=('Segoe Script',8,'italic'), fg = 'red')
	first_t = tk.Entry(root1)
	last_t = tk.Entry(root1)
	id_t = tk.Entry(root1)
	pass_t = tk.Entry(root1, show="*")
	conP_t = tk.Entry(root1, show="*")
	cont_t = tk.Entry(root1)
	def keyPress(event):
		if event.char not in ['0','1','2','3','4','5','6','7','8','9','-']:
			error = tk.Tk()
			error.bell()
			l1 = tk.Label(error,text="Invalid input "+event.char , font = ('Segoe Script',16,'bold'))
			#img = ImageTk.PhotoImage(Image.open("image1.gif"))
			#panel = tk.Label(error, image = img)
			#panel.pack(side = "bottom", fill = "both", expand = "yes")
			l1.pack()
			l1.config(bg = 'black', fg = 'white')
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
	
main = tk.Tk()
main.minsize(1350,1350)
root = tk.Tk()
l1 = tk.Label(root, text = "\nWelcome to Design MyHome\n\n", font = ("Segoe Script", 22, "bold"))
l2 = tk.Label(root, text = "Design MyHome helps you to generate a plan for your dream house." , font = ("Segoe Script", 16))
#img = ImageTk.PhotoImage(Image.open("image1.gif"))
panel = tk.Label(root)#, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")
button1 = tk.Button(root, text="Sign in" , font = ('Segoe Script',12,'bold'),command = sign_in)
button2 = tk.Button(root, text="Create Account" , font = ('Segoe Script',12,'bold'), command = create_account)

l1.pack()
l2.pack()

button1.pack()
button2.pack()

button1.place(x= 270, y= 450)
button2.place(x= 350, y=450)

root.minsize(700,500)
tk.mainloop()
