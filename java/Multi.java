import java.io.*;
import java.util.*;

class MyThread extends Thread
{
	int zahl;
	
	public void run()
	{
		for (int x = 10; x > 0; x--)
		{
			Random randomno = new Random();
			int zahl = randomno.nextInt(5000);

			System.out.println("Thread 1 running " + zahl / 1000 + "s (" + zahl + ")");

			try 
			{
				sleep(zahl);			
			}
			catch (Exception e)
			{
				return;
			}
		}
	}
}

class MyThread2 extends Thread
{
	public void run()
	{
		for (int x = 10; x > 0; x--)
		{

			Random randomno = new Random();
			int zahl = randomno.nextInt(5000);

			System.out.println("Thread 2 running " + zahl / 1000 + "s (" + zahl + ")");
			
			try 
			{
				sleep(zahl);			
			}
			catch (Exception e)
			{
				return;
			}
		}
	}
}

public class Multi
{
	public static void main(String[] args)
	{
		MyThread bla = new MyThread();
		bla.start();
		
		MyThread2 bla2 = new MyThread2();
		bla2.start();
		
	}
}