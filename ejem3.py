
num=[1,5,3,7,6]
x=int(0)

while x==0:
    x=1
    for i in range(0,4):
        if num[i]>num[i+1]:
            aux=num[i+1]
            num[i+1]=num[i]
            num[i]=aux
            x=0
print(num)




