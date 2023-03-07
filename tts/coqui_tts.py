import os.path
import simpleaudio as sa
from TTS.utils.manage import ModelManager 
from TTS.utils.synthesizer import Synthesizer
from interfaces.tts import TTSInterface

path = "./venv/Lib/site-packages/TTS/.models.json"

class CoquiTTS(TTSInterface):
    def __init__(self, model_name, output_path="./output.wav") -> None:
        self.output_path = output_path

        model_manager = ModelManager(path)
        model_path, config_path, model_item = model_manager.download_model(model_name)
        voc_path, voc_config_path, _ = model_manager.download_model(model_item["default_vocoder"])

        self.syn = Synthesizer(
            tts_checkpoint=model_path,
            tts_config_path=config_path,
            vocoder_checkpoint=voc_path,
            vocoder_config=voc_config_path
        )

    def play(self, text):
        outputs = self.syn.tts(text)
        self.syn.save_wav(outputs, self.output_path)

        while True:
            if os.path.isfile(self.output_path):
                try:
                    wave_obj = sa.WaveObject.from_wave_file(self.output_path)
                    play_obj = wave_obj.play()
                    play_obj.wait_done()
                    break
                except Exception as e:
                    print(e)
        
