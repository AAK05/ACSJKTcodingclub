from email.message import EmailMessage
import os
import mimetypes
import smtplib

#Define sender email
sender = "aak.automated@aol.com"

#Initialize emailmessage object
message =  EmailMessage()

#Message headers are set as sender, receiver, subject
message["From"] = sender
message["To"] = ["s2017.student.adrien.kusuma@acsjakarta.sch.id","adrien.kusuma@gmail.com"]
message["subject"] = "Test Email"

#Message body is separate from headers such as From, To, Subject
body = """Hello!

This is a test email to try sending through python.
If you receive this, then it worked!
Attached is a jpg image of raja ampat, to test email attachments.

Adrien"""
#Use the .set_content() method on the EmailMessage object to determine the email body.
message.set_content(body)

#Adding attachments
attachment_path = "C:\\Users\\Adrien\\OneDrive\\Documents\\Python\\Learning\\e-mail\\DJI_0148.JPG"
attachment_path_mac = "/Users/Adrien/Documents/Python/ACSJKTcodingclub/Python/teaching/e-mail/DJI_0148.JPG"
attachment_file = os.path.basename(attachment_path)
print(str(attachment_file))
mime_type_subtype , _ = mimetypes.guess_type(attachment_path) #guess_type returns a tuple, but only index 0 relevant
print(mime_type_subtype)
mimetype,subtype = mime_type_subtype.split("/",1) #separate into type and subtype
attachment_file_mac = os.path.basename(attachment_path_mac)
#print(str(attachment_file))
#print(mimetype,subtype)
try:
    with open(attachment_path,"rb") as ap:
        message.add_attachment(ap.read(), maintype=mimetype,subtype=subtype,filename=attachment_file)
except:
    with open(attachment_path_mac,"rb") as ap:
        message.add_attachment(ap.read(), maintype=mimetype,subtype=subtype,filename=attachment_file_mac)

#print(message)

#Remote SMTP send
mail_server = smtplib.SMTP_SSL("smtp.aol.com") #Make sure to use the correct smtp server
#mail_server.set_debuglevel(1)
#Defining pwd
#pwd = getpass.getpass("Password? ")
#logging in
mail_server.login(sender,"rrberrahkzuznkbc")
fail = mail_server.send_message(message)
mail_server.quit()
#print(fail)