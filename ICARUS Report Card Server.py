#Main Program for creating, accessing and manipulating data stored in REPORT CARD
def Teacher(): # For Teacher to log in using master password
    try:
        wel.destroy()
    except:
        pass
    try:
        suc.destroy()
    except:
        pass

    tch=Tk()
    tch.geometry('500x250')
    tch.title('Teacher Mode')

    passwd=StringVar()

    def printt():   #Commands to be executed after 'Login' Button is selected
        password=passwd.get()
        a="select count(*) from maspass where Password=%s"
        b=(password,)
        c.execute(a,b)
        data1=c.fetchone()
        if data1[0]!=0:

            tch.destroy()

            global suc
            suc=Tk()
            suc.geometry('500x250')
            suc.title("Teacher Mode")

            labH=Label(suc,text="Login Successful",fg='blue',font=("Bold",30)).place(x=120,y=50)
            but1=Button(suc,text="Create Student Account",bg='black',fg='white',command=Sign_Up).place(x=80,y=150)
            but2=Button(suc,text="View Student Details",bg='black',fg='white',command=Tlogin).place(x=240,y=150)
            but3=Button(suc,text="Exit",bg='black',fg='white',command=exitt).place(x=400,y=150)
            
        else:
            lab11=Label(tch,text='Invalid Password',fg='red').place(x=200,y=150)
    

    lab0=Label(tch,text="Teacher Login",fg='blue',font=("Bold",20))
    lab0.place(x=150,y=50)

    lab1=Label(tch,text="Master Password:",font=(10))
    lab1.place(x=80,y=120)
    ent1=Entry(tch,textvar=passwd)
    ent1.place(x=260,y=120)

    but1=Button(tch,text="Login",bg='black',fg='white',command=printt).place(x=200,y=200)
    but2=Button(tch,text="Exit",bg='black',fg='white',command=exitt).place(x=280,y=200)

    
def Tlogin():                           #For Teacher to access student's report card
    try:
        suc.destroy()
    except:
        pass
    try:
        wel.destroy()
    except:
        pass
    global log
    log=Tk()
    log.geometry('400x300')
    log.title("Teacher Mode")

    adm=StringVar()

    def printt():         #Commands to be executed after 'View' Button is selected
        admno=adm.get()
        a="select count(*) from marks where Admission_Number=%s"
        b=(admno,)
        c.execute(a,b)
        data1=c.fetchone()
        if data1[0]!=0:
            log.destroy()
            a="select * from marks where Admission_Number=%s"
            b=(admno,)
            c.execute(a,b)
            data2=c.fetchone()
            l=[]
            for i in data2:
                l.append(i)
            global rep
            rep=Tk()
            rep.geometry('500x600')
            rep.title("Teacher Mode")

            labH=Label(rep,text="Report Card",font=("Bold",20)).place(x=90,y=50)

            lab31=Label(rep,text="Admission No:").place(x=80,y=140)
            lab32=Label(rep,text=l[0]).place(x=240,y=142)
            global an
            an=l[0]

            lab41=Label(rep,text="Name:").place(x=80,y=180)
            lab42=Label(rep,text=l[1]).place(x=240,y=182)

            lab51=Label(rep,text="DoB:").place(x=80,y=220)
            lab52=Label(rep,text=l[2]).place(x=240,y=222)

            lab61=Label(rep,text="English:").place(x=80,y=260)
            lab62=Label(rep,text=l[3]).place(x=240,y=262)

            lab71=Label(rep,text="Computer:").place(x=80,y=300)
            lab72=Label(rep,text=l[4]).place(x=240,y=302)

            lab81=Label(rep,text="Mathematics:").place(x=80,y=340)
            lab82=Label(rep,text=l[5]).place(x=240,y=342)

            lab91=Label(rep,text="Physics:").place(x=80,y=380)
            lab92=Label(rep,text=l[6]).place(x=240,y=382)

            lab101=Label(rep,text="Chemistry:").place(x=80,y=420)
            lab102=Label(rep,text=l[7]).place(x=240,y=422)

            but2=Button(rep,text="Exit",bg='black',fg='white',command=exitt).place(x=80,y=500)
            but3=Button(rep,text="Edit",bg='black',fg='white',command=Edit).place(x=160,y=500)
            but4=Button(rep,text="Delete",bg='black',fg='white',command=Delete).place(x=240,y=500)
            
        else:
            lab11=Label(log,text='Invalid Admission Number',fg='red').place(x=150,y=250)

    lab0=Label(log,text="View Student Details",fg='blue',font=("Bold",20))
    lab0.place(x=70,y=50)

    lab1=Label(log,text="Admission Number:",font=(10))
    lab1.place(x=45,y=140)
    ent1=Entry(log,textvar=adm)
    ent1.place(x=230,y=142)

    but1=Button(log,text="View",bg='black',fg='white',command=printt).place(x=150,y=200)
    but3=Button(log,text="Exit",bg='black',fg='white',command=exitt).place(x=240,y=200)

