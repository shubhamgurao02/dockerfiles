import pandas as pd 
import sys
import xml.etree.ElementTree as ET
excel-template = sys.argv[1]
#print(file1)
data=pd.read_excel(excel-template , engine='openpyxl')
data = data.dropna(how='all')
mon_details=sys.argv[2]
qm_name=sys.argv[3]
agent_name=sys.argv[4]
#print(agent_name+".")
agent_name=agent+"."
#print(agent_name)
f=open(mon_details,'rt')
lines=f.readlines()
#list3 = []
state=sys.argv[5]
#file1='AGNT.MFT.Q01.MFT01.ACE_OMSEU_OMS_BI_PROTECTEDSTOCK_OUT.xml' 
#tree= ET.parse(file1)
#root=tree.getroot()
l2=['Dmn','Dwave','Dnn','Dmt','DpostDestC','DpostSrcC','DpreSrcC','DpreDestC','Dmd','Dpt','Dpi','Dpu','Dsa','Dsm','Dda','Ddm','Ddd','DDPType','DDPRcv','DDPSdr','Dsd','Dttype','Dsrcdisp','Dexists','DmatchType','DmqaPreMon','DmqaPreSrc','DmqaPreDst','DmqaPostDst','DmqaPostSrc','DmqaDeptName','DmqaDocType']

