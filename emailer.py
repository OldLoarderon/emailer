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

# Whereas class must be initiated with pd method foo.iloc[i]
for i in range(len(contacts)):
    email, name, address=contacts.iloc[i]
    port = 143
    #INSERT YOUR SMTP PORT HERE
    smtp_server = "465"

    # Creating mail message using MIMEMultipart
    msg = MIMEMultipart()
    msg['From'] = mycred()[0]
    msg['To'] = email
    msg['Subject'] = "Lorem ipsum"
    body = "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "
    "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur."
    " Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."


    msg.attach(MIMEText(body, 'plain'))
    text = msg.as_string()
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(mycred()[0], password)
        server.sendmail(mycred()[0], msg['To'], text)
    print('Sent to: ', name)
print("The bot finished it's work and ending the process now.")
