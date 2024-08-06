import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
import sys
token ="FdJgPSEBXoHOE5O6RYzIcZm8st3FtmYJEdt1XVFVjIuuAlE-G3-aTm60oka9lJIvzcWMQ_0iPsle9Y19yjvqzg==" #"kVxsoy9vWKCUkhXlchybbsoC7qe7Z886mVcgUT6v8aNWghvUIEag9DwBwA2TltSGYJokEioAvRFhFjyTwUP4Aw=="
org = "Prolifics"
url = "http://192.168.1.39:8086"
data_file=sys.argv[1]
data=open(data_file,'r')
data=data.readlines()
client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)
bucket="demo"

write_api = client.write_api(write_options=SYNCHRONOUS)

for value in data:
    values=value.split(",")
    point = Point("pipeline_runs") \
    .tag("pipeline_name", values[0]) \
    .field("run_id", int(values[1])) \
    .tag("env", values[2]) \
    .field("start_time", values[3]) \
    .field("end_time", values[4]) \
    .tag("state", values[5]) \
    .tag("result", values[6]) \
    .tag("branch", values[7]) \
    .tag("requestor", values[8]) \
    .tag("ci_mode", values[9])
    write_api.write(bucket=bucket, org="Prolifics", record=point)
