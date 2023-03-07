import requests
import sounddevice as sd
import io
import soundfile
import soundfile as sf
from decouple import config
from interfaces.tts import TTSInterface
import json

ELEVEN_LABS_API_KEY = config('ELEVEN_LABS_API_KEY')
API_URL = "https://api.elevenlabs.io/v1/"

class ElevenLabsTTS(TTSInterface):
    def __init__(self, name) -> None:
        self.voice_id = self.get_voice_id_by_name(name)

    def get_voice_id_by_name(self, name):
        voices = self.get_voices()
        for voice in voices:
            if voice['name'] == name:
                return voice['voice_id']
            
        print("[Error]: Voice not found, using default voice")
        return "e4NcGHtMxgBOL5oboq8q"
    
    def get_voices(self):
        url = API_URL + "voices"
        response = requests.get(url, headers={ "xi-api-key": ELEVEN_LABS_API_KEY })
        data = json.loads(response.text)
        return data['voices']

    def get_audio(self, text):
        url = API_URL + "text-to-speech/" + self.voice_id
        myobj = {
            "text": text,
            "voice_settings": {
                "stability": 0,
                "similarity_boost": 0
            }
        }

        response = requests.post(url, json = myobj, headers={ "xi-api-key": "59871c8eaeff210df3c1989e462c25a4" })
        return response.content

    def play(self, text):
        audio_bytes = self.get_audio(text)

        portaudioDeviceID = None
        if portaudioDeviceID is None:
            portaudioDeviceID = sd.default.device
        audioFile = io.BytesIO(audio_bytes)
        soundFile = sf.SoundFile(audioFile)
        playInBackground = False
        sd.play(soundFile.read(), samplerate=soundFile.samplerate, blocking=not playInBackground, device=portaudioDeviceID)
