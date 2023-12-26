import os
from openai import OpenAI
import json
from transcribe import *

def import_json(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)

    return data
 
def gpt_prompt(text, client):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo", 
        messages = text,
        max_tokens=100
    )

    return completion

if __name__ == "__main__":
    api_key = "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"
    client = OpenAI(api_key=api_key)

    data_path = os.getcwd() + '/data.json'
    message_data = import_json(data_path)

    current_slide = ''
    while True:
        text_input = record_text()

        if 'end presentation' in text_input:
            break
        elif 'new slide' in text_input:
            current_slide = ''
        else:
            current_slide += ' ' + text_input

        message_data += {"role": "user", "content": current_slide},

        # chatGPT completion
        completion = gpt_prompt(message_data, client)

        text_output = completion.choices[0].message.content
        message_data += {"role": "assistant", "content": text_output},

        print(text_output, end='\n\n')

