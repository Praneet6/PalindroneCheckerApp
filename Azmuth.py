import mysql.connector as sql
import datetime
from tabulate import tabulate
#db=input("enter the name of your database")

mydb=sql.connect(host="localhost",user="root",passwd="1234")

c1=mydb.cursor()

s="create database if not exists payroll "
c1.execute(s)

print("Database created ")

c1.execute("use payroll ")

#tableName=input("enter the table name")
s="create table if not exists pay " + "\
(empno int primary key,\
name varchar(22) not null,\
job varchar(22),\
BasicSalary int,\
DA float,\
HRA float,\
GrossSalary float,\
Tax float,\
NetSalary float)"
print("table Created successfully")
c1.execute(s)
while True:
    print("\n\n\n")
    print("*"*80)
    print("\t\t\t\t\t MAIN MENU")
    print("*"*80)
    print("\t\t 1. Adding Employee Records")
    print("\t\t 2. For Displaying Record of all Employee")
    print("\t\t 3. For Displaying Record of a particular Employee")
    print("\t\t 4. For Deleting Record of all Employee")
    print("\t\t 5. For Deleting Record of a particular Employee")
    print("\t\t 6. For Modification in a Record of Employee")
    print("\t\t 7. For Displaying Payroll")
    print("\t\t 8. For Displaying Salary slip for all the Employee")
    print("\t\t 9. For Displaying Salary slip for a particular Employee")
    print("\t\t10. For Exit")
    ch=int(input("enter your choice"))
    if ch==1:
        try:
            print("Enter employee information")
            mempno=int(input("enter the employee no: "))
            mname=input("enter the employee name: ")
            mjob=input("enter the employee job: ")
            mbasic=float(input("enter the basic salary: "))
            if mjob.upper()=="OFFICER":
                mda=mbasic*0.5
                mhra=mbasic*.3
                mtax=mbasic*0.2
            elif mjob.upper()=="MANAGER":
                mda=mbasic*0.4
                mhra=mbasic*.3
                mtax=mbasic*0.2
            else:
                mda=mbasic*0.3
                mhra=mbasic*.2
                mtax=mbasic*0.1         
            mgross=mbasic+mda+mhra
            mnet=mgross-mtax
            rec=(mempno,mname,mjob,mbasic,mda,mhra,mgross,mtax,mnet)
            s="insert into pay values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            c1.execute(s,rec)
            mydb.commit()
            print("Record added successfully")
            
        except Exception as e:
            print("please check",e)
    if ch==2:
        try:
            s="select * from pay"
            c1.execute(s)
            print(tabulate(c1, headers=["Empno","Name","Job","Basic","DA","HRA","Gross","Tax","Net"], tablefmt='fancy_grid'))
            break
        except Exception as e:
            print("Error: ",e)
    if ch==3:
        ri=input("enter the Employee no to search: ")
        try:
            s="select * from pay where empno="+ri
            c1.execute(s)
            print(tabulate(c1, headers=["Empno","Name","Job","Basic","DA","HRA","Gross","Tax","Net"], tablefmt='psql'))
            break
        except Exception as e:
            print("Error: ",e)
        
    if ch==4:
        try:
            ch=input("Do you want to delete all the Records(y/n): ")
            if ch.upper()=='Y':
                s="delete from pay"
                c1.execute(s)
                mydb.commit()
                print("All records are deleted:")
            #print(tabulate(c1, headers=["Empno","Name","Job","Basic","DA","HRA","Gross","Tax","Net"], tablefmt='psql'))
        except Exception as e:
            print("Error: ",e)
    if ch==5:
        ri=input("enter the Employee no to DELETE: ")
        try:
            s="delete from pay where empno="+ri
            c1.execute(s)
            mydb.commit()
            print("Deletion done:")
            #print(tabulate(c1, headers=["Empno","Name","Job","Basic","DA","HRA","Gross","Tax","Net"], tablefmt='psql'))
            #break
        except Exception as e:
            print("Error: ",e)
    if ch==6:
        ri=input("enter the Employee no to search: ")
        try:    
            s="select * from pay where empno="+ri
            c1.execute(s)
            print(tabulate(c1, headers=["Empno","Name","Job","Basic","DA","HRA","Gross","Tax","Net"], tablefmt='psql'))
            print("\n \n Type the value to modify or just press enter for no change")
            x=input("Enter name: ")
            if len(x)>0:
                mname=x
                s="update pay set name=" + "'"+mname+"'" + "where empno="+ri
                c1.execute(s)
                mydb.commit()
            x=input("Enter job: ")
            if len(x)>0:
                mjob=x
                s="update pay set job=" + "'"+mjob+"'" + "where empno="+ri
                c1.execute(s)
                mydb.commit()
        
            x=input("enter the basic: ")
            if len(x)>0:
                mbasic=int(x)
                #print(type(mbasic))
                #print(type(x))
                s="update pay set basicsalary=" + "'"+str(mbasic)+"'" + "where empno="+ri
                c1.execute(s)
                mydb.commit()

                s="update pay set da="+ "'" +str(mbasic*.5)+ "'" +"where empno="+ri
                c1.execute(s)
                mydb.commit()

                s="update pay set hra="+ "'" +str(mbasic*.5)+ "'" +"where empno="+ri
                print(s)
                mgross=mbasic+da+hra

                mnet=mgross-tax
                c1.execute(s)
                mydb.commit()
                print("Record updated successfully:")
        except Exception as e:
            print("Error: ",e)
    if ch==7:
        try:
            print("\n\n\n")
            print("*"*95)
            print("Employee Payroll".center(90))
            print("*"*95)
            now =datetime.datetime.now()
            print("Current Date and Time:",end=" ")
            print(now.strftime("%y-%m-%d %H:%M:%S"))
            #print()
            s="select * from pay"
            
            c1.execute(s)
            print(tabulate(c1, headers=["Empno","Name","Job","Basic","DA","HRA","Gross","Tax","Net"], tablefmt='psql'))
                           
        except Exception as e:
            print("Error: ",e)

    if ch==8:
        try:
            print("\n\n\n")
            print("*"*95)
            print("Salary Slip Of all emloyee".center(90))
            print("*"*95)
            now =datetime.datetime.now()
            print("Current Date and Time:",end=" ")
            print(now.strftime("%y-%m-%d %H:%M:%S"))
            #print()
            s="select * from pay"
            c1.execute(s)
            print(tabulate(c1, headers=["Empno","Name","Job","Basic","DA","HRA","Gross","Tax","Net"], tablefmt='psql'))
                           
        except Exception as e:
            print("Error: ",e)


        
    if ch==9:
        try:
            ri=input("Enter the employee number")
            print("\n\n\n")
            print("*"*95)
            print("Salary Slip ".center(90))
            print("*"*95)
            now =datetime.datetime.now()
            print("Current Date and Time:",end=" ")
            print(now.strftime("%y-%m-%d %H:%M:%S"))
            #print()
            s="select * from pay where empno="+ri
            c1.execute(s)
            print(tabulate(c1, headers=["Empno","Name","Job","Basic","DA","HRA","Gross","Tax","Net"], tablefmt='psql'))
                           
        except Exception as e:
            print("Error: ",e)
