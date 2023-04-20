import openai

openai.api_key = ""
# 备用key


def generate_ai(prompt):
    response = openai.Completion.create(
        # 写作模型
        model='text-davinci-003',
        prompt=prompt,
        # 控制随机性
        temperature=0.5,
        # 最大输出,一般除以2为汉字数
        max_tokens=4000,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )

    return response


ai = generate_ai("以可见光未来市场为题，写100字介绍发展前景和发展趋势")
print(ai.choices[0].text)
