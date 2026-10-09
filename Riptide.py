t = int(input())
for _ in range(t):
    x = list(map(int, input().split()))
    x.sort()
    if len(set(x)) != len(x):
        print(0)
    else:
        f = min(x[2]-x[1], x[1] - x[0])
        print(f)
    
             
             
        
       
