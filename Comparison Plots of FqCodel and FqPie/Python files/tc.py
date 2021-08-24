import json
import csv
 
with open('/home/dell/one_tcp_flow fqcodel fqpie ecn on-off/FQ-CoDel-ECN-on-off-comparison/tc-fqcodel-ecn-on.json') as json_file:
    jsondata = json.load(json_file)
 

node_data = jsondata["left-router"][0]["ifb-left-router-right-router-0"]["11:"]


    # "Bias" actual start_time in experiment with user given start time
start_time = float(node_data[0]["timestamp"]) - 0


for data in node_data[1:]:
    data["timestamp"] = float(data["timestamp"]) - start_time
        



data_file = open('tc_FQ-CoDel_ECN_enabled.csv', 'w', newline='')
csv_writer = csv.writer(data_file)
 
count = 0
for data in node_data:
    if count == 0:
        header = data.keys()
        csv_writer.writerow(header)
        count += 1
        
    
    csv_writer.writerow(data.values())
 
data_file.close()
