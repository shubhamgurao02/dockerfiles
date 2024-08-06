import pandas as pd
import sys
import os
#import time
filename="demo.xlsx"
#filename="GS logs.xlsx"
#filename=sys.argv[1]
#start = time.time()
print("Processing excel file....")
tabs = pd.ExcelFile(filename).sheet_names 
print("Total no of sheets in excel file:",len(tabs))
l1=[]
my_df = pd.DataFrame()
for i in tabs:
    print("Processing for sheet:",i)
    excel_file=pd.read_excel(filename, sheet_name=i)
    excel_file=excel_file [excel_file.iloc[:, 0].str.startswith("#")==False]
    #pattern2=excel_file [excel_file.iloc[:, 0].str.contains("\*|530")]
    excel_file=excel_file [excel_file.iloc[:, 0].str.contains("pass|\*|230")]
    # print(pattern2)
    # for j in pattern2.values:
    #     print(j[0].split(' '))
        #ip_addr=j[0].split(' ')[2]
        #print(ip_add)
        #l1.append(ip_add)
    for i in excel_file.values:
        #print(i[0].split(' '))
        ip_add=i[0].split(' ')[2]
        #print(ip_add)
        l1.append(ip_add)
        
#print(l1)
df = pd.DataFrame(l1)
df=df.drop_duplicates()
print("Generating CSV file.....")
df.to_csv("output.csv", index=False , header=None)

