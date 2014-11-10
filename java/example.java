import java.io.*;
import java.net.*;
import java.util.*;

public class example
{
	public static void main(String args[]) throws Exception
	{
		String pat = "Patrick";
		
		List bla = new ArrayList();
		for (int x = 0; x < 10; x++)
		{
			bla.add(x);
		}
		System.out.println(bla.get(0));
		
		System.out.println(pat.length());
		for (int x = 0; x < 10; x++)
		{
			for (int y = 0; y < pat.length(); y++)
			{
				System.out.print("\r");
				System.out.print(pat.charAt(y) + "\r");
				Thread.sleep(50);
			}
		}
	}
}