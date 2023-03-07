# Chat GPT Voice Virtual Assistant Documentation

The Chat GPT Voice Virtual Assistant is a Python program that uses GPT-3 or ChatGPT API to create a chatbot that can respond to user input.
The program offers customization options, such as chatbot type, text-to-speech option, voice, and personality.

## Usage

```bash
# First clone the repo.
git clone https://github.com/desolaser/chatgpt-voice-virtual-assistant.git

# Enter into the root.
cd chatgpt-voice-virtual-assistant

# Then make a virtualenv
virtualenv venv

# Enter into virtualenv
venv\scripts\activate
# Or in linux
source venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Copy .env.example to .env
copy .env.example to .env

# Set your API keys.
# Inside .env you will see this. Change them to your own api keys.
OPENAI_API_KEY="Your open ai key" # Mandatory, without an open ai key the program will not run.
ELEVEN_LABS_API_KEY="Your elevenlabs key" # Optional key

# Run main to run virtual assistant with default parameters
py main.py

# Run main with options.
py main.py --bot-name="Funny AI" --personality="You are a funny AI that makes funny comments about dominating humanity and makes jokes all the time." --chatbot=gpt3 --tts=elevenlabs --tts-voice=Domi 

# Run main with options example 2.
py main.py --bot-name="Blank AI" --personality="You are a helpful AI with no personality whatsoever." --chatbot=chatgpt --tts=coqui --tts-voice=tts_models/en/ljspeech/tacotron2-DDC

## You can use --help command to get the options
py main.py --help

# Displays
Usage: main.py [OPTIONS]

Options:
  --bot-name TEXT             Name of the virtual assistant
  --personality TEXT          Personality of the virtual assistant
  --chatbot [gpt3|chatgpt]    Type of chatbot to use
  --tts [elevenlabs|coqui]    Text-to-speech option
  --tts-voice TEXT            Voice for the text-to-speech option
  --use-audio-input BOOLEAN   Enable audio input
  --use-audio-output BOOLEAN  Enable text-to-speech output
  --audio-file-path TEXT      File path for audio recording
  --help                      Show this message and exit
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

Options explained in detail:

```bash
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
```

## Recommendations

When using ChatGPT you can give it instructions about its task like talking to a person and it will understand.
GPT-3 works better if you make a prompt showing how you want to continue the text. This isn't a prompt course
but you should experiment with the results if you want a better behavior in GPT3, ChatGPT will understand right
off the bat, but it will refuse to roleplay later and can speak out of character very easily.

## ToDo

1. Find an open source way to generate text based on user input: GPT-3 and ChatGPT are the most capable models
for everything, I haven't found an open source option to do the same. I tried BLOOM, which is one of the
best large language models open source out there, but it was dissapointing. Maybe with a better prompt I could
work. If someone knows how to make it work for chatbot purposes, make me know please.
2. Making a GUI: This will improve the UX, I want to make this to be able to write the bot personality in an easier
way, maybe even being able to save personalities for later use.
3. Bot memories: I need the chatbot to remember previous conversations, I want to implement this as well.