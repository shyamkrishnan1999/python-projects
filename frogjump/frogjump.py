
#Input as two lines ist line containing x1 and v1 2nd line containing x2 and v2

x1,v1=map(int,input().split())
x2,v2=map(int,input().split())

while True:
    if x1==x2:
        print("yes")
        break
    else:
        x1+=v1
        x2+=v2
        if (v1>v2 and x1>x2) or (v2>v1 and x2>x1):
            print("No")
            break


