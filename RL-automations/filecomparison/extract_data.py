import os
import xml.etree.ElementTree as ET
import sys
import requests
from openpyxl import Workbook
url=sys.argv[1]
files_directory=sys.argv[2]
# url = "http://127.0.0.1:8000/upload/"
# files_directory = 'C:\\RL\\RLreplace\\RL-automations\\filecomparison\\mft_backup'

wb = Workbook()
ws = wb.active
columns = ['monitorName' , 'monitorTemplate' ,'postDestinationCall' , 'postSourceCall' ,'preSourceCall' , 'preDestinationCall' , 'monitorDirectory' , 'monitorTrigger' , 'pollingInterval' , 'pollingUnit' , 'monitorAgent' , 'monitorQM' , 'destinationAgent' , 'destinationQM' , 'destinationPath' , 'DPMQFTEContentType' , 'DPMQFTEReceiverId' , 'DPMQFTESenderId' , 'sourceResource' , 'transferType' , 'sourceDisposition' , 'destDisposition' , 'matchType' , 'mqaPreMon' , 'mqaPreSrc' , 'mqaPreDst' , 'mqaPostDst' , 'mqaPostSrc' , 'mqaDeptName' , 'Comments' ,  'mqaDocType'	 ]

ws.append(columns)
files = os.listdir(files_directory)


for file_name in files:
    list1=[]
    if file_name.endswith('.xml'):
        file_path=os.path.join(files_directory, file_name)
        tree= ET.parse(file_path)
        root=tree.getroot()
        #list3=[]
        store=[]
        #print(i)
        for name in root.iter('name'): #monitor name 1
    #l3.append(name.text)
            #print(name.text)
            s=name.text 
            list1.append(s)
            break
        list1.append('NOOP')
        list1.append('NOOP')
        list1.append('NOOP')
        list1.append('NOOP')
        list1.append('NOOP')
        #list1.append('NOOP')
        for directory in root.iter('directory'): #monitor directory 8
            d=directory.text
            #print(d) 
            
            list1.append(d)                                     #print(i[2])
            #list3.append(i[2])
        for pattern in root.iter('pattern'): #pattern 9
            pat=pattern.text
            #print(pat)  
            list1.append(pat)

        for interval in root.iter('pollInterval'): #pollinterval and unit
            pollinterval=interval.text
            unit=interval.attrib['units']
            #print(pollinterval) #10
            #print(unit) #11
        list1.append(pollinterval)
        list1.append(unit)
        for sourceAgent in root.iter('sourceAgent'): #agent and QM
            Agentname=sourceAgent.attrib['agent']
            qmgrname=sourceAgent.attrib['QMgr']
            #print(Agentname) #12
            #print(qmgrname)  #13
        list1.append(Agentname)
        list1.append(qmgrname)
        for destinationAgent in root.iter('destinationAgent'): #dest agent and QM
            dAgentname=sourceAgent.attrib['agent']
            dqmgrname=sourceAgent.attrib['QMgr']
            #print(dAgentname) #14
            #print(dqmgrname)  #15
        list1.append(dAgentname)
        list1.append(dqmgrname)
        for file in root.iter('file'): 
            #print(file.text)
            store.append(file.text)
        # print(store[1])  #destinationPath  16
        # print(store[0]) #sourceResource 20
        # print("Hi")
        list1.append(store[1])
        list1.append('NOOP')
        list1.append('NOOP')
        list1.append('NOOP')
        list1.append(store[0])        
        for sourceResource in root.iter('item'): #transferType 21
            s=sourceResource.attrib['mode']
            
            #print(s)
        list1.append(s)
        for source in root.iter('source'): #sourceDisposition  22
            sourceDisposition=source.attrib['disposition']
            #print("Hi")
            #print(sourceDisposition)
        list1.append(sourceDisposition)
        for destination in root.iter('destination'): #destDisposition 23
            #print(destination)
            destination=destination.attrib['exist']
            #print(destination)
        list1.append(destination)
        list1.append('NOOP')

        for mqaPreMon in root.iter('metaData'):
            if mqaPreMon.attrib['key'] == "mqaPreMon":  #25
                #print(mqaPreMon.text)
                list1.append(mqaPreMon.text)
            if mqaPreMon.attrib['key'] == "mqaPreSrc": #26
                #print(mqaPreMon.text)
                list1.append(mqaPreMon.text)
            if mqaPreMon.attrib['key'] == "mqaPreDst": #27
                #print(mqaPreMon.text)
                list1.append(mqaPreMon.text)
            if mqaPreMon.attrib['key'] == "mqaPostDst": #28
                #print(mqaPreMon.text)
                list1.append(mqaPreMon.text)
            if mqaPreMon.attrib['key'] == "mqaPostSrc": #29
                #print(mqaPreMon.text)
                list1.append(mqaPreMon.text)
            
            if mqaPreMon.attrib['key'] == "mqaDeptName": #30
                #print(mqaPreMon.text)
                list1.append(mqaPreMon.text)
            if mqaPreMon.attrib['key'] == "mqaDocType": #32
                #print(mqaPreMon.text)
                list1.append("NOOP")
                list1.append(mqaPreMon.text)
        #print(list1)
        list1=[val if val != 'NOOP' else ' ' for val in list1]
        
        ws.append(list1)
        wb.save('example.xlsx')

payload = {}
files=[
  ('file',('example.xlsx',open('example.xlsx','rb'),'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'))
]
headers = {}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)
