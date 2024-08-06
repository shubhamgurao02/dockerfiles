import pandas as pd
import sys
import os
#import time
filename="demo.xlsx"
#filename="GS logs.xlsx"
user_template="user_details.xlsx"
#filename=sys.argv[1]
#user_template=sys.argv[2]

#start = time.time()
print("Processing excel files....")
user_file=pd.read_excel(user_template, sheet_name=0)
#print(user_file.head())
user_file=user_file.drop(columns=['whenCreated', 'manager'])

#print(user_file.values)
user_list=[]
fail_data=[]
ip_data=[]
login_data=[]
for i in user_file.values:
    #print(i[0])
    user_list.append(i[0])
#print(user_list)
tabs = pd.ExcelFile(filename).sheet_names 
print("Total no of sheets in excel file:",len(tabs))
l1=[]
unique_ip = pd.DataFrame()
failed_login = pd.DataFrame()
success_login = pd.DataFrame()

for i in tabs:
    print("Processing for sheet:",i)
    excel_file=pd.read_excel(filename, sheet_name=i)
    excel_file=excel_file [excel_file.iloc[:, 0].str.startswith("#")==False]
    #pattern2=excel_file [excel_file.iloc[:, 0].str.contains("pass&\*&530")]
    excel_file=excel_file [excel_file.iloc[:, 0].str.contains("pass|\*|230|530|331")]
    #print(excel_file)
    unique_ip=excel_file [excel_file.iloc[:, 0].str.contains("230")]
    unique_ip=pd.concat([unique_ip, unique_ip], ignore_index=True)
    failed_login=excel_file [excel_file.iloc[:, 0].str.contains("530")]
    failed_login=pd.concat([failed_login, failed_login], ignore_index=True)
    success_login=excel_file [excel_file.iloc[:, 0].str.contains("331")]
    success_login=pd.concat([success_login, success_login], ignore_index=True)
print(unique_ip)
#pri
try:
    print("Processing for failed login of invalid users...")
    for failed in failed_login.values:
        #print(failed[0].split(' '))
        fail_code=failed[0].split(' ')[8]
        user_name=failed[0].split(' ')[4]
        if int(fail_code) == 530 and user_name not in user_list:
            #print(failed[0].split(' ')[2],failed[0].split(' ')[4],failed[0].split(' ')[8])
            fail_user_details=[failed[0].split(' ')[2],failed[0].split(' ')[4],failed[0].split(' ')[8]]
            fail_data.append(fail_user_details)
    fail_df = pd.DataFrame(fail_data)
    #print(fail_df.columns)
    
    fail_df.columns = ["IP","Username","Status code"]
    fail_df=fail_df.drop_duplicates(subset=['IP'])
    #print(fail_df.columns)
    fail_df=pd.DataFrame(fail_df.values,columns = ["IP","Username","Status code"])
    print("Generating CSV file for failed login of invalid users.....")
    fail_df.to_csv("failed_login.csv", index=False , header=True)
except:
    print("something wrong or operation not required")
try:
    print("Processing for unique IP ....")
    for ip in unique_ip.values:
    #print(ip[0].split(' '))
        status_code=ip[0].split(' ')[8]
        if int(status_code) == 230 :
            #print(ip[0].split(' ')[2],ip[0].split(' ')[4],ip[0].split(' ')[8])
            unique_ip_details=[ip[0].split(' ')[2],ip[0].split(' ')[4],ip[0].split(' ')[8]]
            ip_data.append(unique_ip_details)
    ip_df = pd.DataFrame(ip_data)
    #print(ip_df.columns)
    
    ip_df.columns = ["IP","Username","Status code"]
    ip_df=ip_df.drop_duplicates(subset=['IP'])
    #print(ip_df.columns)
    ip_df=pd.DataFrame(ip_df.values,columns = ["IP","Username","Status code"])
    print("Generating CSV file for unique IP .....")
    ip_df.to_csv("unique_ip.csv", index=False , header=True)
        #print(i[0].split(' ')[2],i[0].split(' ')[4],i[0].split(' ')[8])
except:
    print("something wrong or operation not required")
try:    
    print("Processing for invalid login of valid users......")
    for  slogin in success_login.values:
        # print(slogin[0].split(' '))
        failed_code=ip[0].split(' ')[8]
        user_name=failed[0].split(' ')[4]

        if int(failed_code) == 530 and user_name in user_list :
                #print(slogin[0].split(' ')[2],slogin[0].split(' ')[4],slogin[0].split(' ')[8])
            success_login_details=[ip[0].split(' ')[2],ip[0].split(' ')[4],ip[0].split(' ')[8]]
            login_data.append(success_login_details)
    login_df = pd.DataFrame(login_data)
        #print(login_data)
    
    login_df.columns = ["IP","Username","Status code"]
    login_df=login_df.drop_duplicates(subset=['IP'])
    #print(login_df.columns)
    login_df=pd.DataFrame(login_df.values,columns = ["IP","Username","Status code"])
    print("Generating CSV file for failed login of valid users .....")
    login_df.to_csv("invalid_login_attempt.csv", index=False , header=True)
except:
    print("something wrong or operation not required")
login_data1=[]
for  slogin in success_login.values:
     # print(slogin[0].split(' '))
    failed_code=ip[0].split(' ')[8]
    user_name=failed[0].split(' ')[4]

    if int(failed_code) == 530 and user_name in user_list :
                #print(slogin[0].split(' ')[2],slogin[0].split(' ')[4],slogin[0].split(' ')[8])
        success_login_details=[ip[0].split(' ')[2],ip[0].split(' ')[4],ip[0].split(' ')[8]]
        login_data1.append(success_login_details)

    print(login_data1)


    