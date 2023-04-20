import smtplib
from email.mime.text import MIMEText
from email.header import Header


# 发件人邮箱和密码
def sendEmail(receiver, resubjiect, content):
    sender = '@qq.com'
    password = ''
    # 收件人邮箱
    receiver = receiver
    # 邮件主题和内容
    subject = resubjiect
    content = content
    # 邮件内容
    message = MIMEText(content, 'plain', 'utf-8')
    message['From'] = Header('发件人姓名', 'gbk  ')
    message['To'] = Header('收件人姓名', 'utf-8')
    message['Subject'] = Header(subject, 'utf-8')
    # 发送邮件
    try:
        smtpObj = smtplib.SMTP('smtp.qq.com', 25)
        smtpObj.login(sender, password)
        smtpObj.sendmail(sender, receiver, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException as e:
        print("Error: 无法发送邮件。", e)


# 读取数据库中的邮箱地址，然后发送邮件
import pymysql

connect = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    database='article',
    user='root',
    passwd='root',
    charset='utf8')

path = "D:\南工程\形势与政策\发送目录"
# 遍历path下的文件
import os

for root, dirs, files in os.walk(path):
    for file in files:
        print(file)
        # 读取指定文件内容
        with open(path + "\\" + file, "r", encoding="utf-8") as f:
            content = f.read()
            # 遍历数据库中的邮箱地址，然后发送邮件
            # 定义SQL -- 查询
            sql5 = "select user_email from user_article where status = 0  LIMIT 1"
            # 获取游标
            cursor = connect.cursor()
            # 执行SQL,并输出结果
            cursor.execute(sql5)
            # 获取所有记录列表
            results = cursor.fetchall()
            for row in results:
                email = row[0]
                sendEmail(email, f"{file}对内容不满意，可重新填文档补发", content)
                # 更新状态
                sql6 = f"update user_article set status = 1 where user_email = '{email}'"
                cursor.execute(sql6)
                connect.commit()
                print("更新成功")
