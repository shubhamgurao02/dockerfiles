#!/bin/sh
######### PREDEFINE VARIABLES ##########################################
min_value=10
threshold_value=20
state="Running"
env=$1
user_name=$2
time_date=`date`
host_name=`hostname`
mail_from=`echo "$2@$host_name.localdomain"`
receipents="ravi.punnana@stonex.com"
smtp_server="apps-outbound.fcstone.com"
smtp_port=25
subject_line="[$env]-Health Check Status-$host_name-$time_date"

#########################ARRAY##########################################
qm_name=()
qm_state=()
ch_status=()
q_status=()
mem_type=()
mem_total=()
mem_used=()
mem_free=()
mem_shared=()
mem_cache=()
mem_available=()

disk_filesystem=()
disk_size=()
disk_used=()
disk_avail=() 
disk_use=() 
disk_mounted=()

fdc_permissions=()
fdc_owner=()
fdc_group=()
fdc_size=()
fdc_mtime=()
fdc_file=()

###################TOP COMMAND OUTPUT ###############
echo "Collecting details about Processes"
top_details=`top -c -bn 1 > health_check_top.txt`
top_state=`echo $?`

if [ $top_state -eq 0 ] ; then
echo "Process data collected"
else
echo "Something wrong"
fi
###################FREE COMMAND OUTPUT ###############
echo "Collecting RAM/SWAP memory Status"
mem_status=`free -g | awk 'NR > 1'`
while IFS= read -r mem; do
    #echo "Current line: $mem"
    m_type=`echo $mem | awk '{print $1}' `
    m_total=`echo $mem | awk '{print $2}' `
    m_used=`echo $mem | awk '{print $3}' `
    m_free=`echo $mem | awk '{print $4}' `
    m_shared=`echo $mem | awk '{print $5}' `
    m_cache=`echo $mem | awk '{print $6}' `
    m_available=`echo $mem | awk '{print $7}' `
    mem_type+=("$m_type")
    mem_total+=("$m_total")
    mem_used+=("$m_used")
    mem_free+=("$m_free")
    mem_shared+=("$m_shared")
    mem_cache+=("$m_cache")
    mem_available+=("$m_available")
done <<< "$mem_status"
###################df -h COMMAND OUTPUT ###############

echo "Collecting disk stats"
disk_stat=`df -h | awk 'NR > 1'`

while IFS= read -r disk; do
    #echo "Current line: $disk"
    d_filesystem=`echo $disk|awk '{print $1}'`
    d_size=`echo $disk|awk '{print $2}'`
    d_used=`echo $disk|awk '{print $3}'`
    d_avail=`echo $disk|awk '{print $4}'` 
    d_use=`echo $disk|awk '{print $5}'` 
    d_mounted=`echo $disk|awk '{print $6}'`
    
    disk_filesystem+=("$d_filesystem")
    disk_size+=("$d_size")
    disk_used+=("$d_avail")
    disk_avail+=("$d_use") 
    disk_use+=("$d_use") 
    disk_mounted+=("$d_mounted")
done <<< "$disk_stat"
###################QMGR HEALTHCHECK ###############
echo "Collecting QMGR healthcheck detils"

qmgr=`dspmq`
while IFS= read -r line; do
    #echo "Current line: $line"
    qmgr_name=`echo "$line"|awk '{print $1}' | grep -oE '\([^)]+\)' | sed 's/[(|)]//g'`
    qmgr_state=`echo "$line"|awk '{print $2}' | grep -oE '\([^)]+\)' | sed 's/[(|)]//g'`
    channel_status=`echo "display chstatus(*)" | runmqsc $qmgr_name|grep -iv -e "IBM Corp." -e "commands" -e "command"` 
    queue_status=`echo "dis ql(*) WHERE (CURDEPTH GT 100)" | runmqsc $qmgr_name | grep -iv -e "IBM Corp." -e "commands" -e "command"` 
    qm_name+=("$qmgr_name")
    qm_state+=("$qmgr_state")
    ch_status+=("$channel_status")
    q_status+=("$queue_status")
done <<< "$qmgr"

####################################################################################################
########################################FDC Logs ###################################################
fdc_logs=`ls -ltr /var/mqm/errors|awk 'NR > 1'`
fdc_perm=`echo $fdc_logs|awk '{print $1}'`
fdc_owner=`echo $fdc_logs|awk '{print $3}'`
fdc_group=`echo $fdc_logs|awk '{print $4}'`
fdc_size=`echo $fdc_logs|awk '{print $5}'`
fdc_mtime=`echo $fdc_logs|awk '{print $6,$7,$8}'`
fdc_file=`echo $fdc_logs|awk '{print $9}'`

fdc_permissions+=("$fdc_perm")
fdc_owner+=("$fdc_owner")
fdc_group+=("$fdc_group")
fdc_size+=("$fdc_size")
fdc_mtime+=("$fdc_mtime")
fdc_file+=("$fdc_file")

