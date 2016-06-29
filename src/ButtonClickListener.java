import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class ButtonClickListener implements ActionListener{
	Sound music;
	public ButtonClickListener() {
		music = new Sound("");
	}

	public void actionPerformed(ActionEvent e) {
		String command = e.getActionCommand();  
		if(command.equals("kill")) {  
			System.exit(0);
		}else if( command.equals("media")) {
			try{
				music.clip.stop();
			}catch(Exception ex){}
			
			music = new Sound("testsong.mp3");
			try{
			music.clip.open();
			}catch(Exception exv){}
			music.clip.start();

		}
		else  {
		}
	}		
}
