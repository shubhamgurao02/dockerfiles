import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import docker
import pytz
import sys
from datetime import datetime, timedelta
import re
client = docker.from_env()
current_time = datetime.now()
past_time = current_time - timedelta(minutes=30)
#print(past_time)
#print(current_time)
#print(past_time.strftime("%Y-%m-%d %I:%M:%S"))
past_time=past_time.strftime("%Y-%m-%d %I:%M:%S")
current_time=current_time.strftime("%Y-%m-%d %I:%M:%S")

containers = client.containers.list()
pattern=r"BIP\d+E:"
pattern2=f"{datetime.now():%Y-%m-%d}"
#print("pattern2",pattern2)
l3=[]
l1=[]
# log_file=open("output1.txt","r")
# log_file=log_file.readlines()
#log_file=[line.strip() for line in log_file]

config_file=open("docker_config_file.txt","r")
config_file=config_file.readlines()
config_file=[line.strip() for line in config_file]
#print(config_file)
for container in containers:
    #print(container.id, container.name)
    container_logs = container.logs( timestamps=True).decode('utf-8')
    
    for i in container_logs.split('\n'):
#for i in log_file:
    #print(i)
        i=str(i)
        if re.search(pattern,i):
        #print("Hi")
            if any(re.search(pattern, i) for pattern in config_file):
                if re.search(pattern2, i):
                    try:
                        error_code=i.split(' ')[3]
                #print("error_code" , error_code)
                        if error_code.split(':')[0] in config_file:
                            
                            l1.append(i)
                    except:
                        pass
                #sys.exit()
            
#print(l1)
for i in l1:
    t=i.split(' ')[2].rstrip(':')
    d=i.split(' ')[1].rstrip(':')
    time_string=f"{d} {t}"
    time_string=datetime.strptime(time_string, '%Y-%m-%d %H:%M:%S.%f')
    actual_time=time_string.strftime('%Y-%m-%d %I:%M:%S')
    if str(current_time) > str(actual_time) > str(past_time):
        print("demo1 line",i)
                                
    
body = "".join(l3)
#print(body)
# Email configuration
smtp_server = "smtp1.poloralphlauren.com"
smtp_port = 25
sender_email ="DP-MQ-FSH-Report@poloralphlauren.com" #"shubham.gurao@ralphlauren.com"

receiver_email = "shubham.gurao@ralphlauren.com"
msg="ACE Container Log analysis error report"
if body:
    style="table, th, td {  border: 1px solid black;}"
    # Create the email message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = f"""ACE Container LOG ERROR Email Alert"""
    html_content = f"""
    <!doctype html>
    <html lang="en">
    <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
<style>
{style}
</style>
  </head>
  <body >
  <h5>ACE Container Log analysis error report </h5>
  <br>
    <table>
  <tr>
    <th>Date</th>
    <th>Error code</th>
    <th>Error</th>
    </tr>
  {body}
  </table>
    <br>

    <!-- Option 1: Bootstrap Bundle with Popper -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>

    <!-- Option 2: Separate Popper and Bootstrap JS -->
    <!--
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js" integrity="sha384-IQsoLXl5PILFhosVNubq5LC7Qb9DXgDA9i+tQ8Zj3iwWAwPtgFTxbJ8NT4GN1R8p" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.min.js" integrity="sha384-cVKIPhGWiC2Al4u+LWgxfKTRIcfu0JTxR+EQDz/bgldoEyl4H0zUF0QKbrJ0EcQF" crossorigin="anonymous"></script>
    -->
  </body>
</html>
    """
    # Email body
    message.attach(MIMEText(html_content, "html"))

    # Connect to the SMTP server and send the email
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        # server.starttls()
        # server.login(sender_email)
        server.sendmail(sender_email, receiver_email, message.as_string())
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print(f"Error: {e}")
