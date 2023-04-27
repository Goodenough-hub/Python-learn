[TOC]

# 用户输入和 while 循环

本章中，会学习

1. 如何接受用户输入。
2. 如何让程序不断地运行。

## 7.1 函数 input()的工作原理

函数`input()`让程序暂停运行，等待用户输入一些文本，`Python`将其赋给一个变量，以方便使用。

```python
message = input("Tell me something, and I will repeat it back to you: ")
print(message)
```

函数`input()`接受一个参数——要向用户显示的提示（prompt）或说明，让用户知道该如何做。

在本例中，`Python`运行第一行代码时，用户将看到提示`Tell me something, and I will repeat it back to you: `。程序等待用户输入，并在用户按回车键后继续运行。输入被赋值变量`message`，接下来的`print(message)`将输入呈现给用户。

用户输入`Hello everyone!`：

```
Tell me something, and I will repeat it back to you: Hello everyone!
Hello everyone!
```

### 7.1.1 编写清晰的程序

每当使用函数`input()`时，都应指定清晰易懂的提示，准确地指出希望用户提供什么样的信息。

```python
name = input("Please enter your name: ")
print(f"\nHello, {name}!")
```

```
Please enter your name: Eric

Hello, Eric!
```

---

有时候，提示可能会超过一行。可以先将提示赋给一个变量，再将该变量传递给函数`input()`。

```python
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name?"

name = input(prompt)
print(f"\nHello, {name}")
```

```
If you tell us who you are, we can personalize the messages you see.
What is your first name?Eric

Hello, Eric
```

### 7.1.2 使用 int()来获取数值输入

使用函数`input()`时，`Python`将用户输入解读为字符串。不能作为数来使用。

```
>>> age = input("How old are you?")
How old are you?21
>>> age
'21'
>>> type(age)
<class 'str'>
```

若试图将输入用于数值比较时，`Python`会引发错误，字符串无法和整数进行比较。

```
>>> age >= 18
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: '>=' not supported between instances of 'str' and 'int'
```

可使用函数`int()`来解决这个问题。函数`int()`将数的字符串表示转换为数值表示。

```
>>> type(age)
<class 'str'>
>>> age = int(age)
>>> type(age)
<class 'int'>
>>> age >= 18
True
```

---

实际上，可以使用函数`int()`直接读取用户输入的数值。

```python
height = input("How tall are you, in inches? ")
height = int(height)

if height >= 48:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a litte older.")
```

用户输入 71：

```
How tall are you, in inches? 71

You're tall enough to ride!
```

> 1. 将数值输入用户计算和比较前，务必将其转换为数值表示。
>
> 2. `type(a)`函数返回`a`的类型。

### 7.1.3 求模运算符

处理数值信息时，求模运算符(%)是个很好的工具，它将两个数相除并返回余数。

```
>>> 4 % 3
1
>>> 5 % 3
2
>>> 6 % 3
0
>>> 7 % 3
1
```

求余运算符的一个经典用法是判断一个数是奇数还是偶数。

```python
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")
```

用户输入 42：

```
Enter a number, and I'll tell you if it's even or odd: 42

The number 42 is even.
```

## 7.2 while 循环简介

`for`循环用于针对集合中的每个元素都执行一个代码块，而`while`循环则不断运行，直到指定的条件不满足为止。

### 7.2.1 使用 while 循环

可以使用`while`循环来数数。

```python
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
```

```
1
2
3
4
5
```

### 7.2.2 让用户选择何时退出

```python
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(message)
```

```
Tell me something, and I will repeat it back to you:
Enter 'quit' to end the program. Hello everone!
Hello everone!

Tell me something, and I will repeat it back to you:
Enter 'quit' to end the program. Hello again.
Hello again.

Tell me something, and I will repeat it back to you:
Enter 'quit' to end the program. quit
```

### 7.2.3 使用标志

使用一个变量，用于判断整个程序是否处于活动状态。这个变量称为`标志(flag)`。

可以让程序在标志位`True`时继续运行，并在任何事件导致标志的值为`False`时让程序停止运行。这样，在`while`语句中就只需检查一个条件：标志的当前值是否为`True`。

```python
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)
```

标志很有用，在任意一个事件导致活动标志变成`False`时，循环将会退出。

