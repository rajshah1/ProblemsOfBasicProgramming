'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
import sys
input1=int(input())
input2=sys.stdin.readlines()
input2 = [int(i) for i in input2]


for j in input2:
    couch=j%12
   # print(couch)
    if (couch==1):
        print('{fu} WS'.format(fu=11+j))
    if (couch==2):
        print('{fu} MS'.format(fu=j+9))
    if (couch==3):
        print('{fu} AS'.format(fu=7+j))
    if (couch==4):
        print('{fu} AS'.format(fu=5+j))
    if (couch==5):
        print('{fu} MS'.format(fu=3+j))
    if (couch==6):
        print('{fu} WS'.format(fu=1+j))
    if (couch==0):
        print('{fu} WS'.format(fu=j-11))
    if (couch==11):
        print('{fu} MS'.format(fu=j-9))
    if (couch==10):
        print('{fu} AS'.format(fu=j-7))
    if (couch==9):
        print('{fu} AS'.format(fu=j-5))
    if (couch==8):
        print('{fu} MS'.format(fu=j-3))
    if (couch==7):
        print('{fu} WS'.format(fu=j-1))
    
        
    
        

    
   
    