from openai import OpenAI
from transcribe import *
 
def gpt_prompt(text, client, model="gpt-3.5-turbo", max_tokens=100):
    completion = client.chat.completions.create(
        model=model, 
        messages=text,
        max_tokens=max_tokens
    )

    return completion.choices[0].message.content

if __name__ == "__main__":
    api_key = "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"
    client = OpenAI(api_key=api_key)
    modelName = 'ft:gpt-3.5-turbo-1106:personal::8aCG2zq6'

    print('Hello! prsntAI will convert your live speech to a presentation slide format.')
    print('Please provide a short, 1-2 sentence summary of your presentation.')
    summary = input('Summary >>> ')
    print('\nOk! Starting now.\n')

    message_data = [
        {"role": "system", "content": f"Convert a short part of a presentation script to presentation slide format seperated by newlines. You can only use titles (title), text (text), bullet points (bullet), and image descriptions (image). Script summary: {summary}"}
    ]

    current_slide = ''
    while True:
        if input('Switch slides? (y/n) >>> ').lower() == 'y':
            current_slide = ''

        print('\nPlease speak into the microphone.')
        text_input = record_text()

        current_slide += ('. ' if len(current_slide) else '') + text_input

        current_data = message_data + [{"role": "user", "content": current_slide}]

        # chatGPT completion
        text_output = gpt_prompt(current_data, client, model=modelName)

        print('\nTRANSCRIPTION:', current_slide)
        print('SLIDE:')
        print(text_output, end='\n\n')
