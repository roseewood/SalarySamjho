import openai
from app.config import OPENAI_KEY

openai.api_key = OPENAI_KEY


def explain(component, amount):
    prompt = f"Explain {component} of Rs {amount} in simple Indian salary terms"

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content