# LLAMA CHAT

A proof of concept AI powered chatbot for Tinkr. 

While the example implements a specific AI chat model (facebook/blenderbot-400M-distill) it can easily be swapped for any model available on [Hugging Face](https://huggingface.co).

**NOTE:** Please don't run this in any serious capacity without making modifications it is only a proof of concept and has plenty of major issues that will make your look like a bot.

## Overview

ai_chat.lua
- reads incomming whisper messages and writes them to a file (message.txt), it will not write new messages until the last has been responded to

- reads responses fromt he AI that are written to a file (response.txt) and responds to the player who sent the whisper

main.py
- reads whisper message written to message.txt, passes it to the AI model, writes the response to response.txt

The delay in .env and in ai_chat.lua will control how often it will try to process a response. I ran with 20 seconds on my M1 Air but you can probably decrease that.

## Requirements

If you don't have python you need to install it via the website, anaconda, brew or whatever.
- [Python](https://www.python.org/) 3.7 +

The rest of the requirements will be installed running the setup process below.
- [PyTorch](https://pytorch.org/)
- [Transformers](https://github.com/huggingface/transformers) from Hugging Face
- [python-dotenv](https://github.com/theskumar/python-dotenv)
- [schedule](https://github.com/dbader/schedule)


## Setup

### 1 - clone the repo and cd into the direcotry

```bash
git clone repo && cd llama_chat
```
### 2 - install the dependencies

(use a virtual env if you know how)

```bash
pip install -r requirements.txt
```

### 3 - create a .env file

```bash
touch .env
```

### 4 - open .env and add the following keys

```python
DELAY = 20
INPUT_FILE = "message.txt"
OUTPUT_FILE = "response.txt"
TINKR_DIRECTORY = "/Users/purplellama/Downloads/LJDvVWKOsQ/"
```
**Note:** obviously don't just copy the example Tinkr directory. Update this with your own. If you decide to change the input and output filenames you will need to manually update those in ai_chat.lua.


### 5 - deploy ai_chat.lua

all this does is copy ai_chat.lua to your Tinkr scripts folder

```bash
python deploy.py
```

### 6 - run main.py 

```bash
python main.py
```

### 7 - load ai_chat.lua in game

open WoW with Tinkr loaded and run

```
/tinkr load ai_chat.lua
```


