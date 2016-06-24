
import java.awt.image.BufferedImage;
import java.io.File;

import javax.imageio.ImageIO;
import javax.swing.ImageIcon;
import javax.swing.JLabel;
import javax.swing.JPanel;


public class Picture {
	
	public Picture(JPanel panel, int x, int y, String imagePath) {
		try{
			java.net.URL image = getClass().getResource(imagePath);
			ImageIcon pic = new ImageIcon(image);
			JLabel picLabel = new JLabel(pic);
	
	        picLabel.setSize(pic.getIconWidth(), pic.getIconHeight());
			picLabel.setLocation(x, y);
			panel.add(picLabel);
			
		}catch(Exception e){
			System.out.println("Failed to load Image.");
		}
	}
}
