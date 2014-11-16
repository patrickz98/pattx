import java.io.*;

public class read 
{
	public static void main(String args[]) throws IOException
	{
	
		String file = "bla.txt";
		BufferedReader br = new BufferedReader(new FileReader(file));
		String line = br.readLine();

		while (line != null) 
		{
			System.out.println(line);
			line = br.readLine();
        }
        br.close();        	
	}
}
