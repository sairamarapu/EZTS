def hash_function(val):
    return val%10
def get_next(arr,current):
    for i in range(current,len(arr)):
        if arr[i]==0:
            return i
        elif i==len(arr)-1:
            i=0
def main():
    search=[12,32,45,34,65,78,90,112]
    n=10
    hash_table=[0 for i in range(n)]
    for i in search:
        current=hash_function(i)
        if hash_table[current]==0:
            hash_table[current]=i
        else:
            get=get_next(hash_table,current)
            hash_table[get]=i
    print(hash_table)
main()