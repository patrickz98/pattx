import java.awt.*;
import java.awt.event.*;

public class awt extends Frame
{
	class snitch extends WindowAdapter
	{
		public void windowClosing(WindowEvent e)
		{
			System.err.println(e);
			System.exit(0);
		}
	}
	
	class Actionsnitch implements ActionListener
	{
		public void actionPerformed(ActionEvent e)
		{
			java.awt.Toolkit.getDefaultToolkit().beep();
			System.err.println(e);
		}
	}
	
	awt(String title)
	{
		super(title);
	
		Button test1 = new Button("test1");
		Button test2 = new Button("test2");

		setLayout(new FlowLayout());
		
		add(test1);
		add(test2);
		
		addWindowListener(new snitch());
		
		test1.addActionListener(new Actionsnitch());
		test2.addActionListener(new Actionsnitch());
	}
	
	public static void main(String[] args)
	{
		awt window = new awt("Test Window");
		
		window.pack();
		window.setVisible(true);
	}
}