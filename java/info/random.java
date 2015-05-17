import java.io.*;
import java.net.*;
import java.util.*;

public class random
{
	public static void main(String args[]) throws Exception
	{
		String pat = args[0];

		char buchstabe;
		int zahl;
		
		for (int x = 0; x < pat.length() * 2; x++)
		{
			Random randomno = new Random();
			zahl = randomno.nextInt(pat.length());
			buchstabe = pat.charAt(zahl);
			
			System.out.print(buchstabe);
			Thread.sleep(50);
		}

		System.out.println();

		byte[] infoBin = pat.getBytes("UTF-8");
        for (byte b : infoBin) 
        {
            System.out.println((char) b + " --> "
                    + Integer.toBinaryString(b));
        }
		System.out.println();
		System.out.println("Finish.");
	}
}