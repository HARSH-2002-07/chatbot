from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_name = "meta-llama/Llama-2-7b-chat"

tokenizer = AutoTokenizer.from_pretrained(model_name, local_files_only=True)

model = AutoModelForCausalLM.from_pretrained(
    model_name, 
    torch_dtype=torch.float16,
    device_map="auto",
    local_files_only=True
)

print("Model Loaded Successfully!")
