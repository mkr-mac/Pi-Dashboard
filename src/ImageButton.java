import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.image.BufferedImage;
import java.io.File;

import javax.imageio.ImageIO;
import javax.swing.BorderFactory;
import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JFrame;


public class ImageButton {

	public ImageButton(JFrame frame, String name, String imagePath, int x, int y) {
		try{
			BufferedImage buttonIcon = ImageIO.read(new File(imagePath));
			JButton button = new JButton(new ImageIcon(buttonIcon));
			button.setBorder(BorderFactory.createEmptyBorder());
			button.setContentAreaFilled(false);

		    button.setActionCommand(name); 
		    button.addActionListener(new ButtonClickListener()); 
		    frame.add(button);
		}catch(Exception e){
			
		}
	}
	
	private class ButtonClickListener implements ActionListener{
		public void actionPerformed(ActionEvent e) {
			String command = e.getActionCommand();  
			if( command.equals( "OK" ))  {
				GUI.statusLabel.setText("Ok Button clicked.");
			}
			else if( command.equals( "Submit" ) )  {
				statusLabel.setText("Submit Button clicked."); 
			}
			else  {
				statusLabel.setText("Cancel Button clicked.");
			}  	
		}		
	}
}
