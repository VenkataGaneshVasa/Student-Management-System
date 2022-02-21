# In order to run this code tkinter,sqlite3,sys packages must be installed on your hardware/server
from tkinter import *
import sqlite3
import sys

window=Tk()
window.title("Student Management System")
window.geometry("700x500")

#below commented code should be run for once to create db and tables to store data entered by users
'''
conn = sqlite3.connect("student_database_system.db")
c = conn.cursor()
c.execute("CREATE TABLE coursedetails (coursecode TEXT, coursename TEXT)")
c.execute("CREATE TABLE studentdetails (studentid INT, studentname TEXT)")
c.execute("CREATE TABLE resultdetails (coursecode TEXT, studentid INT, marks INT)")
c.execute("CREATE TABLE coursecodes (coursecode TEXT)")
conn.commit()
conn.close()
'''

def coursesubmit():
    coursecode = e1.get()
    coursename = e2.get()

    conn = sqlite3.connect("student_database_system.db")
    c = conn.cursor()
    c.execute("INSERT INTO coursedetails VALUES('"+coursecode+"','"+coursename+"')")
    print("course details submitted")
    conn.commit()
    conn.close()

def studentsubmit():
    studentid = e3.get()
    studentname = e4.get()

    conn = sqlite3.connect("student_database_system.db")
    c = conn.cursor()
    c.execute("INSERT INTO studentdetails VALUES("+studentid+",'"+studentname+"')")
    print("student details submitted")
    conn.commit()
    conn.close()

def resultsubmit():
    coursecode = e6.get()
    studentid = e5.get()
    marks = e7.get()
    
    conn = sqlite3.connect("student_database_system.db")
    c = conn.cursor()
    c.execute("INSERT INTO resultdetails VALUES('"+coursecode+"',"+studentid+","+marks+")")
    print("result data submitted")
    conn.commit()
    conn.close()



def addcourse():
    page1=Tk()
    page1.title("Add course page")
    page1.geometry("700x500")

    label2=Label(page1, text="Enter course code", font = "time 15 bold", fg="blue")
    label2.place(x=10,y=50)

    label3=Label(page1, text="Enter course name", font = "time 15 bold", fg="blue")
    label3.place(x=10,y=130)
    global e1
    e1 = Entry(page1)
    e1.place(x=250, y=55)
    global e2
    e2 = Entry(page1)
    e2.place(x=250, y=135)

    b6 = Button(page1, text=" Submit ", font="time 10 bold", width=30, bg="blue", fg="white", command=coursesubmit)
    b6.place(x=100, y=200)

def addstudent():
    page2=Tk()
    page2.title("Add student page")
    page2.geometry("700x500")

    label4=Label(page2, text="Enter student id", font = "time 15 bold", fg="blue")
    label4.place(x=10,y=50)

    label5=Label(page2, text="Enter student name", font = "time 15 bold", fg="blue")
    label5.place(x=10,y=130)
    global e3
    e3 = Entry(page2)
    e3.place(x=250, y=55)
    global e4
    e4 = Entry(page2)
    e4.place(x=250, y=135)

    b7 = Button(page2, text=" Submit ", font="time 10 bold", width=30, bg="blue", fg="white", command=studentsubmit)
    b7.place(x=100, y=200)


def addresult():
    page3=Tk()
    page3.title("Add result page")
    page3.geometry("700x500")

    label6=Label(page3, text="Enter student id", font = "time 15 bold", fg="blue")
    label6.place(x=10,y=50)

    label7=Label(page3, text="Enter course code", font = "time 15 bold", fg="blue")
    label7.place(x=10,y=130)

    label8=Label(page3, text="Enter marks obtained", font = "time 15 bold", fg="blue")
    label8.place(x=10,y=210)
    global e5
    e5 = Entry(page3)
    e5.place(x=250, y=55)
    global e6
    e6 = Entry(page3)
    e6.place(x=250, y=135)
    global e7
    e7 = Entry(page3)
    e7.place(x=280, y=215)

    b8 = Button(page3, text=" Submit ", font="time 10 bold", width=30, bg="blue", fg="white", command=resultsubmit)
    b8.place(x=100, y=280)


def quit():
    print("Thank you for using the system")
    sys.exit()


def viewresults():
    page4=Tk()
    page4.title("View results page")
    page4.geometry("700x500")

    b9 = Button(page4, text="View course results", font="time 10 bold", width=30, bg="blue", fg="white", command = courseresults)
    b9.place(x=180, y=100)

    b10 = Button(page4, text="View student results", font="time 10 bold", width=30, bg="blue", fg="white", command = studentresults)
    b10.place(x=180, y=200)

