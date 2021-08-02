import pydantic 

from tkinter import *
from mpl_toolkits import mplot3d
import numpy as np
import math
import speech_recognition as sr
import pyttsx3


root=Tk()
root.title('Scientific calculator')
e1=Entry(root,borderwidth=10,fg='black',bg='white')
e1.grid(row=0,column=0,columnspan=5,ipadx=200,ipady=10)
e1.insert(0,'')

listener=sr.Recognizer()
engine = pyttsx3.init()
voices= engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
'''
def take_command():
    try:
        with sr.Microphone() as source:
          e1.insert(0,'listening...')
          voice = listener.listen(source)
          command=listener.recognize_google(voice)
          #command=command.lower()
          #if 'friday' in command:
              #command =command.replace('friday','')
          e1.delete(0,END)      
          e1.insert(0,str(command))
    except:
          pass
'''    
def talk():
    engine=pyttsx3.init()
    engine.setProperty('rate',125)
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.say(e1.get())
    engine.runAndWait()
    #e1.delete(0,END)
    
def click(x):
    old=e1.get()
    e1.delete(0,END)
    e1.insert(0,str(old)+str(x))

def add():
    global f_num
    global math
    math='addition'
    first_number=e1.get()
    f_num=int(first_number)
    e1.delete(0,END)
    
    
def cls():
    a=e1.get()
    b=len(a)-1
    e1.delete(b,END)
    
def clear():
    e1.delete(0,END)     

def eqs():
    second_number=e1.get()
    e1.delete(0,END)
    if math=='addition':
       e1.insert(0,f_num + int(second_number))
    if math=='subtraction':
       e1.insert(0,f_num - int(second_number))
    if math=='multiplication':
       e1.insert(0,f_num * int(second_number))
    if math=='division':
       e1.insert(0,f_num / int(second_number))

def sub():
    global f_num
    global math
    math='subtraction'
    first_number=e1.get()
    f_num=int(first_number)
    e1.delete(0,END)
    
def click(x):
    old=e1.get()
    e1.delete(0,END)
    e1.insert(0,str(old)+str(x))

def add():
    global f_num
    global math
    math='addition'
    first_number=e1.get()
    f_num=int(first_number)
    e1.delete(0,END)
   
def mul():
    global f_num
    global math
    math='multiplication'
    first_number=e1.get() 
    f_num=int(first_number)
    e1.delete(0,END)


def div():
    global f_num
    global math
    math='division'
    first_number=e1.get()
    f_num=int(first_number)
    e1.delete(0,END)
    
def solve():
        import re
        from sympy import solve_linear_system,Matrix
        import sympy as sp
        s=e1.get()
        if re.search('(-)?[\d]{1,}x[+|-][\d]{1,}y=-?[\d]{1,}',s):
           p=re.findall('-?[\d]{1,}',s)
           a=p[:3]
           b=p[3:]
           f=list(map(int,a))
           g=list(map(int,b))
           x,y=sp.symbols('x y')
           d= Matrix((a,b))
           ans=solve_linear_system(d,x,y)
           #print(ans)
           z=[ans[x],ans[y]]
           #print(z)
           e1.delete(0,END)
           e1.insert(0,ans)
           talk()
           import matplotlib.pyplot as plt
           import numpy as np
           fig = plt.figure ()
           ax = fig.add_subplot (1, 1, 1)
           x = np.linspace (-5, 5, 100)
           ax.spines['left'].set_position ('center')
           ax.spines['bottom'].set_position ('center')
           ax.spines['right'].set_color ('none')
           ax.spines['top'].set_color ('none')
           ax.xaxis.set_ticks_position ('bottom')
           ax.yaxis.set_ticks_position ('left')
           plt.plot (x,(f[2]-f[0]*x)/f[1], '-r', label='eq1')
           plt.plot (x, g[2]-g[0]*x/g[1], '-g', label='eq2')
           plt.plot (z,label="solution", marker='o', markerfacecolor='blue', markersize=9)
           #plt.plot (x, 2 * x + 3, ':b', label='y=2x+3')
           #plt.plot (x, 2 * x - 3, '--m', label='y=2x-3')
           plt.legend (loc='upper left')
           plt.show ()
           

        if re.search('(-)?[\d]{1,}x[\+|-][\d]{1,}y[\+|-][\d]{1,}z=-?[\d]{1,}',s):
           p=re.findall('-?[\d]{1,}',s) 
           a=p[:4]
           b=p[4:8]
           c=p[8:]
           x,y,z=sp.symbols('x y z')
           d=Matrix((a,b,c))
           ans=solve_linear_system(d,x,y,z)          
           e1.delete(0,END)
           e1.insert(0,ans)
           talk()
           
        if re.search('\(x\+?-?([\d]{1,})\)\^2\+\(y\+?-?([\d]{1,})\)\^2=-?([\d]{1,})',s):
                a=re.findall('-?[\d]{1,}',s)
                d=list(map(int,a))
                d.pop(1)
                d.pop(2)
                b=d[:2]
                c=list(map(lambda i:i*(-1),b))
                c.append(d[2])
                e=c[0]
                f=c[1]
                g=c[2]
                ez={}
                ez['equation']='circle'
                ez['center']=(c[0],c[1])
                ez['radius']=math.sqrt(g)
                e1.delete(0,END)
                e1.insert(0,ez)
                talk()
                import matplotlib.pyplot as plt
                circle1=plt.Circle((c[0],c[1]),c[2], color='r')
                fig, ax = plt.subplots()
                plt.xlim(-50,50) 
                plt.ylim(-50,50)
                plt.grid(linestyle='--')
                ax.set_aspect(1)
                ax.add_artist(circle1)
                plt.show()
                
        if re.search('y\^2=-?[\d]{1,}x',s):
                v=re.findall('-?[\d]{1,}',s)
                d=list(map(int,v))
                d.remove(2)
                ez={}
                ez['equation']='parabola'
                ez['vertex']=(0,0)
                ez['focus']=(d[0]/4,0)
                e1.delete(0,END)
                e1.insert(0,ez)
                talk()
                import matplotlib.pyplot as plt
                a=[]
                b=[]
                for x in range(-50,50,1):
                     y=4*(d[0])*x**2
                     a.append(x)
                     b.append(y)
                fig= plt.figure()
                axes=fig.add_subplot(111)
                axes.plot(a,b)
                plt.grid(linestyle='--')
                plt.show()
                
        if re.search('x\^2=-?([\d]{1,})y',s):
                v=re.findall('-?[\d]{1,}',s)
                d=list(map(int,v))
                d.remove(2)
                ez={}
                ez['equation']='parabola'
                ez['vertex']=(0,0)
                ez['focus']=(0,d[0]/4)
                e1.delete(0,END)
                e1.insert(0,ez)
                talk()
                talk()
                import matplotlib.pyplot as plt
                a=[]
                b=[]
                for x in range(-50,50,1):
                     y=4*(d[0])*x**2
                     a.append(y)
                     b.append(x)
                fig= plt.figure()
                axes=fig.add_subplot(111)
                axes.plot(a,b)
                plt.grid(linestyle='--')
                plt.show()
                

