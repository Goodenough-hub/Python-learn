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

---

打印 1~10 的偶数：

```python
even_numbers = list(range(2, 11, 2))
print(even_numbers)
```

```
[2, 4, 6, 8, 10]
```

---

打印前十个整数的平方

```python
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)
```

```
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

### 4.3.3 对数字列表执行简单的统计计算

有几个专门用于处理数字列表的`Python`函数。求数字列表的最大值、最小值和总和。

```
Windows PowerShell
版权所有 (C) 2014 Microsoft Corporation。保留所有权利。

PS D:\git\Python-learn\Python编程-从入门到实践（第二版）> python
Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
>>> min(digits)
0
>>> max(digits)
9
>>> sum(digits)
45
```

### 4.3.4 列表解析

列表解析将`for`循环和创建新元素的代码合并成一行，并自动附加新元素。

创建平方数列表：

```python
squares = [value ** 2 for value in range(1, 11)]
print(squares)
```

结果与之前的平方数列表相同：

```
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

## 4.4 使用列表的一部分

处理列表的部分元素，`Python`称之为切片。

### 4.4.1 切片

要创建切片，可指定要使用的第一个元素和最后一个元素的索引。与函数`range()`一样，`Python`在到达第二个索引之前的元素后停止。

```python
players = ["charles", "martina", "michael", "florence", "eli"]
print(players[0:3])
```

```
['charles', 'martina', 'michael']
```

> 1. 若没有指定第一个索引，`Python`将自动从列表开头开始。
> 2. 若没有指定第二个索引，`Python`终止于列表末尾。
> 3. 可在切片的方括号内指定第三个值，步长。这个值告诉`Python`在指定范围内每隔多少元素提取一个。

### 4.4.2 遍历切片

若要遍历列表的部分元素，可在`for`循环中使用切片。

```python
players = ["charles", "martina", "michael", "florence", "eli"]

print("Here are the first three players on my team:")
for play in players[:3]:
    print(play.title())
```

```
Here are the first three players on my team:
Charles
Martina
Michael
```

### 4.4.3 复制列表

要复制列表，可创建一个包含整个列表的切片，方法是同时省略其实索引和终止索引([:])。这让`Python`创建一个始于第一个元素、终止于最后一个元素的切片，即整个列表的副本。

```python
my_food = ['pizza', 'falafel', 'carrot cake']
friend_food = my_food[:]

print("My favorite foods are:")
print(my_food)

print("\nMy friend's favorite foods are:")
print(friend_food)
```

```
My favorite foods are:
['pizza', 'falafel', 'carrot cake']

My friend's favorite foods are:
['pizza', 'falafel', 'carrot cake']
```

- 这里`my_food`和`friend_food`分别指向两个列表，`friend_food`是`my_food`的副本。

---

```python
my_food = ['pizza', 'falafel', 'carrot cake']

# 这行不通
friend_food = my_food

print("My favorite foods are:")
print(my_food)

print("\nMy friend's favorite foods are:")
print(friend_food)
```

- 这里是将`my_food`赋给`friend_food`，两个变量指向同一个列表。

## 4.5 元组

[Python 元组](https://www.runoob.com/python/python-tuples.html)

列表是可以修改的。`Python`将不能修改的值称为不可变的，而不可变的列表被称为元组。

### 4.5.1 定义元组

元组看起来很像列表，但使用圆括号而非中括号来标识。定义元组后，就可以使用索引来访问其元素，就像访问列表元素一样。

```python
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
```

```
200
50
```

尝试修改元组`dimensions`的一个元素：

```python
dimensions = (200, 50)
dimensions[0] = 250
```

```
  File "d:/git/Python-learn/Python编程-从入门到实践（第二版）/第一部分 基础知识/code/chapter04/dimensions.py", line 2, in <module>
    dimensions[0] = 250
TypeError: 'tuple' object does not support item assignment
```

> 严格来说，元组是由逗号标识的，圆括号只是让元组看起来更加整洁，更清晰。如果你要定义只包含一个元素的元组，必须在这个元素后面加上逗号：
> `my_t = (3,)`
> 创建只包含一个元素的元组通常没有意义，但自动生成的元组有可能只有一个元素。

### 4.5.2 遍历元组中的所有值

像列表一样，也可以使用`for`循环来遍历元组中的所有值：

```python
dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)
```

```
200
50
```

### 4.5.3 修改元组变量

元组中的元素不能修改，但是可以给存储元组的变量赋值。

```python
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
```

```
Original dimensions:
200
50

Modified dimensions:
400
100
```

- 可以将一个新元组关联到变量`dimensions`。给元组变量赋值是合法的。

## 4.6 设置代码格式

使编写的代码易于阅读。

[Python 编码规范(Google)](https://www.runoob.com/w3cnote/google-python-styleguide.html)

### 4.6.1 格式设置指南

要提出`Python`语言修改建议，需要编写`Python`改进提案(`Python Enhancement Proposal, PEP`)。
`PEP 8`是最古老的`PEP`之一，向`Python`程序员提供了代码格式设置指南。`PEP 8`的篇幅很长，基本上与复杂的编码结构有关。

[PEP 8 -- Style Guide for Python Code](https://learnku.com/docs/styleofcode/PEP_8/7084)

### 4.6.2 缩进

`PEP 8`建议每级缩进都使用四个空格。这既提高了可读性，有留下了足够的多级缩进空间。

- 混合使用制表符和空格会让`Python`解释器感到迷惑，这种问题极难排查。
- 每款文本编辑器都提供了一种设置，可将输入的制表符转换为指定数量的空格。

### 4.6.3 行长

约定行长不超过 79 字符。

### 4.6.4 空行

- 要将程序的不同部分分开，可使用空行。
- 空行不会影响代码的运行，但会影响代码的可读性。`Python`解释器根据水平缩进情况来解读代码，但不关心垂直间距。

### 4.6.5 其他格式设置指南

`PEP 8`还有很多其他的格式设置建议，可以阅读`PEP 8`格式设置指南。

## 4.7 小结

1. 如何高效地处理列表中的元素；
2. 如何使用`for`循环遍历列表，`Python`如何根据缩进来确定程序的结构，以及如何避免一些常见的缩进错误；
3. 如何创建简单的数字列表，以及可对数字列表执行的一些操作；
4. 如何通过切片来使用列表的一部分和复制列表；
5. 元组以及如何设置格式。