if state == "new" :
    list3 = []
    for l in lines :
        #print(l)
        mname=l.split(agent_name)
        mname=mname[1].split('.xml')
        #print(mname)
        monitor_name=mname[0]
        #print("d",monitor_name)
        for m in data.values:
            #print(m[2])
            if str(m[2]) != str(monitor_name):
                print(monitor_name)
                mon_details=[]
    #print(type(i))
                print(m)
                # print(mname)
                # if i[2] in list3:
                # print("yes")
                for index , item in enumerate(m):
        #mon_details=[]
        #print("Hi")
        #if str(i[-1]) != "nan":
        #print(type(item))
                    if index == 0 and str(item) != "nan" :
            #print(" -Dwave="+ str(item) )
                        dwave=" -Dwave="+ '"' + str(item) + '"'
            #print(dwave)
                        mon_details.append(dwave)
                    if index == 1 and str(item) != "nan" :
            #print(" -Dmn="+ str(item))
                        dmn=" -Dmn="+ '"' + str(item) + '"'
                        mon_details.append(dmn)
                    if index == 2 and str(item) != "nan" :
            #print(" -Dnn="+ str(item))
                        dnn=" -Dnn="+ '"' + str(item) + '"'
                        mon_details.append(dnn)
    
    #If cellNumber = 3 Then SetProperty = " -Dnn="
                    if index == 3 and str(item) != "nan" : 
            #print(" -Dmt="+ str(item))
                        dmt=" -Dmt="+ '"' + str(item) + '"'
                        mon_details.append(dmt)
                    if index == 4 and str(item) != "nan" : 
            #print(" -DpostDestC="+ str(item))
                        dpostdestc=" -DpostDestC="+ '"' + str(item) + '"'
                        mon_details.append(dpostdestc)
                    if index == 5 and str(item) != "nan" : 
            #print(" -DpostSrcC="+ str(item))
                        dpostsrcc=" -DpostSrcC="+ '"' + str(item) + '"'
                        mon_details.append(dpostsrcc)
                    if index == 6 and str(item) != "nan" : 
            #print(" -DpreSrcC="+ str(item))
                        dpresrcc=" -DpreSrcC="+ '"' + str(item) + '"'
                        mon_details.append(dpresrcc)
                    if index == 7 and str(item) != "nan" : 
            #print(" -DpreDestC="+ str(item))
                        dpredestc=" -DpreDestC="+ '"' + str(item) + '"'
                        mon_details.append(dpredestc)
                    if index == 8 and str(item) != "nan" : 
            #print(" -Dmd="+ str(item))
                        dmd=" -Dmd="+ '"' + str(item) + '"'
                        mon_details.append(dmd)
                    if index == 9 and str(item) != "nan" : 
            #print(" -Dpt="+ str(item))
                        dpt=" -Dpt="+ '"' + str(item) + '"'
                        mon_details.append(dpt)
                    if index == 10 and str(item) != "nan" : 
            #print(" -Dpi="+ str(item))
                        dpi=" -Dpi="+ '"' + str(item) + '"'
                        mon_details.append(dpi)
                    if index == 11 and str(item) != "nan" :
            #print(" -Dpu=" + str(item))
                        dpu=" -Dpu=" + '"' + str(item) + '"'
                        mon_details.append(dpu)
                    if index == 12 and str(item) != "nan" :
            #print(" -Dsa="+ str(item))
                        dsa=" -Dsa="+ '"' + str(item) + '"'
                        mon_details.append(dsa)
                    if index == 13 and str(item) != "nan" :
            #print(" -Dsm="+ str(item))
                        dsm=" -Dsm="+ '"' + str(item) + '"'
                        mon_details.append(dsm)
                    if index == 14 and str(item) != "nan" :
            #print(" -Dda="+ str(item))
                        dda=" -Dda="+ '"' + str(item) + '"'
                        mon_details.append(dda)
                    if index == 15 and str(item) != "nan" :
            #print(" -Ddm="+ str(item))
                        ddm=" -Ddm="+ '"' + str(item) + '"'
                        mon_details.append(ddm)
                    if index == 16 and str(item) != "nan" :
            #print(" -Ddd="+ str(item))
                        ddd=" -Ddd="+ '"' + str(item) + '"'
                        mon_details.append(ddd)
                    if index == 17 and str(item) != "nan" :
            #print(" -DDPType="+ str(item))
                        ddptype=" -DDPType="+ '"' + str(item) + '"'
                        mon_details.append(ddptype)
                    if index == 18 and str(item) != "nan" :
            #print(" -DDPRcv="+ str(item))
                        ddprcv=" -DDPRcv="+ '"' + str(item) + '"'
                        mon_details.append(ddprcv)
                    if index == 19 and str(item) != "nan" :
            #print(" -DDPSdr=" + str(item))
                        ddpsdr=" -DDPSdr=" + '"' + str(item) + '"'
                        mon_details.append(ddpsdr)
                    if index == 20 and str(item) != "nan" :
            #print(" -Dsd="+ str(item))
                        dsd=" -Dsd="+ '"' + str(item) + '"'
                        mon_details.append(dsd)
                    if index == 21 and str(item) != "nan" :
            #print(" -Dttype="+ str(item))
                        dttype=" -Dttype="+ '"' + str(item) + '"'
                        mon_details.append(dttype)
                    if index == 22 and str(item) != "nan" :
            #print(" -Dsrcdisp="+ str(item))
                        dsrcdisp=" -Dsrcdisp="+ '"' + str(item) + '"'
                        mon_details.append(dsrcdisp)
                    if index == 23 and str(item) != "nan" :
            #print(" -Dexists="+ str(item))
                        dexists=" -Dexists="+ '"' + str(item) + '"'
                        mon_details.append(dexists)
                    if index == 24 and str(item) != "nan" :
            #print(" -DmatchType="+ str(item))
                        dmatchtype=" -DmatchType="+ '"' + str(item) + '"'
                        mon_details.append(dmatchtype)
                    if index == 25 and str(item) != "nan" :
            #print(" -DmqaPreMon="+ str(item))
                        dmqapremon=" -DmqaPreMon="+ '"' + str(item) + '"'
                        mon_details.append(dmqapremon)
                    if index == 26 and str(item) != "nan" :
            #print(" -DmqaPreSrc="+ str(item))
                        dmqapresrc=" -DmqaPreSrc="+ '"' + str(item) + '"'
                        mon_details.append(dmqapresrc)
                    if index == 27 and str(item) != "nan" :
            #print(" -DmqaPreDst="+ str(item))
                        dmqpredst=" -DmqaPreDst="+ '"' + str(item) + '"'
                        mon_details.append(dmqpredst)
                    if index == 28 and str(item) != "nan" :
            #print(" -DmqaPostDst="+ str(item))
                        dmqapostdst=" -DmqaPostDst="+ '"' + str(item) + '"'
                        mon_details.append(dmqapostdst)
                    if index == 29 and str(item) != "nan" :
            #print(" -DmqaPostSrc="+ str(item))
                        dmqapostsrc=" -DmqaPostSrc="+ '"' + str(item) + '"'
                        mon_details.append(dmqapostsrc)
                    if index == 30 and str(item) != "nan" :
            #print(" -DmqaDeptName="+ str(item))
                        dmqadeptname=" -DmqaDeptName="+ '"' + str(item) + '"'
                        mon_details.append(dmqadeptname)
                    if index == 31 and str(item) != "nan" : 
            #print(" -DmqaDocType="+ str(item))
                        dmqadoctype=" -DmqaDocType="+ '"' + str(item) + '"'
                        mon_details.append(dmqadoctype)

        
                mon = open("new_monitors.sh", "a")
                #file.write("/opt/mqm/bin/fteAnt -f ./defineMonitor.xml" .join(str(i) for i in mon_details))
                #b="/opt/mqm/bin/fteAnt -f ./defineMonitor.xml" , *mon_details , sep=" " 
                #print(b)
                #print("/opt/mqm/bin/fteAnt -f ./defineMonitor.xml" , *mon_details , sep=" ")
               
                #command=print("/opt/mqm/bin/fteAnt -f ./defineMonitor.xml" , *mon_details , sep=" ")
                #print(str(command))
                a1= "/opt/mqm/bin/fteAnt -f ./defineMonitor.xml"
                #print("Hii")
                
                #print(mon_details) 
                mon.write(a1 + ' '.join(i for i in mon_details) + "\n")
                mon.close()
            #print("Bye")
                
