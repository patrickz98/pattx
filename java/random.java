public class random 
{
	public static void main( String[] args )
	{
		for(int a = 0; a < 10000; a++)
		{
			System.out.print("\r");
			System.out.print(Math.random());
		}
		System.out.println("");
	}
}
