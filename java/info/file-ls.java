import java.io.*;

public class file
{
	public static void main(String[] args)
	{
		File datei = new File("./");
		File[] listOfFiles = datei.listFiles();
		
		for(int x = 0; x < listOfFiles.length; x++)
		{
			System.out.println(listOfFiles[x]);
		}
	}
}