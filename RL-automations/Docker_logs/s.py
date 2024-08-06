from datetime import datetime, timedelta
i="2023-11-02T09:29:54.165327815Z 2024-02-14 07:12:54.164972: BIP2488E:  (.DeltaInventory_OMS2IA_Rebatch_Loop.Main, 13.4) Error detected whilst executing the SQL statement 'PROPAGATE TO TERMINAL 'out' FINALIZE DEFAULT DELETE DEFAULT;'. "
current_time = datetime.now()
error_code=i.split(' ')[3]
print(error_code)
t=i.split(' ')[2].rstrip(':')
d=i.split(' ')[1].rstrip(':')
time_string=f"{d} {t}"
time_string=datetime.strptime(time_string, '%Y-%m-%d %H:%M:%S.%f')
actual_time=time_string.strftime('%Y-%m-%d %I:%M:%S')
                
past_time = current_time - timedelta(minutes=30)
#print(past_time)
#print(current_time)
#print(past_time.strftime("%Y-%m-%d %I:%M:%S"))
past_time=past_time.strftime("%Y-%m-%d %I:%M:%S")
current_time=current_time.strftime("%Y-%m-%d %I:%M:%S")
print("actual T",actual_time)
print("past",past_time)
print("current",current_time)
if str(current_time) > str(actual_time) > str(past_time):
    print("demo1 line")
                