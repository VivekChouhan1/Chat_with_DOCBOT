#step1 : audio recorder ko set kar rahe hai (ffmpeg and portaudio)
#ffmpeg =library which allow us for audio, video or image processing
#portaudio =library allow us .. agar hame mic use karke code ke liye kuch record karna hai vaha kam aati hai
import logging
import speech_recognition as sr
from pydub import AudioSegment
from io import BytesIO

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')



#ye function mic se audio recor karega and usko save karega mp3 file me
def record_audio(file_path, timeout=20, phrase_time_limit=None):
   
    """
    Args:
    file_path (str): Path to save the recorded audio file.
    timeout (int): Maximum time to wait for a phrase to start (in seconds).
    phrase_time_lfimit (int): Maximum time for the phrase to be recorded (in seconds).
    """
    recognizer = sr.Recognizer()   #it will record the audio coming from mic and usko store karega
    
    try:
        with sr.Microphone() as source:
            logging.info("Adjusting for ambient noise...")
            recognizer.adjust_for_ambient_noise(source, duration=1)   #isse recogniser background ki ambient or extra noise ko cut karga
            logging.info("Start speaking now...")
            
            # ab audio record hogi
            audio_data = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            logging.info("Recording complete.")
            
            # ab jo uppar audio record hui hai usko... mp3 file me store karna hai
            wav_data = audio_data.get_wav_data()
            audio_segment = AudioSegment.from_wav(BytesIO(wav_data))   #audio byte me covert hau
            audio_segment.export(file_path, format="mp3", bitrate="128k")  #audio ko file path par save kar diya
            
            logging.info(f"Audio saved to {file_path}")

    except Exception as e:
        logging.error(f"An error occurred: {e}")


audio_file_path="patient_audio.mp3"
# record_audio(file_path=audio_file_path)  #will record audio by calling function




#step 2: recordered audio ko text me convert karo
#ab hamara kam hai.. ki jo mp3 file bani hai.. vo text me convert ho jaye
#ab hum OPENAI ka Whishper model use karenge ,with the help of groq
import os
from groq import Groq

#for testing
GROQ_API_KEY=os.environ.get("GROQ_API_KEY")  #groq ki help se
stt_model="whisper-large-v3"  #ye model hum use karenge

# client=Groq(api_key=GROQ_API_KEY)
# audio_file=open(audio_file_path, "rb") #audio file jo record hui hia.. usko open karenge and read binary me
# transcription=client.audio.transcriptions.create(    #API ko call kiya . groq ke through
#         model=stt_model,
#         file=audio_file,
#         language="en"
#     )
# print(transcription.text)

def transcribe_with_groq(stt_model, audio_filepath, GROQ_API_KEY):
    client=Groq(api_key=GROQ_API_KEY)
    
    audio_file=open(audio_filepath, "rb")
    transcription=client.audio.transcriptions.create(
        model=stt_model,
        file=audio_file,
        language="en"
    )

    return transcription.text