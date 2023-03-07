# Chat GPT Voice Virtual Assistant Documentation

The Chat GPT Voice Virtual Assistant is a Python program that uses GPT-3 or ChatGPT API to create a chatbot that can respond to user input.
The program offers customization options, such as chatbot type, text-to-speech option, voice, and personality.

## Usage

```
# First clone the repo.
git clone ...
# Then make a virtualenv
virtualenv venv
# Install requirements
pip install -r requirements.txt
# Run main.
py main.py

# Run main with options.
py main.py --bot-name=LydIA --personality="Funny AI that makes funny comments about dominating humanity." --chatbot=gpt3 --tts=elevenlabs --tts-voice=Domi 

# Run main with options example 2.
py main.py --bot-name="Blank AI" --personality="Helpful AI with no personality whatsoever." --chatbot=chatgpt --tts=coqui --tts-voice=tts_models/en/ljspeech/tacotron2-DDC
```

## Program Loop

Receiving Input: The program can receive input through text or audio recording. To record audio, 
press the 'K' key, and release it when finished recording. Whisper API will then convert the audio 
to text for the virtual assistant to process.

Virtual Assistant Receives Text: The virtual assistant receives the input and sends it to OpenAI 
endpoints to generate a response.

Virtual Assistant Gets Response: The virtual assistant saves the response in the chat log and passes
it to the Text-to-Speech (TTS) class.

Virtual Assistant Speaks: If audio output is enabled, the virtual assistant will speak the response
in a natural-sounding voice. The voice can be customized using the text-to-speech option.

## Options

The following are the available parameters that can be customized in the program:

--bot-name: This parameter allows you to specify a name for the virtual assistant. The default name is "AI".

--personality: This parameter can be used to give the virtual assistant a specific personality, otherwise it
will use a default one.

--chatbot: This parameter can be set to either 'gpt3' or 'chatgpt' to choose the type of chatbot to use.
ChatGPT is a simpler option with limited personality customization, while GPT-3 offers more varied and
interesting results at a higher cost.

--tts: This parameter sets the text-to-speech option to either 'elevenlabs' or 'coqui'. ElevenLabs provides 
better performance with a more realistic voice, but it requires an API key and is limited to 10,000 free credits.
CoquiTTS is a free open source alternative, but the voice quality is not as good as ElevenLabs.

--tts-voice: This parameter is only used with ElevenLabs and allows you to choose from different voices
available on their website. For CoquiTTS, you can specify the model to use.

--use-audio-input: This parameter can be set to False to disable audio input and use text input instead.

--use-audio-output: This parameter can be set to False to disable the text-to-speech functionality and receive
responses as text.

--audio-file-path: This parameter specifies the file path for audio recording. It can be customized, but is
not necessary in most cases.

## TODO:

1. Find an open source way to generate text based on user input: GPT-3 and ChatGPT are the most capable models
for everything, I haven't found an open source option to do the same. I tried BLOOM, which is one of the
best large language models open source out there, but it was dissapointing. Maybe with a better prompt I could
work. If someone knows how to make it work for chatbot purposes, make me know please.

3. Making a GUI: This will improve the UX, I want to make this to be able to write the bot personality in an easier
way, maybe even being able to save personalities for later use.

4. Bot memories: I need the chatbot to remember previous conversations, I want to implement this as well.