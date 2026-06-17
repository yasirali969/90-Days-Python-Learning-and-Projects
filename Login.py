#from tkinter import *
#from PIL import ImageTk,Image
#from tkinter import messagebox

'''
def handle_login():
    Email=email_input.get()
    Passwrod=Pass_input.get()
    if Email=="Yasirali@gmail.com" and Passwrod=="1234":
     messagebox.showinfo('Yayyy','Login Successful!')
     messagebox.showerror('Error','Login failed!')
    

root=Tk()
root.title("Login Form")
# root.iconbitmap(" ") # for icon insertion
# root.minsize(400,400) # fix min size
root.geometry("350x500")
root.configure(background="#0096DC")
img=Image.open("8.jpg")
resized_img=img.resize((70,70))
Img=ImageTk.PhotoImage(resized_img)
Img_label=Label(root,image=Img)

# here we will implement gemetry manager decide which
# element would sit where on the interface
Img_label.pack()
Img_label.pack(pady=(10,10))

text_label=Label(root,text="Pandas",fg="white",bg="#0096DC")
text_label.pack()
text_label.config(font=("verdana",24))

email_label=Label(root,text="Enter Email",fg="white",bg="#0096DC")
email_label.pack()
email_label.pack(pady=(20,14))
email_label.config(font=("verdana",12))

email_input=Entry(root,width=50)
email_input.pack(ipady=6)  # ipday for height



password_label=Label(root,text="Enter Password",fg="white",bg="#0096DC")
password_label.pack()
password_label.pack(pady=(30,14))
password_label.config(font=("verdana",12))

Pass_input=Entry(root,width=50)
Pass_input.pack(ipady=6)  # ipday for height

login_button=Button(root,text="Login",width=14,height=2,command=handle_login)
login_button.pack(pady=(40,20))
login_button.config(font=('vardana',10))

root.mainloop()
'''

from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

def login_handle():
    Email=Email_input.get()
    Password=Pass_input.get()
    if Email=="Yasirali@gmail" and Password=="123":
        messagebox.showinfo("Yayyy","Login Successfully!")
        messagebox.showerror("Error","Login Failed!")


root=Tk()
root.title("Login Pandas Screen")
root.geometry("350x500")
root.configure(background="#0096DC")

img=Image.open('8.jpg')
img_resized=img.resize((70,70))
Img=ImageTk.PhotoImage(img_resized)
Imag=Label(root,image=Img)

Imag.pack()
Imag.pack(pady=(10,10))

text_label=Label(root,text="Pandas",fg="white",bg="#0096DC")
text_label.pack()
text_label.config(font=('verdana',18))
text_label.pack(pady=(15,5))


email_text=Label(root,text="Enter Email",fg="white",bg="#0096DC")
email_text.pack()
email_text.pack(pady=(15,5))
email_text.config(font=('verdana',18))

Email_input=Entry(root,width=50)
Email_input.pack(ipady=6)


Password_text=Label(root,text="Enter Password",fg="white",bg="#0096DC")
Password_text.pack()
Password_text.pack(pady=(15,5))
Password_text.config(font=('verdana',18))

Pass_input=Entry(root,width=50)
Pass_input.pack(ipady=6)

Login_button=Button(root,text="Login",width=14,height=2,command=login_handle)
Login_button.pack(pady=(40,20))
root.mainloop()
