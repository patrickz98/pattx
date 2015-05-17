import java.awt.Color;
import java.awt.image.BufferedImage;
import java.io.File;

import javax.imageio.ImageIO;

public class pixel2
{
    public static void main(String[] args) throws Exception
    {

        BufferedImage img = ImageIO.read(new File("mandrill.jpg"));

       	for (int x = 0, maxX = img.getWidth(); x < maxX; x++)
       	{
            for (int y = 0, maxY = img.getHeight(); y < maxY; y++)
            {
                int rgb = img.getRGB(y, x);
		            Color c = new Color(rgb);
		            System.out.printf("\rRed: %3s", c.getRed());
		            System.out.printf(" Green: %3s", c.getGreen());
                System.out.printf(" Blue: %3s", c.getBlue());
			      }
		    }

        System.out.println();
    }
}
