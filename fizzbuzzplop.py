cond=int(input())
cond_values=list(map(int,input().split(" ")))
cond_words=list(input().split(" "))
num=0
string=""




while num<=100:
    num+=1
    word_str=""
    for i in range(0,len(cond_values)):
        if num%cond_values[i]==0:
            word_str=word_str+cond_words[i]
    if word_str=="":
        print(num,end=" ")
    else:
        print(word_str,end=" ")






