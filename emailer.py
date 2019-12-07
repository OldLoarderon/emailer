import os
import pandas as pd
import  smtplib, ssl
from email.mime.multipart import  MIMEMultipart
from email.mime.text import MIMEText
from secrets import mycred

# ''' Pandas connection to DB, reading info from excel sheet, then connecting to SMTP'''

file = pd.read_excel('email_DB.xlsx', sheet_name = 'Sheet1')
contacts=pd.DataFrame(file)
password = mycred()[1]

for i in range(len(contacts)):
    email, name, address=contacts.iloc[i]
    port = 143
    #INSERT YOUR SMTP PORT HERE
    smtp_server = "465"

    # Creating mail message
    msg = MIMEMultipart()
    msg['From'] = mycred()[0]
    msg['To'] = email
    msg['Subject'] = "YCA FV 11/2019r"
    body = "Dzień dobry,"

"W załączeniu faktura za zajęcia w listopadzie."
"Jednocześnie będę wdzięczny za kilka słów, czy jest Pani zadowolona z realizacji i przebiegu moich zajęć"


"Serdecznie pozdrawiam,"
"""
"<br>"
"""
"Jan Mawusi"
"Chief Operations Officer\Tutor"
"+48 534 530 322"
"""
<a href="https://www.facebook.com/codersYoung"><img alt="Young Coders Academy Facebook Page" src="https://i.imgur.com/eJhxC4p.png" width="150" height="40"></a>
"""

# Whereas class kiddos must be initiated with pd method foo.iloc[i]

    msg.attach(MIMEText(body, 'plain'))
    text = msg.as_string()
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(mycred()[0], password)
        server.sendmail(mycred()[0], msg['To'], text)
    print('Sent to: ', name)
print("The bot finished it's work and ending the process now.")
