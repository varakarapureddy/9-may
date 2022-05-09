#program to retrive email id with the name using dictionary
n=int(input())
d={}
for i in range(n):
    x=input().split()
    d[x[0]]=x[1] 
    print(d)
while True:

    try:            
        name=input()
        if name in d:
            print(name,"=",d[name],sep='')
        else:
            print("not found")
    except:
        break
