"""
Step1: Import Package smtplib
Step2: Opening Connection (username,Password)
Step3: Sending mail using Sendmail()
Step4:Close the connection
"""

import smtplib

MyCon = smtplib.SMTP('smtp.gmail.com',587)

MyCon.starttls()

MyCon.login("mani.shukla9lt@gmail.com", "qwerty@1008")

Message ="I hope you are learning new tips and Tricks in python ...!!!"
MyCon.sendmail("mani.shukla9lt@gmail.com","parthshukla@9ledgepro.com",Message)
print("Mail Send Successfully !!!!!!!!!!!")
MyCon.quit()