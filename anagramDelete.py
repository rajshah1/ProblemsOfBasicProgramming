'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
import sys
a=int(input())
listvalue=sys.stdin.readlines()
t=list()

for i in range(1,2*a,2):
    b=list(listvalue[i-1])
    b.remove('\n')
    d=0
    e=0
    c=list(listvalue[i])
    if '\n' in c:
        c.remove('\n')
    #print(b,c)
    #print(len(b),len(c))
    if len(b)>len(c):
        d=len(c)
        e=len(b)
    else:
        d=len(b)
        e=len(c)
    #print(d)
    for j in range(d):
        if d==len(b):
            if b[j] in c:
            #    print(j,b[j])
                t.append(b[j])
                c[c.index(b[j])]='1'
        else:
            if c[j] in b:
            #   print(j,c[j])
                t.append(c[j])
                b[b.index(c[j])]='1'
            
    #print(t)
    print(((d+e)-2*len(t)))
    t.clear()    
    b.clear()
    c.clear()
  
    