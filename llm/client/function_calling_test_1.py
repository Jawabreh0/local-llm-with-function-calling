from openai import OpenAI
import json
from datetime import datetime, timedelta

client = OpenAI(base_url="https://ea69-34-142-204-118.ngrok-free.app/v1", api_key="functionary")

function_descriptions = [
    {
        "name": "get_flight_info",
        "description": "Get flight information between two locations",
        "parameters": {
            "type": "object",
            "properties": {
                "loc_origin": {
                    "type": "string",
                    "description": "The departure airport, e.g. DUS",
                },
                "loc_destination": {
                    "type": "string",
                    "description": "The destination airport, e.g. HAM",
                },
            },
            "required": ["loc_origin", "loc_destination"],
        },
    }
]

user_prompt = "When's the next flight from Amsterdam to New York?"

completion = client.chat.completions.create(
        model="/content/gdrive/MyDrive/CyprusCodesLLM/functionary-7b-v2",
        messages=[
            {"role": "user", "content": user_prompt,}],
            functions=function_descriptions,
            function_call="auto",

    )
output = completion.choices[0].message
print(output)

