from datetime import datetime

# Original timestamp string
timestamp_string = "2024-01-11T19:37:51.390776857Z"

# Parse the timestamp string into a datetime object
print(timestamp_string.split('.'))
datetime_obj = datetime.strptime(timestamp_string.split('.')[0], '%Y-%m-%dT%H:%M:%S')

# Format the datetime object into the desired time format
formatted_time = datetime_obj.strftime('%Y-%m-%d %H:%M:%S')

# Print the formatted time
print(formatted_time)
