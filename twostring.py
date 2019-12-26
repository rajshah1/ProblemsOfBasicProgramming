# Write your code here
import sys
case=int(input())
strings=sys.stdin.readlines()
#print(strings)
#result=list()


for i in range(case):
    a,b =map(str,strings[i].split())
    if(a==b):
        print("YES")
    else:
        count=0
        for j in range(len(a)):
            if (b[j] in a):
                count+=1
                a=a.replace(b[j],"#")
            else:
                break
        #print(count,a,b)
    
        if(count==len(a)):
            print("YES")
        else:
            print("NO")
              
 