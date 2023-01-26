import pymysql
import re
import requests
import time

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='python',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
while True:

    with connection.cursor() as cursor:
        # Membaca data dengan status 0
        sql = "SELECT * FROM sms WHERE status = 0"
        cursor.execute(sql)
        data = cursor.fetchall()

        # Melakukan perubahan status menjadi 1
        for row in data:
            string = row['text']
            result = re.search("gammu --sendsms text (\d+) -text \"(.*)\"", string)
            no_hp = result.group(1)
            pesan = result.group(2)
            time.sleep(1)

            
            url = ""

            payload={'number': no_hp,
            'message': pesan}
            files=[

            ]
            headers = {}

            response = requests.request("POST", url, headers=headers, data=payload, files=files)

            print(response.json()["status"])

            sql = "UPDATE sms SET status = 1 WHERE file_name = %s"
            cursor.execute(sql, (row["file_name"]))
            
        connection.commit()
    time.sleep(5)
