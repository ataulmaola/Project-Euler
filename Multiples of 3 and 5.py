import sys


t = int(input().strip())

for a0 in range(t):
    n = int(input().strip())
    sum=0
    i=1
    x=1
    while (i*3) < n:
        x=i*3
        i+=1
        #print(x)
        sum=sum+x
    #print(sum)
    j=1
    y=1
    while(j*5)< n:
        y=j*5
        j+=1
        #print(y)
        sum=sum+y
    #print(sum)
    k=1
    z=1
    while(3*5*k)<n:
        z=3*5*k
        k+=1
        sum=sum-z
    print(sum)
