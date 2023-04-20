import jieba.analyse as analyse
import jieba.posseg as pseg
# 读取指定txt文本
# 遍历文件夹下的所有文件，读取文件名
import os

# 自定义一个过滤

for root, dirs, files in os.walk("D:\南工程\形势与政策\范文"):
    for file in files:
        # 读取文件内容
        with open(os.path.join(root, file), "r", encoding="utf-8") as f:
            list = []
            tags = analyse.extract_tags(f.read(), topK=20, withWeight=False, allowPOS=())
            # 遍历tags
            for tag in tags:
                word_tags = pseg.cut(tag)
                for tag in word_tags:
                    if tag.flag in ["n", "l", "vn", "nz"]:
                        list.append(tag.word)
        print(list)
        # 将file中的.txt去掉
        file = file.replace(".txt", "")
        # 遍历list
        for tag in list:
            with open(f"D:\南工程\形势与政策\关键词\{file}关键词.txt", "a", encoding="utf-8") as f:
                f.write(tag + ",")

            # pseg_cut = pseg.cut(f.read())
            # for tag in pseg_cut:
            #     if tag.flag in ["n", "l", "vn", "nz"]:
            #         print(tag.word, tag.flag)
            # tags = analyse.extract_tags(f.read(), topK=30, withWeight=False, allowPOS=())
            # # 遍历tags
            # for tag in tags:
            #     cut = pseg.cut(tag)
            #     if cut.flag in ["n", "l", "vn", "nz"]:
            #         print(cut.word, cut.flag)

            # cut = pseg.cut(tags)
            # # 将关键词写入文件
            # for tag in cut:
            #     if tag.flag in ["n", "l", "vn", "nz"]:
            #         print(tag.word, tag.flag)
            # if ".txt" in file:
            #     # 将file中的.txt去掉
            #     file = file.replace(".txt", "")
            # with open(f"D:\南工程\形势与政策\关键词\{file}关键词.txt", "a", encoding="utf-8") as f:
            #     f.write(",".join(tags))
