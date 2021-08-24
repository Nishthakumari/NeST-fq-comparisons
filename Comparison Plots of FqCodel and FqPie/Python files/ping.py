import json
import csv
 
with open('/home/dell/one_tcp_flow fqcodel fqpie ecn on-off/FQ-CoDel-ECN-on-off-comparison/ping-fqcodel-ecn-off.json') as json_file:
    jsondata = json.load(json_file)
 

node_data = jsondata["left-node-0"][0]["10.0.1.1"]

 # First item is the "meta" item with user given information
user_given_start_time = float(node_data[0]["start_time"])

    # "Bias" actual start_time in experiment with user given start time
start_time = float(node_data[1]["timestamp"]) - user_given_start_time


for data in node_data[1:]:
    data["timestamp"] = float(data["timestamp"]) - start_time
        



data_file = open('ping_FQ-CoDel_ECN_disabled.csv', 'w', newline='')
csv_writer = csv.writer(data_file)
 
count = 0
for data in node_data:
    if count == 0:
        count+=1
        continue
    elif count==1:
        header = data.keys()
        csv_writer.writerow(header)
        count += 1
    csv_writer.writerow(data.values())
 
data_file.close()

