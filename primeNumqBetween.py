'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
num =input()
number=int(num)
a=[]
counter=0
if (number>=3):
    
    for i in range(2,number):
        for compare in range(1,i):
            if (i%compare==0):
                counter+=1
      
        if (counter<2):
            a.append(i)
            
            counter=0
        else:
            counter=0
    
    
    for i in range(len(a)):
        print(a[i], end =" ")
   
       
            
                

