import java.io.*;
import java.net.*;

public class example
{
	public static void main(String args[]) throws Exception
	{
		for (int x = 0; x < 20; x++)
		{
			System.out.print(x + "\n");
		}
		
		URL oracle = new URL("http://www.oracle.com/");
        BufferedReader in = new BufferedReader(
        new InputStreamReader(oracle.openStream()));

        String inputLine;
        
        try 
        {
        	File file = new File("example.txt");
        	BufferedWriter output = new BufferedWriter(new FileWriter(file));
          
        	while ((inputLine = in.readLine()) != null)
        		output.write(inputLine + "\n");
        
        	output.close();
        } 
        catch ( IOException e ) 
        {
        	e.printStackTrace();
        }
        
        in.close();
        
        Console cons = System.console();
		cons.printf("\n");
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