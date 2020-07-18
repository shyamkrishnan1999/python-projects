
#Function to calculate pairs
def returnPairs(mylist):
    pairs=0
    myset=set()
    for i in range(0,len(mylist)):
        occur=0
        if mylist[i] in myset:
            continue
        for j in range(i+1,len(mylist)):
            if mylist[i]==mylist[j]:
                occur+=1
            myset.add(mylist[i])
        if occur>=2:
            occur=2
        pairs+=occur
    return pairs




#Inputing the numbers and initializing an empty list
val=map(int,input().split())
res=[]

#Computing the resulting values and storing them into a list
for i in val:
    dup=i
    large=0
    small=0

    while dup!=0:
        k=dup%10
        if k>large:
            large=k
        if k<small:
            small=k
        dup=dup//10

    res_val=(large*11+small*7)%100
    res.append(res_val)

#seperating into even and odd groups

length=len(res)
evn_grp=[]
odd_grp=[]

for i in range(0,length):
    if i%2==0:
        evn_grp.append(res[i]//10)
    else:
        odd_grp.append(res[i]//10)

#calculating pairs

evn_pairs=returnPairs(evn_grp)
odd_pairs=returnPairs(odd_grp)
tot_pairs=evn_pairs+odd_pairs
print(tot_pairs)








