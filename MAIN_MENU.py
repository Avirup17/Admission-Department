import MAIN_MENU
import ADMISSION
import STUDENT_DATA
import STUDENT_DETAILS
print("WELCOME TO JERMELS ACADEMY")
print("                         ")
print("PLEASE ENTER YOUR CHOICE AS PER GIVEN DATA")
print("                         ")
print("1= ADMISSION")
print("2= STUDENT DETAILS")
print("3 =CHECK ALL STUDENT DETAILS")
print("4= RETURN")
print(" ")
choice=int(input("ENTER YOUR PREFERENCE ="))
while True:
  if choice==1:
    ADMISSION.ADM_MENU()
  elif choice==2:
    STUDENT_DATA.STU_MENU()
  elif choice==3:
    STUDENT_DETAILS.ALL_DETAILS()
  else:
    print("ERROR:INVALID SELECTION")
   

