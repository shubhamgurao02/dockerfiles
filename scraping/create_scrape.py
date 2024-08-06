import weaviate
import json
import pandas as pd
#exfile="Book1.xlsx"

print("Hello")
#auth_config = weaviate.AuthApiKey(api_key="mnGhS09f1Fh2cb5c670LVorRwy2uVqtARnln")
#client = weaviate.Client(url="https://my-sandbox-cluster-fl261s0w.weaviate.network", auth_client_secret=auth_config )
client = weaviate.Client(url="http://localhost:8082",)

client.schema.delete_class("Scrap")

class_obj = {
    
    "class": "Scrap",
    "description": "Information from a web scraping! ",
    "moduleConfig": {
        "text2vec-openai": {
            "vectorizeClassName": True
        }
    },
    "invertedIndexConfig": {
        "bm25": {
            "k1": 1.5,  #// Default: 1.2
            "b": 0.75
        }
    },
    "properties": [
        {
            "dataType": ["text"],
            "description": "The text",
            "moduleConfig": {
                "text2vec-openai": {
                    "vectorizePropertyName": True 
                }
            },
            "name": "text",
        },
        {
            "dataType": ["text"],
            "description": "The text",
            "moduleConfig": {
                "text2vec-openai": {
                    "vectorizePropertyName": True 
                }
            },
            "name": "links",
        },
        
    ]
}


# add the schema
client.schema.create_class(class_obj)

# get the schema
schema = client.schema.get()
print(schema)
