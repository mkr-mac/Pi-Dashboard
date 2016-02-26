import java.awt.*;
import java.awt.event.*;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;

import javax.imageio.ImageIO;
import javax.swing.*;

public class GUI {
	
	private JFrame frame;
	private JLabel headerLabel;
	private JLabel statusLabel;
	private JPanel controlPanel;
	
	public GUI(){		
		initialize();
	}

	public static void main(String[] args) {
		GUI g = new GUI();
		g.showEventDemo();
	}

	private void initialize() {
		
		frame = new JFrame();
		frame.setSize(800, 480);
		frame.setExtendedState(JFrame.MAXIMIZED_BOTH);
		frame.setUndecorated(true);
		frame.setLayout(new GridLayout(3,1));
		
		headerLabel = new JLabel("",JLabel.CENTER);
		statusLabel = new JLabel("",JLabel.CENTER);
		
		statusLabel.setSize(350, 100);
		frame.addWindowListener(new WindowAdapter(){
			public void windowClosing(WindowEvent windowEvent){
				System.exit(0);
			}
		});
		controlPanel = new JPanel();
		controlPanel.setLayout(new FlowLayout());
		
		frame.add(headerLabel);
		frame.add(controlPanel);
		frame.add(statusLabel);
		frame.setVisible(true);
	}
	
	private void showEventDemo() {
		headerLabel.setText("Control in action: Button");

		JButton okButton = new JButton("OK");
		JButton cancelButton = new JButton ("Cancel");
		
		okButton.setActionCommand("OK");
		ImageButton submitButton = new ImageButton(frame, "", 0, 0, "title.png");
	    cancelButton.setActionCommand("Cancel");
	    
	    controlPanel.add(okButton);
	    controlPanel.add(cancelButton);       

	    frame.setVisible(true);  
	}
}
