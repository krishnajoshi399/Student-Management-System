from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from sqlite3 import *
import pandas as pd
import matplotlib.pyplot as plt
import itertools
import socket
import requests
import bs4


def add():
        adst.deiconify()
        root.withdraw()
        adst_entRno.focus()

def save_add():
        con=True
        try:
                con=connect("Student_db.db")
                cur=con.cursor()
                sql="insert into student values('%d','%s','%f')"
                if(adst_entRno.get()==""):
                        raise Exception("please enter roll no ")
                if(not adst_entRno.get().isdigit() or int(adst_entRno.get())<1):
                        raise Exception("roll no should be positive integer")
                rno=int(adst_entRno.get())
                if(adst_entName.get()==""):
                        raise Exception("please enter student name")
                if(not adst_entName.get().isalpha() or len(adst_entName.get())<2):
                        raise Exception("invalid name")
                name=adst_entName.get()
                if(adst_entMarks.get()==""):
                        raise Exception("please enter student marks")
                if(not adst_entMarks.get().isdigit()):
                        raise Exception("marks must be in digits")
                marks=float(adst_entMarks.get())
                if(marks<0 or marks>100):
                        raise Exception("Marks must be in the range [1-100]")
                cur.execute(sql%(rno,name,marks))
                con.commit()
                showinfo("Succes","Record inserted")
        except Exception as e:
                con.rollback()
                showerror("Error",e)
        finally:
                if con is not None:
                        con.close()
        adst_entRno.delete(0,END)
        adst_entName.delete(0,END)
        adst_entMarks.delete(0,END)
        adst_entRno.focus()

def back_add():
        root.deiconify()
        adst.withdraw()

def view():
        root.withdraw()
        vist.deiconify()
        vist_stData.delete(1.0,END)
        con=True
        try:
                con=connect("student_db.db")
                cur=con.cursor()
                sql="SELECT * FROM student"
                cur.execute(sql)
                data=cur.fetchall()
                msg=""
                for d in data:
                        msg=msg+"rno = "+str(d[0])+"      name = "+str(d[1])+"      marks = "+str(d[2])+"\n"
                vist_stData.insert(INSERT,msg)
        except Exception as e:
                showerror("Error",e)
        finally:
                if con is not None:
                        con.close()
                                
def back_view():
        vist.withdraw()
        root.deiconify()

def update():
        updst.deiconify()
        root.withdraw()
        updst_entRno.focus()

def save_update():
        con=True
        try:
                con=connect("student_db.db")
                cur=con.cursor()
                sql="update student set name = '%s' , marks = '%s' where rno = '%s'"
                if(updst_entRno.get()==""):
                        raise Exception("please enter roll no")
                rno=int(updst_entRno.get())
                if(updst_entName.get()==""):
                        raise Exception("please enter student name")
                if(not updst_entName.get().isalpha() or len(updst_entName.get())<2):
                        raise Exception("invalid name")
                name=updst_entName.get()
                if(updst_entMarks.get()==""):
                        raise Exception("please enter student marks")
                if(not updst_entMarks.get().isdigit()):
                        raise Exception("marks must be in digits")
                marks=float(updst_entMarks.get())
                if(marks<0 or marks>100):
                        raise Exception("Marks out of range")
                cur.execute(sql%(name,marks,rno))
                if cur.rowcount>0:
                        con.commit()
                        showinfo("Succes","Record updated")
                else:
                        raise Exception("Record does not exists")
        except Exception as e:
                con.rollback()
                showerror("Error",e)
        finally:
                if con is not None:
                        con.close()
        updst_entRno.delete(0,END)
        updst_entName.delete(0,END)
        updst_entMarks.delete(0,END)
        updst_entRno.focus() 
       
def back_update():
        updst.withdraw()
        root.deiconify()

def delete():
        root.withdraw()
        delst.deiconify()
        delst_entRno.focus()
      
