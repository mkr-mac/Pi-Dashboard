import java.awt.image.BufferedImage;
import java.io.File;

import javax.imageio.ImageIO;
import javax.swing.BorderFactory;
import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JFrame;


public class ImageButton {

	public ImageButton(JFrame frame, String action, int x, int y, String imagePath) {
		try{
			BufferedImage buttonIcon = ImageIO.read(new File(imagePath));
			JButton button = new JButton(new ImageIcon(buttonIcon));
			button.setBorder(BorderFactory.createEmptyBorder());
			button.setContentAreaFilled(false);

		    button.setActionCommand("kill"); 
		    button.addActionListener(new ButtonClickListener()); 
		    frame.add(button);
		    
		}catch(Exception e){
			
		}
	}
	
}
