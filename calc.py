import tkinter as tk
import math

root=tk.Tk()
expression=""
operator_clicked=False
dot_clicked=False


def click(number):
    global expression,operator_clicked,dot_clicked
    num=str(number)
    temp=e.get("1.0","end-1c")
    if temp=="Error":
        clear()
    if temp=="0":
        e.delete("1.0","end")
        temp=e.get("1.0","end")

    if num.isdigit():
        expression=expression+str(number)
        e.delete("1.0","end")

        e.insert("end",expression)
    elif number in "+-*/%" or number=="x!":
        operator_clicked=True
        dot_clicked=False
        expression=expression[:-1] if expression.endswith(("+","-","*","/","%","x!")) else expression
        if number=="x!":
             expression+='!'
        elif number=="%":
            expression+='%'
        else:
            expression+=number
        e.delete("1.0","end-1c")
        e.insert("end",expression)
        if number=="%":
            percentage()
        elif number=="x!":
            factorial_number()

    elif number==".":
        if not dot_clicked:
            expression=expression+str(number)
            e.delete("1.0","end")
            e.insert("end",expression)
            dot_clicked=True
        operator_clicked=False

def calculate():
    global expression,operator_clicked,dot_clicked
    try:
        result=eval(expression)
        e.delete("1.0","end")
        e.insert("end",result)
        expression=str(result)
        operator_clicked=False
        dot_clicked=False
    except:
        e.delete("1.0","end")
        e.insert("end","Error")
        expression=""
        operator_clicked=False
        dot_clicked=False

def clear():
    global expression,operator_clicked,dot_clicked
    expression=""
    operator_clicked=False
    dot_clicked=False
    e.delete("1.0","end")
    e.insert("1.0","0")


def percentage():
    global expression,operator_clicked
    if "%" in expression:
        expression=expression[:-1]
        current=float(expression)
    result=current/100
    result=str(result)
    expression=result
    e.delete("1.0","end")
    e.insert("end",expression)


def factorial_number():
    global expression
    try:
        if "!" in expression:
           expression=expression[:-1]
           number=int(expression)
        result=math.factorial(number)
        expression=str(result)
        e.delete("1.0","end")
        e.insert("end",str(result))

    except:
        e.delete("1.0","end")
        e.insert("end","Error")

def delete_button():
    global expression,operator_clicked,dot_clicked
    current=e.get("1.0","end-1c")
    if expression=="Error":
       clear()
    elif len(expression)>1:
        if expression[-1]==".":
            dot_clicked=False
        if expression[-1] in "+-*/":
            operator_clicked=False
            expression=expression[:-1] if expression.endswith(("+","-","*","/",".","%")) else expression
            e.delete("1.0","end")
            e.insert("end",expression)
        else:
            expression=expression[:-1]
            e.delete("1.0","end")
            e.insert("end",expression)
    else:
        clear()
        expression=""

font=("times new roman",18)
font1=("times new roman",16)
font2=("times new roman",16)
e=tk.Text(root,width=70,borderwidth=0,font=font,highlightthickness=0,height=2, bg="black", fg="white")
e.grid(row=0,column=0,columnspan=4,padx=20,pady=20)
e.insert("end", "0")



