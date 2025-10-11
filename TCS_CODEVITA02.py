from collections import deque

def bfs_paths(start,target,adj,N):
    results=[]
    dq=deque()
    dq.append((start,1<<(start-1),1))
    visited=set([(start,1<<(start-1))])
    
    while dq:
        node,mask,cost=dq.popleft()
        if node ==target:
            results.append((mask,cost))
        for nxt in adj[node]:
            bit =1<<(nxt-1)
            if mask & bit:
                continue
            nmask=mask | bit
            state =(nxt,nmask)
            if state not in visited:
                visited.add(state)
                dq.append((nxt,nmask,cost+1))
    return results
    
def solve():
    import sys
    data=sys.stdin.read().strip().split()
    if not data:
        print("impossible")
        return
    it =iter(data)
    N,M=int(next(it)),int(next(it))
    adj={i:[] for i in range(1,N+1)}
    for _ in range(M):
        a,b =int(next(it)),int(next(it))
        adj[a].append(b)
        adj[b].append(a)
    start1, start2=int(next(it)),int(next(it))
    target =int(next(it))
    
    paths1=bfs_paths(start1,target,adj,N)
    paths2 =bfs_paths(start2,target,adj,N)
    
    best=float('inf')
    tgt_bit=1<<(target-1)
    
    for m1,c1 in paths1:
        for m2,c2 in paths2:
            if (m1 & m2) ==tgt_bit:
                total=bin(m1|m2).count("1")
                best=min(best,total)
    
    if best==float('inf'):
        print("Impossible")
    else:
        print(best)
if __name__ == "__main__":
    solve()
