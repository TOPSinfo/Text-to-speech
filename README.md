# Azure Text to Speech Service Demo

## Overview

This is a simple Python demo showcasing the usage of Azure Text to Speech Service. The demo allows you to convert text into spoken words using the Azure Text to Speech API.
Prerequisites

Before running the demo, make sure you have the following prerequisites installed:

    Python 3.x
    Azure SDK for Python (azure-cognitiveservices-speech)

You also need an Azure subscription. If you don't have one, you can create a free account before you begin.
Setup

Install the required Python packages:

    pip install azure-cognitiveservices-speech

Obtain your Azure Text to Speech API key and Replace the placeholder values in the code with your actual API key.

## Usage

Run the demo script:

```
python tts.py
```

Follow the prompts to enter the text you want to convert to speech. The script will make a request to the Azure Text to Speech API and play the resulting audio.


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`SPEECH_KEY`

`SPEECH_REGION`