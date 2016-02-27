import java.awt.image.BufferedImage;
import java.io.File;

import javax.imageio.ImageIO;
import javax.sound.sampled.AudioInputStream;
import javax.sound.sampled.AudioSystem;
import javax.sound.sampled.Clip;
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
		    /*
			String soundName = "click.wav";    
			AudioInputStream audioInputStream = AudioSystem.getAudioInputStream(new File(soundName).getAbsoluteFile());
			Clip clip = AudioSystem.getClip();
			clip.open(audioInputStream);
			clip.start();
			*/
		    panel.add(button);
		    
		}catch(Exception e){
			System.out.println("Failed to create ImageButton.");
		}
	}
	
}
