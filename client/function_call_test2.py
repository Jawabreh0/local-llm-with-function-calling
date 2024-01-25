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
            tool_choice="auto",

    )
output = completion.choices[0].message
print(output)



def get_flight_info(loc_origin, loc_destination):
    """Get flight information between two locations."""

    # Example output returned from an API or database
    flight_info = {
        "loc_origin": loc_origin,
        "loc_destination": loc_destination,
        "datetime": str(datetime.now() + timedelta(hours=2)),
        "airline": "KLM",
        "flight": "KL643",
    }

    return json.dumps(flight_info)


# Use the LLM output to manually call the function
# The json.loads function converts the string to a Python object

origin = json.loads(output.function_call.arguments).get("loc_origin")
destination = json.loads(output.function_call.arguments).get("loc_destination")
params = json.loads(output.function_call.arguments)
type(params)

print(origin)
print(destination)
print(params)

# Call the function with arguments

chosen_function = eval(output.function_call.name)
flight = chosen_function(**params)

print(flight)

# The key is to add the function output back to the messages with role: function
second_completion = client.chat.completions.create(
        model="/content/gdrive/MyDrive/CyprusCodesLLM/functionary-7b-v2",
         messages=[
        {"role": "user", "content": user_prompt},
        {"role": "function", "name": output.function_call.name, "content": flight},
    ],
    functions=function_descriptions,
)
response = second_completion.choices[0].message.content
print(response)