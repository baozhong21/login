import os
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMultiAlternatives

def SendMail(email, code):
    subject = '来自www.IOT.com的注册确认邮件'
    text_content = '''感谢注册www.IOT.com，\
                    如果你看到这条消息，说明你的邮箱服务器不提供HTML链接功能，请联系管理员！'''
    html_content = '''
                    <p>感谢注册<a href="http://{}/confirm/?code={}" target=blank>www.baidu.com</a>，\
                    这里是鲍中的站点</p>
                    <p>请点击站点链接完成注册确认！</p>
                    <p>此链接有效期为{}天！</p>
                    '''.format('127.0.0.1:8000', code, settings.CONFIRM_DAYS)
    msg = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, [email])
    msg.attach_alternative(html_content, "text/html")
    msg.send()