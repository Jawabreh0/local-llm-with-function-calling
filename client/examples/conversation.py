import requests

class LLMCommunicator:
    def __init__(self, server_url, model_path):
        self.server_url = server_url
        self.model_path = model_path

    def send_request(self, user_prompt):
        message = {"role": "user", "content": user_prompt}
        request_payload = {
            "messages": [message],
            "model": self.model_path
        }

        response = requests.post(self.server_url, json=request_payload)
        return response

    def get_response(self, response):
        if response.status_code == 200:
            response_data = response.json()
            return response_data["choices"][0]["message"]["content"]
        else:
            return "Error: Request to the server failed with status code: " + str(response.status_code)

def main():
    server_url = "https://878f-35-247-179-113.ngrok-free.app/v1/chat/completions"
    model_path = "/content/gdrive/MyDrive/CyprusCodesLLM/functionary-7b-v2"

    communicator = LLMCommunicator(server_url, model_path)
    print("\n\n\t\t Welcome To CyprusCodes LLM \n\n")
    while True:
        user_input = input("User: ").lower()
        if user_input in ["exit", "quit", "bye"]:
            break

        response = communicator.send_request(user_input)
        generated_response = communicator.get_response(response)
        print(f"Assistant: {generated_response}\n")

if __name__ == "__main__":
    main()
