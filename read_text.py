import os
import json
import glob

data = {}

folder_path = "G:\\Program Kantor\\Y2K PUSAT\\Y2K\\SMS"
print('start')
for file_name in glob.glob("G:\\Program Kantor\\Y2K PUSAT\\Y2K\\SMS\\FL*.BAT"):
    with open(file_name, "r", encoding='utf-8') as file:
        file_name_key = file_name.split(
            "G:\\Program Kantor\\Y2K PUSAT\\Y2K\\SMS\\")[1]
        if file_name_key not in data or data[file_name_key]["status"] != 1:
            data[file_name_key] = {"file": file_name_key, "text": file.read(),"status":0}
print('read')
with open("SMSdata.json", "w") as json_file:
    json.dump(data, json_file)
print('write')
