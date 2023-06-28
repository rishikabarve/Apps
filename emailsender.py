import smtplib
to=input("Enter the email of the recipant:\n")
content=input("Enter the content for the mail:\n")
def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com', 166)
    server.ehlo()
    server.starttls()
    server.login("rahbaralam626@gmail.com", '82909585791')
    server.sendmail('rishikabarve8@gmail.com', to , content )
    server.close()
sendEmail(to,content)
    
    
