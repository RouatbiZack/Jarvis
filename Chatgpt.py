import openai
openai.api_key = "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" 
def generate_response(prompt):
    model_engine = "text-davinci-003"
    prompt = (f"{prompt}")

    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message.strip()