def Login():                           #For Student to  log in to access report card
    try:
        suc.destroy()
    except:
        pass
    try:
        wel.destroy()
    except:
        pass
    global log
    log=Tk()
    log.geometry('500x400')
    log.title("Student Mode")

    adm=StringVar()
    passwd=StringVar()

    def printt():         #Commands to be executed after 'Login' Button is selected
        admno=adm.get()
        password=passwd.get()
        a="select count(*) from passwd where Admission_Number=%s and Password=%s"
        b=(admno,password)
        c.execute(a,b)
        data1=c.fetchone()
        if data1[0]!=0:
            log.destroy()
            a="select * from marks where Admission_Number=%s"
            b=(admno,)
            c.execute(a,b)
            data2=c.fetchone()
            l=[]
            for i in data2:
                l.append(i)
            global rep
            rep=Tk()
            rep.geometry('500x600')
            rep.title("Student Mode")

            labH=Label(rep,text="Report Card",font=("Bold",20)).place(x=90,y=50)

            lab31=Label(rep,text="Admission No:").place(x=80,y=140)
            lab32=Label(rep,text=l[0]).place(x=240,y=142)
            global an
            an=l[0]

            lab41=Label(rep,text="Name:").place(x=80,y=180)
            lab42=Label(rep,text=l[1]).place(x=240,y=182)

            lab51=Label(rep,text="DoB:").place(x=80,y=220)
            lab52=Label(rep,text=l[2]).place(x=240,y=222)

            lab61=Label(rep,text="English:").place(x=80,y=260)
            lab62=Label(rep,text=l[3]).place(x=240,y=262)

            lab71=Label(rep,text="Computer:").place(x=80,y=300)
            lab72=Label(rep,text=l[4]).place(x=240,y=302)

            lab81=Label(rep,text="Mathematics:").place(x=80,y=340)
            lab82=Label(rep,text=l[5]).place(x=240,y=342)

            lab91=Label(rep,text="Physics:").place(x=80,y=380)
            lab92=Label(rep,text=l[6]).place(x=240,y=382)

            lab101=Label(rep,text="Chemistry:").place(x=80,y=420)
            lab102=Label(rep,text=l[7]).place(x=240,y=422)

            but2=Button(rep,text="Exit",bg='black',fg='white',command=exitt).place(x=160,y=500)
            
        else:
            lab11=Label(log,text='Invalid Admission Number or Password',fg='red').place(x=150,y=350)

    lab0=Label(log,text="Login",fg='blue',font=("Bold",20))
    lab0.place(x=220,y=50)

    lab1=Label(log,text="Admission Number:",font=(10))
    lab1.place(x=80,y=140)
    ent1=Entry(log,textvar=adm)
    ent1.place(x=260,y=142)

    lab2=Label(log,text="Password:",font=(10))
    lab2.place(x=80,y=180)
    ent2=Entry(log,textvar=passwd)
    ent2.place(x=260,y=182)

    but1=Button(log,text="Login",bg='black',fg='white',command=printt).place(x=100,y=250)
    but2=Button(log,text="Forgot Password",bg='black',fg='white',command=Reset).place(x=200,y=250)
    but3=Button(log,text="Exit",bg='black',fg='white',command=exitt).place(x=350,y=250)

