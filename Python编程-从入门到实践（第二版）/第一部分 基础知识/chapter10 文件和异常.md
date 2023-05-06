[TOC]

# 文件和异常

在本章中，将会学习

1. 处理文件，让程序能够快速地分析大量数据；
2. 错误处理，避免程序在面对意外情形时崩溃；
3. 异常，它们是`Python`创建的特殊对象，用于管理程序运行时出现的错误；
4. 模块`json`，它让你能够保存用户数据，以免在程序停止运行后丢失。

## 10.1 从文件中读取数据

每当需要分析或修改文件中的信息时，读取文件都很有用，对数据分析应用程序来说尤其如此。

要使用文本文件中的信息，首先需要将信息读取到内存中。可以一次性读取文件的全部内容，也可以每次一行的方法逐步读取。

### 10.1.1 读取整个文件

读取这个文件，再将其内容显示到屏幕上：

```python
with open('D:\git\Python-learn\Python编程-从入门到实践（第二版）\第一部分 基础知识\code\chapter10\pi_digits.txt') as file_object:
    contents = file_object.read()

print(contents)
```

- 函数`open()`
  打开文件。函数`open()`接受一个参数：要打开的文件的名称。`Python`在当前执行的文件所在的目录中查找指定的文件。函数`open()`返回返回一个表示文件的对象。
- 关键字`with`
  在不再需要访问文件后将其关闭。
- `read()`方法
  读取这个文件的全部内容，并将其作为一个长长的字符串赋给变量`contents`。通过打印`contents`的值，就可将这个文本文件的全部内容显示出来。

```
3.1415926535
8979323846
2643383279
```

### 10.1.2 文件路径

1. 相对路径
   相对文件路径让`Python`到指定的位置去查找，而位置是相对于当前运行的程序所在的目录的。
2. 绝对路径
   将文件在计算机中的准确位置告诉`Python`。

> 绝对路径通常比相对路径长，因此将其赋值给一个变量。
> 通常使用绝对路径，可读取系统中任何地方的文件。就目前而言，最简单的做法是，要么将数据文件存储在程序文件所在的目录，要么将其存储在程序文件所在目录下的一个文件夹中。
> 显示文件路径时，`Windows`系统使用反斜杆（\），而不是斜杆（/），但在代码中依然可以使用斜杆。
> 若在文件路径中直接使用反斜杠，将引发错误，因为反斜杠用于对字符串中的字符进行转义。如果一定要使用反斜杠，可对路径中的每个反斜杠都进行转义（\\）。

### 10.1.3 逐行读取

读取文件时，常常需要检查其中的每一行：可能要在文件中查找特定的信息，或者要以某种方式修改文件中文本。

要以每次一行的方式检查文件，可对文件对象使用`for`循环：

```python
filename = 'D:\git\Python-learn\Python编程-从入门到实践（第二版）\第一部分 基础知识\code\chapter10\pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line)
```

为查看文件的内容，通过对文件对象执行循环来遍历文件中的每一行：

```
3.1415926535

8979323846

2643383279
```

---

要消除多余的空白行，可在函数调用`print()`中使用`rstrip()`：

```python
print(line.rstrip())
```

### 10.1.4 创建一个包含文件各行内容的列表

使用关键字`with`时，`open()`返回的文件对象只在`with`代码块内可用。如果要在`with`代码外访问文件的内容，可在`with`代码块内将文件的各行存储在一个列表中，并在`with`代码块外使用该列表：可以立即处理文件的各个部分，也可以推迟到程序后的再处理。

```python
filename = 'D:\git\Python-learn\Python编程-从入门到实践（第二版）\第一部分 基础知识\code\chapter10\pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
```

`readlines()`从文件中读取每一行，并将其存储在一个列表中。接下来，该列表被赋值给`lines`。在`with`代码块外，依然可使用这个变量。

```
3.1415926535
8979323846
2643383279
```

### 10.1.5 使用文件的内容

将文件读取到内存中后，就能以任何方式使用这些数据了。

