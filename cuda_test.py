# import matplotlib.pyplot as plt
# print("successfully import matplot")
import torch
from torch.utils.cpp_extension import CUDA_HOME, CppExtension, CUDAExtension

print(f"cuda is ok: {torch.cuda.is_available()}")
print(CUDA_HOME)

# import transformers
# print("successfully import transformers")
# Use a pipeline as a high-level helper

# from transformers import pipeline
# pipe = pipeline("text-generation", model="meta-llama/Llama-2-7b-chat-hf")

# Load model directly
# from transformers import AutoTokenizer, AutoModelForCausalLM

# tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-chat-hf")
# model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-7b-chat-hf")
