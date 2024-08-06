import sys
import os
env_dir = sys.argv[1]
path = os.getcwd()
print(path)

#print(os.path.join(path , 'apps', 'config'))
if os.path.exists('configurations'):
    policy_path=os.path.join(path , env_dir , 'policy','Defaultpolicies')    
    print(policy_path)
    print("Hi")