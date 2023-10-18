def bfs(start,des,q,map):
    count=0
    psf=''
    visited=[False for i in range(len(map))]
    while(len(q)!=0):
        current=q.pop(0)
        psf=psf+str(current)
        print(psf)
        visited[current-1]=True
        for i in map[current]:
            if i==des:
                count=count+1
            if visited[i-1]==False:
                q.append(i)
                visited[i-1]=True
    print(count)
map={
      5: [2],
      1: [2, 3], 
      2: [1, 4],  
      3: [1, 5], 
      4: [2,3] 
     }
start=5
q=[5]
bfs(start,3,q,map)