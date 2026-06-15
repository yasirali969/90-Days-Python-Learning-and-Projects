
from tkinter import *

first_no=second_no=operator=None



def get_digit(digit):
    current = str(result_label["text"])

    if current == "0":
        result_label.config(text=str(digit))
    else:
        result_label.config(text=current + str(digit))
    
def clear_digit():
    result_label.config(text='')

def get_operator(op):
    global first_no,operator
    
    first_no=int(result_label['text'])
    operator =op
    result_label.config(text='')
    
def result():
    global second_No,first_no,operator
    
    second_no=int(result_label['text'])
    
    if operator=='+':
        result_label.config(text=str(first_no+second_no))
    elif operator=='-':
        result_label.config(text=str(first_no - second_no))
    elif operator=='*':
        result_label.config(text=str(first_no*second_no))
    else: 
        if second_no==0:
            result_label.config(text='Error')
        else:
            result_label.config(text=str(round(first_no/second_no,2)))
        

root=Tk()
root.title("Calculator")
root.configure(background="black")
root.geometry("370x420")
root.resizable(0,0)

result_label=Label(root,text=0,fg="White",bg="black")
result_label.grid(row=0,column=0,pady=(55,25),columnspan=5,sticky='w')
result_label.config(font=("verdana",30,'bold'))


btn7=Button(root,text="7",width=6,height=2,fg="White",bg="Green",command=lambda:get_digit(7))
btn7.grid(row=1,column=0)
btn7.config(font=("verdana",14))
sticky="nsew"

btn8=Button(root,text="8",width=6,height=2,fg="White",bg="Green",command=lambda:get_digit(8))
btn8.grid(row=1,column=1, padx=4, pady=4)
btn8.config(font=("verdana",14))
sticky="nsew"


btn9=Button(root,text="9",width=6,height=2,fg="White",bg="Green",command=lambda:get_digit(9))
btn9.grid(row=1,column=2, padx=4, pady=4)
btn9.config(font=("verdana",14))
sticky="nsew"

btn_add=Button(root,text="+",width=6,height=2,fg="White",bg="Yellow",command=lambda:get_operator('+'))
btn_add.grid(row=1,column=3, padx=4, pady=4)
btn_add.config(font=("verdana",14))
sticky="nsew"

btn4=Button(root,text="4",width=6,height=2,fg="White",bg="Green",command=lambda:get_digit(4))
btn4.grid(row=2,column=0, padx=4, pady=4)
btn4.config(font=("verdana",14))
sticky="nsew"

btn5=Button(root,text="5",width=6,height=2,fg="White",bg="Green",command=lambda:get_digit(5))
btn5.grid(row=2,column=1, padx=4, pady=4)
btn5.config(font=("verdana",14))
sticky="nsew"

btn6=Button(root,text="6",width=6,height=2,fg="White",bg="Green",command=lambda:get_digit(6))
btn6.grid(row=2,column=2, padx=4, pady=4)
btn6.config(font=("verdana",14))
sticky="nsew"

btn_Sub=Button(root,text="-",width=6,height=2,fg="White",bg="Green",command=lambda:get_operator('-'))
btn_Sub.grid(row=2,column=3, padx=4, pady=4)
btn_Sub.config(font=("verdana",14))
sticky="nsew"

btn1=Button(root,text="1",width=6,height=2,fg="White",bg="Green",command=lambda:get_digit(1))
btn1.grid(row=3,column=0, padx=4, pady=4)
btn1.config(font=("verdana",14))
sticky="nsew"

btn2=Button(root,text="2",width=6,height=2,fg="White",bg="Green",command=lambda:get_digit(2))
btn2.grid(row=3,column=1, padx=4, pady=4)
btn2.config(font=("verdana",14))
sticky="nsew"

btn3=Button(root,text="3",width=6,height=2,fg="White",bg="Green",command=lambda:get_digit(3))
btn3.grid(row=3,column=2, padx=4, pady=4)
btn3.config(font=("verdana",14))
sticky="nsew"

btn_div=Button(root,text="*",width=6,height=2,fg="White",bg="Blue",command=lambda:get_operator('*'))
btn_div.grid(row=3,column=3, padx=4, pady=4 )
btn_div.config(font=("verdana",14))
sticky="nsew"


btn_clear = Button(root, text="C", width=6, height=2,bg="Orange", fg="White",font=("Verdana", 14),command=lambda:clear_digit())
btn_clear.grid(row=4, column=0, padx=4, pady=4)
sticky="nsew"

btn_zero = Button(root, text="0", width=6, height=2,bg="Green", fg="White", font=("Verdana", 14))
btn_zero.grid(row=4, column=1, padx=4, pady=4)
sticky="nsew"

btn_equal = Button(root, text="=", width=6, height=2,bg="Brown", fg="White", font=("Verdana", 14),command=lambda:result())
btn_equal.grid(row=4, column=2,padx=4, pady=4)
sticky="nsew"

btn_div = Button(root, text="/", width=6, height=2, bg="Red", fg="White",    font=("Verdana", 14),command=lambda:get_operator('/'))
btn_div.grid(row=4, column=3, padx=4, pady=4)
sticky="nsew"

root.mainloop()


