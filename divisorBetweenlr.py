'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
a=input()
#print(a)
b=a.split()
counter=0
b=[int(i) for i in b]
while(b[0]<=b[1]):
    if(b[0]%b[2]==0):
        counter+=1
        b[0]+=1
    else:
        b[0]+=1
print(counter)