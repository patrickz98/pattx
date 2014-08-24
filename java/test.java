import java.util.Random;

public class test 
{
	public static void main(String[] args)
	{
		double code = Math.random();
		System.out.println("Code: " + code);
		double code2 = Math.random();
		
		while(true)
		{
			if (code == code2)
			{
			System.out.println("Code is " + code2);
			System.exit(0); 
			}
			else
			{
			System.out.print("\r");
			code2 = Math.random();
			System.out.print(code2);
			}
		}
	}
}