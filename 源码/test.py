import openai
import send

openai.api_key = ""

path="D:\南工程\形势与政策\关键词"

def generate_ai(prompt):
    response = openai.Completion.create(
        model='text-davinci-003',
        prompt=prompt,
        # 控制随机性
        temperature=0.1,
        # 最大输出,一般除以2为汉字数
        max_tokens=1500,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )

    return response

# ai = generate_ai("根据中国式现代化，生成20个关键词，用,隔开")
# print(ai.choices[0].text)

# 遍历文件夹下所有文件
import os

send.sendEmail("3024322726@qq.com","开始生成关键词","开始生成关键词")
#
# for root, dirs, files in os.walk("D:\南工程\形势与政策\关键词2"):
#     for file in files:
#         with open(os.path.join(root, file), "r", encoding="utf-8") as f:
#             split = f.read().split(",")
#             f.close()
#             # 遍历split
#             for i in range(len(split)):
#
#                     ai = generate_ai(f"根据“{split[i]}”问题，生成15个关键词，用,隔开")
#                     # 保存到文件
#                     split[i]=split[i].replace("\n","")
#                     with open(f"D:\南工程\形势与政策\关键词2\{split[i]}2.txt", "a", encoding="utf-8") as f:
#                         f.write(ai.choices[0].text)
#                         f.close()
#
#
