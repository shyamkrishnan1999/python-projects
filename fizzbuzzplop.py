cond=int(input())
cond_values=list(map(int,input().split(" ")))
cond_words=list(input().split(" "))
count=0
num=0
Str,string="",""

for i in cond_words:
    string=string+i



while count<=100:
    num+=1
    for i in range(0,len(cond_values)):
        if num%cond_values[i]==0:
            Str=Str+cond_words[i]
    if str=="":
        print(num,end=" ")
    else:
        print(Str,end=" ")

    if Str==string:
        count+=1





