import smtplib
from email.mime.text import MIMEText

def send_test():
    sender = "cadtc.larry@gmail.com"
    receiver = "chainchi@gmail.com"
    pw = "vyil pdoc wqhd hjte"
    
    msg = MIMEText("這是一封測試信。")
    msg['Subject'] = "阿琪測試信"
    msg['From'] = sender
    msg['To'] = receiver
    
    try:
        print("連線中...")
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, timeout=10) as server:
            server.login(sender, pw)
            server.sendmail(sender, receiver, msg.as_string())
        print("成功：測試信已寄出！")
    except Exception as e:
        print(f"失敗：{e}")

send_test()
