
import java.awt.image.BufferedImage;
import java.io.File;

import javax.imageio.ImageIO;
import javax.swing.ImageIcon;
import javax.swing.JLabel;
import javax.swing.JPanel;


public class Picture {
	
	public Picture(JPanel panel, int x, int y, String imagePath) {
		try{
			BufferedImage image = ImageIO.read(new File(imagePath));
			JLabel picLabel = new JLabel(new ImageIcon(image));
	
	        picLabel.setSize(image.getWidth(), image.getHeight());
			picLabel.setLocation(x, y);
			panel.add(picLabel);
			
		}catch(Exception e){
			System.out.println("Failed to load Image.");
		}
	}
}
