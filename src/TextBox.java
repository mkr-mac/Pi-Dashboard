import java.awt.Font;
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Calendar;

import javax.swing.BorderFactory;
import javax.swing.JPanel;
import javax.swing.JTextField;


public class TextBox {
	
	public TextBox(JPanel panel, String text, int x, int y){
		DateFormat dateFormat = new SimpleDateFormat("HH:mm");
		Calendar cal = Calendar.getInstance();
		JTextField textbox = new JTextField(dateFormat.format(cal.getTime()));
		textbox.setBorder(BorderFactory.createEmptyBorder());
		textbox.setOpaque(false);
		textbox.setLocation(x, y);
		textbox.setSize(350, 78);
		textbox.setFont(new Font("Constantia", Font.BOLD, 60));
		textbox.setEditable(false);
		panel.add(textbox);
	}
}
