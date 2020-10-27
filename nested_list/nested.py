marklist=[]
umarks=set()
n=int(input())
for i in range(0,n):
    name=input()
    marks=float(input())
    marklist.append([name,marks])
    umarks.add(marks)

umarks=sorted(umarks)
secleast=umarks[1]
names=[]

for mark in marklist:
    if mark[1]==secleast:
        names.append(mark[0])

names=sorted(names)
for i in names:
    print(i)