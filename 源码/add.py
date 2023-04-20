import pymysql
connect = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    database='article',
    user='root',
    passwd='root',
    charset='utf8')


# 读取sub.txt的每一行
path="E:\PythonProjects\OpenAi\sub.txt"
with open(path,"r",encoding="utf-8") as f:
    split = f.read().split("\n")
    for line in split:
        print(line)
        # 定义SQL -- 查询email是否存在
        sql5 = f"select * from user_article where user_email = '{line}'"
        print(sql5)
        # 获取游标
        cursor = connect.cursor()
        # 执行SQL,并输出结果
        cursor.execute(sql5)
        # 获取所有记录列表
        results = cursor.fetchall()
        if len(results) == 0:
            # 定义SQL -- 插入
            sql6 = f"insert into user_article(user_email) values ('{line}')"
            # 执行SQL
            print(sql6)
            cursor.execute(sql6)
            # 提交到数据库执行
            connect.commit()
            print("插入成功")