```python
filename = 'D:\git\Python-learn\Python编程-从入门到实践（第二版）\第一部分 基础知识\code\chapter10\pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ""
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))
```

```
3.141592653589793238462643383279
32
```

> 读取文本文件时，`Python`将其中的所有文本都解读为字符串。如果读取的是数，并要将其作为数值使用，就必须使用函数`int()`将其转换为整数或使用函数`float()`将其转换为浮点数。

### 10.1.6 包含一百万位的大型文件

```python
filename = 'D:\git\Python-learn\Python编程-从入门到实践（第二版）\第一部分 基础知识\code\chapter10\pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ""
for line in lines:
    pi_string += line.strip()

print(f"{pi_string[:52]}...")
print(len(pi_string))
```

```
3.14159265358979323846264338327950288419716939937510...
1000002
```

对于可处理的数据量，`Python`没有任何限制。只要系统的内存足够多，你想处理多少数据都可以。

### 10.1.7 圆周率值中包含你的生日吗

```python
filename = 'D:\git\Python-learn\Python编程-从入门到实践（第二版）\第一部分 基础知识\code\chapter10\pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ""
for line in lines:
    pi_string += line.strip()

birthday = input("Enter you birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear int the first million digits of pi.")
```

```
Enter you birthday, in the form mmddyy: 120372
Your birthday appears in the first million digits of pi!
```

## 10.2 写入文件

保存数据的最简单的方式之一是将其写入文件中。通过将输出写入文件，即便关闭包含程序输出的终端窗口，这些输出也依然存在。

### 10.2.1 写入空文件

要将文本写入文件，在调用`open()`时需要提供另一个实参，告诉`Python`你要写入打开的文件。

```python
filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.")
```

调用`open()`时提供了两个实参：

- 第一个实参是要打开的文件的名称。
- 第二个实参(`'w'`)告诉`Python`，要以写入模式打开这个文件。打开文件时，可指定读取模式(`'r'`)、写入模式(`'w'`)、附加模式(`'a'`)或读写模式(`'r+'`)。若忽略了模式实参，`Python`将以默认的只读模式打开文件。

如果要写入的文件不存在，函数`open()`将自动创建它。然而，以写入模式(`'w'`)打开文件时千万要小心，因为如果指定的文件以及存在，`Python`将在返回文件对象前清空该文件的内容。

> `Python`只能将字符串写入文本文件。要将数值数据存储到文本文件中，必须先使用函数`str()`将其转换为字符串格式。

### 10.2.2 写入多行

函数`write()`不会在写入的文本末尾添加换行符，因此如果写入多行时，需要指定换行符：

```python
filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")
```

`programming.txt`文件内容：

```
I love programming.
I love creating new games.

```

像显示到终端输出一样，还可以使用空格、制表符和空行来设置这些输出的格式。

### 10.2.3 附加文件

如果要给文件添加内容，而不是覆盖原有的内容，可以以附加模式打开文件。以附加模式打开文件时，`Python`不会在返回文件对象前清空文件的内容，而是将写入文件的行添加到文件末尾。如果指定的文件不存在，`Python`将为你创建一个空文件。

```python
filename = 'programming.txt'

with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")
```

最终结果是，文件原来的内容还在，后面则是刚添加的内容。`programming.txt`文件内容：

```
I love programming.
I love creating new games.
I also love finding meaning in large datasets.
I love creating apps that can run in a browser.
```

## 10.3 异常

`Python`使用称为异常的特殊对象来管理程序执行期间发生的错误。每当发生让`Python`不知所措的错误时，它都会创建一个异常对象。如果你编写了处理该异常的代码，程序将继续执行；如果未对异常进行处理，程序将停止并显示`traceback`，其中包含有关异常的报告。

异常是使用`try-except`代码块处理的。`try-except`代码块让`Python`执行指定的操作，同时告诉`Python`发生异常时怎么办。使用`try-except`代码块时，即便出现异常，程序也将继续执行：显示你编写好的友好的错误信息，而不是令用户迷惑的`traceback`。

