import java.io.*;
import java.util.*;

class test
{
	BufferedWriter output;
	
	test()
	{
        try 
        {
        	File file = new File("example.txt");
        	this.output = new BufferedWriter(new FileWriter(file));
        } 
        catch ( IOException e ) 
        {
        	e.printStackTrace();
        }
	}
	
	void make(String x)
	{
		try 
        {
			output.write(x + "\n");
        } 
        catch ( IOException e ) 
        {
        	e.printStackTrace();
        }
	}
	
	void end()
	{
		try 
        {
        	output.close();
        } 
        catch ( IOException e ) 
        {
        	e.printStackTrace();
        }
	}
}

public class klassen3
{	
	public static void main(String args[])
	{
		System.out.println("haoll");
		test bla = new test();
		bla.make("test");
		bla.make("test");
		bla.make("test");
		bla.make("test");
		bla.end();
		System.out.println();
	}
}
