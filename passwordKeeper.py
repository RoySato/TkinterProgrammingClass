import sys
import tkinter
from tkinter import messagebox
import csv

passwords = {}

with open("password.csv", newline="") as f:
	reader = csv.reader(f, delimiter=",", quotechar="\'")
	for i in reader: 
		passwords[i[0]] = i[1]

#パスワード追加用のメソッド
def submitEmailPassword(event):

	if box1.get() in passwords.keys():
		answer = messagebox.askyesno("注意", "そのURLはすでに登録されています。更新しますか？")
		if answer != True:
			return
		
	passwords[box1.get()] = box2.get()

	with open("password.csv","w", newline="") as f:
		writer = csv.writer(f, delimiter=",", quotechar="\'", quoting=csv.QUOTE_MINIMAL)
		for i in passwords:
			row = []
			row.append(i)
			row.append(passwords[i])
			writer.writerow(row)
	
	messagebox.showinfo("確認", "URLとパスワードに追加されました")
	box1.delete(0, tkinter.END)
	box2.delete(0, tkinter.END)
	box1.insert(tkinter.END, "URL")
	box2.insert(tkinter.END, "Password")

#パスワード出力用のメソッド
def remindPassword(event):
	with open("password.csv", newline="") as f:
		reader = csv.reader(f, delimiter=",", quotechar="\'")
		for i in reader: 
			passwords[i[0]] = i[1]
	url = box3.get()
	
	if box3.get() in passwords.keys():
		password = passwords[url]
		box4.delete(0, tkinter.END)
		box4.insert(tkinter.END, password)
	else:
		box4.delete(0, tkinter.END)
		box4.insert(tkinter.END, "URLが間違えているか、そのURLを登録していません")
	
	"""
	try:
		password = passwords[url]
		box4.delete(0, tkinter.END)
		box4.insert(tkinter.END, password)
	except:
		box4.delete(0, tkinter.END)
		box4.insert(tkinter.END, "URLが間違えているか、そのURLを登録していません")
	"""	




	
#GUI ウィンドウ設定
root = tkinter.Tk()
root.title("Password Bot")
root.geometry("400x300")

#追加入力
label1 = tkinter.Label(text=u'Enter')
label1.place(x=7, y=20)

box1 = tkinter.Entry(width=50)
box1.insert(tkinter.END, "URL")
box1.place(x=40, y=20)

box2 = tkinter.Entry(width=50)
box2.insert(tkinter.END, "Password")
box2.place(x=40, y=50)

button1 = tkinter.Button(text=u'Submit')
button1.bind("<Button-1>", submitEmailPassword)
button1.place(x=40,y=80)

#パスワードを出力
box3 = tkinter.Entry(width=50)
box3.insert(tkinter.END, "URL")
box3.place(x=40, y=120)

box4 = tkinter.Entry(width=50)
box4.insert(tkinter.END, "ここに出力されます")
box4.place(x=40, y=150)

button2 = tkinter.Button(text=u'Submit2')
button2.bind("<Button-1>", remindPassword)
button2.place(x=40,y=180)

#GUI起動
root.mainloop()