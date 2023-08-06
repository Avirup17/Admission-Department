import MAIN_MENU
import ADMISSION
import mysql.connector as co
def ADM_MENU():
    while True:
        print(" ")
        print("........WELCOME TO JERMELS ACADEMY DATABASE SYSTEM.......")
        print("                                                         ")
        print("1= NEW ADMISSION")
        print("2= SHOW ADMISSION DETAILS")
        print("3= SEARCH")
        print("4= DELETE EXISTING RECORDS")
        print("5= CHANGE ADMISSION DETAILS")
        print("6= RETURN")
        print("                                 ")
        choice=int(input("ENTER YOUR CHOICE ="))
        if choice==1:
            ADMISSION.ADMIN_DETAILS()
        elif choice==2:
            ADMISSION.show_admin_details()
        elif choice==3:
            ADMISSION.SEARCH_ADMIN_DETAILS()
        elif choice==4:
            ADMISSION.DELETE_ADMIN_DETAILS()
        elif choice==5:
            ADMISSION.EDIT_ADMIN_DETAILS()
        elif choice==6:
            return
        else:
            print("ERROR:INVALID SELECTION")
def ADMIN_DETAILS():
    mycon=co.connect(host="localhost",user="root",password="avirup",database="ip")
    cursor=mycon.cursor()
    admno=int(input("ENTER ADMISSION NUMBER ="))
    name=input("ENTER STUDENT NAME =")
    cls=input("ENTER CLASS =")
    roll=int(input("ENTER ROLL NUMBER ="))
    section=input("ENTER CLASS SECTION=")
    email=input("ENTER EMAIL ID =")
    phoneno=input("ENTER PHONE NUMBER =")
    city=input("ENTER CITY/TOWN NAME =")
    state=input("ENTER STATE NAME(eg:WEST BENGAL) =")
    address=input("ENTER ADDRESS =")
    

    query="insert into ip(admno,name,cls,roll,section,email,phoneno,address,state)values({},'{}','{}',{},'{}','{}','{}','{}','{}')".format(admno,name,cls,roll,section,email,phoneno,address,state)
    cursor.execute(query)
    mycon.commit()
    mycon.close()
    cursor.close()
    print("RECORD HAS BEEN SAVED IN ADMISSION TABLE")
        
def show_admin_details():
    mycon=co.connect(host="localhost",user="root",password="avirup",database="ip")
    cursor=mycon.cursor()
    cursor.execute("select * from ip")
    data=cursor.fetchall()
    for row in data:
        print(row)
        
def SEARCH_ADMIN_DETAILS():
    print("1:SEARCH THROUGH ADMISSION NUMBER")
    print("2:SEARCH THROUGH CLASS")
    preference=int(input("ENTER YOUR CHOICE="))
    if preference==1:
        mycon=co.connect(host="localhost",user="root",password="avirup",database="ip")
        cursor=mycon.cursor()
        ad=int(input("ENTER THE ADMISSION NUMBER="))
        sc="select * from ip where admno='%s'"%(ad)
        cursor.execute(sc)
        data=cursor.fetchall()
        print(data)
    elif preference==2:
        mycon=co.connect(host="localhost",user="root",password="avirup",database="ip")
        cursor=mycon.cursor()
        ad=int(input("ENTER THE CLASS="))
        sc="select * from ip where cls='%s'"%(ad)
        cursor.execute(sc)
        data=cursor.fetchall()
        print(data)
    else:
        print("             ERROR                   ")
        
def DELETE_ADMIN_DETAILS():
    try:
        mycon=co.connect(host="localhost",user="root",password="avirup",database="ip")
        cursor=mycon.cursor()
        ac=int(input("ENTER ADMISSION NUMBER =")) 
        st="delete from ip where admno='%s'"%(ac)
        cursor.execute(st)
        mycon.commit()
        print("DATA DELETED SUCCESSFULLY")
    except:
        print("ERROR")
def EDIT_ADMIN_DETAILS():
    mycon=co.connect(host="localhost",user="root",password="avirup",database="ip")
    cursor=mycon.cursor()
    print("1=EDIT NAME")
    print("2=EDIT EMAIL")
    print("3=EDIT PHONE NUMBER")
    print("4=RETURN")
    choice=int(input("ENTER YOUR CHOICE ="))
    if choice==1:
        ADMISSION.EDIT_NAME()
    elif choice==2:
        ADMISSION.EDIT_EMAIL()
    elif choice==3:
        ADMISSION.EDIT_PHONE()
    elif choice==4:
            return
    else:
        print("ERROR:INVLAID CHOICE ENTERED")
def EDIT_NAME():
    mycon=co.connect(host="localhost",user="root",password="avirup",database="ip")
    cursor=mycon.cursor()
    ac=int(input("ENTER ADMISSION NUMBER="))
    nm=input("ENTER CORRECT NAME =")
    st="update ip set name='%s' where admno='%s'"%(nm,ac)
    cursor.execute(st)
    mycon.commit()
    print("DATA UPDATED SUCCESSFULLY")
def EDIT_EMAIL():
    mycon=co.connect(host="localhost",user="root",password="avirup",database="ip")
    cursor=mycon.cursor()
    ac=input("ENTER ADMISSION NUMBER =")
    ad=input("ENTER CORRECT EMAIL ID ")
    st="update ip set email='%s' where admno='%s'"%(ad,ac)
    cursor.execute(st)
    mycon.commit()
    print("DATA UPDATED SUCCESSFULLY")
def EDIT_PHONE():
    try:
        mycon=co.connect(host="localhost",user="root",password="avirup",database="ip")
        cursor=mycon.cursor()
        ac=input("ENTER ADMISSION NUMBER")
        ph=input("ENTER CORRECT PHONE NUMBER =")
        st="update ip set phoneno='%s' where admno='%s'"%(ph,ac)
        cursor.execute(st)
        mycon.commit()
        print("DATA UPDATED SUCCESSFULLY")
    except:
        print("ERROR")
                 
        
        
            
        
            