elif state == "exist":
    list3=[]
    for i in data.values:
        #print(i)
        for name in root.iter('name'):
    #l3.append(name.text)
            #print(name.text)
            s=name.text 
            #print(i[2])
            if str(i[2]) == str(s):
                #print("Hello")
                for directory in root.iter('directory'):
                    d=directory.text
                    if str(i[8]) == str(d):
                        #print("directory")
                        pass
                    else:
                        #print(i[2])
                        list3.append(i[2])
                        print("./fteDeleteMonitor -mm" , qm ,"-ma", agent, "-mn", i[2])
                        print('\n')
                        # if str(i[2]) != str(monitor_name):
                #print(m)
                        mon_details=[]
    #print(type(i))
                # if i[2] in list3:
                # print("yes")
                        for index , item in enumerate(i):
        #mon_details=[]
        #print("Hi")
        #if str(i[-1]) != "nan":
        #print(type(item))
                            if index == 0 and str(item) != "nan" :
            #print(" -Dwave="+ str(item) )
                                dwave=" -Dwave="+ '"' + str(item) + '"'
            #print(dwave)
                                mon_details.append(dwave)
                            if index == 1 and str(item) != "nan" :
            #print(" -Dmn="+ str(item))
                                dmn=" -Dmn="+ '"' + str(item) + '"'
                                mon_details.append(dmn)
                            if index == 2 and str(item) != "nan" :
            #print(" -Dnn="+ str(item))
                                dnn=" -Dnn="+ '"' + str(item) + '"'
                                mon_details.append(dnn)
    
    #If cellNumber = 3 Then SetProperty = " -Dnn="
                            if index == 3 and str(item) != "nan" : 
            #print(" -Dmt="+ str(item))
                                dmt=" -Dmt="+ '"' + str(item) + '"'
                                mon_details.append(dmt)
                            if index == 4 and str(item) != "nan" : 
            #print(" -DpostDestC="+ str(item))
                                dpostdestc=" -DpostDestC="+ '"' + str(item) + '"'
                                mon_details.append(dpostdestc)
                            if index == 5 and str(item) != "nan" : 
            #print(" -DpostSrcC="+ str(item))
                                dpostsrcc=" -DpostSrcC="+ '"' + str(item) + '"'
                                mon_details.append(dpostsrcc)
                            if index == 6 and str(item) != "nan" : 
            #print(" -DpreSrcC="+ str(item))
                                dpresrcc=" -DpreSrcC="+ '"' + str(item) + '"'
                                mon_details.append(dpresrcc)
                            if index == 7 and str(item) != "nan" : 
            #print(" -DpreDestC="+ str(item))
                                dpredestc=" -DpreDestC="+ '"' + str(item) + '"'
                                mon_details.append(dpredestc)
                            if index == 8 and str(item) != "nan" : 
            #print(" -Dmd="+ str(item))
                                dmd=" -Dmd="+ '"' + str(item) + '"'
                                mon_details.append(dmd)
                            if index == 9 and str(item) != "nan" : 
            #print(" -Dpt="+ str(item))
                                dpt=" -Dpt="+ '"' + str(item) + '"'
                                mon_details.append(dpt)
                            if index == 10 and str(item) != "nan" : 
            #print(" -Dpi="+ str(item))
                                dpi=" -Dpi="+ '"' + str(item) + '"'
                                mon_details.append(dpi)
                            if index == 11 and str(item) != "nan" :
            #print(" -Dpu=" + str(item))
                                dpu=" -Dpu=" + '"' + str(item) + '"'
                                mon_details.append(dpu)
                            if index == 12 and str(item) != "nan" :
            #print(" -Dsa="+ str(item))
                                dsa=" -Dsa="+ '"' + str(item) + '"'
                                mon_details.append(dsa)
                            if index == 13 and str(item) != "nan" :
            #print(" -Dsm="+ str(item))
                                dsm=" -Dsm="+ '"' + str(item) + '"'
                                mon_details.append(dsm)
                            if index == 14 and str(item) != "nan" :
            #print(" -Dda="+ str(item))
                                dda=" -Dda="+ '"' + str(item) + '"'
                                mon_details.append(dda)
                            if index == 15 and str(item) != "nan" :
            #print(" -Ddm="+ str(item))
                                ddm=" -Ddm="+ '"' + str(item) + '"'
                                mon_details.append(ddm)
                            if index == 16 and str(item) != "nan" :
            #print(" -Ddd="+ str(item))
                                ddd=" -Ddd="+ '"' + str(item) + '"'
                                mon_details.append(ddd)
                            if index == 17 and str(item) != "nan" :
            #print(" -DDPType="+ str(item))
                                ddptype=" -DDPType="+ '"' + str(item) + '"'
                                mon_details.append(ddptype)
                            if index == 18 and str(item) != "nan" :
            #print(" -DDPRcv="+ str(item))
                                ddprcv=" -DDPRcv="+ '"' + str(item) + '"'
                                mon_details.append(ddprcv)
                            if index == 19 and str(item) != "nan" :
            #print(" -DDPSdr=" + str(item))
                                ddpsdr=" -DDPSdr=" + '"' + str(item) + '"'
                                mon_details.append(ddpsdr)
                            if index == 20 and str(item) != "nan" :
            #print(" -Dsd="+ str(item))
                                dsd=" -Dsd="+ '"' + str(item) + '"'
                                mon_details.append(dsd)
                            if index == 21 and str(item) != "nan" :
            #print(" -Dttype="+ str(item))
                                dttype=" -Dttype="+ '"' + str(item) + '"'
                                mon_details.append(dttype)
                            if index == 22 and str(item) != "nan" :
            #print(" -Dsrcdisp="+ str(item))
                                dsrcdisp=" -Dsrcdisp="+ '"' + str(item) + '"'
                                mon_details.append(dsrcdisp)
                            if index == 23 and str(item) != "nan" :
            #print(" -Dexists="+ str(item))
                                dexists=" -Dexists="+ '"' + str(item) + '"'
                                mon_details.append(dexists)
                            if index == 24 and str(item) != "nan" :
            #print(" -DmatchType="+ str(item))
                                dmatchtype=" -DmatchType="+ '"' + str(item) + '"'
                                mon_details.append(dmatchtype)
                            if index == 25 and str(item) != "nan" :
            #print(" -DmqaPreMon="+ str(item))
                                dmqapremon=" -DmqaPreMon="+ '"' + str(item) + '"'
                                mon_details.append(dmqapremon)
                            if index == 26 and str(item) != "nan" :
            #print(" -DmqaPreSrc="+ str(item))
                                dmqapresrc=" -DmqaPreSrc="+ '"' + str(item) + '"'
                                mon_details.append(dmqapresrc)
                            if index == 27 and str(item) != "nan" :
            #print(" -DmqaPreDst="+ str(item))
                                dmqpredst=" -DmqaPreDst="+ '"' + str(item) + '"'
                                mon_details.append(dmqpredst)
                            if index == 28 and str(item) != "nan" :
            #print(" -DmqaPostDst="+ str(item))
                                dmqapostdst=" -DmqaPostDst="+ '"' + str(item) + '"'
                                mon_details.append(dmqapostdst)
                            if index == 29 and str(item) != "nan" :
            #print(" -DmqaPostSrc="+ str(item))
                                dmqapostsrc=" -DmqaPostSrc="+ '"' + str(item) + '"'
                                mon_details.append(dmqapostsrc)
                            if index == 30 and str(item) != "nan" :
            #print(" -DmqaDeptName="+ str(item))
                                dmqadeptname=" -DmqaDeptName="+ '"' + str(item) + '"'
                                mon_details.append(dmqadeptname)
                            if index == 31 and str(item) != "nan" : 
            #print(" -DmqaDocType="+ str(item))
                                dmqadoctype=" -DmqaDocType="+ '"' + str(item) + '"'
                                mon_details.append(dmqadoctype)

        
        
                        print("./all fteAnt -f defineMonitor.xml" , *mon_details , sep=" " )
                        print('\n')
                    #break
                    # for agent in root.iter('agent'):
                    #     a= agent.text
                    #     if str(i[12]) == str(a):
                    #         print("a")
                break
    #print(state)
