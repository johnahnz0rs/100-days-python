import smtplib
my_email = "johnahnz0rsisl33t@yahoo.com"
my_password = "l33th4x0rsOMGwtf!!"


connection = smtplib.SMTP("smtp.mail.yahoo.com")
connection.starttls()
connection.login(user=my_email, password=my_password)
connection.sednmail(from_addr=my_email, to_addrs="johnahn123@gmail.com", msg="Subject:Hello\n\nhelloworld")
connection.close()