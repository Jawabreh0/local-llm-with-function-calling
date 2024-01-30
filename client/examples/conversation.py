import requests

# Set the URL of your LLM server's inference endpoint
server_url = "https://4570-34-125-55-28.ngrok-free.app/v1/chat/completions"

# Get the user's prompt input
user_prompt = input("Enter your prompt: ")

# Define the message with the user's input prompt
message = {
    "role": "user",
    "content": user_prompt
}

# Create the request payload
request_payload = {
    "messages": [message],
    # the model value here is the value of argument "--model" in deploying: server_vllm.py or server.py
    "model": "/content/gdrive/MyDrive/CyprusCodesLLM/functionary-7b-v2"  
}

# Send a POST request to the server
response = requests.post(server_url, json=request_payload)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Extract and display the generated response
    response_data = response.json()
    generated_response = response_data["choices"][0]["message"]["content"]
    print("Generated Response:")
    print(generated_response)
else:
    print("Error: Request to the server failed with status code:", response.status_code)