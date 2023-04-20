# 遍历文件夹下所有文件
import os
# 生成随机数
import random
import openai

openai.api_key = ""
from jieba import analyse


# 定义一个方法，用于生成标题，参数为一句话,且有返回值
def generate_ai(prompt):
    response = openai.Completion.create(
        model='text-davinci-003',
        prompt=prompt,
        # 控制随机性
        temperature=0.9,
        # 最大输出,一般除以2为汉字数
        max_tokens=1500,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )
    return response


# for循环两次
for i in range(2):
    # 系统时间
    path = "D:\南工程\形势与政策\关键词"
    for root, dirs, files in os.walk(path):
        for file in files:
            # 读取每个txt文件
            with open(os.path.join(root, file), "r", encoding="utf-8") as f:
                split = f.read().split("、")
                print(split)
                f.close()
                # 随机生成三个不同的数字
                random_num1 = random.randint(0, len(split) - 1)
                random_num2 = random.randint(0, len(split) - 1)
                random_num3 = random.randint(0, len(split) - 1)
                print(random_num1, random_num2, random_num3)
                # 检查三个随机数是否有重复
                while split[random_num1] == split[random_num2] or split[random_num1] == split[random_num3] or split[
                    random_num2] == split[random_num3]:
                    random_num1 = random.randint(0, len(split) - 1)
                    random_num2 = random.randint(0, len(split) - 1)
                    random_num3 = random.randint(0, len(split) - 1)
                # 生成标题
                titile = f" 我将以{file}为主题，{split[random_num1]}和{split[random_num2]}和{split[random_num3]}为关键词，写一篇论文，请帮我拟个标题"
                print("等待生成标题")
                titile = generate_ai(titile).choices[0].text.replace("\n", "")
                titile = titile.replace("。", "").replace("：", "").replace(":", "").replace("？", "").replace("、",
                                                                                                            "").replace(
                    "《", "").replace("》", "")

                abstract = f" 我将以{file}为主题，{split[random_num1]}和{split[random_num2]}和{split[random_num3]}为关键词，写一篇论文，请帮我拟个200字到300字的摘要   "
                print("等待生成摘要")
                abstract = generate_ai(abstract).choices[0].text
                abstract = f"摘要：{abstract}"

                keyword = f" 关键词：{split[random_num1]} {split[random_num2]} {split[random_num3]}"

                body1 = f"以{file}为主题，{split[random_num1]}为关键词，用中文写一篇450字到500字的论文，并给出不超过15个字的标题，标题格式“一、标题”。论文内容不要出现二级标题。内容里不要出现首先，然后，此外，因此，其次，总之等总结性的词语"
                print("等待生成正文")
                body1 = generate_ai(body1).choices[0].text

                body2 = f"以{file}为主题，以{split[random_num2]}为主题，用中文写一篇450字到500字的论文，并给出不超过15个字的标题，标题格式“二、标题”。论文内容不要出现二级标题。内容里不要出现首先，然后，其次，总之等总结性的词语"
                print("等待生成正文")
                body2 = generate_ai(body2).choices[0].text

                body3 = f"以{file}为主题，以{split[random_num3]}为主题，用中文写一篇450字到500字的论文，并给出不超过15个字的标题，标题格式“三、标题”。论文内容不要出现二级标题。内容里不要出现首先，然后，此外，因此，其次，总之等总结性的词语"
                print("等待生成正文")
                body3 = generate_ai(body3).choices[0].text

                bibliography = f"我将以{file}为主题，{split[random_num1]}和{split[random_num2]}和{split[random_num3]}为关键词，写一篇论文，请帮我找三至五个中文参考文献，文章发表时间是2018到2022年之间的"
                print("等待生成参考文献")
                bibliography = generate_ai(bibliography).choices[0].text
                bibliography = f"参考文献：{bibliography}"

                # 得到时间
                import time

                time = time.time()
                file = file.replace(".txt", "")
                # 保存到文件
                with open(f"D:\南工程\形势与政策\chatGPT生成\{file}_{titile}_{time}.txt", "a", encoding="utf-8") as f:
                    f.write(titile + "\r\n")
                    f.write(abstract + "\r\n")
                    f.write(keyword + "\r\n")
                    f.write(body1 + "\r\n")
                    f.write(body2 + "\r\n")
                    f.write(body3 + "\r\n")
                    f.write(bibliography)
