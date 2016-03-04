import java.awt.image.BufferedImage;
import java.io.File;

import javax.imageio.ImageIO;
import javax.swing.BorderFactory;
import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JPanel;


public class ImageButton {

	public ImageButton(JPanel panel, String action, int x, int y, String imagePath) {
		try{
			BufferedImage buttonIcon = ImageIO.read(new File(imagePath));
			JButton button = new JButton(new ImageIcon(buttonIcon));
			button.setBorder(BorderFactory.createEmptyBorder());
			button.setContentAreaFilled(false);

	        button.setSize(334, 79);
	        button.setLocation(x, y);
			
		    button.setActionCommand(action); 
		    button.addActionListener(new ButtonClickListener());
		    panel.add(button);
		    
		}catch(Exception e){
			System.out.println("Failed to create ImageButton.");
		}
	}
	
}
