import os
from openai import OpenAI
import json

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

    while True:
        text_input = input("> ")
        message_data += {"role": "user", "content": text_input},

        # chatGPT completion
        completion = gpt_prompt(message_data, client)

        text_output = completion.choices[0].message.content
        message_data += {"role": "assistant", "content": text_output},

        print(text_output, end='\n\n')

