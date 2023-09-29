
def linear(li,target):
    for i in li:
        if i==target:
            print(i)
            return True
    return False
n=int(input())
li=list(map(int,input().strip().split()))[:n]
print(li)
target=int(input())
print(linear(li,target))

#space complexity parallel to time complexity
#same amount of space regardless of the input size n
#ex:sum of array elements
#space os dependent on values


