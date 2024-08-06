from datetime import datetime, timedelta
import re
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

############################ Predefined variables #####################################
smtp_server = "smtp1.poloralphlauren.com"
smtp_port = 25
sender_email ="DP-MQ-FSH-Report@poloralphlauren.com" 
receiver_email = ["DL-Group-IT-ESB-Middleware-Support@RalphLauren.com" , "annu.singh@prolifics.com"]
msg="RDQM Log analysis error report "
######################################################################################
current_time1 = datetime.now()
#print(current_time1)
current_time1=current_time1.strftime("%Y-%m-%d %H:%M:%S")
past_time = current_time1 - timedelta(minutes=30)
#print(past_time.strftime("%Y-%m-%d %I:%M:%S"))
past_time=past_time.strftime("%Y-%m-%d %H:%M:%S")
m=str(current_time1.strftime("%b"))
y=str(current_time1.strftime("%Y"))
d=str(current_time1.strftime("%d"))
strtw= f"{m} {d}"
try:
    env=sys.argv[4]
    log_file=sys.argv[1]
#print(log_file)
    log_file=open(log_file,'r')
    log_file=log_file.readlines()

    patterns=sys.argv[2]
    patterns= open(patterns,'r')    
    patterns=patterns.readlines()
    sub_patterns=sys.argv[3]
    sub_patterns= open(sub_patterns,'r')
    sub_patterns=sub_patterns.readlines()
except:
    print("Kindly provide proper file path")
    sys.exit()
##################################List declaration#################################    
l1=[]
l2=[]
l4=[]

##################################Code implementation #############################
sub_patterns=[item for item in sub_patterns if item.strip()]
patterns=[item for item in patterns if item.strip()]
if log_file:
    for i in log_file:
    #if any(re.search(pattern, i) for pattern in patterns):
        if re.search(strtw, i) :
        #print(i)
            l1.append(i)
    
#print(l1)
if l1:
    for i in l1:
        if any(re.search(pattern.rstrip(), i) for pattern in patterns):
        #print(i.strip())
            l2.append(i.strip())
if l2:
    l4 = [line for line in l2 if any(target.strip() in line for target in sub_patterns)]
l3=[]
if l4:
    for i in l4:
        #print(i.split())
        try:
            month=i.split()[0]
            day=i.split()[1]
            time=i.split()[2]
            date_string=f"{y} {month} {day} {time}"
        #print(date_string)
            actual_time = datetime.strptime(date_string, '%Y %b %d %H:%M:%S')
    #print(actual_time)
            if str(current_time1) > str(actual_time) > str(past_time):
        #print(i.split(' '))
            #print(actual_time)
                server=i.split(' ')[3]
                details=' '.join(i.split(' ')[4:])
                data=f"<tr><td>{actual_time}</td><td>{server}</td><td>{details}</td>"
                l3.append(data)
        except:
            pass

if l3:
    body = "".join(l3)
    style="table, th, td {  border: 1px solid black;}"
    # Create the email message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = ', '.join(receiver_email)
    message["Subject"] = f"""RDQM LOG ERROR Email Alert for {env} environment"""
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
    <h5> RDQM Log analysis error report for {env} environment</h5>
  
    <table>
    <tr>
    
    <th>Date</th>
    <th>Server</th>
    <th>Error Message</th>
    
    </tr>
    {body}
    </table>
    <br>

    </body>
    </html>
    """
    # Email body
    message.attach(MIMEText(html_content, "html"))

    # Connect to the SMTP server and send the email
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        # server.starttls()
        # server.login(sender_email,email_password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print(f"Error: {e}")
else:
    print(" No log entries present in log file ")

