import requests
from aiohttp import web
from integrations.speech_to_text import SpeechToText


async def speechrecognition(request):
    """
    Speech recognition
    :return: Sends data to localhost:8000 with decoded audio
    """
    data = None
    query_data = {}

    async for line in request.content:
        data = line.decode('utf-8').split('&')

    query_data['user_id'] = data[0].replace('user_id=', '')
    audio_path = data[1].replace('audio_path=', '')
    query_data['audio_path'] = audio_path
    audio_decoded = await SpeechToText.speech_to_text(audio_path)
    query_data['audio_decoded'] = audio_decoded
    print(query_data)
    url = 'http://localhost:8000/savepitt/'
    try:
        requests.post(url=url, data=query_data)
        return web.Response(text='success')
    except requests.ConnectionError:
        return web.Response(text='Unable to connect to the server.')
