import os
import io
from google import genai
from dotenv import load_dotenv
from gtts import gTTS

load_dotenv()

my_api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=my_api_key)


# note api
def note_generate(images):
   prompt = """Summary of the notes in 100 words, 
   make sure nessary markdown to differentiate sections."""

   response = client.models.generate_content(
    model = "gemini-3-flash-preview",  
    contents = [images, prompt]
   )
   return response.text


def audio_generate(text):
      speech = gTTS(text, lang = 'en', slow = False)
      audio_buffer = io.BytesIO()
      speech.write_to_fp(audio_buffer)
      return audio_buffer

      
def quiz_generate(image,difficulty):
   prompt = f"Generate a quiz based on the {difficulty} level. Meke sure to add marksdown to differentiate the options. Add corect answer at the end of the quiz with the heading 'Answer'"
   response = client.models.generate_content(
    model = "gemini-3-flash-preview",  
    contents = [image, prompt]
   )
   return response.text