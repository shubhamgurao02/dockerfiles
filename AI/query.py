import weaviate
import json
from collections import Counter

client = weaviate.Client(
    url="http://localhost:8080",
)
# question="OMSRLEU.OMS.FORTER.ORDUPDATE.ERROR.DETAILS "
question = "what is venakt"
# question="<Text>java.net.SocketTimeoutException: Read timed out</Text>"
# nearText = {"concepts": [question],

#              }

# # where_filter = {
# #     "path": ["situation"],
# #     "operator": "Like",
# #     "valueText": question
# # }

# where_filter = {
#     "operator": "Or",
#     "operands":[{
#     "path": ["situation"],
#     "operator": "Like",
#     "valueText": question

# },
# {
#    "path": ["testcase"],
#     "operator": "Like",
#     "valueText": question
# },
# {
#    "path": ["solution"],
#     "operator": "Like",
#     "valueText": question
# },]
# }


# response = (
#     client.query
#     .get("Rlai", ["situation", "testcase", "solution"])
#     .with_generate(single_prompt=generate_prompt)
#     .with_near_text(nearText)
#     .with_additional(['certainty'])
#     .with_where(where_filter)
#     .with_limit(3)
#     .do()
# )
response = (
    client.query.get("Rlai", ["situation", "testcase", "solution"])
    .with_hybrid(
        query=question,
    )
    .with_additional(["certainty"])
    .with_limit(3)
    .do()
)
list1 = [
    "what",
    "if",
    "when",
    "as",
    "a",
    "who",
    "the",
    "how",
    "can",
    "should",
    "be",
    "is",
    "resolve",
    "and",
    "whom",
]
# print(json.dumps(response, indent=4))
result = json.dumps(response, indent=4)
print(result)
result = json.loads(result)
# result=json.loads(result["data"])
# print(result["data"]["Get"]["Rlai"][0]["_additional"]["certainty"])
split_question = question.split(" ")
# print(split_question)
words = list((Counter(split_question) - Counter(list1)).elements())
# print(words)
words = [x.strip("") for x in words]
# print(words)

output = result["data"]["Get"]["Rlai"]
print(output)
# for i in output:

#     for j in words:
#         sample=i["situation"]
#         #print("sample:",sample)
#         valid=sample.replace(':',' ')
#         valid=valid.replace('\n',' ').split(" ")
#         print(valid)
#         if j in valid:
#             print("certainty:" , i["_additional"]["certainty"])
#             print("\n")
#             print("Output:")
#             print("\n")
#             print("Situation:", i["situation"] )
#             print("\n")
#             print( "Solution:",i["solution"] )
#             print("\n")
#             print("Testcase:", i["testcase"] )
#             print("\n")
#             print("==========================================================================================")
#             break
#         else:
#             print("Please provide proper query")

#################################################################
if len(output) > 0:
    # print(output)
    for i in output:
        sample = i["situation"] + i["testcase"] + i["solution"]
        # print("sample:",sample)
        valid = sample.replace(":", " ")
        valid = valid.replace("\n", " ").split(" ")
        valid = [x.strip("") for x in valid]
        # print("valid:",valid)
        # print("words:",words)
        if any(element in words for element in valid):
            # print("Hello")
            print("certainty:", i["_additional"]["certainty"])
            print("\n")
            print("Output:")
            print("\n")
            print("Situation:", i["situation"])
            print("\n")
            print("Solution:", i["solution"])
            print("\n")
            print("Testcase:", i["testcase"])
            print("\n")
            print(
                "=========================================================================================="
            )
            break
        else:
            print("Please provide proper query")
else:
    print("Please provide proper query")
#################################################################
# print("certainty:" , i["_additional"]["certainty"])
# print("\n")

# print("Output:")
# print("\n")
# print("Situation:", i["situation"] )
# print("\n")
# print( "Solution:",i["solution"] )
# print("\n")
# print("Testcase:", i["testcase"] )
# print("\n")
# print("==========================================================================================")
