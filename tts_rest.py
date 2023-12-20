import requests
import os
from dotenv import load_dotenv

load_dotenv()
# API endpoint

SPEECH_KEY = os.environ.get('SPEECH_KEY')
SPEECH_REGION = os.environ.get('SPEECH_REGION')

url = f"https://{SPEECH_REGION}.tts.speech.microsoft.com/cognitiveservices/v1"

# Request headers
headers = {
    f"Ocp-Apim-Subscription-Key": "{SPEECH_KEY}",
    "Content-Type": "application/ssml+xml",
    "X-Microsoft-OutputFormat": "audio-16khz-128kbitrate-mono-mp3",
    "User-Agent": "curl"
}

# Request body (SSML)
data = "<speak version='1.0' xml:lang='en-US'><voice xml:lang='en-US' xml:gender='Female' name='en-US-JennyNeural'>my voice is my passport verify me</voice></speak>"

# Send POST request
response = requests.post(url, headers=headers, data=data)

# Check if the request was successful (HTTP status code 200)
if response.status_code == 200:
    # Save the response content (audio) to a file
    with open("output.mp3", "wb") as file:
        file.write(response.content)
    print("Audio file saved successfully.")
else:
    print("Error:", response.status_code)
