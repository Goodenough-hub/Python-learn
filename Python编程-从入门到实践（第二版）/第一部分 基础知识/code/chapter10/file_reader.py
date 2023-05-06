filename = 'D:\git\Python-learn\Python编程-从入门到实践（第二版）\第一部分 基础知识\code\chapter10\pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