### 10.3.1 处理 ZeroDivisionError 异常

```python
print(5 / 0)
```

```
Traceback (most recent call last):
  File "d:/git/Python-learn/Python编程-从入门到实践（第二版）/第一部分 基础知识/code/chapter10/division_calculator.py", line 1, in <module>

    print(5 / 0)
ZeroDivisionError: division by zero
```

在上述`traceback`中，指出错误`ZeroDivisionError`是个异常对象。`Python`无法按你的要求做时，就会创建这种对象。在这种情况下，`Python`将停止运行程序，并指出引发了哪种异常，而我们可以根据这些信息对程序进行修改。

### 10.3.2 使用 try-except 代码块

当你认为可能会发生错误时，可编写一个`try-except`代码块来处理可能引发的异常。让`Python`尝试运行一些代码，并告诉它如果这些代码引发了指定的异常该怎么办。

```python
try:
    print(5 / 0)
except ZeroDivisionError:
    print("You can't divide by zero!")
```

如果`try`代码块中的代码运行起来没有问题，`Python`将跳过`except`代码块；如果`try`代码块中的代码导致了错误，`Python`将查找与之匹配的`except`代码块并运行其中的代码。

```
You can't divide by zero!
```

如果`try-except`代码块后面还有其他代码，程序将接着运行。

### 10.3.3 使用异常避免崩溃

发生错误时，如果程序还有工作尚未完成，妥善地处理错误就尤其重要。这种情况经常会出现在要求用户提供输入的程序中；如果程序能够妥善地处理无效输入，就能再提示用户提供有效输入，而不至于崩溃。

```python
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if (first_number == 'q'):
        break
    second_number = input("Second number: ")
    if (second_number == 'q'):
        break
    answer = int(first_number) / int(second_number)
    print(answer)
```

该程序没有采取任何处理错误的措施，因此在执行除数为 0 的除法运算是，它将崩溃：

```
Give me two numbers, and I'll divide them.
Enter 'q' to quit.

First number: 5
Second number: 0
Traceback (most recent call last):
  File "d:/git/Python-learn/Python编程-从入门到实践（第二版）/第一部分 基础知识/code/chapter10/division_calculator.py", line 11, in <module>
    answer = int(first_number) / int(second_number)
ZeroDivisionError: division by zero
```

### 10.3.4 else 代码块

通过将可能引发错误的代码放在`try-except`代码块中，可提高程序抵御错误的能力。`try`代码块中只包含可能导致错误的代码。依赖`try`代码块成功执行的代码都放在`else`代码块中。

`try-except-else`代码块的工作原理大致如下。`Python`尝试执行`try`代码块中的代码，只有可能引发异常的代码才需要放在`try`语句中。仅在`try`代码块成功执行时才需要运行的代码放在`else`代码块中。

```python
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if (first_number == 'q'):
        break
    second_number = input("Second number: ")
    if (second_number == 'q'):
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)
```

```
Give me two numbers, and I'll divide them.
Enter 'q' to quit.

First number: 5
Second number: 0
You can't divide by 0!

First number: 5
Second number: 2
2.5

First number: q
```

通过预测可能发生错误的代码，可编写健壮的程序。它们即使面临无效数据或缺少资源，也能继续执行，从而抵御无意的用户错误和恶意的攻击。

### 10.3.5 处理 FileNotFoundError

使用文件时，一种常见的问题是找不到文件：查找的文件可能在其他地方，文件名可能不正确，或者这个文件根本就不存在。对于所有这些情形，都可使用`try-except`代码块以直观的方式处理。
尝试读取一个不存在的文件：

```python
filename = 'alice.txt'

with open(filename, encoding='utf-8') as f:
    contents = f.read()
```

这里文件打开方式有两个不同：

1. 使用变量`f`来表示文件对象。
2. 给参数`encoding`指定了值，在系统的默认编码与要读取文件使用的编码不一致时，必须这样做。（`Python`中默认的编码格式是 `ASCII` 格式）

