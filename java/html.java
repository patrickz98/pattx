import java.io.*;
import java.net.*;
import java.util.*;

public class html
{
	public static void main(String args[]) throws Exception
	{
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
	}
}