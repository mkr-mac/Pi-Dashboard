import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;

import javax.imageio.ImageIO;
import javax.swing.ImageIcon;
import javax.swing.JLabel;
import javax.swing.JPanel;


public class Picture {
	
	public Picture(JPanel panel, int x, int y, int sizeX, int sizeY, String imagePath) {
		try{
			BufferedImage myPicture = ImageIO.read(new File(imagePath));
			JLabel picLabel = new JLabel(new ImageIcon(myPicture));
	
	        picLabel.setSize(sizeX, sizeY);
			picLabel.setLocation(x, y);
			panel.add(picLabel);
			
		}catch(Exception e){
			System.out.println("Failed to load Image.");
		}
	}
}
