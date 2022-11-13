import time
import schedule
from os import path
from dotenv import dotenv_values
from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration

mname = "facebook/blenderbot-400M-distill"
model = BlenderbotForConditionalGeneration.from_pretrained(mname)
tokenizer = BlenderbotTokenizer.from_pretrained(mname)

config = dotenv_values(".env")
input_path = path.join(config['TINKR_DIRECTORY'], config['INPUT_FILE'])
output_path = path.join(config['TINKR_DIRECTORY'], config['OUTPUT_FILE'])
delay = int(config['DELAY'])

last_message = ""

def generate_response(UTTERANCE):
    inputs = tokenizer([UTTERANCE], return_tensors="pt")
    reply_ids = model.generate(**inputs)
    reply = tokenizer.batch_decode(reply_ids, skip_special_tokens=True)
    return reply[0]

def read_message():
    f = open(input_path, "r")
    message = f.read()
    f.close
    if message == last_message: 
        return False
    else:
        last_message = message
        return message

def write_response(response):
    f = open(output_path, "w")
    f.write(response)
    f.close()

def create_response():
    UTTERANCE = read_message()
    print("message: ", UTTERANCE)
    response = generate_response(UTTERANCE)
    write_response(response)
    print("response: ", response)

def main():
    schedule.every(delay).seconds.do(create_response)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
