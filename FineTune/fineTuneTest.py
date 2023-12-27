from openai import OpenAI
 
def gpt_prompt(text, client, model="gpt-3.5-turbo", max_tokens=100):
    completion = client.chat.completions.create(
        model=model, 
        messages=text,
        max_tokens=max_tokens
    )

    return completion.choices[0].message.content

api_key = "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"
client = OpenAI(api_key=api_key)
modelName = 'ft:gpt-3.5-turbo-1106:personal::8aCG2zq6'
message_data = [
    {"role": "system", "content": "Convert a short part of a presentation script to presentation slide format seperated by newlines. You can only use titles (title), text (text), bullet points (bullet), and image descriptions (image). Script summary: A presentation on TikTok's data colonialism."},
    {"role": "user", "content": "TikTok has over 1.6 billion users, that is almost 20 percent of the world's current population. With the amount of reach TikTok has, it is crucial to ensure its platform is safe for all users. Especially considering how approximately one fourth of TikTok users are under 18 years of age."}
]

completion = gpt_prompt(message_data, client, modelName)
print(completion, end='\n\n')