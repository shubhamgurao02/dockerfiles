
import weaviate
import json
from weaviate.gql.get import HybridFusion
from transformers import RagTokenizer, RagRetriever, RagTokenForGeneration
tokenizer = RagTokenizer.from_pretrained("facebook/rag-token-base")
retriever = RagRetriever.from_pretrained("facebook/rag-token-base")
model = RagTokenForGeneration.from_pretrained("facebook/rag-token-base", retriever=retriever)

client = weaviate.Client(
            url="http://localhost:8080",
        )
limit=3         
question = "OMSRLEU"
response = (
            client.query.get("Rlai", ["situation", "testcase", "solution"])
            .with_hybrid(
                query=question, fusion_type=HybridFusion.RELATIVE_SCORE, alpha=0.25
            )
            .with_additional(["score", "explainScore"])
            .with_limit(limit)
            .do()
        )

result = json.dumps(response, indent=4)
        #print(result)
result = json.loads(result)
        
        # print(json.dumps(response, indent=4))
output = result["data"]["Get"]["Rlai"]
print(output)

entities = [result["solution"] for result in output]


input_text = question + " " + " ".join(entities)  # Concatenate user query and entity names
input_dict = tokenizer.prepare_seq2seq_batch(input_text, return_tensors="pt")

# Generate a response using the RAG model
output_ids = model.generate(input_dict["input_ids"], max_length=50, num_return_sequences=1)
generated_response = tokenizer.decode(output_ids[0], skip_special_tokens=True)

# Print the generated response
print("Generated Response:", generated_response)
