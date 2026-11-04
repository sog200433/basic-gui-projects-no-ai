import smtplib
from datetime import *
from tkinter import *
my_email="sogfuture200433@gmail.com"
password="ntjp xgau pcrb nrgi"



today=date.today()

day_of_week=today.isoweekday()

while day_of_week==1:
    print("email sent succesfully for monday")
    connection=smtplib.SMTP("smtp.gmail.com",587)
    
    connection.starttls()
    connection.login(user=my_email,password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="saw199033@outlook.com",
                        msg="""Subject: Monday\n\n  To spend time is to pass it in a specified manner. To waste time is to expend it thoughtlessly or carelessly.
                               We all have time to either spend or waste, and it is our decision what to do with it. But once passed, 
                               it is gone forever. If you love life, dont waste time, for time is what life is made up of.""")
    connection.close()
    break