'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here

    
import sys
cases=int(input())
arr=sys.stdin.readlines()
#print(cases,arr)
count=0
s=''
def check(count):
    s1=''
    while(count!=0):
        if(count%2==0):
            s1+='1'
            count-=2
        else:
            s1+='7'
            count-=3
    return s1
    
for i in range(cases):
    a=arr[i]
    for j in range(len(a)):
        if(a[j] in '069'):
            count+=6
            
        elif(a[j] in '352'):
            count+=5
            
        elif(a[j]=='8'):
            count+=7
            
        elif(a[j]=='4'):
            count+=4
            
        elif(a[j]=='7'):
            count+=3
        elif(a[j]=='1'):
            count+=2
            
    #print(count)
    print(check(count))
    count=0


 
        