b1=Button(root,text='1',padx=10,pady=5,relief=RAISED,fg="white",bg="black",command=lambda:click("1")).grid(row=5,column=1,ipadx=42)
b2=Button(root,text='2',padx=10,pady=5,relief=RAISED,fg="white",bg="black",command=lambda:click("2")).grid(row=5,column=2,ipadx=42)
b3=Button(root,text='3',padx=11,pady=5,relief=RAISED,fg='white',bg="black",command=lambda:click("3")).grid(row=5,column=3,ipadx=42)
b4=Button(root,text='4',padx=10,pady=5,relief=RAISED,fg='white',bg="black",command=lambda:click("4")).grid(row=4,column=1,ipadx=42)
b5=Button(root,text='5',padx=10,pady=5,relief=RAISED,fg='white',bg="black",command=lambda:click("5")).grid(row=4,column=2,ipadx=42)
b6=Button(root,text='6',padx=11,pady=5,relief=RAISED,fg='white',bg="black",command=lambda:click("6")).grid(row=4,column=3,ipadx=42)
b7=Button(root,text='7',padx=10,pady=5,relief=RAISED,fg='white',bg="black",command=lambda:click("7")).grid(row=3,column=1,ipadx=42)
b8=Button(root,text='8',padx=10,pady=5,relief=RAISED,fg='white',bg="black",command=lambda:click("8")).grid(row=3,column=2,ipadx=42)
b9=Button(root,text='9',padx=11,pady=5,relief=RAISED,fg='white',bg="black",command=lambda:click("9")).grid(row=3,column=3,ipadx=42)
b0=Button(root,text='0',padx=27,pady=5,relief=RAISED,fg='white',bg="black",command=lambda:click("0")).grid(row=6,column=1,columnspan=2,ipadx=84)

badd=Button(root,text='+',padx=10,pady=5,fg='black',bg='grey',command=add).grid(row=3,column=4,ipadx=42)
bsub=Button(root,text='-',padx=11,pady=5,fg='black',bg='grey',command=sub).grid(row=4,column=4,ipadx=42)
bmul=Button(root,text='*',padx=11,pady=5,fg='black',bg='grey',command=mul).grid(row=5,column=4,ipadx=42)
bdiv=Button(root,text='/',padx=11,pady=5,fg='black',bg='grey',command=div).grid(row=6,column=4,ipadx=42)
bc=Button(root,text='=',padx=10,pady=5,fg='black',bg='orange',command=eqs).grid(row=6,column=3,ipadx=42)

bc=Button(root,text='C',padx=10,pady=5,bg='grey',command=cls).grid(row=2,column=3,ipadx=42)
bc=Button(root,text='AC',padx=6,pady=5,bg='red',fg='black',command=clear).grid(row=2,column=4,ipadx=42)

bc=Button(root,text='x',padx=11,pady=5,fg='black',bg='blue',command=lambda : click('x')).grid(row=4,column=0,ipadx=42)
bc=Button(root,text='y',padx=11,pady=5,fg='black',bg='blue',command=lambda : click('y')).grid(row=5,column=0,ipadx=42)
bc=Button(root,text='z',padx=11,pady=5,fg='black',bg='blue',command=lambda : click('z')).grid(row=6,column=0,ipadx=42)

bc=Button(root,text=',',padx=12,pady=5,bg='blue',command=lambda : click(',')).grid(row=3,column=0,ipadx=42)
bc=Button(root,text='^',padx=9,pady=5,bg='blue',command=lambda : click('^')).grid(row=2,column=0,ipadx=42)

bc=Button(root,text='(',padx=11,pady=5,bg='blue',command=lambda : click('(')).grid(row=2,column=1,ipadx=42)
bc=Button(root,text=')',padx=11,pady=5,bg='blue',command=lambda : click(')')).grid(row=2,column=2,ipadx=42)

bc=Button(root,text='Solve',padx=71,pady=5,bg='light green',command=solve).grid(row=11,column=0,columnspan=5,ipadx=210)
bc=Button(root,text='speak',padx=71,pady=5,bg='dark green',command=talk).grid(row=12,column=0,columnspan=5,ipadx=210)

root.mainloop()    






























