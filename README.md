# CyprusCodes LLM

CyprusCodes LLM, is a language model that can interpret and execute functions/tools. 

The model is designed to intelligently decide the timing and sequence of function executions, opting for either parallel or serial processing based on the requirements. It is capable of interpreting the outputs of these functions and initiates them only when necessary. The definitions of these functions are structured as JSON Schema Objects, which bear resemblance to the function calls used in OpenAI GPT.

## Setup Server On Google Collb

You can set up a server on Google Colab to run your projects. There are two ways to do this: using cloud computing resources or running it locally. In this guide, we will use Google Colab for cloud-based server setup.

1. Create New Collab Note Book

2. Mount Google Drive: To access your Google Drive files, you need to mount it. Use the following command to mount your drive:
```bash
from google.colab import drive
drive.mount("/content/gdrive")
```

3. Change Directory to MyDrive: Navigate to your Google Drive's MyDrive directory using this command:
```bash
%cd /content/gdrive/MyDrive/
```
4. Create a New Directory: Create a new directory, for example, "cypruscodesllm_test" using the following code:
```python

import os

# Define the directory path
directory_path = '/content/gdrive/MyDrive/cypruscodesllm_test'

# Check if the directory already exists
if not os.path.exists(directory_path):
    # Create the directory
    os.makedirs(directory_path)
    print(f"Directory '{directory_path}' created successfully.")
else:
    print(f"Directory '{directory_path}' already exists.")
```
5. Change Directory to the Created Directory: Navigate to the newly created directory:
```bash
%cd cypruscodesllm_test
```

6. Clone this repository inside the created directory
```bash
git clone https://github.com/Jawabreh0/CyprusCodes_LLM.git
```

7. Clone the Model Repository: Clone the model repository. Note that this repository contains LFS files.
```bash
git clone https://huggingface.co/meetkai/functionary-7b-v2
```

8. Change Directory to CyprusCodes_LLM and Install Requirements: Navigate to the CyprusCodes_LLM directory and install the required dependencies:
```bash
%cd CyprusCodes_LLM
pip install -r requirements.txt
```

9. Start google collab terminal CyprusCodes_LLM (availbe only for paid accounts)

10. Change Directory to CyprusCodes_LLM: Inside the terminal, change the directory to CyprusCodes_LLM:
```bash
cd gdrice/MyDrive/cypruscodesllm_test/CyprusCodes_LLM
```

11. Run the Server: Run the server from the terminal (do not run it from the cells):
```bash
python3 server_vllm.py --model "/content/gdrive/MyDrive/cypruscodesllm_test/functionary-7b-v2" --host 0.0.0.0
```

12. Give It Time: Allow some time for the server to start running. Please note that you need a paid Colab account with at least an Nvidia A100 GPU with 30-40 GPU vRAM.

13. Check Server Status: After running the server, ensure that it is running correctly and functioning as expected.

14. Add a New Cell to Install ngrok and Set the Tunnel Token: Install ngrok and set the tunnel token in a new cell:
```bash
!pip install pyngrok
!ngrok authtoken REPLACE_THIS_WITH_YOUR_NGROK_TOKEN
```

15. Create a Public URL: Create a public URL for your server:
```bash
from pyngrok import ngrok
public_url = ngrok.connect(addr="8000", proto="http")
print("Public URL:", public_url
```

Now, your server is running in the terminal, and you have provided a public URL for clients to access it.



