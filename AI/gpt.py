from transformers import RagTokenizer, RagRetriever, RagTokenForGeneration

# Load the pretrained RAG components (tokenizer, retriever, and model) as you did before
tokenizer = RagTokenizer.from_pretrained("facebook/rag-sequence-base")
retriever = RagRetriever.from_pretrained("facebook/rag-sequence-base")
model = RagTokenForGeneration.from_pretrained("facebook/rag-sequence-base", retriever=retriever)

# Define a user query
user_query = "Who holds the record in 100m freestyle?"

# Encode the user query
input_dict = tokenizer.prepare_seq2seq_batch(user_query, return_tensors="pt")

# Pass the input through the model to generate a response
output_ids = model.generate(input_dict["input_ids"], max_length=50, num_return_sequences=1)

# Decode and print the generated response
generated_response = tokenizer.decode(output_ids[0], skip_special_tokens=True)
print("Generated Answer:", generated_response)
