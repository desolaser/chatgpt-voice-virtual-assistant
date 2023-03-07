import whisper
from recorder.py_recorder import PyRecorder

class VirtualAssistant():
    def __init__(
        self,
        bot_name,
        chatbot,
        tts,
        use_audio_input=False,
        use_audio_output=False,
        audio_file_path="./recording.wav"
    ) -> None:
        self.bot_name = bot_name
        self.use_audio_input = use_audio_input
        self.use_audio_output = use_audio_output
        self.audio_file_path = audio_file_path
        self.rec = PyRecorder(self.audio_file_path)
        self.chatbot = chatbot
        self.tts = tts
    
    def loop(self):
        while True:
            text = ""
            if self.use_audio_input:
                text = self.get_audio_input()
            else:
                text = self.get_text_input()

            response = self.chatbot.get_response(text)
            print(f"{self.bot_name}:{response}")
            if self.use_audio_output:
                self.tts.play(response)

    def get_text_input(self):
        text = input("You: ")
        return text

    def get_audio_input(self):
        self.rec.record()

        model = whisper.load_model("base")
        result = model.transcribe(self.audio_file_path)
        text = result["text"]
        print(f"You: {text}")
        return text