# Problems: 

This are the type of problems that will help in coding practice and are fun .Please let me know if you find any error and Make sure to star the repos if you like .

## 1.) 2 string   
file name: twosstring.py

Given two strings of equal length, you have to tell whether they both strings are identical.

Two strings S1 and S2 are said to be identical, if any of the permutation of string S1 is equal to the string S2. See Sample explanation for more details.

## Input :

First line, contains an intger 'T' denoting no. of test cases.
Each test consists of a single line, containing two space separated strings S1 and S2 of equal length.

## Output:

For each test case, if any of the permutation of string S1 is equal to the string S2 print YES else print NO.

```
3
sumit mitsu                 
ambuj jumba                 
abhi hibb

output:
YES
YES
NO
```



## 2). Prime between 1 and given number

file name : primeNumBetween

You are given an integer N. You need to print the series of all prime numbers till N.

## Input Format

The first and only line of the input contains a single integer N denoting the number till where you need to find the series of prime number.

## Output Format

Print the desired output in single line separated by spaces.

```
9
output
2 3 5
```


##  3). seating arrengment

file name : settingArr.py


Akash and Vishal are quite fond of travelling. They mostly travel by railways. They were travelling in a train one day and they got interested in the seating arrangement of their compartment. The compartment looked something like

Window Seat : WS
Middle Seat : MS
Aisle Seat : AS

##  INPUT
First line of input will consist of a single integer T denoting number of test-cases. Each test-case consists of a single integer N denoting the seat-number.

## OUTPUT
For each test case, print the facing seat-number and the seat-type, separated by a single space in a new line.

```
2
18
40

output
19 WS
45 AS
```

## 4) anagram Delete Problem

Given two strings, a and b , that may or may not be of the same length, determine the minimum number of character deletions required to make a and b anagrams. Any characters can be deleted from either of the strings.

## Input :

test cases,t
two strings a and b, for each test case

## Output:

Desired O/p
Constraints :
string lengths<=10000

```
1
cde
abc
OUTPUT:
4
```

## 5).  Find product

file name : findProduct.py

You have been given an array A of size N consisting of positive integers. You need to find and print the product of all the number in this array Modulo .

## Input Format:
The first line contains a single integer N denoting the size of the array. The next line contains N space separated integers denoting the elements of the array

## Output Format:
Print a single integer denoting the product of all the elements of the array Modulo 10^9+7.   

```
5
1 2 3 4 5
output 
120
```


## 6). count divisors
file name :devisoreBetweenlr.py
 You have been given 3 integers - l, r and k. Find how many numbers between l and r (both inclusive) are divisible by k. You do not need to print these numbers, you just have to find their count.

## Input Format
The first and only line of input contains 3 space separated integers l, r and k.

## Output Format
Print the required answer on a single line.

```
1 10 1
output:
10
```

## 7). Bricks game 
file name : bricks.c

Patlu and Motu works in a building construction, they have to put some number of bricks N from one place to another, and started doing their work. They decided , they end up with a fun challenge who will put the last brick.

They to follow a simple rule, In the i'th round, Patlu puts i bricks whereas Motu puts ix2 bricks.

There are only N bricks, you need to help find the challenge result to find who put the last brick.

 ## Input:

First line contains an integer N.

## Output:

Output "Patlu" (without the quotes) if Patlu puts the last bricks ,"Motu"(without the quotes) otherwise.

```
13
Motu
```

## 8). Lift queries

There are 7 floors in BH3 and only 2 lifts. Initially Lift A is at the ground floor and Lift B at the top floor. Whenever someone calls the lift from N th floor, the lift closest to that floor comes to pick him up. If both the lifts are at equidistant from the N th floor, them the lift from the lower floor comes up.

## INPUT

First line contains a integer T denoting the number of test cases.

Next T lines contains a single integer N denoting the floor from which lift is called.

## OUTPUT
Output T lines containing one character "A" if the first lift goes to N th floor or "B" for the second lift.

```
2
3
5

output:
A
A
```

## 9). palyWithNumbers.py
You are given an array of n numbers and q queries. For each query you have to print the floor of the expected value(mean) of the subarray from L to R.

## Input:

First line contains two integers N and Q denoting number of array elements and number of queries.
Next line contains N space seperated integers denoting array elements.
Next Q lines contain two integers L and R(indices of the array).

## Output:
print a single integer denoting the answer.
contraints:
1<= N ,Q,L,R <= 10^6
1<= Array elements <= 10^9

## 10). Seven Segment 

## Input Format:
First line contains T (test cases).
Next T lines contain a Number N.

## Output Format:
Print the largest possible number numerically that can be generated using at max that many number of matchsticks which was used to generate N.

```
2
1
0
Output:
1
111
```

11.) Magic word
FILE NAME : magicWord.py 

Dhananjay has recently learned about ASCII values.He is very fond of experimenting. With his knowledge of ASCII values and character he has developed a special word and named it Dhananjay's Magical word.

A word which consist of alphabets whose ASCII values is a prime number is an Dhananjay's Magical word. An alphabet is Dhananjay's Magical alphabet if its ASCII value is prime.

Dhananjay's nature is to boast about the things he know or have learnt about. So just to defame his friends he gives few string to his friends and ask them to convert it to Dhananjay's Magical word. None of his friends would like to get insulted. Help them to convert the given strings to Dhananjay's Magical Word.

Rules for converting:

1.Each character should be replaced by the nearest Dhananjay's Magical alphabet.
2.If the character is equidistant with 2 Magical alphabets. The one with lower ASCII value will be considered as its replacement.

## Input format:

First line of input contains an integer T number of test cases. Each test case contains an integer N (denoting the length of the string) and a string S.

## Output Format:

For each test case, print Dhananjay's Magical Word in a new line.

## Constraints:
1 <= T <= 100
1 <= |S| <= 500

```
1
6
AFREEN

output: CGSCCSO
```