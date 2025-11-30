no=int(input("Enter no of rows =>"))
m=1

for i in range(no,0,-1):
    for j in range(1,i+1,1):
        print("",m,end="")
        m+=2
        m=1
    print("")