# from dotenv import load_dotenv
# from s3_uploader import generate_presigned_url, upload_audiostream_to_s3
# from text_to_speech_stream import text_to_speech_stream

# load_dotenv()


import os
import uuid

# from dotenv import load_dotenv
from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs

# load_dotenv()

ELEVENLABS_API_KEY ='sk_25924befef13864e02540f79688328264ac9ffed05bc9736'# os.getenv("ELEVENLABS_API_KEY")

if not ELEVENLABS_API_KEY:
    raise ValueError("ELEVENLABS_API_KEY environment variable not set")

client = ElevenLabs(
    api_key=ELEVENLABS_API_KEY,
)


def text_to_speech_file(text: str, output_path: str) -> str:
    """
    Converts text to speech and saves the output as an MP3 file.

    This function uses a specific client for text-to-speech conversion. It configures
    various parameters for the voice output and saves the resulting audio stream to an
    MP3 file with a unique name.

    Args:
        text (str): The text content to convert to speech.

    Returns:
        str: The file path where the audio file has been saved.
    """
    # Calling the text_to_speech conversion API with detailed parameters
    response = client.text_to_speech.convert(
        voice_id="cgSgspJ2msm6clMCkdW9",  # Adam pre-made voice
        optimize_streaming_latency="0",
        output_format="mp3_22050_32",
        text=text,
        model_id="eleven_turbo_v2",  # use the turbo model for low latency, for other languages use the `eleven_multilingual_v2`
        voice_settings=VoiceSettings(
            stability=0.0,
            similarity_boost=1.0,
            style=0.0,
            use_speaker_boost=True,
        ),
    )

    # Generating a unique file name for the output MP3 file
    save_file_path = output_path # f"{uuid.uuid4()}.mp3"
    # Writing the audio stream to the file

    with open(save_file_path, "wb") as f:
        for chunk in response:
            if chunk:
                f.write(chunk)

    print(f"A new audio file was saved successfully at {save_file_path}")

    # Return the path of the saved audio file
    return save_file_path


if __name__ == "__main__":
    text_to_speech_file("Hello, world! This is a test of the ElevenLabs API.")

# def main(text: str):
#     audio_stream = text_to_speech_stream(text)
#     s3_file_name = upload_audiostream_to_s3(audio_stream)
#     signed_url = generate_presigned_url(s3_file_name)

#     print(f"Signed URL to access the file: {signed_url}")


# if __name__ == "__main__":
#     main("This is a test of the ElevenLabs API.")