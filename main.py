import click
from tts.eleven_labs_tts import ElevenLabsTTS
from tts.coqui_tts import CoquiTTS
from chatbots.gpt_chatbot import GPTChatbot
from chatbots.chat_gpt_chatbot import ChatGPTChatbot
from virtual_assistant import VirtualAssistant

@click.command()
@click.option('--bot-name', default='AI', help='Name of the virtual assistant')
@click.option('--personality', default='You are a helpful AI assistant expert in several domains', help='Personality of the virtual assistant')
@click.option('--chatbot', type=click.Choice(['gpt3', 'chatgpt']), default='chatgpt', help='Type of chatbot to use')
@click.option('--tts', type=click.Choice(['elevenlabs', 'coqui']), default='coqui', help='Text-to-speech option')
@click.option('--tts-voice', help='Voice for the text-to-speech option', default='')
@click.option('--use-audio-input', type=bool, default=True, help='Enable audio input')
@click.option('--use-audio-output', type=bool, default=True, help='Enable text-to-speech output')
@click.option('--audio-file-path', default='audio.wav', help='File path for audio recording')
def virtual_assistant(bot_name, personality, chatbot, tts, tts_voice, use_audio_input, use_audio_output, audio_file_path):
    click.echo(f'Virtual assistant: {bot_name}')
    click.echo(f'Personality: {personality}')
    click.echo(f'Chatbot type: {chatbot}')
    click.echo(f'Text-to-speech option: {tts}')
    click.echo(f'Text-to-speech voice: {tts_voice}')
    click.echo(f'Audio input enabled: {use_audio_input}')
    click.echo(f'Text-to-speech output enabled: {use_audio_output}')
    click.echo(f'Audio file path: {audio_file_path}')

    chatbot_instance = None
    if chatbot == 'gpt3':
        chatbot_instance = GPTChatbot(personality, bot_name)
    elif chatbot == 'chatgpt':
        chatbot_instance = ChatGPTChatbot(personality)
    else:
        raise ValueError("Invalid chatbot type. Should be 'gpt3' or 'chatgpt'")
    
    tts_instance = None
    if tts == 'elevenlabs':
        if not tts_voice:
            tts_voice = "Arnold"        
        tts_instance = ElevenLabsTTS(tts_voice)
    elif tts == 'coqui':
        if not tts_voice:
            tts_voice = "tts_models/en/ljspeech/tacotron2-DDC"
        tts_instance = CoquiTTS(tts_voice)
    else:
        raise ValueError("Invalid chatbot type. Should be 'elevenlabs' or 'coqui'")

    assistant = VirtualAssistant(
        bot_name, 
        chatbot_instance, 
        tts_instance, 
        use_audio_input,
        use_audio_output,
        audio_file_path
    )
    assistant.loop()


if __name__ == "__main__":
    virtual_assistant()