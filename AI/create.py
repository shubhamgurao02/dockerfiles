import weaviate
import json
import pandas as pd
#exfile="Book1.xlsx"
exfile="RL_KEDB_updated.xlsx"
data=pd.read_excel(exfile )#,names=['Situation','Test Cases','Troubleshooting Steps'])
print(data.columns)
print(data.drop(['Interface'], axis=1))
data=data.drop(['A schema validation \n     ','Interface'], axis=1)
h=data.to_json(orient='records', indent=2)
print(h)

print("Hello")
#auth_config = weaviate.AuthApiKey(api_key="mnGhS09f1Fh2cb5c670LVorRwy2uVqtARnln")
#client = weaviate.Client(url="https://my-sandbox-cluster-fl261s0w.weaviate.network", auth_client_secret=auth_config )
client = weaviate.Client(url="http://localhost:8080",)

#client.schema.delete_class("Rlai")

class_obj = {
    "class": "Rlai",
    "vectorIndexType": "hnsw",
    "vectorIndexConfig": { 
                "skip": False,
                "cleanupIntervalSeconds": 300,
                "pq": {"enabled": False,},
                "maxConnections": 64,
                "efConstruction": 128,
                "ef": -1,
                "dynamicEfMin": 100,
                "dynamicEfMax": 500,
                "dynamicEfFactor": 8,
                "vectorCacheMaxObjects": 2000000,
                "flatSearchCutoff": 40000,
                "distance": "cosine"
            },
    "description": "Information from a Jeopardy! question",  # description of the class
    "properties": [
        {
            "dataType": ["text"],
            "description": "The question",
            "name": "situation",
        },
        {
            "dataType": ["text"],
            "description": "The answer",
            "name": "testcase",
        },
        {
            "dataType": ["text"],
            "description": "The category",
            "name": "solution",
        },
    ],
}


# add the schema
client.schema.create_class(class_obj)

# get the schema
schema = client.schema.get()
print(schema)
h=json.loads(h)
with client.batch as batch:
    batch.batch_size=100
    for d in h: 
    #print(d['Situation'])   
        properties= {
            "situation": str(d["Situation"]), 
            "testcase": str(d["Test Cases"]),
            "solution": str(d["Troubleshooting Steps"]),
            }

        s=client.batch.add_data_object(properties, "Rlai")
        print(s)


