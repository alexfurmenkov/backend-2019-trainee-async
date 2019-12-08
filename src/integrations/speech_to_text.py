import base64
import os
# Imports the Google Cloud client library
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
import io


class SpeechToText:

    @staticmethod
    async def speech_to_text(audio_path):
        # Instantiates a client
        client = speech.SpeechClient()

        media_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../media'))

        file_name = os.path.join(media_path, audio_path)

        # Loads the audio into memory
        discr_freq = 48000
        with io.open(file_name, 'rb') as audio_file:
            content = audio_file.read()
            content_encoded = base64.b64encode(content)

        config = types.RecognitionConfig(
            encoding=enums.RecognitionConfig.AudioEncoding.FLAC,
            sample_rate_hertz=discr_freq,
            language_code='en-US')

        # Detects speech in the audio file
        content_decoded = base64.b64decode(content_encoded)
        audio_decoded = types.RecognitionAudio(content=content_decoded)
        response = client.recognize(config, audio_decoded)
        phrase = ''

        for top_results in response.results:
            for inside_results in top_results.alternatives:
                phrase = inside_results.transcript
        return base64.b64encode(phrase.encode('utf-8'))








