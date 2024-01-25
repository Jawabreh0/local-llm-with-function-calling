# CyprusCodes LLM

CyprusCodes LLM, is a language model that can interpret and execute functions/tools. 

The model is designed to intelligently decide the timing and sequence of function executions, opting for either parallel or serial processing based on the requirements. It is capable of interpreting the outputs of these functions and initiates them only when necessary. The definitions of these functions are structured as JSON Schema Objects, which bear resemblance to the function calls used in OpenAI GPT.

## Setup

1. Prepare The Server Side Work

There are two ways to do that, either running it on a cloud computing resources, or running it localy, for the cloud computing resources i'll use Google Collab

1.1 Prepare The Server Side Work On Google Collab

1.1.1 Create New Collab Note Book

1.1.2 Mount the drive
```bash
from google.colab import drive
drive.mount("/content/gdrive")
```

1.1.3 Change directory to MyDrive
```bash
%cd /content/gdrive/MyDrive/
```






