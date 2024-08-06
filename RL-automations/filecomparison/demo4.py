import pandas as pd 
import sys
import xml.etree.ElementTree as ET
excel_file =sys.argv[1]
data=pd.read_excel(excel_file , engine='openpyxl')
data = data.dropna(how='all')
agent_names=data.iloc[:, 2].drop_duplicates()

mon_list = sys.argv[2]
f=open(mon_list,'rt')
lines=f.readlines()
mon_list=[]
add_monitors=[]
update_monitor=[]
delete_monitor=[]
mon_details=[]
a1= "/opt/mqm/bin/fteAnt -f ./defineMonitor.xml"
f1= "./fteDeleteMonitor -mm"
f2 = "-ma"
f3 = "-mn"

for j in lines:
    mon_name=j.split('.xml')[0].split('.')[-1]
#    print(mon_name)
    mon_list.append(mon_name)
#print(mon_list)

for i in data.values:
    #print(i)
    if str(i[-1]) != 'nan': 
        #print(i[-1])
        if str(i[-1].lower()) == 'add':
            add_monitors.append(list(i))
            if i[0] not in mon_list:
                #print("Hi")
                mon_details=[]
            #print(i[-1])
                for index , item in enumerate(i):
#                print(index, item)
                
                    if index == 0 and str(item) != "nan" and str(item) != " ":
#                    print(" -Dmn="+ str(item))
                    #print(index)
                        dmn=" -Dmn="+ '"' + str(item) + '"'
                        mon_details.append(dmn)
                    if index == 1 and str(item) != "nan" and str(item) != " ":
            #print(" -Dnn="+ str(item))
                        dmt=" -Dmt="+ '"' + str(item) + '"'
                        mon_details.append(dmt.strip())
    
    #If cellNumber = 3 Then SetProperty = " -Dnn="
                    
                    if index == 2 and str(item) != "nan" and str(item) != " ": 
            #print(" -DpostDestC="+ str(item))
                        dpostdestc=" -DpostDestC="+ '"' + str(item) + '"'
                        mon_details.append(dpostdestc)
                    if index == 3 and str(item) != "nan" and str(item) != " ": 
            #print(" -DpostSrcC="+ str(item))
                        dpostsrcc=" -DpostSrcC="+ '"' + str(item) + '"'
                        mon_details.append(dpostsrcc)
                    if index == 4 and str(item) != "nan" and str(item) != " ": 
            #print(" -DpreSrcC="+ str(item))
                        dpresrcc=" -DpreSrcC="+ '"' + str(item) + '"'
                        mon_details.append(dpresrcc)
                    if index == 5 and str(item) != "nan" and str(item) != " ": 
            #print(" -DpreDestC="+ str(item))
                    #print(index)
                        dpredestc=" -DpreDestC="+ '"' + str(item) + '"'
                        mon_details.append(dpredestc)
                    if index == 6 and str(item) != "nan" and str(item) != " ": 
            #print(" -Dmd="+ str(item))
                        dmd=" -Dmd="+ '"' + str(item) + '"'
                        mon_details.append(dmd)
                    if index == 7 and str(item) != "nan" and str(item) != " ": 
            #print(" -Dpt="+ str(item))
                        dpt=" -Dpt="+ '"' + str(item) + '"'
                        mon_details.append(dpt)
                    if index == 8 and str(item) != "nan" and str(item) != " ": 
            #print(" -Dpi="+ str(item))
                        dpi=" -Dpi="+ '"' + str(int(item)) + '"'
                        mon_details.append(dpi)
                    if index == 9 and str(item) != "nan" and str(item) != " ":
            #print(" -Dpu=" + str(item))
                        dpu=" -Dpu=" + '"' + str(item) + '"'
                        mon_details.append(dpu)
                    if index == 10 and str(item) != "nan" and str(item) != " ":
            #print(" -Dsa="+ str(item))
                        dsa=" -Dsa="+ '"' + str(item) + '"'
                        mon_details.append(dsa)
                    if index == 11 and str(item) != "nan" and str(item) != " ":
            #print(" -Dsm="+ str(item))
                        dsm=" -Dsm="+ '"' + str(item) + '"'
                        mon_details.append(dsm)
                    if index == 12 and str(item) != "nan" and str(item) != " ":
            #print(" -Dda="+ str(item))
                        dda=" -Dda="+ '"' + str(item) + '"'
                        mon_details.append(dda)
                    if index == 13 and str(item) != "nan" and str(item) != " ":
            #print(" -Ddm="+ str(item))
                        ddm=" -Ddm="+ '"' + str(item) + '"'
                        mon_details.append(ddm)
                    if index == 14 and str(item) != "nan" and str(item) != " ":
            #print(" -Ddd="+ str(item))
                        ddd=" -Ddd="+ '"' + str(item) + '"'
                        mon_details.append(ddd)
                    if index == 15 and str(item) != "nan" and str(item) != " ":
            #print(" -DDPType="+ str(item))
                        ddptype=" -DDPType="+ '"' + str(item) + '"'
                        mon_details.append(ddptype)
                    if index == 16 and str(item) != "nan" and str(item) != " ":
            #print(" -DDPRcv="+ str(item))
                        ddprcv=" -DDPRcv="+ '"' + str(item) + '"'
                        mon_details.append(ddprcv)
                    if index == 17 and str(item) != "nan" and str(item) != " ":
            #print(" -DDPSdr=" + str(item))
                        ddpsdr=" -DDPSdr=" + '"' + str(item) + '"'
                        mon_details.append(ddpsdr)
                    if index == 18 and str(item) != "nan" and str(item) != " ":
            #print(" -Dsd="+ str(item))
                        dsd=" -Dsd="+ '"' + str(item) + '"'
                        mon_details.append(dsd)
                    if index == 19 and str(item) != "nan" and str(item) != " ":
            #print(" -Dttype="+ str(item))
                        dttype=" -Dttype="+ '"' + str(item) + '"'
                        mon_details.append(dttype)
                    if index == 20 and str(item) != "nan" and str(item) != " ":
            #print(" -Dsrcdisp="+ str(item))
                        dsrcdisp=" -Dsrcdisp="+ '"' + str(item) + '"'
                        mon_details.append(dsrcdisp)
                    if index == 21 and str(item) != "nan" and str(item) != " ":
                       
                        dexists=" -Dexists="+ '"' + str(item) + '"'
                        mon_details.append(dexists)
                    if index == 22 and str(item) != "nan" and str(item) != " ":
            #print(" -DmatchType="+ str(item))
                        dmatchtype=" -DmatchType="+ '"' + str(item) + '"'
                        mon_details.append(dmatchtype)
                    if index == 23 and str(item) != "nan" and str(item) != " ":
            #print(" -DmqaPreMon="+ str(item))
                        dmqapremon=" -DmqaPreMon="+ '"' + str(item) + '"'
                        mon_details.append(dmqapremon)
                    if index == 24 and str(item) != "nan" and str(item) != " ":
            #print(" -DmqaPreSrc="+ str(item))
