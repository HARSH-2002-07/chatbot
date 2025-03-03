from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_name = "meta-llama/Llama-2-7b-chat"  # Ensure this matches your downloaded model path

# Load the tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Load the model with 8-bit precision to save VRAM (if needed)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float16,  # Use float16 for lower VRAM usage
    device_map="auto"  # Automatically selects GPU if available
)

# Move model to GPU (if available)
device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)

print("Model Loaded Successfully!")
