import java.io.File;

import javax.sound.sampled.AudioInputStream;
import javax.sound.sampled.AudioSystem;
import javax.sound.sampled.Clip;

public class Sound {
	Clip clip;
	AudioInputStream audioInputStream;
	
	public Sound(String path){
		try{
		audioInputStream = AudioSystem.getAudioInputStream(new File(path).getAbsoluteFile());
		clip = AudioSystem.getClip();
		clip.open(audioInputStream);
		clip.start();
		}catch(Exception ex){}
	}
}
