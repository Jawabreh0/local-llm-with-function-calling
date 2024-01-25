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
