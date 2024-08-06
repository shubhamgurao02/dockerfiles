import yaml

file1 = open("C:\\RL\\RLreplace\\IA\\qa_build.txt", 'r')
list1 = file1.readlines()

file2 = open("C:\\RL\\RLreplace\\IA\\qa_deploy.txt", 'r')
list2 = file2.readlines()

# Define the output file path
output_file = 'generated.yaml'

# Iterate over both lists simultaneously
for i in range(min(len(list1), len(list2))):
    path1=f"Pipelines/{str(list1[i]).strip()}"
    print(path1)
    path2= f"Pipelines/{str(list2[i]).strip()}"
    # Define the YAML data with variables and triple single quotes around file paths
    data = {
        'include': [
            {'local': path1 },
            {'local': path2 }
        ]
    }

    # Write data to the YAML file
    with open(output_file, 'a') as file:
        yaml.dump(data, file, default_flow_style=False)

print(f'YAML data written to {output_file}')
