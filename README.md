# CyprusCodes LLM

CyprusCodes LLM, is a language model that can interpret and execute functions/tools. 

The model is designed to intelligently decide the timing and sequence of function executions, opting for either parallel or serial processing based on the requirements. It is capable of interpreting the outputs of these functions and initiates them only when necessary. The definitions of these functions are structured as JSON Schema Objects, which bear resemblance to the function calls used in OpenAI GPT.

## Setup

1. Clone the repository:
```bach
git clone git@github.com:Jawabreh0/CyprusCodes_LLM.git
cd CyprusCodes_LLM
```

2. Install PyTorch
PyTorch with CPU support
```bach
pip install torch
```
OR
If you have a compatible GPU and want to install PyTorch with GPU support (CUDA)
```bach
pip install torch torchvision torchaudio -f https://download.pytorch.org/whl/cpu/torch_stable.html
```

3. Install the required dependencies
```bach
pip install -r requirements.txt
```

4. Run The Server
Running a large language model (LLM) locally can be a bit complex, and the choice between CPU or GPU depends on your machine's capabilities. While there are projects like [LocalAI](https://github.com/mudler/LocalAI) that aim to enable LLM execution on CPUs, it's important to note that running an LLM on your CPU, even if it's a powerful one, may not yield satisfactory performance. The process of sending a prompt and receiving a response from the LLM when it runs on a CPU can take anywhere from 30 seconds to 3 minutes. This demonstrates that running an LLM on a CPU is not the most efficient approach. However, you can explore [LocalAI](https://github.com/mudler/LocalAI) if you have specific reasons to do so. Below, you can find evidence of the time it takes to run a simple prompt without function calls on a 4-core CPU.

https://github.com/Jawabreh0/CyprusCodes_LLM/assets/98946028/ff469318-3477-4bc9-ae99-751d6ace6ae9

As our project designed mainly to give the user the best experince so we designed it to run on the GPU and here it comes that to run the server you need a GPU with 30 - 40 GB vRAM, below is the hardware resources usage while running the server.
![Example Image](assets/resources_usage.png)




