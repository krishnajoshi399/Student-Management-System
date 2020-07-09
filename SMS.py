from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from sqlite3 import *

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
                if(not adst_entRno.get().isdigit() or int(adst_entRno.get())<0):
                        raise Exception("roll no should be positive integer")
                rno=int(adst_entRno.get())
                if(adst_entName.get()==""):
                        raise Exception("please enter student name")
                if(not adst_entName.get().isalpha() or len(adst_entName.get())<2):
                        raise Exception("invalid name")
                name=adst_entName.get()
                if(adst_entMarks.get()==""):
                        raise Exception("please enter student marks")
                marks=float(adst_entMarks.get())
                if(marks<0 or marks>100):
                        raise Exception("Marks out of range")
                cur.execute(sql%(rno,name,marks))
                con.commit()
                showinfo("Succes","row inserted")
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
        vist_stData.delete('1.0',END)
        root.withdraw()
        vist.deiconify()
        con=True
        try:
                con=connect("student_db.db")
                cur=con.cursor()
                sql="SELECT * FROM student"
                cur.execute(sql)
                data=cur.fetchall()
                msg=""
                for d in data:
                        msg=msg+"rno = "+str(d[0])+",  name = "+str(d[1])+",  marks = "+str(d[2])+"\n"
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
                marks=float(updst_entMarks.get())
                if(marks<0 or marks>100):
                        raise Exception("Marks out of range")
                cur.execute(sql%(name,marks,rno))
                if cur.rowcount>0:
                        con.commit()
                        showinfo("Succes","row updated")
                else:
                        raise Exception("row does not exists")
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
                        showinfo("Sucess","row deleted")
                else:
                        raise Exception("row does not exists")
        except Exception as e:
                con.rollback()
                showerror("Error",e)
        delst_entRno.delete(0,END)
        delst_entRno.focus()
def back_delete():
        delst.withdraw()
        root.deiconify()


def charts():
        pass
        


root=Tk()
root.title("Student Management System")
root.geometry("400x500+450+100")
root.resizable(False,False)
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

#Add record

adst=Toplevel(root)
adst.title("Add Student")
adst.geometry("400x500+450+100")
adst.resizable(False,False)
adst.configure(background="light blue")

adst_lblRno=Label(adst,text="enter rno:",width=10,font=("arial",18,"bold"))
adst_lblRno.pack(pady=10)
adst_entRno=Entry(adst,bd=5,width=25,font=("arial",18,"bold"))
adst_entRno.pack(pady=10)
adst_lblName=Label(adst,text="enter name:",width=10,font=("arial",18,"bold"))
adst_lblName.pack(pady=10)
adst_entName=Entry(adst,bd=5,width=25,font=("arial",18,"bold"))
adst_entName.pack(pady=10)
adst_lblMarks=Label(adst,text="enter marks:",width=10,font=("arial",18,"bold"))
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

updst_lblRno=Label(updst,text="enter rno:",width=10,font=("arial",18,"bold"))
updst_lblRno.pack(pady=10)
updst_entRno=Entry(updst,bd=5,width=25,font=("arial",18,"bold"))
updst_entRno.pack(pady=10)
updst_lblName=Label(updst,text="enter name:",width=10,font=("arial",18,"bold"))
updst_lblName.pack(pady=10)
updst_entName=Entry(updst,bd=5,width=25,font=("arial",18,"bold"))
updst_entName.pack(pady=10)
updst_lblMarks=Label(updst,text="enter marks:",width=10,font=("arial",18,"bold"))
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

delst_lblRno=Label(delst,text="enter rno:",width=10,font=("arial",18,"bold"))
delst_lblRno.pack(pady=10)
delst_entRno=Entry(delst,bd=5,width=25,font=("arial",18,"bold"))
delst_entRno.pack(pady=10)
delst_btnSave=Button(delst,text="Save",width=8,font=("arial",17,"bold"),command=save_delete)
delst_btnSave.pack(pady=10)
delst_btnBack=Button(delst,text="Back",width=8,font=("arial",17,"bold"),command=back_delete)
delst_btnBack.pack(pady=10)
delst.withdraw()


root.mainloop()
