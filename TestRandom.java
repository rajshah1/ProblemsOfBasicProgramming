package testrandom;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Random;

public class TestRandom {
	public static void main(String[] args) {
		// TODO Auto-generated method stub
	int totalUser=10;
	
	HashMap<String,List<String>> finalResultMap=new HashMap<>();
	for (int CurrentUserCounter=0;CurrentUserCounter<totalUser;CurrentUserCounter++) {
		int addThisManyFriends=getRandomNumberUsingNextInt(totalUser-1);
		List<Integer> temListRandomNumber=new ArrayList<Integer>();
		List<String> temConvertedList=new ArrayList<String>();
		temListRandomNumber=generateRandomNumber(totalUser,addThisManyFriends,(CurrentUserCounter+1));
		
		temListRandomNumber.parallelStream().forEach(e->{
			temConvertedList.add("User"+e.toString());
		});
		//temListRandomNumber.stream().forEach(System.out::println);
		//temConvertedList.stream().forEach(System.out::println);
		
		finalResultMap.put("User"+(CurrentUserCounter+1),temConvertedList);
	}
	System.out.println("Final Random Genrated Relationship Mash : "+finalResultMap);
}
	public static List<Integer> generateRandomNumber(int totalUser,int addThisManyFriends,int currentValue) {
		ArrayList<Integer> allInteratbleExceptCurrentUser = new ArrayList<Integer>();
		ArrayList<Integer> finalRandomList = new ArrayList<Integer>();
        for (int i=1; i<totalUser+1; i++) {
        	if(i!=currentValue) {
        		allInteratbleExceptCurrentUser.add(new Integer(i));
        	}
        }
        Collections.shuffle(allInteratbleExceptCurrentUser);
        for (int i=0; i<addThisManyFriends; i++) {
        	finalRandomList.add(allInteratbleExceptCurrentUser.get(i));
        }
		return finalRandomList;
	}
	
	public static int getRandomNumberUsingNextInt(int totalNumberOfUsers) {
        int min=0;
		Random random = new Random();
        return random.nextInt(totalNumberOfUsers-min)+min+1;
    }

}