def Sign_Up():       #For creating a new account to store marks in report card
    try:
        suc.destroy()
    except:
        pass
    
    sig=Tk()
    sig.geometry('500x600')
    sig.title("Teacher Mode")

    ad=StringVar()
    nam=StringVar()
    do=StringVar()
    en=StringVar()
    com=StringVar()
    ma=StringVar()
    ph=StringVar()
    ch=StringVar()
    pa=StringVar()

    def sign():          #Commands to be executed after 'Create' Button is selected
        adm=ad.get()
        name=nam.get()
        dob=do.get()
        eng=en.get()
        comp=com.get()
        math=ma.get()
        phy=ph.get()
        chem=ch.get()
        passwd=pa.get()

        a="Insert into marks values(%s,%s,%s,%s,%s,%s,%s,%s)"
        b=(adm,name,dob,eng,comp,math,phy,chem)
        c.execute(a,b)
        a="Insert into passwd values(%s,%s)"
        b=(adm,passwd)
        c.execute(a,b)
        con.commit()

        sig.destroy()

        global suc
        suc=Tk()
        suc.geometry('500x250')
        suc.title("Teacher Mode")

        labH=Label(suc,text="Created Successfully",fg='blue',font=("Bold",30)).place(x=70,y=50)
        but2=Button(suc,text="Home",bg='black',fg='white',command=Teacher).place(x=150,y=150)
        but3=Button(suc,text="Exit",bg='black',fg='white',command=exitt).place(x=250,y=150)

    lab0=Label(sig,text="Create New Account",fg='blue',font=("Bold",20)).place(x=70,y=50)

    lab1=Label(sig,text="Admission Number:").place(x=80,y=140)
    ent1=Entry(sig,textvar=ad).place(x=240,y=142)

    lab2=Label(sig,text="Name:").place(x=80,y=180)
    ent2=Entry(sig,textvar=nam).place(x=240,y=182)

    lab3=Label(sig,text="DoB(YYYY-MM-DD):").place(x=80,y=220)
    ent3=Entry(sig,textvar=do).place(x=240,y=222)

    lab4=Label(sig,text="English Marks:").place(x=80,y=260)
    ent4=Entry(sig,textvar=en).place(x=240,y=262)

    lab5=Label(sig,text="Computer Marks:").place(x=80,y=300)
    ent5=Entry(sig,textvar=com).place(x=240,y=302)

    lab6=Label(sig,text="Mathematics Marks:").place(x=80,y=340)
    ent6=Entry(sig,textvar=ma).place(x=240,y=342)

    lab7=Label(sig,text="Physics Marks:").place(x=80,y=380)
    ent7=Entry(sig,textvar=ph).place(x=240,y=382)

    lab8=Label(sig,text="Chemistry Marks:").place(x=80,y=420)
    ent8=Entry(sig,textvar=ch).place(x=240,y=422)

    lab9=Label(sig,text="Password:").place(x=80,y=460)
    ent9=Entry(sig,textvar=pa).place(x=240,y=462)

    but1=Button(sig,text="Create",bg='black',fg='white',command=sign).place(x=150,y=525)
    but2=Button(sig,text="Exit",bg='black',fg='white',command=exitt).place(x=250,y=525)
    
def Reset():      #To reset password incase forgotten

    log.destroy()
    
    global res
    res=Tk()
    res.geometry('500x400')
    res.title("Student Mode")

    ad=StringVar()
    do=StringVar()
    pa1=StringVar()
    pa2=StringVar()

    def confirm():       #Commands to be executed after 'Reset Password' Button is selected
        adm=ad.get()
        dob=do.get()
        pass1=pa1.get()
        pass2=pa2.get()

        a="select count(*) from marks where Admission_Number=%s and DoB=%s"
        b=(adm,dob)
        c.execute(a,b)
        data1=c.fetchone()

        if data1[0]==0:
            lab5=Label(res,text="Incorrect Admission Number or DoB",fg='red',font=(10)).place(x=70,y=300)
        elif data1[0]!=0 and pass1!=pass2:
            lab5=Label(res,text="Passwords Do Not Match. Please Try Again",fg='red',font=(10)).place(x=50,y=300)
        else:
            res.destroy()
            a="Update passwd set password=%s where Admission_Number=%s"
            b=(pass1,adm)
            c.execute(a,b)
            con.commit()

            global suc
            suc=Tk()
            suc.geometry('600x250')
            suc.title("Student Mode")

            labH=Label(suc,text="Password Reset Successful",fg='blue',font=("Bold",30)).place(x=70,y=50)
            but2=Button(suc,text="Login",bg='black',fg='white',command=Login).place(x=200,y=150)
            but3=Button(suc,text="Exit",bg='black',fg='white',command=exitt).place(x=300,y=150)
            
            

    lab0=Label(res,text="Reset Password",fg='blue',font=("Bold",20))
    lab0.place(x=150,y=50)

    lab1=Label(res,text="Admission Number:",font=(10))
    lab1.place(x=80,y=140)
    ent1=Entry(res,textvar=ad)
    ent1.place(x=260,y=142)

    lab2=Label(res,text="DoB:",font=(10))
    lab2.place(x=80,y=180)
    ent2=Entry(res,textvar=do)
    ent2.place(x=260,y=182)

    lab3=Label(res,text="Enter Password:",font=(10))
    lab3.place(x=80,y=220)
    ent3=Entry(res,textvar=pa1)
    ent3.place(x=260,y=222)

    lab4=Label(res,text="Confirm Password:",font=(10))
    lab4.place(x=80,y=260)
    ent4=Entry(res,textvar=pa2)
    ent4.place(x=260,y=262)

    but1=Button(res,text="Reset Password",bg='black',fg='white',command=confirm,font=(15)).place(x=150,y=330)

