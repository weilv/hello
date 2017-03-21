# coding=utf-8
# 格式转成 utf-8
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(( \
        Header(name, 'utf-8').encode(), \
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))

def sendEmail(email, content):


    # 你的邮箱
    from_addr = 'shychenglove@163.com'

    # 你的授权码，注意了，大写的注意，不是你邮箱的登录密码，是授权码
    password = 'qymxc871123'

    # 你要发送到的邮箱
    to_addr = email

    # 163 的 smtp 服务器
    smtp_server = 'smtp.163.com'

    msg = MIMEText(content, 'plain', 'utf-8')
    msg['From'] = _format_addr(u'叫我亲爱的 <%s>' % from_addr)
    msg['To'] = _format_addr(u'亲爱的 <%s>' % to_addr)
    msg['Subject'] = Header(u'这里是资讯推送！', 'utf-8').encode()

    # 连接服务器，163的smtp端口号，为25
    server = smtplib.SMTP(smtp_server, 25)

    server.set_debuglevel(1)

    # 登录邮箱
    server.login(from_addr, password)

    # 发送邮件
    server.sendmail(from_addr, [to_addr], msg.as_string())

    # 退出服务器
    server.quit()

sendEmail('329579453@qq.com','测试封装是否成功')