'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
import sys
import math
a=sys.stdin.readlines()
#converting int list to string list 
# results = list(map(int, results))
#print(a)
#math.pow(10,9)
c=1
for i in a:
    b=str(i).split()
    b = [int(j) for j in b]
for k in b:
    c=k*c

#print(c)
e=int(math.pow(10,9)+7)
print(c%e)


#print(b)



    
    
   