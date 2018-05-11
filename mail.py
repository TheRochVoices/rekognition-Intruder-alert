import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders

fromaddr = 'xxxxxxxxxxxxxxxxxx'
toaddr = 'xxxxxxxxxxxxxxxxxx'
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Intruder Alert"
body = "This person was at the wrong place at the wrong time. We though we might let you know"
msg.attach(MIMEText(body, 'plain'))
filename = 'test.jpg'
attachment = open(filename, 'rb')

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
msg.attach(part)
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('xxxxxxxxxxxxxxxxxxx', '**********')
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