### 7.2.4 使用 break 退出循环

要立即退出`while`循环，不在运行循环中余下的代码，也不管条件测试的结果如何，可使用`break`语句。

`break`语句用于控制程序流程。

```python
prompt = "\nPlease enter the name of a city you have visited: "
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")
```

```
Please enter the name of a city you have visited:
(Enter 'quit' when you are finished.)New York
I'd love to go to New York!

Please enter the name of a city you have visited:
(Enter 'quit' when you are finished.)san francisco
I'd love to go to San Francisco!

Please enter the name of a city you have visited:
(Enter 'quit' when you are finished.)quit
```

> 在任何`Python`循环中都可使用`break`语句。

### 7.2.5 在循环中使用 continue

要返回循环开头，并根据条件测试结果决定是否继续执行循环，可使用`continue`语句。

```python
currrent_number = 0
while currrent_number < 10:
    currrent_number += 1
    if currrent_number % 2 == 0:
        continue # 不再执行下面的代码

    print(currrent_number)
```

打印 10 以内的所有奇数：

```
1
3
5
7
9
```

### 7.2.6 避免无限循环

每个`while`循环都必须有停止运行的途径，这样才不会没完没了地执行下去。

```python
x = 1
while x <= 5:
    print(x)
```

```
1
1
1
1
--snip--
```

若程序陷入无线循环，可按`Ctrl + C`或关闭显示程序输出的终端窗口来退出循环。

## 7.3 使用 while 循环处理列表和字典

要记录大量的用户和信息，需要在`while`循环中使用列表和字典。

`for`循环是一种遍历列表的有效方式，但不应在`for`循环中修改列表，否则将导致`Python`难以跟踪其中的元素。要在遍历列表的同时对其进行修改，可使用`while`循环。通过将`while`循环同列表和字典结合起来使用，可收集、存储并组织大量输入，供以后查看和显示。

### 7.3.1 在列表之间移动元素

```python
# 首先，创建一个待验证用户列表
#   和一个用于存储以验证用户的空列表。
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# 验证每个用户，直到没有未验证用户为止。
#   将每个经过验证的用户都移到已验证用户列表中。
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

# 显示所有已验证的用户。
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user)
```

```
Verifying user: Candace
Verifying user: Brian
Verifying user: Alice

The following users have been confirmed:
candace
brian
alice
```

### 7.3.2 删除为特定值的所有列表元素

第三章中，使用函数`remove()`来删除列表中的特定值。若要删除列表中某个特定元素（有重复），可使用`while`循环。

```python
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:  # 当列表中有cat则执行循环
    pets.remove('cat')

print(pets)
```

```
['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
['dog', 'dog', 'goldfish', 'rabbit']
```

### 7.3.3 使用用户输入来填充字典

```python
respones = {}

# 设置一个标志，指出调查是否继续。
polling_active = True

while polling_active:
    # 提示输入被调查者的名字和回答。
    name = input("\nWhat is your name? ")
    respone = input("Which mountain would you like to climb someday? ")

    # 将回答存储在字典中
    respones[name] = respone

    # 看看是否还有人要参与调查。
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == "no":
        polling_active = False

# 调查结束，显示结果
print("\n--- Poll Results ---")
for name, respone in respones.items():
    print(f"{name} would like to climb {respone}.")
```

`respones`是一个字典，存储`name`和`respone`键值对：

```
What is your name? Eric
Which mountain would you like to climb someday? Denali
Would you like to let another person respond? (yes/no) yes

What is your name? Lynn
Which mountain would you like to climb someday? Devil's Thumb
Would you like to let another person respond? (yes/no) no

--- Poll Results ---
Eric would like to climb Denali.
Lynn would like to climb Devil's Thumb.
```

## 7.4 小结

在本章中，学习了：

1. 如何在程序中使用`input()`来让用户提供信息；
2. 如何处理文本和数的输入，以及如何使用`while`循环让程序按用户的要求不断运行；
3. 多种控制`while`循环流程的方式：设置活动标志、使用`break`语句以及使用`continue`语句；
4. 如何使用`while`循环在列表之间移动元素，以及如何从列表中删除所有包含特定值的元素；
5. 如何结合使用`while`循环和字典。
