import sys
#import xml.etree.ElementTree as ET
from lxml import etree
#import xml.etree.ElementTree as ET
file1=open("C:\\RL\\RLreplace\\RL-automations\\filecomparison\\AGNT.MFT.Q01.MFT01.ACE_OMSEU_OMS_BI_PROTECTEDSTOCK_OUT.xml","r")
#lines=file1.read()
tree= etree.parse(file1)
root=tree.getroot()
for name in root.iter('name'):
    #l3.append(name.text)
    print(name.text)
    s=name.text
    break
for agent in root.iter('agent'):
    print(agent.text)
for pollinterval in root.iter('pollInterval'):
    print(pollinterval.attrib['units'])
    print(pollinterval.text)
for directory in root.iter('directory'):
    print(directory.text)
for pattern in root.iter('pattern'):
    print(pattern.text)
for srcagent in root.iter('sourceAgent'):
    print(srcagent.attrib['QMgr'])
    print(srcagent.attrib['agent'])
for destagent in root.iter('destinationAgent'):
    print(destagent.attrib['QMgr'])
    print(destagent.attrib['agent'])
for metadata in root.iter('metaData'):
    print(metadata.attrib['key'],metadata.text )
for source in root.iter('source'):
    print(source.attrib['disposition'])
for fname in root.iter('file'):
    print(fname.text)
for dest in root.iter('destination'):
    print(dest.attrib['exist'])
print("Hi",root)
# import xml.etree.ElementTree as ET

# # Define the XML snippet as a string
# xml_string = '''
# <item checksumMethod="MD5" mode="binary">
#     <source disposition="delete" recursive="false">
#         <file>/tmp</file>
#     </source>
#     <destination exist="overwrite" type="directory">
#         <file>/tmp/out</file>
#     </destination>
# </item>
# '''
# #print(' '.join(lines))
# # Parse the XML string
# root = ET.fromstring(xml_string)
# #root = tree.getroot()
# # Extract information from the XML elements
# checksum_method = root.get('checksumMethod')
# mode = root.get('mode')
# source_file = root.find('source/file').text
# destination_file = root.find('destination/file').text
# destination_exist = root.find('destination').get('exist')
# destination_type = root.find('destination').get('type')

# # Print the extracted information
# print(f'Checksum Method: {checksum_method}')
# print(f'Mode: {mode}')
# print(f'Source File: {source_file}')
# print(f'Destination File: {destination_file}')
# print(f'Destination Exist: {destination_exist}')
# print(f'Destination Type: {destination_type}')
