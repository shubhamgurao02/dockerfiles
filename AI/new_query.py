import weaviate
import json
from collections import Counter
import torch
from transformers import BertModel, BertTokenizer,AutoTokenizer
import nltk
from weaviate.gql.get import HybridFusion

#from weaviate_client import WeaviateClient

# Create a BERT model.
# bert = AutoTokenizer.from_pretrained("bert-base-uncased")

# # Tokenize your search query.
# tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
# search_query = "What is the capital of France?"
# tokenized_query = tokenizer(search_query)

# # Vectorize your search query with BERT.
# encoded_query = tokenized_query
# print(encoded_query)
# query_vector = encoded_query[0][0]

client = weaviate.Client(
    url="http://localhost:8080",
)
# question="OMSRLEU.OMS.FORTER.ORDUPDATE.ERROR.DETAILS "
question = "what is venkat"
question=question.replace("\n", " ")
where_filter = {
    "operator": "Or",
    "operands":[{
    "path": ["situation"],
    "operator": "Like",
    "valueText": question

},
{
   "path": ["testcase"],
    "operator": "Like",
    "valueText": question
},
{
   "path": ["solution"],
    "operator": "Like",
    "valueText": question
},]
}


response = (
    client.query.get("Rlai", ["situation", "testcase", "solution"])
    .with_hybrid( query=question ,
        fusion_type=HybridFusion.RELATIVE_SCORE,
                alpha=0.25

 )
    .with_additional(["score", "explainScore"])
    
    .with_limit(3)
    .do()
)

result = json.dumps(response, indent=4)
print(result)
result=json.loads(result)
print(result["data"]["Get"]["Rlai"][0])
#data=result["data"]["Get"]["Rlai"][0]