#                    print("DmqaPreSrc",item)
                        dmqapresrc=" -DmqaPreSrc="+ '"' + str(item) + '"'
                        mon_details.append(dmqapresrc)
                    if index == 25 and str(item) != "nan" and str(item) != " ":
            #print(" -DmqaPreDst="+ str(item))
                        dmqpredst=" -DmqaPreDst="+ '"' + str(item) + '"'
                        mon_details.append(dmqpredst)
                    if index == 26 and str(item) != "nan" and str(item) != " ":
#                    print(" -DmqaPostDst="+ str(item))
                        dmqapostdst=" -DmqaPostDst="+ '"' + str(item) + '"'
                        mon_details.append(dmqapostdst)
                    if index == 27 and str(item) != "nan" and str(item) != " ":
                    #print(" -DmqaPostSrc="+ str(item))
                        dmqapostsrc=" -DmqaPostSrc="+ '"' + str(item) + '"'
                        mon_details.append(dmqapostsrc)
                    if index == 28 and str(item) != "nan" and str(item) != " ":
                    #print(" -DmqaDeptName="+ str(item))
                        dmqadeptname=" -DmqaDeptName="+ '"' + str(item) + '"'
                        mon_details.append(dmqadeptname)
                    if index == 29 and str(item) != "nan" and str(item) != " ": 
            #print(" -DmqaDocType="+ str(item))
                        dmqadoctype=" -DmqaDocType="+ '"' + str(item) + '"'
                        mon_details.append(dmqadoctype)
                #print(mon_details)
                mon = open("new_monitors.sh", "a")  
                mon.write(a1 + ' '.join(i for i in mon_details) + "\n" + "\n")
                mon.close()    
        if str(i[-1].lower()) == 'update':
            add_monitors.append(list(i))
            if i[0] in mon_list:
                mon = open("new_monitors.sh", "a")
                mon.write(f1 + " " + i[11] + " " + " " + f2 + " " + i[10] + " " + " " + f3 + " " + i[0] + "\n" + "\n")
                mon.close()
                mon_details=[]
            #print(i[-1])
                for index , item in enumerate(i):
