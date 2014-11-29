import java.io.*;
import java.net.*;
import java.util.*;

public class aktien
{
	public static void main(String args[]) throws Exception
	{
		URL oracle = new URL("http://finance.yahoo.com/d/quotes.csv?s=AAPL&f=n+o+p2+p5");
        BufferedReader in = new BufferedReader(
        new InputStreamReader(oracle.openStream()));

        String inputLine;
        
        try 
        {
        	while ((inputLine = in.readLine()) != null)
        	{
				Date bla = new Date();
				System.out.print(bla + "\n");
        		System.out.print(inputLine + "\n");
        	}        	
        } 
        catch ( IOException e ) 
        {
        	e.printStackTrace();
        }
        
        in.close();
	}
}
