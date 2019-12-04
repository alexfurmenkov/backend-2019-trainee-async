from aiohttp import web
from integrations.speech_to_text import SpeechToText
import requests
import json


async def speechRecognition(request):
    data = None
    query_data = {}

    async for line in request.content:
        data = line.decode('utf-8').split('&')

    query_data['user_id'] = data[0].replace('user_id=', '')
    audio_path = data[1].replace('audio_path=', '')
    query_data['audio_path'] = audio_path
    audio_decoded = await SpeechToText.speech_to_text(audio_path)
    query_data['audio_decoded'] = audio_decoded
    query_data_json = json.dumps(query_data)
    data = json.loads(query_data_json)
    print(data)
    url = 'http://localhost:8000/savepitt/'
    try:
        r = requests.post(url=url, data=data)
        return web.Response(text=audio_decoded)
    except requests.ConnectionError:
        return web.Response(text='Unable to connect to the server.')
