a=[1,"ai",3,"laptop","fruit"]
print('ori:',a)
n=input("add an element:")
k=int(input("index of placing:"))
a.append(k)
for i in range(0,len(a)):
    if i>=k:
        t=a[i]
        a[i]=n
        n=t
print(a)        