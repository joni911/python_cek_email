import imaplib
import threading
import json
from email import message_from_bytes
from email.utils import parsedate_to_datetime
import requests

log_file = "email_log.json"
# kredensial akun email
username = ""
password = ""
site = ""
# fungsi untuk mengecek email
def check_email():
    # koneksi ke server email
    mail = imaplib.IMAP4_SSL(site,993)
    mail.login(username, password)
    mail.select("inbox")

    # cek email masuk
    result, data = mail.search(None, "ALL")
    mail_ids = data[0]
    id_list = mail_ids.split()

    # jika ada email masuk
    # if id_list:
    #     latest_email_id = id_list[-1]
    #     result, data = mail.fetch(latest_email_id, "(RFC822)")
    #     raw_email = data[0][1]
# jika ada email masuk
    if id_list:
        latest_email_id = id_list[-1]
        result, data = mail.fetch(latest_email_id, "(RFC822)")
        email_msg = message_from_bytes(data[0][1])
        
        # membuat json dari email
        no_wa = ""
        pengirim = email_msg["From"]
        prihal = email_msg["Subject"]
        tujuan = email_msg["To"]
        tgl = parsedate_to_datetime(email_msg["Date"]).strftime("%Y-%m-%d %H:%M:%S")
        email_json = {
            "subject": email_msg["Subject"],
            "from": email_msg["From"],
            "to": email_msg["To"],
            "time": parsedate_to_datetime(email_msg["Date"]).strftime("%Y-%m-%d %H:%M:%S"),
            # "body": email_msg.get_payload(decode=True).decode()
        }

        url = ""

        payload = {'number': no_wa, 'message': f"Pengirim: {pengirim}\nPrihal: {prihal}\nTujuan: {tujuan}\nDi terima: {tgl}"}
        
        
        files=[

        ]
        headers = {}

        # cek log
        try:
            with open(log_file, "r") as f:
                email_log = json.load(f)
        except:
            email_log = []

        # jika email belum pernah diterima sebelumnya
        if email_json not in email_log:
            email_log.append(email_json)

            # simpan log
            with open(log_file, "w") as f:
                json.dump(email_log, f)

            # tampilkan isi email
            print(email_json)
           
            response = requests.request("POST", url, headers=headers, data=payload, files=files)
            print(response)
        else:
            print("Email has been received before.")
            
            
    # tutup koneksi
    mail.logout()
    
    # jalankan kembali setelah waktu tertentu
    threading.Timer(60, check_email).start()

# jalankan fungsi
check_email()