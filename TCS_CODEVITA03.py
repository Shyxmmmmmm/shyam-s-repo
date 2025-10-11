
def inside(x,y,w,h,N,M):
    return x>=0 and y>=0 and x+w <=N and y+h <=M

def overlap_or_touch(r1,r2):
    x1,y1,w1,h1=r1
    x2,y2,w2,h2=r2
    
    if x1+w1<x2-1 or x2+w2<x1-1 or y1+h1 <y2-1 or y2+h2 <y1-1:
        return False
    return True

def solve():
    M,N=map(int,input().split())
    c=int(input())
    rects=[]
    invalid=[]
    for _ in range(c):
        cmd=input().strip()
        parts=cmd.split()
        op=parts[0]
        x,y,w,h=map(int,parts[1:])
        new_rect=(x,y,w,h)
        
        if op == "draw":
            if not inside(x,y,w,h,N,M):
                invalid.append(cmd)
                continue
            if any(overlap_or_touch(r,new_rect) for r in rects):
                invalid.append(cmd)
                continue
            rects.append(new_rect)
        elif op=="remove":
            if new_rect in rects:
                rects.remove(new_rect)
            else:
                invalid.append(cmd)
        
        elif op in ("extend","shrink"):
            found=None
            for r in rects:
                if r[0] ==x and r[1] ==y:
                    found=r
                    break
            if not found:
                invalid.append(cmd)
                continue
            
            if op =="shrink" and (w>found[2] or h>found[3]):
                invalid.append(cmd)
                continue
            
            newr=(x,y,w,h)
            if not inside(x,y,w,h,N,M):
                invalid.append(cmd)
                continue
            temp=[r for r in rects if r!=found]
            if any(overlap_or_touch(r,newr) for r in temp):
                invalid.append(cmd)
                continue
            rects.remove(found)
            rects.append(newr)
        else:
            invalid.append(cmd)
    for i in invalid:
        print(i)
    print(len(rects))
        
                
        
