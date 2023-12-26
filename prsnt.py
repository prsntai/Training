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

    # do actual fine tuning later
    data_path = os.getcwd() + '/prsnt.json'
    message_data = import_json(data_path)

    state_path = os.getcwd() + '/state.json'
    state_data = import_json(state_path)

    current_slide = ''
    while True:
        text_input = record_text()
        current_slide += ' ' + text_input

        state_data += {"role": "user", "content": current_slide},

        # state detection (switch slides or stay)
        state_raw = gpt_prompt(state_data, client)
        state = state_raw.choices[0].message.content

        state_data += {"role": "assistant", "content": state},

        if 'switch' in state:
            current_slide = text_input
            print('\n--- switching slides ---\n')

        message_data += {"role": "user", "content": current_slide},

        # chatGPT completion
        completion = gpt_prompt(message_data, client)

        text_output = completion.choices[0].message.content
        message_data += {"role": "assistant", "content": text_output},

        print('Transcription:', text_input)
        print('Slide:', text_output, end='\n\n')
