
import docker
import pytz
from datetime import datetime, timedelta
import re
client = docker.from_env()
current_time = datetime.now()
past_time = current_time - timedelta(minutes=30)
print(past_time)
print(current_time)
containers = client.containers.list()
#since_time = datetime.now() - timedelta(minutes=30)
#est=pytz.timezone('US/Eastern')
#since_time=est.localize(since_time)
# print(since_time.strftime("%Y-%m-%dT%H:%M:%SZ"))
# since_time=since_time.strftime("%Y-%m-%dT%H:%M:%SZ")
pattern=r"BIP\d+E:"
l1=[]
config_file=open("docker_config_file.txt","r")
config_file=config_file.readlines()
config_file=[line.strip() for line in config_file]

for container in containers:
    #print(container.id, container.name)
    container_logs = container.logs( timestamps=True).decode('utf-8')
    #print(container_logs.split('\n'))
    print("Start")
    #print(container_logs)
    #container_logs = [log for log in container_logs if log and datetime.strptime(log.split()[0], "%Y-%m-%dT%H:%M:%S.%fZ") > since_time]

    for i in container_logs.split('\n'):
        
        if re.search(pattern, i):
            #print(i)
            try:
                actual_time=str(i.split(' ')[1])
                actual_time=str(actual_time).split(' ')[2]
                actual_time=actual_time[:-1]
                print(actual_time)
            except:
                pass
            if str(current_time) > str(actual_time) > str(past_time):
            
                error_code=i.split(' ')[3]
                print("error_code" , error_code)
                if error_code not in config_file:
                    print(i)
                    print("end")
                else:
                    print(i.split(' ')[2:])
    print("Hi")
