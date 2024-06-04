nums=[1,3,-1,-3,5,3,6,7]
k=3
i,j=0,0
count=1
maxi=[]
maci,mac=0,0
com=[]
c=0
while(j<len(nums)):
    if count==k:
        com.append(nums[j])
        maci=max(com)
        if maci>=mac:
            maxi.append(maci)
        else:
            maxi.append(0)
        com.remove(com[0]) 
        i=i+1
        j=j+1
    else:
                com.append(nums[j])
                j=j+1
                count=count+1
print(maxi)