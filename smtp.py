import smtplib
s= smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
#Next, log in to the server
s.login("yogi66796@gmail.com", "sainikita")
#Send the mail
msg = "Hello!"
 # The /n separates the message from the headers
s.sendmail("yogi66796@gmail.com","vinodkumarm7.vr@gmail.com", msg)
s.quit()

