import pyaudio
import wave
import keyboard

# Define audio parameters
CHUNK = 1024 # number of audio samples per frame
FORMAT = pyaudio.paInt16 # audio format
CHANNELS = 2 # mono audio
RATE = 44100 # sample rate

class PyRecorder():
    def __init__(self, mic_index=3) -> None:
        self.mic_index = mic_index
        pass

    def record(self, file_path="recording.wav"):

        print("Press K to start recording...")
        keyboard.wait('k')
        print("Recording...")
        audio = pyaudio.PyAudio()
        stream = audio.open(
            format=FORMAT,
            channels=CHANNELS,
            rate=RATE,
            input=True,
            input_device_index=self.mic_index,
            frames_per_buffer=CHUNK)
        frames = []

        while keyboard.is_pressed('k'):
            data = stream.read(CHUNK)
            frames.append(data)

        print("Recording finished.")

        # Save the recorded audio as a WAV file
        self.generate_audio_file(file_path, audio, frames)

        # Stop and close the stream
        stream.stop_stream()
        stream.close()
        audio.terminate()

    def generate_audio_file(self, file_path, audio, frames):
        wave_file = wave.open(file_path, "wb")
        wave_file.setnchannels(CHANNELS)
        wave_file.setsampwidth(audio.get_sample_size(FORMAT))
        wave_file.setframerate(RATE)
        wave_file.writeframes(b"".join(frames))
        wave_file.close()

        print(f"Audio saved as {file_path}")

    def print_available_inputs():        
        p = pyaudio.PyAudio()

        for i in range(p.get_device_count()):
            dev = p.get_device_info_by_index(i)
            print((i,dev['name'], dev['maxInputChannels']))
