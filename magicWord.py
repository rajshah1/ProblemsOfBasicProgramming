'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here

import sys
# find if given number is prime or not
def MakePrime(n,plmn):
    if n<=65:
        m=67
    elif n<= 97 and n>=90:
        m=89 if abs(n-97)>abs(n-90) else 97
    elif n>=122:
        m=113
    elif(plmn==0):
        j=n+1
        m=NextPrime(j,plmn)
        #print(b)
    elif (plmn==1):
        j=n-1
        m=NextPrime(j,plmn)
    return m

def NextPrime(n,plmn):
  
    # Corner cases
  
    # This is checked so that we can skip  
    # middle five numbers in below loop 
    if (n % 2 == 0 or n % 3 == 0) : 
        return MakePrime(n,plmn)
  
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return MakePrime(n,plmn)
        i = i + 6
  
    return n
  
cases=input()
arr=sys.stdin.readlines()
#print(len(arr))
for i in range(1,len(arr),2):
        #print(i)
        for j in range(int(arr[i-1])):
            #print(j,arr[i-1])
            #print(ord((arr[i])[j]))
            c=NextPrime(ord((arr[i])[j]),0)
            k=NextPrime(ord((arr[i])[j]),1)
            #print(c,k,(k-ord((arr[i])[j])),(c-ord((arr[i])[j])))
            if (abs(c-ord((arr[i])[j]))>=abs(k-ord((arr[i])[j])) and ord((arr[i])[j])>=65):
                print(chr(k),end='')
            elif(ord((arr[i])[j])>=65):
                print(chr(c),end='')
            else:
                print(chr(67),end='')
        print()
    
        