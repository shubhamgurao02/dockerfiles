import sys
import pandas as pd
# if sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
#     rm_cmd=f"/opt/mqm/bin/fteAnt"
# elif sys.platform.startswith('win'):
#     rm_cmd=f"rmdir /s /q {cloned_folder}"

a1= "/opt/mqm/bin/fteAnt -f ./defineMonitor.xml"
f1= "./fteDeleteMonitor -mm"
f2 = "-ma"
f3 = "-mn"

l2=['Dmn','Dnn','Dmt','DpostDestC','DpostSrcC','DpreSrcC','DpreDestC','Dmd','Dpt','Dpi','Dpu','Dsa','Dsm','Dda','Ddm','Ddd','DDPType','DDPRcv','DDPSdr','Dsd','Dttype','Dsrcdisp','Dexists','DmatchType','DmqaPreMon','DmqaPreSrc','DmqaPreDst','DmqaPostDst','DmqaPostSrc','DmqaDeptName','DmqaDocType']

excel_file =sys.argv[1]
#print(file1)
data=pd.read_excel(excel_file , engine='openpyxl')
data = data.dropna(how='all')
unique_values = data.iloc[:, 2].drop_duplicates()
print(list(unique_values))
#print(list(data.iloc[:, 0].drop_duplicates()))
# empty_cells_indices = data.index[data.iloc[:, 1].isnull()].tolist()
# print(empty_cells_indices)
# if empty_cells_indices:

#     print("Hi")
# for i in data.values:

#     print(i)
