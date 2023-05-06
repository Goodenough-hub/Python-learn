def count_words(filename):
    """计算一个文件大致包含多少个单词。"""
    filepath = 'D:\\git\\Python-learn\\Python编程-从入门到实践（第二版）\第一部分 基础知识\\reference\chapter10\\'
    try:
        with open(filepath+filename, encoding="utf-8") as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exits.")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")


filenames = ['alice.txt', 'siddhartha.txt',
             'moby_dick.txt', 'little_women.txt']  # 不存在siddhartha.txt文件
for filename in filenames:
    count_words(filename)