######################################################################################################
body=$(cat <<'EOF'
<!DOCTYPE html>
<html>
<head>
<style>
table, th, td {
  border: 1px solid black;
}
</style>
</head>
<body>
<h3> RAM/SWAP memory Status</h3>
<table>
<tr>
<th>Memmory Type</th>
<th>Memmory Total</th>
<th>Memmory Used</th>
<th>Memmory Free</th>
<th>Memmory Shared</th>
<th>Memmory Cache</th>
<th>Memmory Available</th>
</tr>
EOF
)

for ((i = 0; i < ${#mem_type[@]}; i++)); do
    body+="<tr><td>${mem_type[$i]}</td><td>${mem_total[$i]}</td><td>${mem_used[$i]}</td><td>${mem_free[$i]}</td><td>${mem_shared[$i]}</td><td>${mem_cache[$i]}</td><td>${mem_available[$i]}</td></tr>"
done

body+=$(cat <<'EOF'
</table>
<br>
<h3> Disk memory Status</h3>
<table>
<tr>
<th>Filesystem</th>
<th>Size</th>
<th>Used Space</th>
<th>Space Available</th>
<th>Used in Percentage</th>
<th>Mounted</th>
</tr>
EOF
)

for ((i = 0; i < ${#disk_filesystem[@]}; i++)); do
    used_space=$(echo ${disk_use[$i]} | tr -d '%')

    if [ "$used_space" -ge "$threshold_value" ] ; then
        body+="<tr><td>${disk_filesystem[$i]}</td><td>${disk_size[$i]}</td><td>${disk_used[$i]}</td><td>${disk_avail[$i]}</td><td bgcolor='red'>${disk_use[$i]}</td><td>${disk_mounted[$i]}</td></tr>"
    elif [ "$used_space" -ge "$min_value" ] && [ "$used_space" -lt "$threshold_value" ] ; then
        body+="<tr><td>${disk_filesystem[$i]}</td><td>${disk_size[$i]}</td><td>${disk_used[$i]}</td><td>${disk_avail[$i]}</td><td bgcolor='yellow'>${disk_use[$i]}</td><td>${disk_mounted[$i]}</td></tr>"
    else
        body+="<tr><td>${disk_filesystem[$i]}</td><td>${disk_size[$i]}</td><td>${disk_used[$i]}</td><td>${disk_avail[$i]}</td><td>${disk_use[$i]}</td><td>${disk_mounted[$i]}</td></tr>"
    fi
done

body+=$(cat <<'EOF'
</table>
<br>
<h3> Queue Manager Status</h3>
<table>
<tr>
<th>Queue Manager Name</th>
<th>State</th>
<th>Channel status</th>
<th>Queue status</th>
</tr>
EOF
)

for ((i = 0; i < ${#qm_name[@]}; i++)); do
    if [ "${qm_state[$i]}" == "$state" ] ; then
        body+="<tr><td>${qm_name[$i]}</td><td>${qm_state[$i]}</td><td>${ch_status[$i]}</td><td>${q_status[$i]}</td></tr>"
    else
        body+="<tr><td>${qm_name[$i]}</td><td bgcolor='red'>${qm_state[$i]}</td><td>${ch_status[$i]}</td><td>${q_status[$i]}</td></tr>"
    fi
done

body+=$(cat <<'EOF'
</table>
<br>
<h3> FDC error logs file status</h3>
<table>
<tr>
<th>Permission</th>
<th>File owner</th>
<th>Group</th>
<th>Size</th>
<th>Modification Time</th>
<th>Filename</th>
</tr>
EOF
)

for ((i = 0; i < ${#fdc_permissions[@]}; i++)); do
    body+="<tr><td>${fdc_permissions[$i]}</td><td>${fdc_owner[$i]}</td><td>${fdc_group[$i]}</td><td>${fdc_size[$i]}</td><td>${fdc_mtime[$i]}</td><td>${fdc_file[$i]}</td></tr>"
done

body+="</table><br></body></html>"

python -c "import smtplib; from email.mime.text import MIMEText; msg = MIMEText('''$body''', 'html'); msg['Subject'] = '''$subject_line'''; msg['From'] = '''$mail_from'''; msg['To'] = '''$receipents''' ; server = smtplib.SMTP('''$smtp_server''', '''$smtp_port'''); server.sendmail('''$mail_from''', '''$receipents''', msg.as_string()); server.quit()"
#python3 -c "import smtplib; from email.mime.text import MIMEText; from email.mime.multipart import MIMEMultipart; body='$body'; subject_line='$subject_line'; mail_from='$mail_from'; receipents='$receipents'; smtp_server='$smtp_server';smtp_port='$smtp_port' msg = MIMEMultipart(); msg.attach(MIMEText(body, "html")); msg['Subject'] = subject_line; msg['From'] = mail_from; msg['To'] = receipents; server = smtplib.SMTP(smtp_server, smtp_port); server.sendmail(mail_from, receipents.split(), msg.as_string()); server.quit()"
