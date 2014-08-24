import java.util.*;

class test2
{
	public static void main(String[] args)
	{
		ArrayList<String> liste = new ArrayList<String>();
		
		for(String a: args)
		{
			liste.add(a);
		}
		
		liste.add("bla");
		liste.add("huhuh");
		
		System.out.println(liste.size());
		
		liste.remove("Nachbar");
				
		liste.set(3, "Marmelade");
		
		if( liste.contains("bla") )
		{
			System.out.println(liste);
		}

		System.out.println(liste.get(2));
	}  
}