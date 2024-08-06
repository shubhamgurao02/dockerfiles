import weaviate

# Instantiate the client with the auth config
client = weaviate.Client(
    url="https://my-sandbox-cluster-fl261s0w.weaviate.network",  # Replace w/ your endpoint
    auth_client_secret=weaviate.AuthApiKey(api_key="mnGhS09f1Fh2cb5c670LVorRwy2uVqtARnln"),  # Replace w/ your Weaviate instance API key
)
print(client)



# schema = {
#   "classes": [{
#     "class": "Hellorl",
#     "description": "RL related ai activities",
#     "properties": [
#       {
#         "dataType": [
#           "text"
#         ],
#         "description": "testcases",
#         "name": "testcase"
#       },
#       {
#         "dataType": [
#           "text"
#         ],
#         "description": "solutions of testcase",
#         "name": "solution"
#       },
#       {
#         "dataType": [
#             "text"
#         ],
#         "description": "situation for testcase",
#         "name": "situation"
#       }
#     ]
# }]
#   }

# client.schema.create(schema)
print(client.schema.get())
