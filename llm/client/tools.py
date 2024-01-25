from openai import OpenAI

client = OpenAI(base_url="https://7a63-34-143-151-63.ngrok-free.app/v1", api_key="functionary")

client.chat.completions.create(
    model="/content/gdrive/MyDrive/CyprusCodesLLM/functionary-7b-v2",
    messages=[{"role": "user",
            "content": "What is the weather for Istanbul?"}
    ],
    tools=[{
            "type": "function",
            "function": {
                "name": "get_current_weather",
                "description": "Get the current weather",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "The city and state, e.g. San Francisco, CA"
                        }
                    },
                    "required": ["location"]
                }
            }
        }],
    tool_choice="auto"
)