def courseresults():
    page5=Tk()
    page5.title("Course results page")
    page5.geometry("700x500")
    label=Label(page5, text="Course results", font = "time 15 bold", bg="blue", fg="white", padx=268, pady=10)
    label.grid(row = 0, column = 0, columnspan=20)

    p1=Label(page5, text="Name", font="time 10 bold")
    p1.grid(row=1, column=0, padx =10, pady=10)

    p2 = Label(page5, text="Course code", font="time 10 bold")
    p2.grid(row=1, column=8, padx=10, pady=10)

    p3 = Label(page5, text="Marks", font="time 10 bold")
    p3.grid(row=1, column=15, padx=10, pady=10)


    
    conn = sqlite3.connect("student_database_system.db")
    c = conn.cursor()
    c.execute("SELECT studentdetails.studentname, resultdetails.coursecode, resultdetails.marks FROM studentdetails INNER JOIN resultdetails ON studentdetails.studentid = resultdetails.studentid ")
    r=c.fetchall()
    num = 2
    for i in r:
        coursecode=Label(page5, text=i[0], font ="time 8 bold", fg="blue")
        coursecode.grid(row=num, column=0, padx=10, pady=10)

        studentid=Label(page5, text=i[1], font="time 8 bold", fg="blue")
        studentid.grid(row=num, column=8, padx=10, pady=10)

        studentid=Label(page5, text=i[2], font="time 8 bold", fg="blue")
        studentid.grid(row=num, column=15, padx=10, pady=10)
        
        num=num+1

    conn.commit()
    conn.close()





def studentresults():
    page6=Tk()
    page6.title("Student results page")
    page6.geometry("700x500")
    label=Label(page6, text="Student results", font = "time 15 bold", bg="blue", fg="white", padx=268, pady=10)
    label.grid(row = 0, column = 0, columnspan=20)

    p4=Label(page6, text="Student id", font="time 10 bold")
    p4.grid(row=1, column=0, padx =10, pady=10)

    p5 = Label(page6, text="Student Name", font="time 10 bold")
    p5.grid(row=1, column=3, padx=10, pady=10)

    p6 = Label(page6, text="Course code", font="time 10 bold")
    p6.grid(row=1, column=6, padx=10, pady=10)

    p7 = Label(page6, text="Marks", font="time 10 bold")
    p7.grid(row=1, column=9, padx=10, pady=10)

    conn = sqlite3.connect("student_database_system.db")
    c = conn.cursor()
    c.execute("SELECT studentdetails.studentid, studentdetails.studentname, resultdetails.coursecode, resultdetails.marks FROM studentdetails INNER JOIN resultdetails ON studentdetails.studentid = resultdetails.studentid")
    r=c.fetchall()
    num = 3
    for i in r:
        coursecode=Label(page6, text=i[0], font ="time 8 bold", fg="blue")
        coursecode.grid(row=num, column=0, padx=10, pady=10)

        studentid=Label(page6, text=i[1], font="time 8 bold", fg="blue")
        studentid.grid(row=num, column=3, padx=10, pady=10)

        marks=Label(page6, text=i[2], font="time 8 bold", fg="blue")
        marks.grid(row=num, column=6, padx=10, pady=10)

        marks=Label(page6, text=i[3], font="time 8 bold", fg="blue")
        marks.grid(row=num, column=9, padx=10, pady=10)

        num=num+1

    conn.commit()
    conn.close()








label1=Label(window,text="Student Management System",fg="blue",font="times 28 bold")
label1.place(x=350,y=20,anchor="center")

b1=Button(window,text="1) Add a course",font = "time 10 bold",width=20,bg="blue", fg="white", command=addcourse)
b1.place(x=350,y=100,anchor="center")

b2=Button(window,text="2) Add a student",font = "time 10 bold",width=20,bg="blue", fg="white", command=addstudent)
b2.place(x=350,y=170,anchor="center")

b3=Button(window,text="3) Add a result",font = "time 10 bold",width=20,bg="blue", fg="white", command=addresult)
b3.place(x=350,y=240,anchor="center")

b4=Button(window,text="4) View results",font = "time 10 bold",width=20,bg="blue", fg="white", command=viewresults)
b4.place(x=350,y=310,anchor="center")

b5=Button(window,text="5) Quit",font = "time 10 bold",width=20,bg="blue", fg="white", command=quit)
b5.place(x=350,y=380,anchor="center")

window.mainloop()