def save_delete():
        con=True
        try:
                con=connect("student_db.db")
                cur=con.cursor()
                sql="delete from student where rno = '%s'"
                if delst_entRno.get()=="":
                        raise Exception("please enter roll no")
                if(not delst_entRno.get().isdigit()):
                        raise Exception("roll no should be positive number")
                rno=int(delst_entRno.get())
                cur.execute(sql%(rno))
                if cur.rowcount>0:
                        con.commit()
                        showinfo("Sucess","Record deleted")
                else:
                        raise Exception("Record does not exists")
        except Exception as e:
                con.rollback()
                showerror("Error",e)
        delst_entRno.delete(0,END)
        delst_entRno.focus()
        
def back_delete():
        delst.withdraw()
        root.deiconify()

def charts():
        con=True
        try:
                name=[]
                marks=[]
                con=connect("student_db.db")
                cur=con.cursor()
                sql="select name from student"
                cur.execute(sql)
                r=cur.fetchall()
                name=list(itertools.chain(*r))
                sql="select marks from student"
                cur.execute(sql)
                r=cur.fetchall()
                marks=list(itertools.chain(*r))
                color1=["red","blue","yellow","green"]
                plt.bar(name,marks,linewidth=2,color=color1)
                plt.xlabel("NAMES")
                plt.ylabel("MARKS")
                plt.title("Batch Information")
                plt.show()       

        except Exception as e:
                showerror(" Chart Error",e)
        finally:
                if con is not None:
                        con.close()

def locationFunctn(locationLbl):
    try:
        google_url=("www.google.com",80)
        socket.create_connection(google_url)              
        web_url="https://ipinfo.io/"
        response=requests.get(web_url)
        # print(response) #200....-->correct , 4...-->error
        
        data=response.json()    
        city_name =data['city']
        locationLbl.config(text="Location: "+ city_name) 
        return city_name   
    except Exception as e:
        showerror("connection Issue: ",e)

def tempFunctn(tempLbl):
    try:
        google_url=("www.google.com",80)
        socket.create_connection(google_url)
        city=a
        a1="http://api.openweathermap.org/data/2.5/weather?units=metric"
        a2="&q="+city
        a3="&appid=c6e315d09197cec231495138183954bd"
        web_url=a1+a2+a3
        response =requests.get(web_url)   
        data=response.json()   
        main =data['main']
        temp1=main['temp']
        q=str(temp1)
        tempLbl.config(text="Temp:"+q)
    except OSError as e:
        showerror("Connection Issue: ",e)
    except KeyError as e:
        showinfo("check Location name ",e)

def quotdFunctn(quotdLbl):
    try:
        web_url="https://www.brainyquote.com/quote_of_the_day"
        res= requests.get(web_url)
        soup=bs4.BeautifulSoup(res.text,"html.parser")
        info=soup.find_all("img",{"class":"p-qotd"})
        quote=info[0]['alt']
        quotdLbl.config(text="QUOTD: "+quote)
    except Exception as e:
        showerror("Issue: ",e)




root=Tk()
root.title("Student Management System")
root.geometry("700x500+450+100")
root.resizable(True,False)
root.configure(background="light green");

btnAdd=Button(root,text="Add",width=12,font=("arial",18,"bold"),command=add)
btnAdd.pack(pady=10)
btnView=Button(root,text="View",width=12,font=("arial",18,"bold"),command=view)
btnView.pack(pady=10)
btnUpdate=Button(root,text="Update",width=12,font=("arial",18,"bold"),command=update)
btnUpdate.pack(pady=10)
btnDel=Button(root,text="Delete",width=12,font=("arial",18,"bold"),command=delete)
btnDel.pack(pady=10)
btnChart=Button(root,text="Charts",width=12,font=("arial",18,"bold"),command=charts)
btnChart.pack(pady=10)
locationLbl=Label(root,text="Location:",bg="light green",width=15,font=("arial",15,"bold"))
locationLbl.pack(pady=10,side=LEFT)
a=locationFunctn(locationLbl)
tempLbl=Label(root,text="Temp:",width=10,bg="light green",font=("arial",15,"bold"))
tempLbl.pack(pady=10,side=RIGHT)
tempFunctn(tempLbl)

quotdLbl=Label(root,text="QUOTD:",width=100,bg="light green",font=("arial",15,"bold"))
quotdLbl.pack(pady=10,side=LEFT)
quotdFunctn(quotdLbl)
quotdLbl.place(relx=0.0,rely=1.0,anchor='sw')

