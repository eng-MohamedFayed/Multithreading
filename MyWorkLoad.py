import psutil
import datetime
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

# def send_email(subject, body, attachment_file=0):
#     sender_email = 'madabenten@gmail.com'
#     receiver_email = 'mohamed.fayed@ejust.edu.eg'
#     password = ''
#
#     msg = MIMEMultipart()
#     msg['Subject'] = subject
#     msg['From'] = sender_email
#     msg['To'] = receiver_email
#
#     text = MIMEText(body)
#     msg.attach(text)
#
#
#     #to check if there an attached file
#     if attachment_file !=0:
#         with open(attachment_file, 'rb') as f:
#             part = MIMEApplication(f.read(), Name='workload.txt')
#             part.add_header('Content-Disposition', 'attachment', filename='workload.txt')
#             msg.attach(part)
#
#     with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
#         smtp.starttls()
#         smtp.login(sender_email, password)
# #         # smtp.sendmail(sender_email, receiver_email, msg.as_string())
#         smtp.send_message(msg)
# #         # print("Sent...")
while True:
    cpu_percent = psutil.cpu_percent()
    memory_percent = psutil.virtual_memory().percent
    hdd_percent = psutil.disk_usage('/').percent
    network_io_counters = psutil.net_io_counters()
    
    with open('workload.txt', 'a') as f:
        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        f.write(f'{current_time}:\n* CPU percentage is {cpu_percent}%\n* memory percentage is {memory_percent}%\n* HDD percentage is {hdd_percent}%\n* '
                f'network bytes sent is {network_io_counters.bytes_sent}\n* network bytes received is {network_io_counters.bytes_recv}\n\n\n\n')
    # #an email would be send with the file as an attachment twice, once at 12 am and once at 12 pm
    # if datetime.datetime.now().hour % 12 == 0:
    #     send_email('Workload Report', 'Please see attached file for the workload report.', 'workload.txt')
    # the function will work once every 10 minutes
    time.sleep(10)


    
    
