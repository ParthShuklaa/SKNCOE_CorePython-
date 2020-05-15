"""

Step1:Import Package SMTPlib
Step2: OPen Connection (Gmail/Hotmail)(username, Password
Step3: open connection in secure way (SSL/TLS)
Step4: Send mail(User name , Sender Add, Message)
Step5: Close connection


"""

import smtplib
con = smtplib.SMTP('smtp.gmail.com',587)
con.login("manishukla9lt@Gmail.com","Qwerty@1008")
con.starttls()
message = " I hope you are learning new tips and Tricks in python ..."
con.sendmail("manishukla9lt@Gmail.com","parthshukla@9ledgepro.com",msg = message)
print("mail Sent sucessfully ......")
con.close()