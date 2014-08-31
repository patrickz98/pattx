import java.util.*;

class test2
{
	public static void main(String[] args)
	{
  		int input = Integer.parseInt(args[0]);
  		int[] list = new int[12];
		for(int a = 0; a < 12; a++)
		{
			list[a] = a + a;
		}
		for(int a = 0; a < 12; a++)
		{
			System.out.println(list[a]);
		}
	}  
}