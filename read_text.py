import time
import json
import glob
import pymysql
import datetime
while True:
    # kode Anda di sini
    data = {}

    connection = pymysql.connect(host='localhost',
                                user='root',
                                password='',
                                db='python',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)

    folder_path = "D:\\Pelatihan\\PUSAT\\Y2K\\sms"
    print('start')
    with connection.cursor() as cursor:
        for file_name in glob.glob("D:\Pelatihan\PUSAT\Y2K\sms\[0-9]*.BAT"):
            with open(file_name, "r", encoding='utf-8') as file:
                file_name_key = file_name.split(
                    "D:\\Pelatihan\\PUSAT\\Y2K\\sms\\")[1]
                if file_name_key not in data or data[file_name_key]["status"] != 1:
                    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    sql = "INSERT IGNORE INTO sms (file_name, text, status,time) VALUES (%s, %s, 0,%s)"
                    cursor.execute(sql, (file_name_key, file.read(),timestamp))
                    # data[file_name_key] = {"file": file_name_key, "text": file.read(),"status":0}
                    
            connection.commit()
        for file_name in glob.glob("D:\\Pelatihan\\PUSAT\\Y2K\\sms\\FL*.BAT"):
            with open(file_name, "r", encoding='utf-8') as file:
                file_name_key = file_name.split(
                    "D:\\Pelatihan\\PUSAT\\Y2K\\sms\\")[1]
                if file_name_key not in data or data[file_name_key]["status"] != 1:
                    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    sql = "INSERT IGNORE INTO sms (file_name, text, status,time) VALUES (%s, %s, 0,%s)"
                    cursor.execute(sql, (file_name_key, file.read(),timestamp))
                    # data[file_name_key] = {"file": file_name_key, "text": file.read(),"status":0}
                    
            connection.commit()
    connection.close()

    print('read')
    # with open("SMSdata.json", "w") as json_file:
    #     json.dump(data, json_file)
    # print('write')
    time.sleep(5)

