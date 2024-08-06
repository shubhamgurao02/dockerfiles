
#python test2.py -p configurations/dev/policy/ -k configurations/dev/config/keystore/ -s configurations/dev/config/server.conf.yaml -t configurations/dev/config/truststore/ -hv

# import yaml
# with open('demo.yaml', 'r') as file:
#     prime_service = yaml.safe_load(file)

# print(prime_service['get'].append('macha'))

# prime_service=prime_service['get'].append('macha')
# with open("demo.yaml", "w") as f:
#     yaml.dump(prime_service, f)
# import yaml

# # Define the new value to be added to the 'get' list
# new_value = 'ssh'

# # Read the existing YAML file
# with open('demo.yaml', 'r') as file:
#     yaml_data = yaml.safe_load(file)

# # Update the YAML data with the new value
# if 'get' in yaml_data:
#     yaml_data['get'].append(new_value)
# else:
#     yaml_data['get'] = [new_value]

# # Write the updated YAML data back to the file
# with open('demo.yaml', 'w') as file:
#     yaml.safe_dump(yaml_data, file, default_flow_style=False)

# print("YAML file has been updated.")
# from ruamel.yaml import YAML

# # Define the new value to be added to the 'get' list
# new_value = 'hello babes'

# # Create an instance of the YAML class
# yaml = YAML()

# # Read the existing YAML file
# with open('demo.yaml', 'r') as file:
#     yaml_data = yaml.load(file)

# # Update the YAML data with the new value
# if 'get' in yaml_data:
#     yaml_data['get'].append(new_value)
# else:
#     yaml_data['get'] = [new_value]

# # Write the updated YAML data back to the file
# with open('demo.yaml', 'w') as file:
#     yaml.dump(yaml_data, file)

# print("YAML file has been updated.")

##for bar urls
# from ruamel.yaml import YAML

# # Define the new values to replace the 'get' list
# new_values = ['ssh', 'bye', 'btw']

# # Create an instance of the YAML class
# yaml = YAML()

# # Read the existing YAML file
# with open('demo.yaml', 'r') as file:
#     yaml_data = yaml.load(file)

# # Replace the 'get' array with new values
# yaml_data['get'] = new_values

# # Write the updated YAML data back to the file
# with open('demo.yaml', 'w') as file:
#     yaml.dump(yaml_data, file)

# print("YAML file has been updated.")

from ruamel.yaml import YAML

# Define the new value for the 'set' key
new_value_for_set = 'new_value'

# Create an instance of the YAML class
yaml = YAML()

# Read the existing YAML file
with open('demo.yaml', 'r') as file:
    yaml_data = yaml.load(file)

# Update the 'set' key with the new value
yaml_data['set'] = new_value_for_set

# Write the updated YAML data back to the file
with open('demo.yaml', 'w') as file:
    yaml.dump(yaml_data, file)

print("YAML file has been updated.")
