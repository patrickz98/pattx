import java.io.*;
import java.net.*;
import java.util.*;
import java.util.regex.*;

public class spiegel
{
	public static void main(String args[]) throws Exception
	{
		long startTime = System.currentTimeMillis();
		URL html = new URL("http://www.spiegel.de/schlagzeilen/");
        BufferedReader in = new BufferedReader(new InputStreamReader(html.openStream(), "ISO-8859-1"));

        String inputLine;
        
        ArrayList<String> title = new ArrayList<String>();
		ArrayList<String> link = new ArrayList<String>();

        try
        {
        	File file = new File("spiegel.txt");
        	BufferedWriter output = new BufferedWriter(new FileWriter(file));

        	while ((inputLine = in.readLine()) != null)
        	{
         		byte cache[] = inputLine.getBytes();
  				String line = new String(cache, "UTF-8");
				
        		Pattern r = Pattern.compile("<a href=\"(.*?)\".*?title=\"(.*?)\">");
				Matcher m = r.matcher(line);

				if (m.find() && !m.group(1).matches("http://www.spiegel.de/.*") 
					&& !m.group(2).equals("Anzeige") && !m.group(2).matches(".*class=\".*")
					&& m.group(2).matches(".*[Ww]irtschaft.*") | m.group(1).matches(".*[Ww]irtschaft.*"))
				{
					output.write(m.group(2) + " --> http://www.spiegel.de" + m.group(1) + "\n");
					title.add(m.group(2));
					link.add("http://www.spiegel.de" + m.group(1));
				}
        	}

			output.close();
			
        } 
        catch ( IOException e ) 
        {
        	e.printStackTrace();
        }
        
        System.out.println("Spiegel title size --> " + title.size());
        in.close();
        System.out.println("Runtime --> " + (System.currentTimeMillis() - startTime));
	}
}