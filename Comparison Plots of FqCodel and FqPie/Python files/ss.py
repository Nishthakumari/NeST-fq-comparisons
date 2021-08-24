import json
import csv
 
with open('ss_copy.json') as json_file:
    jsondata = json.load(json_file)
 

node_data = jsondata["left-node-0"][0]["10.0.1.1"]["36437"]

 # First item is the "meta" item with user given information
user_given_start_time = float(node_data[0]["start_time"])

    # "Bias" actual start_time in experiment with user given start time
start_time = float(node_data[1]["timestamp"]) - user_given_start_time


for data in node_data[1:]:
    data["timestamp"] = float(data["timestamp"]) - start_time
        



data_file = open('ss_json_copy.csv', 'w', newline='')
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

