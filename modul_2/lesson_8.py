# import smtplib
#
# host = 'smtp.gmail.com'
# port = 465
# email = 'tannagashevalisher07@gmail.com'
# email1 = 'abdunabiyevjavlon731@gmail.com'
# password = 'cjnljtiexucjhqpe'
# # 'cjnljtiexucjhqpe'
# msg = 'Yetqizing manga sherbekligizni!'
# with smtplib.SMTP_SSL(host, port) as server:
#     server.login(email, password)
#     server.sendmail(email, email1, msg)
#     print('send to email!')
# with open('python.png', 'rb') as f:
#     data = f.read()
#
# with open('rasm.txt', 'w') as f:
#     f.write(data)

import base64
# text, binary


# # # image->text
# with open('img_1.png', 'rb') as f:
#     data = f.read()
#     data = base64.b64encode(data).decode('utf-8')
#
# with open('data.txt', 'w') as f:
#     f.write(data)


# text->image


# with open('noname.txt') as f:
#     d = f.read()
#     d = base64.b64decode(d)
#     with open('../rasm.png', 'wb') as file:
#         file.write(d)


import smtplib
from email.message import EmailMessage

port = 465
host = 'smtp.gmail.com'
email = 'tannagashevalisher07@gmail.com'
password = 'cjnljtiexucjhqpe'

to_email = 'akhmadjonovr.98@gmail.com'

msg = EmailMessage()
msg["Subject"] = "File yuborish"
msg["From"] = email
msg["To"] = to_email

with open("data.txt") as fp:
    msg.add_attachment(fp.read(), subtype="txt")


with smtplib.SMTP_SSL(host, port) as server:
    server.login(email, password)
    server.send_message(msg)
    print('rasm ketti')