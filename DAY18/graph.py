while queue:
    count=0
    remove_node=queue.popleft()
    visited.add(tuple(removed_node))
    pfs=((removed_node[0])+str(remove_node[1]))
    print(psf)
    for nbr in graph[removed_node[0]]:
        if nbr[i]==des:
            count=count+1
        if nbr[i] not in visited:
            queue.append([nbr[i],psf]) 
            visited.add(nbr[i])
