import xml.etree.ElementTree as ET
import pandas as pd 
excel_file ="qmdetails.xlsx"
#print(file1)
data=pd.read_excel(excel_file , engine='openpyxl')
data = data.dropna(how='all')
mon_list = "monitor_details.txt"

f=open(mon_list,'rt')
lines=f.readlines()
#list3 = []
#state=sys.argv[5]
#file1='AGNT.MFT.Q01.MFT01.ACE_OMSEU_OMS_BI_PROTECTEDSTOCK_OUT.xml' 
#tree= ET.parse(file1)
#root=tree.getroot()
a1= "/opt/mqm/bin/fteAnt -f ./defineMonitor.xml"
f1= "/opt/mqm/bin/fteDeleteMonitor -mm"
f2 = "-ma"
f3 = "-mn"
l2=['Dmn','Dwave','Dnn','Dmt','DpostDestC','DpostSrcC','DpreSrcC','DpreDestC','Dmd','Dpt','Dpi','Dpu','Dsa','Dsm','Dda','Ddm','Ddd','DDPType','DDPRcv','DDPSdr','Dsd','Dttype','Dsrcdisp','Dexists','DmatchType','DmqaPreMon','DmqaPreSrc','DmqaPreDst','DmqaPostDst','DmqaPostSrc','DmqaDeptName','DmqaDocType']
#existing_mons={}
mon_set=set()
for i in data.values :
    #print(i[33])
    if i[33] == "update" :
        #print(i[33])
        #print(i[1])
        #print(i[12])
        file1=i[12]+i[1]+".xml"
        #print(file1)
        tree= ET.parse(file1)
        root=tree.getroot()
        list3=[]
    
        #print(i)
        for name in root.iter('name'):
    #l3.append(name.text)
            #print(name.text)
            s=name.text 
            print(s)
            break
        for directory in root.iter('directory'):
            d=directory.text
            print(d)                                      #print(i[2])
            #list3.append(i[2])
        for pattern in root.iter('pattern'):
            pat=pattern.text
            print(pat)  
        # for item in root.iter('item'):
        #     item=item.attrib
        #     for source in item:
        #         sour=source.attrib
        #         print(sour)  
        for meta in root.iter('metaData'):
            m=meta.text
            v=meta.attrib['key']
            print(v+":"+m)
            #print(v)
        for interval in root.iter('pollInterval'):
            m=interval.text
            v=interval.attrib['units']
            print(m)
            print(v)
        for sourceAgent in root.iter('sourceAgent'):
            Agentname=sourceAgent.attrib['agent']
            qmgrname=sourceAgent.attrib['QMgr']
            print(Agentname)
            print(qmgrname)
        for sourceResource in root.iter('item'):
            s=sourceResource.attrib['mode']
            print(s)
        for source in root.iter('source'):
            sourceDisposition=source.attrib['disposition']
            print(sourceDisposition)
        for file in root.iter('file'):
            print(file.text)
        for file in root.iter('file'):
            print(file.text)
            
        