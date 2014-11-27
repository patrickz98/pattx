import java.io.*;
import java.net.*;
import java.util.*;
import java.util.regex.*;

public class example2
{
	public static void main(String args[]) throws Exception
	{
		URL oracle = new URL("http://www.oracle.com/");
        BufferedReader in = new BufferedReader(
        new InputStreamReader(oracle.openStream()));

        String inputLine;
        
        List tmp = new ArrayList();
        
        try
        {
        	while ((inputLine = in.readLine()) != null)
        	{
        		boolean bla = inputLine.matches(".*[Oo]racle.*");
				if (bla)
				{
//					System.out.print(bla + "\n");
//					System.out.print(" --> " + inputLine.split("[Oo]racle")[1] + "\n");
					tmp.add(inputLine);
				}
        	}
        } 
        catch ( IOException e ) 
        {
        	e.printStackTrace();
        }
        
        System.out.println(oracle);
        System.out.println("Oracle size --> " + tmp.size());
        in.close();
	}
}