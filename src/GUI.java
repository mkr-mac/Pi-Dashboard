import java.awt.*;
import java.awt.event.*;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;

import javax.imageio.ImageIO;
import javax.swing.*;

public class GUI {
	
	private JFrame frame;
	private JFrame mediaLine;
	private JPanel panel;
	private JPanel mediaPanel;
	
	public GUI(){		
		initialize();
	}

	public static void main(String[] args) {
		GUI g = new GUI();
		g.addPanelContent();
	}

	private void initialize() {
		
		frame = new JFrame();
		frame.setSize(800, 480);
		frame.setExtendedState(JFrame.MAXIMIZED_BOTH);
		frame.setUndecorated(true);
		
		mediaLine = new JFrame();
		mediaLine.setSize(800, 72);
		mediaLine.setExtendedState(JFrame.MAXIMIZED_BOTH);
		mediaLine.setUndecorated(true);
		mediaLine.setAlwaysOnTop(true);
		mediaLine.setLocationByPlatform(true);
        mediaLine.setBackground(new Color(1.0f,1.0f,1.0f,0.0f));
		
		panel = new JPanel();
        panel.setOpaque(true);
        panel.setBackground(Color.BLUE);
        panel.setLayout(null);
		
        mediaPanel = new JPanel();
        mediaPanel.setOpaque(false);
        mediaPanel.setLayout(null);
        
		frame.addWindowListener(new WindowAdapter(){
			public void windowClosing(WindowEvent windowEvent){
				System.exit(0);
			}
		});
		frame.setVisible(true);
	}
	
	private void addPanelContent() {

		TextBox b1text = new TextBox(mediaPanel, "Media", 10, 0);
		ImageButton button1 = new ImageButton(panel, "kill", 24, 112, "LargeButton.png");
		ImageButton button2 = new ImageButton(panel, "kill", 24, 204, "LargeButton.png");
		ImageButton button3 = new ImageButton(panel, "kill", 24, 296, "LargeButton.png");


		Picture topLine = new Picture(mediaPanel, 0, 0, "TopLine.png");
		Picture bottomLine = new Picture(mediaPanel, 0, 408, "BottomLine.png");
		Picture minuteHand = new Picture(panel, 395, 61, "MinuteHand.png");
		Picture clock = new Picture(panel, 395, 61, "Clock.png");
		Picture background = new Picture(panel, 0, 0, "Background.png");
		
	    frame.setContentPane(panel);
	    frame.setVisible(true);
	    mediaLine.setContentPane(mediaPanel);
	    mediaLine.setVisible(true);
	}
}
