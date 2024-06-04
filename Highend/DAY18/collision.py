def hash_function(val):
    return val%10
def main():
    search=[12,23,45,43,42,54,53,65,75,67,87]
    n=11
    hash_table=[[]for i in range(n)]
    for i in search:
        val=hash_function(i)
        hash_table[val].append(i)
    print(hash_table)
main()

