
import pyttsx3

def text_to_speech(text, output_filename):
    engine = pyttsx3.init()
    
    engine.setProperty('rate', 200)  
    engine.setProperty('volume', 0.9)  
    engine.save_to_file(text, output_filename)
    
    engine.runAndWait()
    
    print(f"Speech saved as {output_filename}")

