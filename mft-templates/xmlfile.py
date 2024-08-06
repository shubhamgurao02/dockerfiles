# # import sys
import xml.etree.ElementTree as ET

file1='mft_backup\\AGNT.MFT.Q01.MFT01.ACE_OMSEU_OMS_BI_PROTECTEDSTOCK_OUT.xml'
# Read XML content from file
with open(file1, "r") as file:
    your_xml_string = file.read()

# #file1="mft_backup\\" + agent_name + i[2] + ".xml"  
# # tree= ET.parse(file1)
# # root=tree.getroot()
# # list3=[]
# # for name in root.iter('name'):
# #     s=name.text
# #     print(s) 
# #     break
# # for directory in root.iter('directory'):
# #     d=directory.text
# #     print(d)
# #     break                

tree = ET.fromstring(your_xml_string)

# # Find the mqaPreMon element
# mqa_pre_mon_element = tree.find('.//metaData[@key="mqaPreMon"]')

# # Extract the value of mqaPreMon
# if mqa_pre_mon_element is not None:
#     mqa_pre_mon = mqa_pre_mon_element.text
# else:
#     mqa_pre_mon = None


print(element.attrib.items())
# print("mqaPreMon:", mqa_pre_mon)

#import xml.etree.ElementTree as ET

# Parse the XML document
# tree = ET.fromstring(your_xml_string)

# Extract parameter values
# Print attributes of an element
def print_element_attributes(element):
    for key, value in element.attrib.items():
        print(f"Attribute: {key} = {value}")

# Print elements and their text content
def print_elements_and_text(element):
    if element.text and element.text.strip():
        print(f"Element: {element.tag}, Text Content: {element.text.strip()}")

    for child in element:
        print_elements_and_text(child)

# Call the functions to print attributes and elements
print_element_attributes(tree)
print_elements_and_text(tree)
