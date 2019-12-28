m, n = map(int, input().split())
a = list(map(int, input().split()))
s = []
s1 = 0
#print(m,n)
#print(a)
for i in range(m):
    s1 += a[i]
    s.append(s1)
#print(s)
for i in range(n):
    x, y = map(int, input().split())
    #print(x,y)
    if x == 1:
        print((s[y-1])//(y-x+1))
    else:
        print((s[y-1] - s[x-2])//(y-x+1))