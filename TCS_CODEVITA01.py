from collections import deque
import sys
import re
def parse_row(s):
    tokens=re.findall(r'(\d+)([A-Z])',s.replace(" ",""))
    row=[]
    for count,ch in tokens:
        row+=[ch]*int(count)
    return row
def min_green_breaks(N,lines):
    grid=[]
    i=0
    for line in lines:
        if line.strip() =="":
            continue
        row=parse_row(line.strip())
        if len(row)!=N:
            raise ValueError(f"Parsed row length {len(row)} != N({N}) for line: {line!r}")
        grid.append(row)
        i=i+1
        if i==N:
            break
    if len(grid)!=N:
        raise ValueError("Not enough Non-empty rows Provided")
    starts=[]
    targets=set()
    for r in range(N):
        for c in range(N):
            if grid[r][c]=='S':
                starts.append((r,c))
            if grid[r][c]=='D':
                targets.add((r,c))
                
    INF=10**9
    dist=[[INF]*N for _ in range(N)]
    dq=deque()
    for (r,c) in starts:
        dist[r][c]=0
        dq.appendleft((r,c))
    
    dirs =[(1,0),(-1,0),(0,1),(0,-1)]
    while dq:
        r,c=dq.popleft()
        if (r,c) in targets:
            return dist[r][c]
        for dr,dc in dirs:
            nr,nc= r+dr,c+dc
            if not (0 <=nr <N and 0 <=nc <N):
                continue
            cell=grid[nr][nc]
            if cell =='R':
                continue
            add_cost=1 if cell =='G' else 0
            nd=dist[r][c] +add_cost
            if nd<dist[nr][nc]:
                dist[nr][nc]=nd
                if add_cost==0:
                    dq.appendleft((nr,nc))
                else:
                    dq.append((nr,nc))
    
    best=min((dist[r][c] for (r,c) in targets),default=INF)
    return best if best < INF else -1
if __name__ =="__main__":
    data=sys.stdin.read().strip().splitlines()
    if not data:
        print(-1)
        sys.exit(0)
    idx=0
    while idx<len(data) and data[idx].strip()== "":
        idx+=1
    if idx>=len(data):
        print(-1); sys.exit(0)
    N=int(data[idx].strip());idx+=1
    lines =data[idx:]
    try:
        ans=min_green_breaks(N,lines)
        print(ans)
    except Exception as e:
        print(-1)
