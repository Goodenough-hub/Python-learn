filepath = 'D:\\git\\Python-learn\\Python编程-从入门到实践（第二版）\\第一部分 基础知识\\reference\\chapter10\\alice.txt'
filename = 'alice.txt'
try:
    with open(filepath, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")
else:
    # 计算该文件大致包含多少个单词。
    words = contents.split()
    num_words = len(words)
    print(f"The file {filename} has about {num_words} words.")
