from openai import OpenAI
import json
from datetime import datetime, timedelta

# Initialize the OpenAI client
client = OpenAI(base_url="https://4570-34-125-55-28.ngrok-free.app/v1", api_key="functionary")

# Define tools (functions that the model can call)
tools = [
    {
        "name": "get_flight_info",
        "description": "Get flight information between two locations",
        "parameters": {
            "type": "object",
            "properties": {
                "loc_origin": {"type": "string", "description": "The departure airport, e.g. DUS"},
                "loc_destination": {"type": "string", "description": "The destination airport, e.g. HAM"}
            },
            "required": ["loc_origin", "loc_destination"]
        }
    }
]

# Define the function that the tool represents
def get_flight_info(loc_origin, loc_destination):
    # Dummy implementation, replace with your actual logic
    return f"Flight from {loc_origin} to {loc_destination} is at 3 PM"

# User's prompt
user_prompt = "When's the next flight from Amsterdam to New York?"

# Initial request to the model
completion = client.chat.completions.create(
    model="/content/gdrive/MyDrive/CyprusCodesLLM/functionary-7b-v2",
    messages=[{"role": "user", "content": user_prompt}],
    functions=tools,
    function_call="auto"
)

# Process the model's response
output = completion.choices[0].message
if output.tool_calls:
    function_call = output.tool_calls[0]
    if function_call.function.name == "get_flight_info":
        # Extract arguments and call the function
        args = json.loads(function_call.function.arguments)
        function_result = get_flight_info(**args)

        # Follow-up request with function result
        follow_up_completion = client.chat.completions.create(
            model="/content/gdrive/MyDrive/CyprusCodesLLM/functionary-7b-v2",
            messages=[
                {"role": "user", "content": user_prompt},
                {"role": "system", "content": function_result}
            ],
            functions=tools,
            function_call="auto"
        )
        follow_up_output = follow_up_completion.choices[0].message.content
        print(follow_up_output)
else:
    print(output.content)
