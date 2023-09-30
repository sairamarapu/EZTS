#in the given array every number occurs twice only one number occurs one time
'''a=[1,5,1,2,3,2,3]
num=0
for i in a:
    num=num^i
print(num)'''

#swap 2 numbers using xor
'''a=100
b=200
a=a^b
b=a^b
a=a^b
print(a)
print(b)'''

#for given number n check the kth bit is set or not
'''a=int(input())
k=int(input())
#formula n&(1<<k-1)
******************
n=a&(1<<k-1)
print(n)'''

#print xor of all nums
'''n=int(input())
j=0
#O(n)
for i in range(1,n+1):
    j=j^i
print(j)
#O(1)
if(n%4==0):
    print(n)
elif(n%4==1):
    print(1)
elif(n%4==3):
    print(n+1)
elif(n%4==3):
    print(0)'''

#find the xor of all given numbers within the range
'''ll=int(input())
ul=int(input())
j=0
for i in range(li,ul+1):
    j=(j^i)^(j^(ll-ul))
print(j)'''