b7=tk.Button(root,text="7",bg="black",fg="white",activebackground="orange",padx=40,pady=40,font=font, borderwidth=0, highlightthickness=0,command=lambda:click(7))
b8=tk.Button(root,text="8",bg="black",fg="white",activebackground="orange",padx=40,pady=40,font=font, borderwidth=0, highlightthickness=0,command=lambda:click(8))
b9=tk.Button(root,text="9",bg="black",fg="white",activebackground="orange",padx=40,pady=40,font=font, borderwidth=0, highlightthickness=0,command=lambda:click(9))
b4=tk.Button(root,text="4",bg="black",fg="white",activebackground="orange",padx=40,pady=40,font=font, borderwidth=0, highlightthickness=0,command=lambda:click(4))
b5=tk.Button(root,text="5",bg="black",fg="white",activebackground="orange",padx=40,pady=40,font=font, borderwidth=0, highlightthickness=0,command=lambda:click(5))
b6=tk.Button(root,text="6",bg="black",fg="white",activebackground="orange",padx=40,pady=40,font=font, borderwidth=0, highlightthickness=0,command=lambda:click(6))
b1=tk.Button(root,text="1",bg="black",fg="white",activebackground="orange",padx=40,pady=40,font=font, borderwidth=0, highlightthickness=0,command=lambda:click(1))
b2=tk.Button(root,text="2",bg="black",fg="white",activebackground="orange",padx=40,pady=40,font=font, borderwidth=0, highlightthickness=0,command=lambda:click(2))
b3=tk.Button(root,text="3",bg="black",fg="white",activebackground="orange",padx=40,pady=40,font=font, borderwidth=0, highlightthickness=0,command=lambda:click(3))
bc=tk.Button(root,text="C",bg="black",fg="orange",activebackground="sky blue",padx=40,pady=40,font=font1, borderwidth=0, highlightthickness=0,command=lambda:clear())
bd=tk.Button(root,text="D",bg="black",fg="orange",activebackground="sky blue",padx=40,pady=40,font=font1, borderwidth=0, highlightthickness=0,command=lambda:delete_button())
bp=tk.Button(root,text="%",bg="black",fg="orange",activebackground="sky blue",padx=40,pady=40,font=font2, borderwidth=0, highlightthickness=0,command=lambda:click("%"))
bf=tk.Button(root,text="x!",bg="black",fg="orange",activebackground="sky blue",padx=40,pady=40,font=font2, borderwidth=0, highlightthickness=0,command=lambda:click("x!"))
b0=tk.Button(root,text="0",bg="black",fg="white",activebackground="orange",padx=40,pady=40,font=font2, borderwidth=0, highlightthickness=0,command=lambda:click(0))
bdo=tk.Button(root,text=".",bg="black",fg="white",activebackground="orange",padx=40,pady=40,font=font2, borderwidth=0, highlightthickness=0,command=lambda:click("."))
bdi=tk.Button(root,text="/",bg="black",fg="orange",activebackground="sky blue",padx=40,pady=40,font=font2, borderwidth=0, highlightthickness=0,command=lambda:click("/"))
bm=tk.Button(root,text="*",bg="black",fg="orange",activebackground="skyblue",padx=40,pady=40,font=font2, borderwidth=0, highlightthickness=0,command=lambda:click("*"))
bs=tk.Button(root,text="-",bg="black",fg="orange",activebackground="sky blue",padx=40,pady=40,font=font2, borderwidth=0, highlightthickness=0,command=lambda:click("-"))
ba=tk.Button(root,text="+",bg="black",fg="orange",activebackground="sky blue",padx=40,pady=40,font=font2, borderwidth=0, highlightthickness=0,command=lambda:click("+"))
be=tk.Button(root,text="=",bg="black",fg="orange",activebackground="light green",padx=40,pady=40,font=font2, borderwidth=0, highlightthickness=0,command=lambda:calculate())



bc.grid(row=2,column=0)
bd.grid(row=2,column=1)
bp.grid(row=2,column=2)
b7.grid(row=3,column=0)
b8.grid(row=3,column=1)
b9.grid(row=3,column=2)
b4.grid(row=4,column=0)
b5.grid(row=4,column=1)
b6.grid(row=4,column=2)
b1.grid(row=5,column=0)
b2.grid(row=5,column=1)
b3.grid(row=5,column=2)
bf.grid(row=6,column=0)
b0.grid(row=6,column=1)
bdo.grid(row=6,column=2)
bdi.grid(row=2,column=3)
bm.grid(row=3,column=3)
bs.grid(row=4,column=3)
ba.grid(row=5,column=3)
be.grid(row=6,column=3)


root.configure(bg="black")
root.title("Calculator")
root.minsize(900,700)
root.maxsize(1000,700)
root.mainloop()