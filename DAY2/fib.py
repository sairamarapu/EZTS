def fib(a):
    if a==1 :
        return 1
    if a==0:
        return 0
    return fib(a-2)+fib(a-1)
a=int(input())  
print(fib(a))
'''n1=0
n2=1
i=0
while(i<10):
    print(n1,end=" ")
    temp=n2
    n2=n2+n1
    n1=temp
    i=i+1'''