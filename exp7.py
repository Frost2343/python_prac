PROGRAM:

class emp:
	def __init__ (self, id1, name1):
    	self.id = id1
    	self.name = name1
	def display(self):
    	print(self.id)
    	print(self.name)
	def setvalue(self, id1, name1):
    	self.id = id1
    	self.name = name1
   	 
l1= list()
    
user=False
while not user:
    choice=int(input("\n\n1.Read an employee\n2.Modify the emloyee\n3.Display employees\n4.Delete employee\n5.Exit\nEnter choice: "))
    if choice==1 :
    	no_e=int(input("Enter the no of employees: "))
    	for i in range(no_e):
        	eid = int(input("Employee id: "))
        	ename = input("Employee name: ")
        	e1 = emp(eid, ename)
        	l1.append(e1)
       	 
    elif choice==2 :
    	upid=int(input("Enter employee id to be updated: "))
    	upname=input(f"Enter employee name to be updated at id {upid}: ")
    	for q in l1:
        	if q.id == upid:
            	q.setvalue(upid, upname)
      	 
    elif choice==3 :
    	print("\n\n\t\tEMPLOYEES\t\t\n")
    	for i in l1:
        	print(f"\tId: {i.id} | Name: {i.name}")

    elif choice==4 :
    	did=int(input("Enter employee id to be deleted: "))
    	for d in l1:
        	if d.id == did:
            	l1.remove(d)
   	 
    elif choice==5 :
   	 user=True
    else :
   	 print("Invalid choice")

OUTPUT:

1.Read an employee
2.Modify the emloyee
3.Display employees
4.Delete employee
5.Exit
Enter choice: 1
Enter the no of employees: 3
Employee id: 101
Employee name: a
Employee id: 102
Employee name: b
Employee id: 103
Employee name: t


1.Read an employee
2.Modify the emloyee
3.Display employees
4.Delete employee
5.Exit
Enter choice: 2
Enter employee id to be updated: 102
Enter employee name to be updated at id 102: h


1.Read an employee
2.Modify the emloyee
3.Display employees
4.Delete employee
5.Exit
Enter choice: 3


   	 

EMPLOYEES   	 

    Id: 101 | Name: a
    Id: 102 | Name: h
    Id: 103 | Name: t


1.Read an employee
2.Modify the emloyee
3.Display employees
4.Delete employee
5.Exit
Enter choice: 4
Enter employee id to be deleted: 101


1.Read an employee
2.Modify the emloyee
3.Display employees
4.Delete employee
5.Exit
Enter choice: 3


   	 EMPLOYEES   	 

    Id: 102 | Name: h
    Id: 103 | Name: t


1.Read an employee
2.Modify the emloyee
3.Display employees
4.Delete employee
5.Exit
Enter choice: 5


