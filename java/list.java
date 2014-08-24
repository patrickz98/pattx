import java.util.*;

class list
{
	public static void main(String[] args)
	{
		ArrayList<String> liste1 = new ArrayList<String>();
    	liste1.add("ABC");
    	liste1.add("Nachbar");
    	liste1.add("Transfer");
    	liste1.add("Oma");
    	liste1.add("Niemand");
		
		for(String a: liste1)
		{
			System.out.println(a);
		}
	}  
}