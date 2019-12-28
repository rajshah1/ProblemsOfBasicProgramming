'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here

import sys
case=int(input())
floors=sys.stdin.readlines()
floors=[int(k) for k in floors]
a_postion=0
b_postion=7
for i in range(case):
    current_lif_call=floors[i]
    if(abs(current_lif_call-a_postion)>abs(current_lif_call-b_postion)):
        b_postion=current_lif_call
        print("B")
    elif(abs(current_lif_call-a_postion)<abs(current_lif_call-b_postion)):
        a_postion=current_lif_call
        print("A")
    else:
        if(current_lif_call>a_postion):
            a_postion=current_lif_call
            print("A")

            