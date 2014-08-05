import pymysql
import tkinter as tk

def check_password(id):
	# return the pwd of tat particular user id 
	con = pymysql.connect()
	con.autocommit(True)
	cur=con.cursor()
	cur.execute("use test")
	cur.execute("select u.pwd from user_account u where u.uid= %s",id)
	row=cur.fetchone()
	cur.close()
	con.close()
	return row[0]
	
def check_userid(id):
	#run thru the db abd validate if it is already present
	con = pymysql.connect()
	con.autocommit(True)
	cur=con.cursor()
	cur.execute("use test")
	cur.execute("select uid from user_account ")
	rows= cur.fetchall()
	x=0
	for i in rows:
		if (id==i[0]):
			x=1
	cur.close()
	con.close()
	if x==1 : 
		return True 

	else : 
		return False 


def fetch_user_id():
	#return a list of all the user ids present in the db
	con = pymysql.connect()
	con.autocommit(True)
	cur=con.cursor()
	cur.execute("use test")
	cur.execute("select uid from user_account ")
	rows= cur.fetchall()
	l=[]
	for i in rows:
		l.append(i[0])
	cur.close()
	con.close()
	return l
		


def insert(l):
	#insert the details of every user into the db
	con = pymysql.connect()
	con.autocommit(True)
	cur=con.cursor()
	cur.execute("use test")
	for i in l:
		print(i,type(i))
	cur.execute("insert into user_account values (%s,%s,%s,%s,%s)",(l[0],l[1],l[2],l[3],l[5]))
	cur.close()
	con.close()

def get_file(id):
	con = pymysql.connect()
	con.autocommit(True)
	cur=con.cursor()
	cur.execute("use test")
	cur.execute("select file from site_plan where uid=%s",id)
	rows= cur.fetchone()
	cur.close()
	con.close()
	return rows[0]

def upload(upload, uid, f_n):
	con = pymysql.connect()
	con.autocommit(True)
	cur=con.cursor()
	cur.execute("use test")
	try:
		cur.execute("insert into site_plan values (%s, %s)", (uid, f_n))
	except Exception as e:
		print(e)
	cur.close()
	con.close()
	upload.destroy()

#x=["Geetha","D","gee","1234","8970364100"]

#insert(x)	
	
#y=check_password("gee")
#print(y)	

#z=check_userid("gee")
#print(z)


#u=fetch_user_id()
#print(u)
#file=retrieve_files("gee")
#print(file)