#                print(index, item)
                    if index == 0 and str(item) != "nan" and str(item) != " ":
#                    print(" -Dmn="+ str(item))
                    #print(index)

                        dmn=" -Dmn="+ '"' + str(item) + '"'
                        mon_details.append(dmn)
                    
    #If cellNumber = 3 Then SetProperty = " -Dnn="
                    if index == 1 and str(item) != "nan" and str(item) != " ": 
            #print(" -Dmt="+ str(item))
                        dmt=" -Dmt="+ '"' + str(item) + '"'
                        mon_details.append(dmt)
                    if index == 2 and str(item) != "nan" and str(item) != " ": 
            #print(" -DpostDestC="+ str(item))
                        dpostdestc=" -DpostDestC="+ '"' + str(item) + '"'
                        mon_details.append(dpostdestc)
                    if index == 3 and str(item) != "nan" and str(item) != " ": 
            #print(" -DpostSrcC="+ str(item))
                        dpostsrcc=" -DpostSrcC="+ '"' + str(item) + '"'
                        mon_details.append(dpostsrcc)
                    if index == 4 and str(item) != "nan" and str(item) != " ": 
            #print(" -DpreSrcC="+ str(item))
                        dpresrcc=" -DpreSrcC="+ '"' + str(item) + '"'
                        mon_details.append(dpresrcc)
                    if index == 5 and str(item) != "nan" and str(item) != " ": 
            #print(" -DpreDestC="+ str(item))
                    #print(index)
                        dpredestc=" -DpreDestC="+ '"' + str(item) + '"'
                        mon_details.append(dpredestc)
                    if index == 6 and str(item) != "nan" and str(item) != " ": 
            #print(" -Dmd="+ str(item))
                        dmd=" -Dmd="+ '"' + str(item) + '"'
                        mon_details.append(dmd)
                    if index == 7 and str(item) != "nan" and str(item) != " ": 
            #print(" -Dpt="+ str(item))
                        dpt=" -Dpt="+ '"' + str(item) + '"'
                        mon_details.append(dpt)
                    if index == 8 and str(item) != "nan" and str(item) != " ": 
            #print(" -Dpi="+ str(item))
                        dpi=" -Dpi="+ '"' + str(int(item)) + '"'
                        mon_details.append(dpi)
                    if index == 9 and str(item) != "nan" and str(item) != " ":
            #print(" -Dpu=" + str(item))
                        dpu=" -Dpu=" + '"' + str(item) + '"'
                        mon_details.append(dpu)
                    if index == 10 and str(item) != "nan" and str(item) != " ":
            #print(" -Dsa="+ str(item))
                        dsa=" -Dsa="+ '"' + str(item) + '"'
                        mon_details.append(dsa)
                    if index == 11 and str(item) != "nan" and str(item) != " ":
            #print(" -Dsm="+ str(item))
                        dsm=" -Dsm="+ '"' + str(item) + '"'
                        mon_details.append(dsm)
                    if index == 12 and str(item) != "nan" and str(item) != " ":
            #print(" -Dda="+ str(item))
                        dda=" -Dda="+ '"' + str(item) + '"'
                        mon_details.append(dda)
                    if index == 13 and str(item) != "nan" and str(item) != " ":
            #print(" -Ddm="+ str(item))
                        ddm=" -Ddm="+ '"' + str(item) + '"'
                        mon_details.append(ddm)
                    if index == 14 and str(item) != "nan" and str(item) != " ":
            #print(" -Ddd="+ str(item))
                        ddd=" -Ddd="+ '"' + str(item) + '"'
                        mon_details.append(ddd)
                    if index == 15 and str(item) != "nan" and str(item) != " ":
            #print(" -DDPType="+ str(item))
                        ddptype=" -DDPType="+ '"' + str(item) + '"'
                        mon_details.append(ddptype)
                    if index == 16 and str(item) != "nan" and str(item) != " ":
            #print(" -DDPRcv="+ str(item))
                        ddprcv=" -DDPRcv="+ '"' + str(item) + '"'
                        mon_details.append(ddprcv)
                    if index == 17 and str(item) != "nan" and str(item) != " ":
            #print(" -DDPSdr=" + str(item))
                        ddpsdr=" -DDPSdr=" + '"' + str(item) + '"'
                        mon_details.append(ddpsdr)
                    if index == 18 and str(item) != "nan" and str(item) != " ":
            #print(" -Dsd="+ str(item))
                        dsd=" -Dsd="+ '"' + str(item) + '"'
                        mon_details.append(dsd)
                    if index == 19 and str(item) != "nan" and str(item) != " ":
            #print(" -Dttype="+ str(item))
                        dttype=" -Dttype="+ '"' + str(item) + '"'
                        mon_details.append(dttype)
                    if index == 20 and str(item) != "nan" and str(item) != " ":
            #print(" -Dsrcdisp="+ str(item))
                        dsrcdisp=" -Dsrcdisp="+ '"' + str(item) + '"'
                        mon_details.append(dsrcdisp)
                    if index == 21 and str(item) != "nan" and str(item) != " ":
            #print(" -Dexists="+ str(item))
                        dexists=" -Dexists="+ '"' + str(item) + '"'
                        mon_details.append(dexists)
                    if index == 22 and str(item) != "nan" and str(item) != " ":
            #print(" -DmatchType="+ str(item))
                        dmatchtype=" -DmatchType="+ '"' + str(item) + '"'
                        mon_details.append(dmatchtype)
                    if index == 23 and str(item) != "nan" and str(item) != " ":
            #print(" -DmqaPreMon="+ str(item))
                        dmqapremon=" -DmqaPreMon="+ '"' + str(item) + '"'
                        mon_details.append(dmqapremon)
                    if index == 24 and str(item) != "nan" and str(item) != " ":
            #print(" -DmqaPreSrc="+ str(item))
