import pyqrcode

myname = "Parth Shukla\n"
Email_ID = "parthshukla@9ledgepro.com\n"
website = "shuklaparth.com"
Mobile_No = "9599587014"


MYQR = pyqrcode.create(myname+"\n"+Email_ID+"\n"+website+"\n"+Mobile_No)
MYQR.svg("MYDetails.svg")