def Edit():        #To modify the marks in report card
    rep.destroy()
    ed=Tk()
    ed.geometry('500x400')
    ed.title("Teacher Mode")

    en=StringVar()
    com=StringVar()
    ma=StringVar()
    ph=StringVar()
    ch=StringVar()

    def conf():        #Commands to be executed after 'Confirm' Button is selected
        eng=en.get()
        comp=com.get()
        math=ma.get()
        phy=ph.get()
        chem=ch.get()

        ed.destroy()
        
        a='update marks set english=%s where admission_number=%s'
        b=(eng,an)
        c.execute(a,b)

        a='update marks set mathematics=%s where admission_number=%s'
        b=(math,an)
        c.execute(a,b)

        a='update marks set computer=%s where admission_number=%s'
        b=(comp,an)
        c.execute(a,b)

        a='update marks set physics=%s where admission_number=%s'
        b=(phy,an)
        c.execute(a,b)

        a='update marks set chemistry=%s where admission_number=%s'
        b=(chem,an)
        c.execute(a,b)

        con.commit()

        global suc
        suc=Tk()
        suc.geometry('600x250')
        suc.title("Teacher Mode")

        labH=Label(suc,text="Edition Successful",fg='blue',font=("Bold",30)).place(x=120,y=50)
        but2=Button(suc,text="Home",bg='black',fg='white',command=Teacher).place(x=200,y=150)
        but3=Button(suc,text="Exit",bg='black',fg='white',command=exitt).place(x=300,y=150)

    lab0=Label(ed,text="Edit",fg='blue',font=("Bold",20)).place(x=220,y=50)

    lab1=Label(ed,text="English Marks:").place(x=80,y=140)
    ent1=Entry(ed,textvar=en).place(x=240,y=142)

    lab2=Label(ed,text="Computer Marks").place(x=80,y=180)
    ent2=Entry(ed,textvar=com).place(x=240,y=182)

    lab3=Label(ed,text="Mathematics Marks:").place(x=80,y=220)
    ent3=Entry(ed,textvar=ma).place(x=240,y=222)

    lab4=Label(ed,text="Physics Marks:").place(x=80,y=260)
    ent4=Entry(ed,textvar=ph).place(x=240,y=262)

    lab5=Label(ed,text="Chemistry Marks:").place(x=80,y=300)
    ent5=Entry(ed,textvar=ch).place(x=240,y=302)

    but1=Button(ed,text="Confirm",bg='black',fg='white',command=conf).place(x=200,y=350)
    
def Delete():        #To delete an individual's report card from the database
    
    dl=Tk()
    dl.geometry('450x250')
    dl.title("Teacher Mode")

    def delete():         #Commands to be executed after 'Yes' Button is selected

        rep.destroy()
        dl.destroy()

        a="Delete from marks where Admission_Number=%s"
        b=(an,)
        c.execute(a,b)

        a="Delete from passwd where Admission_Number=%s"
        b=(an,)
        c.execute(a,b)

        con.commit()

        global suc
        suc=Tk()
        suc.geometry('600x250')
        suc.title("Teacher Mode")

        labH=Label(suc,text="Deletion Successful",fg='blue',font=("Bold",30)).place(x=120,y=50)
        but2=Button(suc,text="Home",bg='black',fg='white',command=Teacher).place(x=200,y=150)
        but3=Button(suc,text="Exit",bg='black',fg='white',command=exitt).place(x=300,y=150)
        
    lab_1=Label(dl,text="Are you sure you want to delete?",fg='red',font=("Bold",20)).place(x=20,y=50)
    but_1=Button(dl,text="Yes",bg='black',fg='white',font=(15),command=delete).place(x=150,y=150)
    but_2=Button(dl,text="No",bg='black',fg='white',font=(15),command=dl.destroy).place(x=250,y=150)
    
def exitt():       #To exit from the python program when 'Exit' button is selected
        exit()

def Main():      #Main Function that is executed first when the program runs
    try:
        suc.destroy()
    except:
        pass
    global wel

    wel=Tk()
    wel.geometry('550x250')
    wel.title("ICARUS Report Card Server")
    lab_1=Label(wel,text="Welcome to\nICARUS Report Card Server ",fg='blue',font=("Bold",30)).place(x=15,y=30)
    but_1=Button(wel,text="Teacher",bg='black',fg='white',font=(15),command=Teacher).place(x=90,y=150)
    but_2=Button(wel,text="Student",bg='black',fg='white',font=(15),command=Login).place(x=240,y=150)
    but_3=Button(wel,text="Exit",bg='black',fg='white',font=(15),command=exitt).place(x=390,y=150)

from tkinter import *
import mysql.connector
con=mysql.connector.connect(host="localhost",user='root',passwd='12345678',database='School')
c=con.cursor()
Main()


