import java.util.*;
import java.io.*;
import java.net.*;

public class keyfile
{
	public static void main(String[] args)
	{
		try
		{
			String textdoc = "filewriter.txt";
			Console cons = System.console();
			FileWriter text = new FileWriter(textdoc);
			
			Scanner sc = new Scanner(cons.reader());
			
			cons.printf("Write into " + textdoc + "\n");
			
			String line = sc.nextLine();
			byte[] bin = line.getBytes("UTF-8");
			
			for (byte x: bin)
			{
				System.out.print((char) x + " --> ");
				System.out.print(Integer.toBinaryString(x) + "\n");
				text.write((char) x + " --> " + Integer.toBinaryString(x) + "\n");
			}
			
			text.close();
			
			
// 			for (int x = 0; x < 10000; x++)
// 			{
// 				for (byte y: bin)
// 				{
// 					System.out.print(Integer.toBinaryString(x) + "\r");
// 				}
// 			}
// 			System.out.println();

		}
		catch(Exception e)
		{
			System.err.println("File Error");
		}
	}
}