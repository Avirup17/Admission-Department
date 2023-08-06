import MAIN_MENU
import ADMISSION
import STUDENT_DATA
import STUDENT_DETAILS
import mysql.connector as co
def ALL_DETAILS():
    while True:
        print(" ")
        print("ENTER 1 TO SEE ALL DETAILS")
        print("ENTER 2 TO SEE ANY SPECIFIC DATA")
        print(" ")
        print(" ")
        print("****HIGH SENSITIVE DATA SEARCH****")
        print("************BE CAREFUL************")
        print(" ")
        a=int(input("ENTER YOUR CHOICE ="))
        if a==1:
            STUDENT_DETAILS.ALL_DETAIL()
        elif a==2:
            STUDENT_DETAILS.one_SPECIFIC()
        else:
            print("none")
def ALL_DETAIL():
    mycon=co.connect(host="localhost",user="root",password="avirup",database="ip")
    cursor=mycon.cursor()
    cursor.execute("select * from ip, student")
    data=cursor.fetchall()
    for row in data:
        print(row)
def one_SPECIFIC():
    print(" ")
    print("1 = ALL RECORDS OF STUDENTS OF SPECIFIC CLASS")
    print("2 = ALL RECORDS OF STUDENTS OF SPECIFC SUBJECT(HINDI/BENGALI)")
    print("3 = ALL STUDENTS NAME WHICH CONTAINS ANY SPECIFIC WORD")
    print(" ")
    b=int(input("ENTER YOUR CHOICE ="))
    if b==1:
        STUDENT_DETAILS.CLASS()
    elif b==2:
        STUDENT_DETAILS.SUBJECT()
    elif b==3:
        STUDENT_DETAILS.NAME()
    else:
        print("INVALID CHOICE")
def CLASS():
    mycon=co.connect(host="localhost",user="root",password="avirup",database="ip")
    cursor=mycon.cursor()
    print(" ")
    cl=int(input("ENTER CLASS="))
    print(" ")
    st="select * from student where stclass='%s'"%(cl)
    cursor.execute(st)
    data=cursor.fetchall()
    print(data)
def NAME():
    mycon=co.connect(host="localhost",user="root",password="avirup",database="ip")
    cursor=mycon.cursor()
    print(" ")
    i=input("ENTER THE WORD =")
    print(" ")
    st="select * from ip where name like '%s%%';"%(i)
    cursor.execute(st)
    data=cursor.fetchall()
    print(data)
def SUBJECT():
    mycon=co.connect(host="localhost",user="root",password="avirup",database="ip")
    cursor=mycon.cursor()
    print(" ")
    cl=input("ENTER SUB2=")
    print(" ")
    st="select * from student where sub2='%s'"%(cl)
    cursor.execute(st)
    data=cursor.fetchall()
    print(data)
