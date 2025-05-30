import sys
import os

from TextToSpeech.elevenlabsTTS import text_to_speech_file

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import openai

import AIVT_Config


OpenAITTS_Voice_list = [
    "alloy",
    "echo",
    "fable",
    "onyx",
    "nova",
    "shimmer",
]
OpenAITTS_Model_list = [
    "tts-1",
    "tts-1-hd",
]

openaitts_parameters = {
    "output_path": "Audio/output_openaitts_01.mp3",
    "model": "tts-1",
    "voice": "alloy",
    "speed": 1.00,
    "format": "mp3",
    "timeout": 10.0,
}


def openaitts_bak(
    text="",
    output_path="Audio/output_openaitts_01.wav",
    model="tts-1",
    voice="alloy",
    speed=1.00,
    format="wav",
    timeout=10.0,
):

    openai.api_key = AIVT_Config.openai_api_key

    response = openai.audio.speech.create(
        input=text,
        model=model,
        voice=voice,
        speed=speed,
        response_format=format,
        timeout=timeout,
    )

    try:
        response.write_to_file(output_path)

    except Exception as e:
        print(f"Error openai tts\n{e}\n")


def openaitts(
    text="",
    output_path="Audio/tts/output_openaitts_01.mp3",
    model="tts-1",
    voice="alloy",
    speed=1.00,
    format="mp3",
    timeout=10.0,
):

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    try:
        # response.write_to_file(output_path)
        text_to_speech_file(text, output_path)

    except Exception as e:
        print(f"Error openai tts\n{e}\n")


if __name__ == "__main__":

    input_text = "Never gonna give you up never gonna let you down"

    openaitts(
        text=input_text,
        output_path="Audio/output_openaitts_01.wav",
        model="tts-1",
        voice="alloy",
        speed=1.00,
        format="wav",
        timeout=10.0,
    )