```
Traceback (most recent call last):
  File "d:/git/Python-learn/Python编程-从入门到实践（第二版）/第一部分 基础知识/code/chapter10/alice.py", line 3, in <module>
    with open(filename, encoding='utf-8') as f:
FileNotFoundError: [Errno 2] No such file or directory: 'alice.txt'
```

`Python`无法读取一个不存在的文件，会报告`FileNotFoundError`异常。

---

这个错误是`open()`导致的。因此，要处理这个错误，必须将`try`语句放在`open()`的代码行之前：

```python
filename = 'alice.txt'

try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")
```

```
Sorry, the file alice.txt does not exist.
```

### 10.3.6 分析文本

可以分析包含整本书的文本文件。

---

- `split()`方法：
  根据一个字符串创建一个单词列表。

```
>>> title = "Alice in Wonderland"
>>> title.split()
['Alice', 'in', 'Wonderland']
```

---

```python
filepath = 'D:\\git\\Python-learn\\Python编程-从入门到实践（第二版）\\第一部分 基础知识\\reference\\chapter10\\alice.txt'
filename = 'alice.txt'
try:
    with open(filepath, encoding='gbk') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")
else:
    # 计算该文件大致包含多少个单词。
    words = contents.split()
    num_words = len(words)
    print(f"The file {filename} has about {num_words} words.")
```

对变量`contents`（它现在是一个长长的字符串，包含通话的全部文本。）调用方法`split()`，以生成一个列表，其中包含这部通话中的所有单词。使用`len()`来确定这个列表的长度时，就能知道原始字符串大致包含多少个单词了。

```
The file alice.txt has about 19064 words.
```

### 10.3.7 使用多个文件

将文件的名称存储在一个列表中，然后对列表中的每个文件调用函数`count_words()`。

```python
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
```

siddhartha.txt 文件不存在，但丝毫不影响该程序处理其他文件。

```
The file alice.txt has about 19064 words.
Sorry, the file siddhartha.txt does not exits.
The file moby_dick.txt has about 212446 words.
The file little_women.txt has about 187602 words.
```

在本例中，使用`try-except`代码块提供了两个重要优点：避免用户看见`traceback`，以及让程序继续分析能够找到的其他文件。

### 10.3.8 静默失败

有时候希望程序在发生异常时保持静默，就像什么都没有发生一样继续执行。要让程序静默失败，可像通常那样编写`try`代码块，但在`except`代码块中明确地告诉`Python`什么都不要做。`Python`有一个`pass`语句，可用于让`Python`在代码块中什么都不要做。

```python
def count_words(filename):
    """计算一个文件大致包含多少个单词。"""
    filepath = 'D:\\git\\Python-learn\\Python编程-从入门到实践（第二版）\第一部分 基础知识\\reference\chapter10\\'
    try:
        --snip--
    except FileNotFoundError:
        pass
    else:
        --snip--


filenames = ['alice.txt', 'siddhartha.txt',
             'moby_dick.txt', 'little_women.txt']  # 不存在siddhartha.txt文件
for filename in filenames:
    count_words(filename)
```

出现`FileNotFoundError`异常时，将执行`except`代码块中的`pass`语句，但什么也不会发生。这种错误发生时，不会出现`traceback`，也没有任何输出：

```
The file alice.txt has about 19064 words.
The file moby_dick.txt has about 212446 words.
The file little_women.txt has about 187602 words.
```

`pass`语句还充当了占位符，提醒你在程序的某个地方什么都没有做，并且以后也许要在这里做些什么。

### 10.3.9 决定报告哪些错误

通常依赖于外部因素的程序，可能会出现异常。常见的外部因素有用户输入、指定文件、网络链接等。凭借经验可判断该程序的什么地方包含异常处理块，以及出现错误时该向用户提供多少相关的信息。

## 10.4 存储数据

程序把用户提供的信息存储在列表和字典等数据结构中。用户关闭程序时，几乎总是要保存他们提供的信息。一种简单的方式是使用`json`来存储数据。

