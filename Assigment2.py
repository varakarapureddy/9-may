#program to remove student id details in dictionary.
n=int(input('Enter number of values:'))
d1={}
d2={}
d3={}
for i in range(n):
	sid=int(input("Enter the student id"))
	snam=input("Enter the student mame")
	scls=input("Enter the student  class ")
	sres=float(input("Enter the result of student"))
	d1[sid]=snam
	d2[sid]=scls
	d3[sid]=sres
print(d1,d2,d3)	
a=int(input("Enter the student id"))
d1.pop(a)
d2.pop(a)
d3.pop(a)
print(d1,d2,d3)
