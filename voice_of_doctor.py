#step 1: steups text to speech model(GTTS or ElevenLabs)

#option a:(TTS with gTTS)                                    (NOT WORKING RIGHT-NOW)
# import os
# from gtts import gTTS

# def text_to_speech_with_gtts_old(input_text, output_filepath):
#     language="en"

#     audioobj= gTTS(
#         text=input_text,
#         lang=language,
#         slow=False
#     )
#     audioobj.save(output_filepath)   #audio object jo mila haia... usko output file me store karenge

# #testing
# input_text="Hi hello how are you? ,, this is vivek"
# text_to_speech_with_gtts_old(input_text=input_text, output_filepath="gtts_testing.mp3")


#option a (part 2): (TTS with pyttsx3)  //python based local service

#install pyttsx3 ... by pipenv install pyttsx3
import pyttsx3

def text_to_speech_with_pyttsx3_old(input_text, output_filepath):  #old isliye kykoi.. ab hum step 3 me copy kiya hai inko
    engine = pyttsx3.init()  # Initialize the TTS engine
    engine.save_to_file(input_text, output_filepath)  # Save speech to file
    engine.runAndWait()  # Process the voice command

#testing
# input_text = "Hi hello how are you? ,, this is vivek"
# text_to_speech_with_pyttsx3(input_text=input_text, output_filepath="pyttsx3_testing.mp3")




# option b: TTS with ElevenLabs

#install elevenLabs by.. pipenv install elevenlabs
#then setup elevenlabs API key
from elevenlabs.client import ElevenLabs
from elevenlabs import save
import os

# It's best to initialize the client once outside the function
# It will automatically use the ELEVEN_API_KEY from your .env file
client = ElevenLabs()

def text_to_speech_with_elevenlabs_old(input_text, output_filepath):

    audio = client.text_to_speech.convert(
        voice_id="21m00Tcm4TlvDq8ikWAM",  # voice of rachel
        text=input_text,
        model_id="eleven_multilingual_v2" 
    )

    # The new function to save the audio file
    save(audio, output_filepath)
    print(f"Audio saved to {output_filepath}")

#testing
# input_text = "Hello.. I am vivek chouhan"
# text_to_speech_with_elevenlabs_new(input_text=input_text, output_filepath="ElevenLabs_testing.mp3")





#Step 3: audio file save hone ke baad ..autoplay ho jaye.. ab vo setup karna hai
#iske liye hum SUBPROCESS library use kareng

import subprocess
import platform #ye pata karega .. ki kis plateform (Mac, window or linux) par use ho raha hai

def text_to_speech_with_pyttsx3_new(input_text, output_filepath): 
    engine = pyttsx3.init()  # Initialize the TTS engine
    engine.save_to_file(input_text, output_filepath)  # Save speech to file
    engine.runAndWait()  # Process the voice command
    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":  # Windows
            subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync();'])
        elif os_name == "Linux":  # Linux
            subprocess.run(['aplay', output_filepath])  # Alternative: use 'mpg123' or 'ffplay'
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")

#testing pyttsx3
# input_text = "Hi hello how are you? ,, this is vivek"
# text_to_speech_with_pyttsx3_new(input_text=input_text, output_filepath="pyttsx3_testing.mp3")


                              #NOT IN USE.. SOME ERROR IN THIS FUNCTION
def text_to_speech_with_elevenlabs_new(input_text, output_filepath):

    audio = client.text_to_speech.convert(
        voice_id="21m00Tcm4TlvDq8ikWAM",  # voice of rachel
        text=input_text,
        model_id="eleven_multilingual_v2" 
    )

    # The new function to save the audio file
    save(audio, output_filepath)
    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":  # Windows
            subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync();'])
        elif os_name == "Linux":  # Linux
            subprocess.run(['aplay', output_filepath])  # Alternative: use 'mpg123' or 'ffplay'
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")


#testing for elevenLabs
# input_text = "Hello.. I am vivek chouhan"
# text_to_speech_with_elevenlabs_new(input_text=input_text, output_filepath="ElevenLabs_testing.mp3")