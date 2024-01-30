from openai import OpenAI
import json
import requests

# Initialize the OpenAI client
client = OpenAI(base_url="https://878f-35-247-179-113.ngrok-free.app/v1", api_key="functionary")

# AviationStack API key
aviationstack_api_key = "76eec478b67e77b3d23fddb1ee62dc0f"

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

# Updated get_flight_info function
def get_flight_info(loc_origin, loc_destination):
    base_url = "http://api.aviationstack.com/v1/flights"
    url = f"{base_url}?access_key={aviationstack_api_key}&dep_iata={loc_origin}&arr_iata={loc_destination}"
    
    response = requests.get(url)
    if response.status_code == 200:
        flights = response.json().get('data', [])
        if flights:
            flight = flights[0]  # Using the first flight for demonstration
            return {
                "airline": flight['airline']['name'],
                "departure_airport": flight['departure']['airport'],
                "arrival_airport": flight['arrival']['airport'],
                "departure_time": flight['departure']['estimated'],
                "arrival_time": flight['arrival']['estimated']
            }
        else:
            return "No flights found."
    else:
        return "Error retrieving flight information."

# Get user's prompt
user_prompt = input("Enter your prompt: ")

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
        args = json.loads(function_call.function.arguments)
        function_result = get_flight_info(**args)

        # Follow-up request with function result
        follow_up_completion = client.chat.completions.create(
            model="/content/gdrive/MyDrive/CyprusCodesLLM/functionary-7b-v2",
            messages=[
                {"role": "user", "content": user_prompt},
                {"role": "system", "content": json.dumps(function_result)}
            ],
            functions=tools,
            function_call="auto"
        )
        follow_up_output = follow_up_completion.choices[0].message.content
        print(follow_up_output)
else:
    print(output.content)
