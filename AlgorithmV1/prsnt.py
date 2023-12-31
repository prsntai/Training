import os
from openai import OpenAI
import json
from transcribe import *

def import_json(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)

    return data
 
def gpt_prompt(text, client, model="gpt-3.5-turbo", max_tokens=100):
    completion = client.chat.completions.create(
        model=model, 
        messages=text,
        max_tokens=max_tokens
    )

    return completion.choices[0].message.content

if __name__ == "__main__":
    api_key = "API_KEY"
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
        state = gpt_prompt(state_data, client)

        state_data += {"role": "assistant", "content": state},

        if 'switch' in state:
            current_slide = text_input
            print('\n--- switching slides ---\n')

        message_data += {"role": "user", "content": current_slide},

        # chatGPT completion
        text_output = gpt_prompt(message_data, client)

        message_data += {"role": "assistant", "content": text_output},

        print('Transcription:', text_input)
        print('Slide:', text_output, end='\n\n')