#                    print("DmqaPreSrc",item)
                        dmqapresrc=" -DmqaPreSrc="+ '"' + str(item) + '"'
                        mon_details.append(dmqapresrc)
                    if index == 25 and str(item) != "nan" and str(item) != " ":
            #print(" -DmqaPreDst="+ str(item))
                        dmqpredst=" -DmqaPreDst="+ '"' + str(item) + '"'
                        mon_details.append(dmqpredst)
                    if index == 26 and str(item) != "nan" and str(item) != " ":
#                    print(" -DmqaPostDst="+ str(item))
                        dmqapostdst=" -DmqaPostDst="+ '"' + str(item) + '"'
                        mon_details.append(dmqapostdst)
                    if index == 27 and str(item) != "nan" and str(item) != " ":
                    #print(" -DmqaPostSrc="+ str(item))
                        dmqapostsrc=" -DmqaPostSrc="+ '"' + str(item) + '"'
                        mon_details.append(dmqapostsrc)
                    if index == 28 and str(item) != "nan" and str(item) != " ":
                    #print(" -DmqaDeptName="+ str(item))
                        dmqadeptname=" -DmqaDeptName="+ '"' + str(item) + '"'
                        mon_details.append(dmqadeptname)
                    if index == 29 and str(item) != "nan" and str(item) != " ": 
            #print(" -DmqaDocType="+ str(item))
                        dmqadoctype=" -DmqaDocType="+ '"' + str(item) + '"'
                        mon_details.append(dmqadoctype)
                #print(mon_details)
                mon = open("new_monitors.sh", "a")  
                mon.write(a1 + ' '.join(i for i in mon_details) + "\n" + "\n")
                mon.close() 
        if str(i[-1].lower()) == 'delete':
            if i[0] in mon_list:
                if i[0] in mon_list:
                    mon = open("new_monitors.sh", "a")
                    mon.write(f1 + " " + i[11] + " " + " " + f2 + " " + i[10] + " " + " " + f3 + " " + i[0] + "\n" + "\n")
                    mon.close()
           
    #print(mon_details)
    # mon = open("new_monitors.sh", "a")  
    # mon.write(a1 + ' '.join(i for i in mon_details) + "\n" + "\n")
    # mon.close()
    # print("Updated monitor: ")  
    #             #break