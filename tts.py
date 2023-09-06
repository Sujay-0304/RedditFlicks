# from gtts import gTTS 

# def text(text, lang):
#     tts = gTTS(text=text, lang=lang)
#     tts.save("text.mp3") 
# text("did you know that the average human has less than 2 legs?", "en")
import pyttsx3

def text_to_speech(text, output_filename):
    engine = pyttsx3.init()
    
    engine.setProperty('rate', 200)  
    engine.setProperty('volume', 0.9)  
    engine.save_to_file(text, output_filename)
    
    engine.runAndWait()
    
    print(f"Speech saved as {output_filename}")


# text = "did you know that the average human has less than 2 legs? if we take the average of 2 and 0, we get 1. so the average human has 1 leg."
# output_filename = "output.mp3"
# text_to_speech(text, output_filename)
