import os
import json
from dotenv import load_dotenv
# from google import genai
from openai import OpenAI, RateLimitError 
# from pydantic import BaseModel, Field

load_dotenv()

openrouter_api_key = os.getenv("OPENROUTER_API_KEY")
if not openrouter_api_key:
    raise SystemExit("OPENROUTER_API_KEY environment variable is not set.")

Client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=openrouter_api_key)
model = "baidu/ernie-5.5-flash-preview:free"

def llm_answer(prompt):
    message = {
        "role":"user",
        "content":prompt
    }
    messages = [message]
    response = Client.chat.completions.create(model=model, messages=messages, )
    answer = response.choices[0].message.content
    return answer

bad_prompt=""""
This ia a user complaint:
My laptop is not working
I wnat a new laptop money.
or else repair my laptop.
"""

good_prompt = """
#ROLE:
You are a support assistant at a mobile/laptop company.
#TASK
You have to classify the issue in a category.
#CONSTRAINT
You have to classify the issue in one of the three categories namely billing, technical, return.
#OUTPUT FORMAT
Your answer should be strictly one word only. The one word answer should be one of the categories given in constraints.
#Here is the complaint:
{bad_prompt}
"""

print(llm_answer(good_prompt))

