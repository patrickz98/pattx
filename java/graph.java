import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class grahp extends JFrame
{
	CMeinCanvas m_malflaeche;
	int aktFunktion = 0;
	
	public static void main(String[] args)
	{
		CFunkPlotter fenster = new CFunkPlotter("Bladsfadsf");
		fenster.pack();
		fenster.setSize(450,350);
		fenster.setResizable(false);
		fenster.setVisible(true);
	}
	
	CFunkPlotter(String title)
	{
		super(title);
		setLayout(new FlowLayout());
		m_malflaeche = new CMeinCavas();
		add(m_malflaeche);
		
		JButton f1 = new JButton("tan(x)");
		JButton f2 = new JButton("x^3");
		add(f1);
		add(f2);
		
		class CMeinActionLauscher implements ActionListener
		{
			public void actionPerformed(ActionEvent e)
			{
				String label;
				
				label = e.getActionCommand();
				
				if(label.equals("tan(x)"))
					aktFunktion = 1;
				else
				aktFunktion = 2;
				
				m_malflaeche.repaint();
			}
		}
		
		f1.addActionListener(new CMeinActionLauscher());
		f2.addActionListener(new CMeinActionLauscher());
		
		setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
	}
}