import os
import azure.cognitiveservices.speech as speechsdk
from dotenv import load_dotenv

load_dotenv()

def speech_synthesis_realtime():
    # This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
    speech_config = speechsdk.SpeechConfig(subscription=os.environ.get('SPEECH_KEY'), region=os.environ.get('SPEECH_REGION'))
    # audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
    file_name = "/home/tops/text_to_speech/outputaudio.mp3"
    audio_config = speechsdk.audio.AudioOutputConfig(filename=file_name)
    # The language of the voice that speaks.
    speech_config.speech_synthesis_voice_name='gu-IN-DhwaniNeural'

    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

    # Get text from the console and synthesize to the default speaker.
    print("Enter some text that you want to speak >")
    text = input()

    # file_path = "/home/tops/text_to_speech/gujrati_text.txt"  # Replace with the actual path to your file
    # file = open(file_path, "r")

    # Read the contents of the file
    # file_contents = file.read()

    # # Close the file
    # file.close()

    ssml = f"<speak version='1.0' xmlns='http://www.w3.org/2001/10/synthesis' xmlns:mstts='https://www.w3.org/2001/mstts' xml:lang='gu-IN'><voice xml:lang='gu-IN' name='gu-IN-DhwaniNeural'><mstts:express-as style='sad' styledegree='8'>{text}</mstts:express-as></voice></speak>"

    # speech_synthesis_result = speech_synthesizer.speak_text_async(file_contents).get()
    speech_synthesis_result = speech_synthesizer.speak_ssml_async(ssml).get()

    if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        print("Speech synthesized for the text" )
    elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_synthesis_result.cancellation_details
        print("Speech synthesis canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            if cancellation_details.error_details:
                print("Error details: {}".format(cancellation_details.error_details))
                print("Did you set the speech resource key and region values?")



speech_synthesis_realtime()