import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class swing extends JFrame
{
	JButton test1, test2;
	int i = 0;
	int j = 100;

	class Actionsnitch1 implements ActionListener
	{
		public void actionPerformed(ActionEvent e)
		{
			test1.setText(String.valueOf(i));
			i++;
		}
	}

	class Actionsnitch2 implements ActionListener
	{
		public void actionPerformed(ActionEvent e)
		{
			test2.setText(String.valueOf(j));
			j--;
		}
	}

	swing(String title)
	{
		super(title);
		
		test1 = new JButton("test1");
		test2 = new JButton("test2");
		
		setLayout(new FlowLayout());
		
		add(test1);
		add(test2);
		
		setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
		
		test1.addActionListener(new Actionsnitch1());
		test2.addActionListener(new Actionsnitch2());
	}
	
	public static void main(String[] args)
	{
		swing window = new swing("Test window whit swing");
		window.pack();
		window.setSize(300,100);
		window.setVisible(true);
	}
}