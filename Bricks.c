/*
// Sample code to perform I/O:
#include <stdio.h>

int main(){
	int num;
	scanf("%d", &num);              			// Reading input from STDIN
	printf("Input number is %d.\n", num);       // Writing output to STDOUT
}

// Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
*/

// Write your code here
#include <stdio.h>

int main(){
	int n,i,j,k,s=0,f=0,fl=0,m,p;
	scanf("%d",&n);
	for(i=1;i<=n;i++)
	{
	   m=2*i,p=i;
	   for(j=1;j<=p;j++)
	  {
	      if(s<n)
	      s++;
	      if(s==n)
	      {
	          printf("Patlu");
	          f=1;
	          break;
	      }
	  }
	  if(f==0)
	  {
	      for(k=1;k<=m;k++)
	  {
	      if(s<n)
	      ++s;
	      if(s==n)
	      {
	          printf("Motu");
	          fl=1;
	          break;
	      }
	   }
	}
	if(f==1 ||fl==1)
	  break;
}
}