import smtplib

sender_email = "zacneley@gmail.com"
receiver_email = "zikourouatbi@gmail.com"
password = "wjujxoyppdroalqn"
message = "Subject: A Test Mail\n\nThis is a test email sent using Python smtplib library."

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(sender_email, password)
server.sendmail(sender_email, receiver_email, message)
server.quit()

