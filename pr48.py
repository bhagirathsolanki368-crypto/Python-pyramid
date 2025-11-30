x=int(input("enter  row =>"))

for i in range(x, 0, -1):
    for j in range(x- i):
        print(" ", end="")
    for k in range(1, i + 1):
         if i%2==0:
            print(" #",end="")
         else :
            print(" *",end="")
    print() 