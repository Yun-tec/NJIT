import os

path = "D:\南工程\形势与政策\chatGPT生成"
# 遍历path下的所有文件
num = 0
for root, dirs, files in os.walk(path):
    for file in files:
        # 读取每个txt文件
        with open(os.path.join(root, file), "r+", encoding="utf-8") as f:
            # 读取每个txt文件的内容
            content = f.read()

            # 把内容分割成列表
            if content.__contains__("也不要出现陈述性的句子，应该以论证的句子为主") or content.__contains__(
                    "也不要出现陈述性的句子，应该以论证的句子为主") or content.__contains__("也不要出现虚构的故事"):
                num += 1
                print(num)

                # 把列表转换成字符串
                content = content.replace("也不要出现陈述性的句子，应该以论证的句子为主。", "").replace(
                    "也不要出现陈述性的句子，应该以论证的句子为主", "").replace("也不要出现虚构的故事", "")
                # 把列表转换成字符串
                f.truncate(0)
                f.seek(0)
                f.write(content)
                f.close()
