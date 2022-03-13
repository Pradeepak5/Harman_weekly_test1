import sqlite3 as sql
from prettytable import PrettyTable

connection=sql.connect("EmployeeManagement.db")
ListOfTable=connection.execute("select name from sqlite_master where type='table' and name='Employee'").fetchall()

if ListOfTable!=[]:
    print("Table already Created")
else:
    connection.execute('''create table Employee(
                                 ID integer primary key autoincrement,
                                 empCode integer,
                                 name text,
                                 phone integer,
                                 email text,
                                 designation text,
                                 salary integer,
                                 company text
                                 );''')
    print("Table created Successfully.")

while True:
    print("1. Add the Employees")
    print("2. View all employees")
    print("3. Search an employee using employee name")
    print("4. Update an employee details using employee Code")
    print("5. Delete an  employee using employee Code")
    print("6. Display all the details of employees whose salary is greater than 50000")
    print("7. Display the count of total number of employee in the company")
    print("8. Display all the employee details in alphabetical order, within the specific salary range")
    print("9. Display all the employee data, whose salary is less than the average salary of all the employees")
    print("10. EXIT")

    choice=int(input("Enter Your choice from the above Menu :"))

    if choice==1:
        getempcode=input("Employee Code :")
        getname=input("Employee Name :")
        getphone=input("Phone No :")
        getemail=input("Email :")
        getdesignation=input("Designation :")
        getsalary=input("Salary :")
        getcompany=input("Company Name :")

        connection.execute("insert into Employee(empCode,name,phone,email,designation,salary,company)\
                           values("+getempcode+",'"+getname+"','"+getphone+"','"+getemail+"','"+getdesignation+"',"+getsalary+",'"+getcompany+"')")
        print("Data Inserted Successfullyy.")
        connection.commit()

    elif choice==2:
        result=connection.execute("select * from Employee")
        table=PrettyTable(["ID","Employee code","Name","Phone","Email","Designation","Salary","Company"])
        for i in result:
            table.add_row([i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]])
        print(table)

    elif choice==3:
        getname = input("Search Employee by Employee Name :")
        result=connection.execute("select * from Employee where name like '%"+getname+"%'")
        table = PrettyTable(["ID", "Employee code", "Name", "Phone", "Email", "Designation", "Salary", "Company"])
        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]])
        print(table)

    elif choice==4:
        getempcode=input("Update Employee using Employee Code :")

        getname = input("Employee Name :")
        getphone = input("Phone No :")
        getemail = input("Email :")
        getdesignation = input("Designation :")
        getsalary = input("Salary :")
        getcompany = input("Company Name :")
        connection.execute("update Employee set name='"+getname+"',phone="+getphone+",email='"+getemail+"',designation='"+getdesignation+"',salary="+getsalary+",company='"+getcompany+"' where empCode="+getempcode+"")
        print("Data updated successfully.")
        connection.commit()

    elif choice==5:
        getempcode=input("Delete Employee using Employee Code :")
        connection.execute("delete from Employee where empCode="+getempcode+"")
        print("Employee Deleted successfully.")
        connection.commit()

    elif choice==6:
        result=connection.execute("select * from Employee where salary > 50000")
        table = PrettyTable(["ID", "Employee code", "Name", "Phone", "Email", "Designation", "Salary", "Company"])
        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]])
        print(table)
        connection.commit()

    elif choice==7:
        result=connection.execute("select company,count(*) from Employee group by company")
        table=PrettyTable(["Company","Count"])
        for i in result:
           table.add_row([i[0],i[1]])
        print(table)

    elif choice==8:
        lowersalary=input("Enter lower salary :")
        highersalary=input("Enter higher salary :")

        result=connection.execute("select * from Employee where salary between "+lowersalary+" and "+highersalary+" order by name")
        table = PrettyTable(["ID", "Employee code", "Name", "Phone", "Email", "Designation", "Salary", "Company"])
        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]])
        print(table)
        connection.commit()

    elif choice==9:
        result=connection.execute("select * from Employee where salary < (select avg(salary) from Employee)")
        table = PrettyTable(["ID", "Employee code", "Name", "Phone", "Email", "Designation", "Salary", "Company"])
        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]])
        print(table)
        connection.commit()

    elif choice==10:
        break

    else:
        print("oops You have choosed an INVALID option ....try again by Choosing Valid option.")