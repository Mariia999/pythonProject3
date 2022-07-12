x = int(input("number = "))
i = 1
a=[]
while i*i<=x:
    if x%i==0:
        a.append(i)
        if i!=x//i:
            a.append(x//i)
    i+=1
a.sort()
print(a)