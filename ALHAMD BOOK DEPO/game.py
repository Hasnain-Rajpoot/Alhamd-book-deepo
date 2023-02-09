def help():
    a=tmsg.showinfo("help","hasnain will help you")
def rate():
    a=tmsg.askquestion("was your experience good","was you experience good")
    if a=="yes":
        tmsg.showinfo("nice","rate us on playstore")
    else:
        tmsg.showinfo("ohh no","tell us whats wrong we will fix")

def te():
    y.configure(bg="teal")
def pu():
    y.configure(bg="pirple")
def wall():
    y.configure(bg="teal")
def gr():
    y.configure(bg="gray")
def or():
    y.configure(bg="orange")                
menu2=Menu(y)
m1=Menu(menu2,tearoff=0)
m1.add_command(label="teal",command=te)
m1.add_command(label="purple",command=pu)
m1.add_command(label="wall",command=wall)
m1.add_command(label="gray",command=gr)
m1.add_command(label="orange",command=or)
menu2.add_cascade(label="background colour change",menu=m1)
menu2.add_command(label="help",command=help)
menu2.add_command(label="Rate us",command=rate)
y.config(menu=menu2)