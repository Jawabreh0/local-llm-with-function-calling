import openai
import os
import asyncio
from chatlab import Chat  # Importing Chat instead of Conversation

# Set the API key and base URL for Functionary
openai.api_key = "functionary"
os.environ['OPENAI_API_KEY'] = "functionary"
openai.api_base = "https://7a63-34-143-151-63.ngrok-free.app/v1/chat/completions"

# Define the function to get the current weather (mock implementation)
def get_current_weather(location: str):
    """
    Get the current weather for a given location.
    This is a mock implementation. Replace with real API call or logic.
    """
    # Placeholder response
    return {"weather": "Sunny", "temperature": "25°C"}

# Define other functions as needed...
# For example, a function to estimate property value (a mock implementation)
def estimate_property_value(property_details: dict):
    """
    Estimate the market value of a property.
    This is a mock implementation. Replace with real API call or logic.
    """
    # Placeholder response
    return {"estimated_value": "$500,000"}

# Function to handle the conversation asynchronously

async def handle_conversation():
    # Initialize the chat
    chat = Chat(model="/content/gdrive/MyDrive/CyprusCodesLLM/functionary-7b-v2")
    
    # Register functions
    chat.register(get_current_weather)
    chat.register(estimate_property_value)

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break

        # Submit the user prompt to the conversation and await the response
        await chat.submit(user_input)

        # Process the conversation messages
        for message in chat.messages:
            role = message["role"].upper()
            if "function_call" in message:
                func_name = message["function_call"]["name"]
                func_param = message["function_call"]["arguments"]
                print(f"{role}: call function: {func_name}, arguments:{func_param}")

                # Parse func_param from string to dictionary if necessary
                if isinstance(func_param, str):
                    import json
                    try:
                        func_param = json.loads(func_param.replace('\n', ''))
                    except json.JSONDecodeError:
                        print("Error parsing function parameters.")
                        continue

                # Implement your function call handling here...
                if func_name == "get_current_weather":
                    response = get_current_weather(**func_param)
                    print(f"FUNCTION: {response}")
                elif func_name == "estimate_property_value":
                    response = estimate_property_value(**func_param)
                    print(f"FUNCTION: {response}")
            else:
                content = message["content"]
                print(f"{role}: {content}")

# Run the conversation handler
if __name__ == "__main__":
    asyncio.run(handle_conversation())