模块`json`让你能够将简单的`Python`数据结构转储到文件中，并在程序再次运行时加载该文件中的数据。你还可以使用`json`在`Python`程序之间分享数据。更重要的是，`JSON`数据格式并非`Python`专用的，这让你能够将以`JSON`格式存储的数据与使用其他编程语言的人分享。

> `JSON`(JavaScript Object Notation)格式最初是为`JavaScript`开发的，但随后成了一种常见格式，被包括`Python`在内的众多语言采用。

### 10.4.1 使用 json.dump()和 json.load()

使用`json.dump()`存储一组数，`json.load()`将一组数读到内存中。

- 函数`json.dump()`接受两个实参：要存储的数据，以及可用于存储数据的文件对象。
  使用`json.dump()`来存储数字列表：

  ```python
  import json

  numbers = [2, 3, 5, 7, 11, 13]

  filename = 'numbers.json'
  with open(filename, 'w') as f:
      json.dump(numbers, f)
  ```

  `numbers.json`的内容：

  ```
  [2, 3, 5, 7, 11, 13]
  ```

- 函数`json.load()`将`JSON`格式的文件读入内存。

  ```python
  import json

      filename = 'numbers.json'
      with open(filename) as f:
          numbers = json.load(f)

      print(numbers)
  ```

  ```
  [2, 3, 5, 7, 11, 13]
  ```

这是一种在程序之间共享数据的简单方式。

### 10.4.2 保存和读取用户生成的数据

如果不使用`json`保存用户生成的数据，用户的信息会在程序停止运行时丢失。

例：提示用户首次运行程序时输入自己的名字，并在再次运行程序时记住他。

```python
import json

username = input("What is your name? ")

filename = 'username.json'
with open(filename, 'w') as f:
    json.dump(username, f)
    print(f"We'll remember you when you come back, {username}!")
```

```
What is your name? Eric
We'll remember you when you come back, Eric!
```

再编写一个程序，向以存储了名字的用户发出问候：

```python
import json

filename = 'username.json'

with open(filename) as f:
    username = json.load(f)
    print(f"Welcome back, {username}!")
```

```
Welcome back, Eric!
```

---

将两个程序合并到一个程序中。这个程序运行时，将尝试从文件`username.json`中获取用户名。首先编写一个尝试恢复用户名的`try`代码块。如果这个文件不存在，就在`except`代码块中提示用户输入用户名，并将其存储到`username.json`中，以便程序再次运行时能够获取：

```python
import json

# 如果以前存储了用户名，就加载它。
# 否则，提示用户输入用户名并存储它。
filename = 'username.json'
try:
    with open(filename) as f:
        username = json.load(f)
except FileNotFoundError:
    username = input("What is your name? ")
    with open(filename, 'w') as f:
        json.dump(username, f)
        print(f"We'll remember you when you come back, {username}!")
else:
    print(f"Welcome back, {username}!")
```

若不存在`username.json`文件，输出将如下：

```
What is your name? Eric
We'll remember you when you come back, Eric!
```

否则，输出：

```
Welcome back, Eric!
```

### 10.4.3 重构

通过将程序划分为一系列完成具体工作的函数，称为重构。重构让代码更清晰、更易于理解、更容易扩展。每个函数都执行单一而清晰的任务。

```python
import json


def get_stored_username():
    """如果以前存储了用户名，就获取它。"""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """提示用户输入用户名。"""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username


def greet_user():
    """问候用户，并指出其名字。"""
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")


greet_user()
```

## 10.5 小结

在本章中，学习了：

1. 如何使用文件；
2. 如何一次性读取整个文件，如何以每次一行的方式读取文件的内容以及将各行存储在一个列表中；
3. 如何写入文件，以及如何将文本附加到文件末尾；
4. 什么是异常以及如何处理程序程序可能引发的异常；
5. 如何存储`Python`数据结构，以保存用户提供的信息，避免用户每次运行程序时都需要重新提供。
