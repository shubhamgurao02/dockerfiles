import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
import sys
data_file=sys.argv[1]
data=open(data_file,'r')
data=data.readlines()
import psycopg2

conn = psycopg2.connect(
    dbname="demo",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432"
)
cur = conn.cursor()
for line in data:
        # Split the line into values based on the delimiter
    line=line.strip("\n")
    line=line.replace("None","Null")
    values = line.split(',')  # Assuming comma (,) is the delimiter
    #print(values)
    values=['NULL' if value is None else value for value in values]
    print(values)
        # Insert data into the database
    try:
        cur.execute("""
            INSERT INTO pipeline_runs (pipeline_name, run_id, env, start_time, end_time, status, result, branch, requestor, ci_mode)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """, values)
    except:
        pass
# Commit changes
conn.commit()
cur.close()
conn.close()