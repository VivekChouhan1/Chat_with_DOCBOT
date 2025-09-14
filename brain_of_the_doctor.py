#Step1: sabse pehle GROQ API setup karenge
import os
GROQ_API_KEY=os.environ.get("GROQ_API_KEY")






#Step2: image ko required form me convert karenge
import base64
image_path="acne.jpg"


#for chceking purpose of pre stored acne image
# image_path="acne.jpg"
# image_file=open(image_path, "rb")    #rb means= read binary.. image to binary
# encoded_image=base64.b64encode(image_file.read()).decode('utf-8')    #image encode ho gai

def encode_image(image_path):   
    image_file=open(image_path, "rb")
    return base64.b64encode(image_file.read()).decode('utf-8')




#Step3: Setup Multimodal LLM 
from groq import Groq


# //for testing
query="Is there something wrong with my face?"
model="meta-llama/llama-4-scout-17b-16e-instruct" #llama LLM model... by groq
# client=Groq()
# messages=[
#         {
#             #two input,,, image and text
#             "role": "user",
#             "content": [
#                 {
#                     "type": "text", 
#                     "text": query
#                 },
#                 {
#                     "type": "image_url",
#                     "image_url": {
#                         "url": f"data:image/jpeg;base64,{encoded_image}",
#                     },
#                 },
#             ],
#         }]

# chat_completion=client.chat.completions.create(   #calling groq api here .. in this line
#     #yhaa hamne message kya dena hai and model bata diya hai API call ke liye
#         messages=messages,
#         model=model
#     )
# print(chat_completion.choices[0].message.content)  #jo bhi response aaya hai usko print kar rahe hai

def analyze_image_with_query(query, model, encoded_image):
    client=Groq()  
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text", 
                    "text": query
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{encoded_image}",
                    },
                },
            ],
        }]
    chat_completion=client.chat.completions.create(
        messages=messages,
        model=model
    )

    return chat_completion.choices[0].message.content