[TOC]

# 操作列表

## 4.1 遍历整个列表

`for`循环打印列表所有元素

```python
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
```

```
alice
david
carolina
```

### 4.1.1 深入研究循环

`Python`从列表中依次取出一个元素。

### 4.1.2 在 for 循环中执行更多操作

```python
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
```

```
Alice, that was a great trick!
David, that was a great trick!
Carolina, that was a great trick!
```

### 4.1.3 在 for 循环结束后执行一些操作

```python
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
print("Thank you, everyone. That was a great magic show!")
```

```
Alice, that was a great trick!
David, that was a great trick!
Carolina, that was a great trick!
Thank you, everyone. That was a great magic show!
```

## 4.2 避免缩进错误

`Python`根据缩进来判断代码行与前一个代码行的关系， 使用缩进让代码整洁而结构清晰。

### 4.2.1 忘记缩进

对于`for`语句后面且属于循环组成部分的代码行，一定要缩进。若忘记缩进，`Python`会提醒。

```python
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
print(magician)
```

```
  File "d:/git/Python-learn/Python编程-从入门到实践（第二版）/第一部分 基础知识/code/chapter04/magicians.py", line 3
    print(magician)
    ^
IndentationError: expected an indented block
```

### 4.2.2 忘记缩进额外的代码行

试图在循环中执行多项任务，却忘记缩进其中的一些代码，可能导致的结果并不符合预期。

```python
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
print(f"I can't wait to see your next trick, {magician.title()}.\n")
```

第二个函数调用`print()`原本需要缩进，但`Python`发现`for`语句后面有一行代码是缩进的，因此没有报告错误。

最终结果是，对于列表中的元素，都执行了第一个函数调用`print()`，因为它缩进了；而第二个函数调用`print()`没有缩进，因此只在循环结束后执行一次。变量`magician`的终值为`carolina`，结果只有她收到了消息`looking forward to the next trick`。

```
Alice, that was a great trick!
David, that was a great trick!
Carolina, that was a great trick!
I can't wait to see your next trick, Carolina.
```

### 4.2.3 不必要的缩进

如果不小心缩进了无需缩进的代码行，`Python`会指出。

```python
message = "Hello Python world!"
    print(message)
```

```
  File "d:/git/Python-learn/Python编程-从入门到实践（第二版）/第一部分 基础知识/code/chapter04/hello_word.py", line 2
    print(message)
    ^
IndentationError: unexpected indent
```

### 4.2.4 循环后不必要的缩进

如果不小心缩进了应在循环结束后执行的代码，这些代码将针对每个列表元素重复执行。在一些情况下，可能会导致`Python`报告语法错误，但大多数情况下，只会导致逻辑错误。

```python
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

    print("Thank you everyone, that was a great magic show!")

```

```
Alice, that was a great trick!
I can't wait to see your next trick, Alice.

Thank you everyone, that was a great magic show!
David, that was a great trick!
I can't wait to see your next trick, David.

Thank you everyone, that was a great magic show!
Carolina, that was a great trick!
I can't wait to see your next trick, Carolina.

Thank you everyone, that was a great magic show!
```

### 4.2.5 遗漏了冒号

`for`语句末尾的冒号告诉`Python`，下一行是循环的第一行。

```python
magicians = ['alice', 'david', 'carolina']
for magician in magicians
    print(magician)

```

遗漏了冒号会导致语法错误。这种错误难以发现。

## 4.3 创建数值列表

列表适合用于存储数字集合，`Python`提供了很多工具，可以帮助你高效地处理数字列表。

### 4.3.1 使用函数 range()

[Python range() 函数用法](https://www.runoob.com/python/python-func-range.html)
`Python`中的函数`range()`让你能够轻松地生成一系列数。

```python
for value in range(1, 5):
    print(value)
```

打印数 1~4。不包含 5。（编程语言中常见的差一行为结果）

```
1
2
3
4
```

> 1. 调用函数`range()`时，也可以只指定一个参数，从 0 开始。例：`range(6)`返回数 0~5。
> 2. `range()`函数还有第三个参数，是步长，默认为 1。例：`range(1, 5, 2)`输出 1，3。

### 4.3.2 使用 range()创建数字列表

要创建数字列表，可使用函数`list()`将`range()`的结果直接转换为列表。如果将`range()`作为`list()`的参数，输出将是一个数字列表。

```python
numbers = list(range(1, 6))
print(numbers)
```

结果如下：

```
[1, 2, 3, 4, 5]
```

### 4.3.3 对数字列表执行简单的统计计算

### 4.3.4 列表解析

## 4.4 使用列表的一部分

### 4.4.1 切片

### 4.4.2 遍历切片

### 4.4.3 复制列表

## 4.5 元组

### 4.5.1 定义元组

### 4.5.2 遍历元组中的所有值

### 4.5.3 修改元组变量

## 4.6 设置代码格式

### 4.6.1 格式设置指南

### 4.6.2 缩进

### 4.6.3 行长

### 4.6.4 空行

### 4.6.5 其他格式设置指南

## 4.7 小结
