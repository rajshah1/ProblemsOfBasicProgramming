package coding;

import java.util.ArrayList;

public class reverse {
    public static double reverseInt(int num) {
    	double reversenum=0,zeroes=0,d=num;
    	while(d%10 == 0 && d != 0) {
    		  zeroes++;
   			  d /= 10;
    	}
    	while( num != 0 )
        {
            reversenum = reversenum * 10;
            reversenum = reversenum + num%10;
            num = num/10;
        }	
        	if(zeroes>0) {
        		reversenum=Math.pow(10.0,zeroes)*reversenum;
        	}
    	return reversenum;
    }
	 
	public static void main(String[] args) {
		// TODO Auto-generated method stub
	    ArrayList<Integer> IntList = new ArrayList<>();
	    IntList.add(972423194);IntList.add(776100481);IntList.add(736859790);IntList.add(844690424);IntList.add(823033042);IntList.add(944853776);
	    IntList.add(971324293);IntList.add(162355436);
	    long sum=0;	
	    for (Integer num : IntList) { 		      
	           sum+=reverseInt(num);		
	      }
	    System.out.println(sum);

	}
	
	
	

}
