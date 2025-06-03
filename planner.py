import os
import json
import openai
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def suggest_next_topic(memory):
    prompt = f"""
You are a helpful AI study coach.

The user’s goal is: {memory['goal']}
Their current level is: {memory['level']}
They have already completed: {memory['completed']}
They have skipped: {memory['skipped']}
They prefer to avoid: {memory['preferences']}

Suggest 1 next learning topic in artificial intelligence or machine learning with:
- A title
- A 1-sentence reason why it’s next
- A resource (link to video or notebook)
Format your response as JSON with keys: title, type, link, reason.
"""

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Or use "gpt-3.5-turbo"
            messages=[
                {"role": "system", "content": "You are a smart study planner."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )

        text = response['choices'][0]['message']['content']
        return json.loads(text)

    except Exception as e:
        print("❌ Error calling OpenAI:", e)
        return {
            "title": "Linear Regression (fallback)",
            "type": "video",
            "link": "https://youtu.be/pa0FMyyHz2U",
            "reason": "Fallback topic in case GPT response fails."
        }
