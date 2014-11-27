class pat
{
	protected String enter;

	pat (String y)
	{
		enter = y;	
	}

	void blup()
	{
		System.out.println(enter);
	}
}

public class klassen2
{	
	static void patprint(String x)
	{
		System.out.println(x);
		System.out.println();
		System.out.println("Class:");
		
		pat test = new pat("classe void");
		test.blup();
		System.out.println(test.enter + " outside");
	}
	
	public static void main(String args[])
	{
		System.out.println("Start");
		System.out.println();
		
		patprint("test void");
	}
}