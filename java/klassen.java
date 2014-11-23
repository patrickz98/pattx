class test
{
	test(String x)
	{
		System.out.println(x);
	}
	void pat()
	{
		System.out.println("class");
	}
}

class test2 extends test
{
	test2(String y)
	{
		super(y);
		System.out.println(y + "2");
	}
	
	void pat2()
	{
		System.out.println("class2");
	}
}

public class klassen
{	
	public static void main(String args[])
	{
		System.out.println("haoll");
		test bla = new test("huhu");
		bla.pat();
		
		System.out.println();

		test2 bla2 = new test2("huhu");
		bla2.pat2();
	}
}
