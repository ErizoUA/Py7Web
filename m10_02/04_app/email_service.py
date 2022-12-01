import smtplib


def send_email(email_from, email_target, message):
    with smtplib.SMTP('localhost', 1025) as server:
        server.sendmail(email_from, email_target, message.encode('utf-8'))


if __name__ == '__main__':
    send_email('info@roga_copyta.com.ua', 'yuri@meta.ua', 'By!!!111')

# Старт Email Server в режимі debug
#  py -m smtpd -c DebuggingServer -n localhost:1025
