from aiohttp import web
from integrations.speech_to_text import SpeechToText
import requests


def speechRecognition(request):
    audio_decoded = SpeechToText.speech_to_text()
    data = {'id': 1, 'user_id': 'user_id', 'audio_path': 'audio.flac', 'audio_decoded': audio_decoded}
    r = requests.post(url='http://localhost:8000/makepitt/', data=data)
    return web.Response(text='Success')
