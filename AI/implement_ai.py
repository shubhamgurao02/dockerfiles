from transformers import GPT2Tokenizer, GPT2LMHeadModel

# Load the pre-trained GPT-2 XL model and tokenizer
model_name = "gpt2-xl"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

# Set the maximum token limit
max_tokens = 100  # Adjust as needed

# User input
user_input = "Once upon a time, in a land far, far away, there was a"

# Encode the user input
input_ids = tokenizer.encode(user_input, return_tensors="pt")

# Generate a response with the specified max_tokens limit
output = model.generate(input_ids, max_length=max_tokens, num_return_sequences=1)

# Decode the generated response
response = tokenizer.decode(output[0], skip_special_tokens=True)

# Print the generated response
print("Generated Response:", response)
