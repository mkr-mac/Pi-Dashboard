import java.awt.Font;
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Calendar;

import javax.swing.BorderFactory;
import javax.swing.JPanel;
import javax.swing.JTextField;


public class TextBox {
	JTextField textbox;
	public TextBox(JPanel panel, String text, int x, int y){
		
		if(text.equals("CURRENT_TIME")){
			time();
		}else{
			textbox = new JTextField(text);
		}
		textbox.setBorder(BorderFactory.createEmptyBorder());
		textbox.setOpaque(false);
		textbox.setLocation(x, y);
		textbox.setSize(350, 78);
		textbox.setFont(new Font("Constantia", Font.BOLD, 60));
		textbox.setEditable(false);
		panel.add(textbox);
	}
	
	private void time() {
		DateFormat dateFormat = new SimpleDateFormat("hh:mm");
		Calendar cal = Calendar.getInstance();
		textbox = new JTextField(dateFormat.format(cal.getTime()));
	}
}
