
#Function to calculate maximum no children to whom choclates could be distributed
def cadbury(length,width):
    count=0
    while True:
        pro=(length*width)-pow(min(length,width),2)
        length=max(width,length-width)
        width-=min(length,width)
        count+=1
        if width==1:
            count+=length
            break
        if length==1:
            count+=width
            break
        if(pro==0):
            break
    return count


#Taking inputs and applying function
min_len=int(input())
max_len=int(input())
min_width=int(input())
max_width=int(input())

counts=[]

for i in range(min_len,max_len+1):
    for j in range(min_width,max_width+1):
        res=cadbury(i,j)
        counts.append(res)

#Finding the total sum
sum=0
for i in counts:
    sum+=i

print(counts)