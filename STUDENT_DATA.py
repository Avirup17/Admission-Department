import MAIN_MENU
import ADMISSION
import STUDENT_DATA
import mysql.connector as co
def STU_MENU():
    while True:
        print("                                               ")
        print("......WELCOME TO JERMELS ACADEMY MANAGEMENT SYSTEM.....")
        print("1:ADD STUDENT RECORD")
        print("2:SHOW STUDENT DETAILS")
        print("3:SEARCH STUDENT RECORD")
        print("4:DELETE STUDENT RECORD")
        print("5:EDIT STUDENT RECORD")
        print("6:EXIT")
        print("                            ")
        choice=int(input("ENTER YOUR CHOICE="))
        print(" ")
        if choice==1:
            STUDENT_DATA.ADD_RECORDS()
        elif choice==2:
            STUDENT_DATA.SHOW_STU_DETAILS()
        elif choice==3:
            STUDENT_DATA.SEARCH_STU_DETAILS()
        elif choice==4:
            STUDENT_DATA.DELETE_STU_DETAILS()
        elif choice==5:
            STUDENT_DATA.EDIT_STU_DETAILS()
        elif choice==6:
            return
        else:
            print("ERROR;INVALID CHOICE")
def ADD_RECORDS():
    mycon=co.connect(host="localhost",user="root",password="avirup",database="ip")
    cursor=mycon.cursor()
    session=input("ENTER ACADEMIC SESSION(eg:2019-20)=")
    stname=input("ENTER STUDENT NAME =")
    stroll=int(input("ENTER STUDENT ROLL NUMBER ="))
    stclass=int(input("ENTER STUDENT CLASS ="))
    stsec=input("ENTER STUDENT SECTION =")
    sub2=input("ENTER 2st SUBJECT(HINDI/BENGALI) =")
    sub3=input("ENTER 3st SUBJECT =")
    sub4=input("ENTER 4st SUBJECT =")
    sub5=input("ENTER 5st SUBJECT =")
    sub6=input("ENTER 6st SUBJECT =")
    query="insert into student(session,stroll,stname,stclass,stsec,sub2,sub3,sub4,sub5,sub6)values('{}',{},'{}',{},'{}','{}','{}','{}','{}','{}')".format(session,stroll,stname,stclass,stsec,sub2,sub3,sub4,sub5,sub6)
    cursor.execute(query)
    mycon.commit()
    mycon.close()
    cursor.close()
    print("RECORD HAS BEEN SAVED")

def SEARCH_STU_DETAILS():
     mycon=co.connect(host="localhost",user="root",password="avirup",database="ip")
     cursor=mycon.cursor()
     ac=int(input("ENTER ROLL NUMBER="))
     cl=int(input("ENTER CLASS="))
     st="select * from student where stroll='%s' and stclass='%s'"%(ac,cl)
     cursor.execute(st)
     data=cursor.fetchall()
     print(data)
     
def SHOW_STU_DETAILS():
    mycon=co.connect(host="localhost",user="root",password="avirup",database="ip")
    cursor=mycon.cursor()
    cursor.execute("select * from student")
    data=cursor.fetchall()
    for row in data:
        print(row)

def DELETE_STU_DETAILS():
    try:
        mycon=co.connect(host="localhost",user="root",password="avirup",database="ip")
        cursor=mycon.cursor()
        ac=int(input("ENTER ROLL NUMBER ="))
        print(" ")
        cl=int(input("ENTER STUDENT CLASS="))
        st="delete from student where stroll='%s' and stclass='%s'"%(ac,cl)
        print(" ")
        cursor.execute(st)
        mycon.commit()
        print("DATA DELETED SUCCESSFULLY")
    except:
        print("ERROR")

def EDIT_STU_DETAILS():
    mycon=co.connect(host="localhost",user="root",password="avirup",database="ip")
    cursor=mycon.cursor()
    print("1=EDIT STUDENT NAME")
    print("2=EDIT STUDENT CLASS")
    print("3=EDIT STUDENT ROLL NUMBER")
    print("4=RETURN")
    choice=int(input("ENTER YOUR CHOICE ="))
    if choice==1:
        STUDENT_DATA.EDIT_STUDENT_NAME()
    elif choice==2:
        STUDENT_DATA.EDIT_STUDENT_CLASS()
    elif choice==3:
        STUDENT_DATA.EDIT_STUDENT_ROLL()
    elif choice==4:
            return
    else:
        print("ERROR:INVLAID CHOICE ENTERED")

def EDIT_STUDENT_NAME():
    mycon=co.connect(host="localhost",user="root",password="avirup",database="ip")
    cursor=mycon.cursor()
    ac=int(input("ENTER ROLL NUMBER="))
    cl=int(input("ENTER STUDENT CLASS="))
    nm=input("ENTER CORRECT NAME =")
    st="update student set stname='%s' where stroll='%s' and stclass='%s'"%(nm,ac,cl)
    cursor.execute(st)
    mycon.commit()
    print("DATA UPDATED SUCCESSFULLY")

def EDIT_STUDENT_CLASS():
    mycon=co.connect(host="localhost",user="root",password="avirup",database="ip")
    cursor=mycon.cursor()
    rl=int(input("ENTER ROLL NUMBER="))
    nm=input("ENTER STUDENT NAME=")
    cl=int(input("ENTER STUDENT'S CORRECT CLASS "))
    st="update student set stclass='%s' where stroll='%s' and stname='%s'"%(cl,rl,nm)
    cursor.execute(st)
    mycon.commit()
    print("DATA UPDATED SUCCESSFULLY")

def EDIT_STUDENT_ROLL():
    mycon=co.connect(host="localhost",user="root",password="avirup",database="ip")
    cursor=mycon.cursor()
    ac=int(input("ENTER CLASS="))
    nm=input("ENTER NAME=")
    rl=int(input("ENTER CORRECT ROLL ="))
    st="update student set stroll='%s' where stclass='%s' and stname='%s'"%(rl,ac,nm)
    cursor.execute(st)
    mycon.commit()
    print("DATA UPDATED SUCCESSFULLY")
    

    
    
