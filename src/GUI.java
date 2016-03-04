import java.awt.*;
import java.awt.event.*;

import javax.swing.*;

public class GUI {
	
	private JFrame frame;
	private JFrame mediaLine;
	private JPanel panel;
	private JPanel mediaPanel;
	
	TextBox time;
	TextBox date;
	ImageButton button1;
	ImageButton button2;
	ImageButton button3;

	Picture topLine;
	Picture bottomLine;
	Picture minuteHand;
	Picture clock;
	Picture background;
	
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

		time = new TextBox(mediaPanel, "CURRENT_TIME", 660, 400);
		date = new TextBox(mediaPanel, "CURRENT_DATE", 350, 420);
		button1 = new ImageButton(panel, "media", 24, 112, "assets\\MediaButton.png");
		button2 = new ImageButton(panel, "kill", 24, 204, "assets\\LargeButton.png");
		button3 = new ImageButton(panel, "kill", 24, 296, "assets\\LargeButton.png");


		topLine = new Picture(mediaPanel, 0, 0, "assets\\TopLine.png");
		bottomLine = new Picture(mediaPanel, 0, 408, "assets\\BottomLine.png");
		minuteHand = new Picture(panel, 395, 61, "assets\\MinuteHand.png");
		clock = new Picture(panel, 395, 61, "assets\\Clock.png");
		background = new Picture(panel, 0, 0, "assets\\Background.png");
		
	    frame.setContentPane(panel);
	    frame.setVisible(true);
	    mediaLine.setContentPane(mediaPanel);
	    mediaLine.setVisible(true);
	}
}
