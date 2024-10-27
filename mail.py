import smtplib
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('m.velmuruga95@gmail.com','svbsbthgwccucxot')
server.sendmail('m.velmuruga95@gmail.com','muruganveltvl@gmail.com','HEllo')
print('sended')
