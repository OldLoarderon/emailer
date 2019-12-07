from tkinter import *
from tkinter import ttk
import pandas as pd
import smtplib, ssl
from email.mime.multipart import  MIMEMultipart
from email.mime.text import MIMEText
from emailer.py import *

root=Tk()
root.title("Mawu's Email sender")
mainframe = ttk.Frame(root, padding = "3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


email = StringVar()
name = StringVar()


mail_entry = ttk.Entry(mainframe