#Add record

adst=Toplevel(root)
adst.title("Add Student")
adst.geometry("400x500+450+100")
adst.resizable(False,False)
adst.configure(background="light blue")

adst_lblRno=Label(adst,text="enter rno:",bg="light blue",width=10,font=("arial",18,"bold"))
adst_lblRno.pack(pady=10)
adst_entRno=Entry(adst,bd=5,width=25,font=("arial",18,"bold"))
adst_entRno.pack(pady=10)
adst_lblName=Label(adst,text="enter name:",bg="light blue",width=10,font=("arial",18,"bold"))
adst_lblName.pack(pady=10)
adst_entName=Entry(adst,bd=5,width=25,font=("arial",18,"bold"))
adst_entName.pack(pady=10)
adst_lblMarks=Label(adst,text="enter marks:",bg="light blue",width=10,font=("arial",18,"bold"))
adst_lblMarks.pack(pady=10)
adst_entMarks=Entry(adst,bd=5,width=25,font=("arial",18,"bold"))
adst_entMarks.pack(pady=10)

adst_btnSave=Button(adst,text="Save",width=8,font=("arial",17,"bold"),command=save_add)
adst_btnSave.pack(pady=10)
adst_btnBack=Button(adst,text="Back",width=8,font=("arial",17,"bold"),command=back_add)
adst_btnBack.pack(pady=10)

adst.withdraw()

# View Record

vist=Toplevel(root)
vist.title("View Student")
vist.geometry("700x400+350+100")
vist.resizable(False,False)
vist.configure(background="rosy brown")

vist_stData=ScrolledText(vist,width=55,height=10,font=("arial",15,"bold"))
vist_stData.pack(pady=20)

vist_btnBack=Button(vist,text="Back",width=8,font=("arial",16,"bold"),command=back_view)
vist_btnBack.pack(pady=25)

vist.withdraw()

#Update record

updst=Toplevel(root)
updst.title("Update Student")
updst.geometry("400x500+450+100")
updst.resizable(False,False)
updst.configure(background="light yellow")

updst_lblRno=Label(updst,text="enter rno:",bg="light yellow",width=10,font=("arial",18,"bold"))
updst_lblRno.pack(pady=10)
updst_entRno=Entry(updst,bd=5,width=25,font=("arial",18,"bold"))
updst_entRno.pack(pady=10)
updst_lblName=Label(updst,text="enter name:",bg="light yellow",width=10,font=("arial",18,"bold"))
updst_lblName.pack(pady=10)
updst_entName=Entry(updst,bd=5,width=25,font=("arial",18,"bold"))
updst_entName.pack(pady=10)
updst_lblMarks=Label(updst,text="enter marks:",bg="light yellow",width=10,font=("arial",18,"bold"))
updst_lblMarks.pack(pady=10)
updst_entMarks=Entry(updst,bd=5,width=25,font=("arial",18,"bold"))
updst_entMarks.pack(pady=10)

updst_btnSave=Button(updst,text="Save",width=8,font=("arial",17,"bold"),command=save_update)
updst_btnSave.pack(pady=10)
updst_btnBack=Button(updst,text="Back",width=8,font=("arial",17,"bold"),command=back_update)
updst_btnBack.pack(pady=10)

updst.withdraw()

#Delete record

delst=Toplevel(root)
delst.title("Delete Student")
delst.geometry("400x300+450+100")
delst.resizable(False,False)
delst.configure(background="grey")

delst_lblRno=Label(delst,text="enter rno:",bg="grey",width=10,font=("arial",18,"bold"))
delst_lblRno.pack(pady=10)
delst_entRno=Entry(delst,bd=5,width=25,font=("arial",18,"bold"))
delst_entRno.pack(pady=10)
delst_btnSave=Button(delst,text="Save",width=8,font=("arial",17,"bold"),command=save_delete)
delst_btnSave.pack(pady=10)
delst_btnBack=Button(delst,text="Back",width=8,font=("arial",17,"bold"),command=back_delete)
delst_btnBack.pack(pady=10)
delst.withdraw()


root.mainloop()
