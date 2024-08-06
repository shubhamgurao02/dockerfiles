h="PRLUS01\APP-FTP-QAMICROS"

def contains_forward_slash(input_string):
    return '\\' in input_string

# Test the function
input_string = "Hello\world"
if contains_forward_slash(input_string):
    print("The string contains a forward slash.")
else:
    print("The string does not contain a forward slash.")

if '\\' in input_string:
    print('yes')
else:
    print('no')