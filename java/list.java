import java.util.*;

class list
{
	public static void main(String[] args)
	{
		ArrayList<String> liste = new ArrayList<String>();
		
		liste.add("bla");
		liste.add("huhuh");
		
		for(String a: args)
		{
			liste.add(a);
		}

		
		System.out.println(liste.size());
		
		liste.remove("Nachbar");
//		liste.set(3, "Marmelade");
		
		if( liste.contains("bla") )
		{
			System.out.println(liste);
		}
//		System.out.println(liste.get(2));
	}  
}