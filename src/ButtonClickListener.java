import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class ButtonClickListener implements ActionListener{
	public ButtonClickListener() {
		//Java says I need this
	}

	public void actionPerformed(ActionEvent e) {
		String command = e.getActionCommand();  
		if( command.equals( "kill" ))  {  
			System.exit(0);
		}
		/*else if( command.equals( "Submit" ) )  {
				statusLabel.setText("Submit Button clicked."); 
			}
			else  {
				statusLabel.setText("Cancel Button clicked.");
			}*/
	}		
}
