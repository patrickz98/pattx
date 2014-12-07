import java.io.*;
import java.util.*;

public class test
{
	public static void main(String[] args) throws Exception
	{
		System.out.print("Host ip:\t");
		BufferedReader stdin = new BufferedReader( new InputStreamReader(System.in));
		String tmp = stdin.readLine();

		if (tmp.equals(""))
		{
			System.out.println("true");
		}
	}
}