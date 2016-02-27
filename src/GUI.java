import java.awt.*;
import java.awt.event.*;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;

import javax.imageio.ImageIO;
import javax.swing.*;

public class GUI {
	
	private JFrame frame;
	private JPanel panel;
	
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
		
		panel = new JPanel();
        panel.setOpaque(true);
        panel.setBackground(Color.BLUE);
        panel.setLayout(null);
		
		frame.addWindowListener(new WindowAdapter(){
			public void windowClosing(WindowEvent windowEvent){
				System.exit(0);
			}
		});
		frame.setVisible(true);
	}
	
	private void showEventDemo() {
		//headerLabel.setText("Control in action: Button");

		ImageButton button1 = new ImageButton(panel, "kill", 24, 112, "LargeButton.png");
		ImageButton button2 = new ImageButton(panel, "kill", 24, 204, "LargeButton.png");
		ImageButton button3 = new ImageButton(panel, "kill", 24, 296, "LargeButton.png");

		Picture clock = new Picture(panel, 395, 61, 358, 358, "Clock.png");
		Picture background = new Picture(panel, 0, 0, 800, 480, "Background.png");
		
	    frame.setContentPane(panel);
	    frame.setVisible(true);
	}
}
