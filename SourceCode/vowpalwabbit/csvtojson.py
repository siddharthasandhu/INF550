import csv
import json

csvfile = open('/home/squirrel/Documents/INF 550 Dataset/train.csv', 'r')
jsonfile = open('/home/squirrel/Documents/INF 550 Dataset/train.json', 'w')

fieldnames = ('id','click','hour','C1','banner_pos','site_id','site_domain','site_category','app_id','app_domain','app_category','device_id'\
        ,'device_ip','device_model','device_type','device_conn_type','C14','C15','C16','C17','C18','C19','C20','C21')
reader = csv.DictReader(csvfile,fieldnames)

for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n')
csvfile.close()
jsonfile.close()