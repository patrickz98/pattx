import java.io.*;
import java.net.*;
import java.util.*;

public class shell
{
	public static void main(String args[]) throws Exception
	{
        Console cons = System.console();
		cons.printf("Shell: ");
		String eingabe = cons.readLine();
		System.out.print(eingabe + "\n");

		Runtime r = Runtime.getRuntime();
		Process p = r.exec(eingabe);
		p.waitFor();
		BufferedReader b = new BufferedReader(new InputStreamReader(p.getInputStream()));
		String line = "";

		while ((line = b.readLine()) != null) 
		{
			System.out.println(line);
		}

		b.close();
	}
}