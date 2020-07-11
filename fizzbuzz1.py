count,num=0,0
while count<=100:
    num+=1
    if num%3==0 and num%5==0:
        print("FizzBuzz",end=" ")
        count+=1
    elif num%5==0:
        print("Buzz",end=" ")
    elif num%3==0:
        print("Fizz",end=" ")
    else:
        print(num,end=" ")




