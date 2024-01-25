# CyprusCodes LLM

CyprusCodes LLM, is a language model that can interpret and execute functions/tools. 

The model is designed to intelligently decide the timing and sequence of function executions, opting for either parallel or serial processing based on the requirements. It is capable of interpreting the outputs of these functions and initiates them only when necessary. The definitions of these functions are structured as JSON Schema Objects, which bear resemblance to the function calls used in OpenAI GPT.

## Setup Server On Google Collb

There are two ways to do that, either running it on a cloud computing resources, or running it localy, for the cloud computing resources i'll use Google Collab

1. Create New Collab Note Book

2. Mount the drive
```bash
from google.colab import drive
drive.mount("/content/gdrive")
```

3. Change directory to MyDrive
```bash
%cd /content/gdrive/MyDrive/
```
4. Create new directory and name it for example cypruscodesllm_test
```bash

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
5. Change directory to the create directory
```bash
%cd cypruscodesllm_test
```

6. Clone this repository inside the created directory
```bash
git clone https://github.com/Jawabreh0/CyprusCodes_LLM.git
```

7. Clone the model repository
note this repository contains LFS files
```bash
git clone https://huggingface.co/meetkai/functionary-7b-v2
```

8. Change directory to CyprusCodes_LLM and install the requrements
```bash
%cd CyprusCodes_LLM
pip install -r requirements.txt
```

9. Start google collab terminal CyprusCodes_LLM (availbe only for paid accounts)

10. change directory to CyprusCodes_LLM
```bash
%cd gdrice/MyDrive/cypruscodesllm_test/CyprusCodes_LLM
```

11. From the terminal run the server (dont run it from the cells)
```bash
python3 server_vllm.py --model "/content/gdrive/MyDrive/cypruscodesllm_test/functionary-7b-v2" --host 0.0.0.0
```

12. Give little bit time and the server will start running, note you need paid collab account with at least Nvidea A100 GPU with 30-40 GPU vRam

13. After running the server, make sure that the server is running and working good.

14. add new cell,install ngrok and set the tunnel token
```bash
!pip install pyngrok
!ngrok authtoken REPLACE_THIS_WITH_YOUR_NGROK_TOKEN
```

15. Create Public URL
```bash
from pyngrok import ngrok
public_url = ngrok.connect(addr="8000", proto="http")
print("Public URL:", public_url
```

Now the server is running in the terminal, and you provided public URL to be used be the clients.




