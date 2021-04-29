# Python code to illustrate Sending mail from
# your Gmail account
import smtplib

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login("rohitasw1choudhary@gmail.com", "RohitaswChoudhary@2002")

# message to be sent
message = "Hii... Balak!!!!!,  kaisa laga"

# sending the mail

for i in range(100):
    s.sendmail("rohitasw1choudhary@gmail.com", "vishalkumar86032@gmail.com", message)

# terminating the session
s.quit()
