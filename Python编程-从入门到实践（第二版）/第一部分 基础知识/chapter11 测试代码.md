[TOC]

# 测试代码

编写函数或类时，还可为其编写测试。通过测试，可确定代码面对各种输入都能够按要求的那样工作。

在本章中，你将学习如何使用`Python`模块`unittest`中的工具来测试代码。

## 11.1 测试函数

要学习测试，必须有要测试的代码。

函数`get_formatted_name()`将名和姓合并成姓名：在名和姓之间加上一个空格并将其首字母大写，再返回结果。`name_function.py`内容：

```python
def get_formatted_name(first, last):
    """生成整洁的姓名。"""
    full_name = f"{first} {last}"
    return full_name.title()
```

`names.py`从`name_function.py`中导入`get_formatted_name()`：

```python
from name_function import get_formatted_name

print("Enter 'q' at any time to quit.")

while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("Please give me a last name: ")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print(f"\tNeatly formatted name: {formatted_name}.")
```

```
Enter 'q' at any time to quit.

Please give me a first name: janis
Please give me a last name: joplin
        Neatly formatted name: Janis Joplin.

Please give me a first name: bob
Please give me a last name: dylan
        Neatly formatted name: Bob Dylan.

Please give me a first name: q
```

### 11.1.1 单元测试和测试用例

`Python`标准库中的模块`unittest`提供了代码测试工具。

单元测试用于核实函数的某个方面没有问题。

测试用例是一组单元测试，它们一道核实函数在各种情形下的行为都符合要求。良好的测试用例考虑到了函数可能收到的各种输入，包含针对所有这些情形的测试。

全覆盖的测试用例包含一整套单元测试，涵盖了各种可能的函数使用方式。大型项目进行全覆盖测试很难。

### 11.1.2 可通过的测试

要为函数编写测试用例，可先导入模块`unittest`和要测试的函数，再创建一个继承`unittest.TestCase`的类，并编写一系列方法对函数行为的不同方面进行测试。

```python
import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """测试name_function.py。"""

    def test_first_last_name(self):
        """能够正确处理像Janis Joplin这样的姓名吗?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')


if __name__ == '__main__':
    unittest.main()
```

- 首先，导入了模块`unittest`和要测试的函数`get_formatted_name()`。
- 创建了一个名为`NamesTestCase`的类，用于包含一系列针对`get_formatted_name()`的单元测试。
  - 这个类可以随意命名，但最好让它看起来与要测试的函数相关并包含`Test`字样。这个类必须继承`unittest.TestCase`类，这样`Python`才知道如何运行你编写的测试。
  - `NamesTestCase`只包含一个方法，用于测试`get_formatted_name()`的一个方面。将该方法命名为`test_first_last_name()`，因为要核实的是只有名和姓的姓名能否被正确格式化。
- 运行`test_name_function.py`时，所有`test_`打头的方法都将自动运行。
  在这个方法中，调用了要测试的函数。实参`'janis`'和`'joplin'`调用`get_formatted_name()`，并将结果赋给变量`formatted_name`。
- 断言方法是`unittest`类的最有用的功能之一。
  断言方法核实得到的结果是否与期望的结果一致。将`formatted_name`的值与字符串`'Janis Joplin'`比较。
- 变量`__name__`是程序执行时设置的。
  - 很多测试框架都会导入测试文件再运行。导入文件时，解释器将在导入的同时执行它。
  - 如果这个文件作为主程序执行，变量`__name__`将被设置为`'__main__'`。在这里，调用`unittest`来运行测试用例。
  - 如果这个文件被测试框架导入，变量`__name__`的值将不是`'__main__'`，因此不会调用`unittest.main()`。

运行`test_name_function.py`时，得到的输出如下：

```
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```

- 第一行的句点表示有一个测试通过了。
- 接下来的一行指出，`Python`运行了一个测试，消耗的时间不到 0.001 秒。
- 最后的 OK 表明该测试用例中的所有单元测试都通过了。

### 11.1.3 未通过的测试

修改`get_formatted_name()`，使其能够处理中间名，但同时故意让该函数无法正确处理像`Janis Joplin`这样只有名和姓的姓名。

`get_formatted_name()`要求通过一个实参指定中间名：

```python
def get_formatted_name(first, middle, last):
    """生成整洁的姓名。"""
    full_name = f"{first} {middle} {last}"
    return full_name.title()
```

这个版本应该能够正确处理包含中间名的姓名，但对其进行测试时，我们发现它不在能正确处理只有名和姓的姓名。

```
E
======================================================================
ERROR: test_first_last_name (__main__.NamesTestCase)
能够正确处理像Janis Joplin这样的姓名吗?
----------------------------------------------------------------------
Traceback (most recent call last):
  File "d:/git/Python-learn/Python编程-从入门到实践（第二版）/第一部分 基础知识/code/chapter11/test_name_function.py", line 10, in test_first_last_name
    formatted_name = get_formatted_name('janis', 'joplin')
TypeError: get_formatted_name() missing 1 required positional argument: 'last'

----------------------------------------------------------------------
Ran 1 test in 0.001s

FAILED (errors=1)
```

- 第一行输出只有一个字母 E，指出测试用例中有一个单元测试导致了错误。
- 接下来，看到`NamesTestCase`中的`test_first_last_name()`导致了错误。
- `traceback`指出函数调用`get_formatted_name('janis', 'joplin')`有问题，因为缺少了一个必不可少的位置实参。
- `Ran 1 test in 0.001s`表明运行了一个单元测试
- 最后一条消息，指出整个测试用例未通过，因为运行该测试用例时发生了一个错误。

### 11.1.4 测试未通过怎么办

测试通过意味着函数的行为是对的，而测试未通过意味着编写的新代码有错。因此，测试未通过时，不要修改测试，而应修复导致测试不能通过的代码：检查刚刚对函数所做的修改，找出导致函数行为不符合预期的修改。

修改`get_formatted_name()`，将中间名设置为可选的，然后再次运行这个测试用例。

```python
def get_formatted_name(first, last, middle=""):
    """生成整洁的姓名。"""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()
```

```
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```

### 11.1.5 添加新测试

再编写一个测试，用于测试包含中间名的姓名：

```python
import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """测试name_function.py。"""

    def test_first_last_name(self):
        """能够正确处理像Janis Joplin这样的姓名吗?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        """能够正确地处理像 Wolfgang Amadeus Mozart 这样的姓名吗? """
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')


if __name__ == '__main__':
    unittest.main()
```

```
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```

## 11.2 测试类

下面来编写针对类的测试。

### 11.2.1 各种断言方法

`Python`在`unittest.TestCase`类中提供了很多断言方法。断言方法检查你认为应该满足的条件是否确实满足。如果该条件确实满足，你对程序行为的假设就得到了确认，可以确信其中没有错误。如果你认为应该满足的条件实际上并不满足，`Python`将会引发异常。

下面描述了 6 个常用的断言方法。使用这些方法可核实返回的值等于或不等于预期的值，返回的值为`True`和`False`，以及返回的值在列表中或不在列表中。只能在继承`unittest.TestCase`的类中使用这些方法。

`unittest`模块中的断言方法：
| **_方法_** | **_用途_** |
|:-----------------------:|:------------------:|
| assertEqual(a, b) | 核实 a == b |
| assertNotEqual(a, b) | 核实 a != b |
| assertTrue(x) | 核实 x 为 True |
| assertFalse(x) | 核实 x 为 False |
| assertIn(item, list) | 核实 item 在 list 中 |
| assertNotIn(item, list) | 核实 item 不在 list 中 |

### 11.2.2 一个要测试的类

类的测试与函数的测试相似，你所做的大部分工作是测试类中方法的行为。不过还是存在一些不同之处，下面编写一个要测试的类。来看一个帮助管理匿名调查的类(`survey.py`)：

```python
class AnonymousSurvey:
    """收集匿名调查问卷的答案。"""

    def __init__(self, question):
        """存储一个问题，并为存储答案做准备。"""
        self.question = question
        self.responses = []

    def show_question(self):
        """显示调查问卷。"""
        print(self.question)

    def store_response(self, new_response):
        """存储单份调查答卷。"""
        self.responses.append(new_response)

    def show_results(self):
        """显示收集到的所有答卷。"""
        print("Survey results:")
        for response in self.responses:
            print(f"- {response}")
```

为证明`AnonymousSurvey`类能够正确工作，编写一个使用它的程序：

```python
from survey import AnonymousSurvey

# 定义一个问题，并创建一个调查。
question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

# 显示问题并存储答案。
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)

# 显示调查结果。
print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()
```

用户输入所有答案（输出 q 要求退出）：

```
What language did you first learn to speak?
Enter 'q' at any time to quit.

Language: English
Language: Spanish
Language: English
Language: Mandarin
Language: q

Thank you to everyone who participated in the survey!
Survey results:
- English
- Spanish
- English
- Mandarin
```

### 11.2.3 测试 AnnoymousSurvey 类

编写一个测试，对`AnnoymousSurvey`类的行为进行验证：如果用户面对调查问题只提供一个答案，这个答案也能被妥善地存储。在答案被存储后，使用方法`assertIn()`来核实它确实在答案列表中：

```python
import unittest
from survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    """针对 AnonymousSurvey 类的测试。"""

    def test_store_single_response(self):
        """测试单个答案会被妥善地存储。"""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')
        self.assertIn('English', my_survey.responses)


if __name__ == '__main__':
    unittest.main()
```

==要测试类的行为，需要创建实例==。使用问题`"What language did you first learn to speak?"`创建一个名为`my_survey`的实例，然后使用方法`store_response()`存储单个答案`English`。接下来，检查`English`是否包含在一个列表`my_survey.responses`中，以核实这个答案是否被妥善地存储。

运行`test_survey.py`时，测试通过了：

```
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```

---

下面核实当用户提供三个答案时，它们也能被妥善地存储。

```python
import unittest
from survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    """针对 AnonymousSurvey 类的测试。"""

    def test_store_single_response(self):
        --snip--

    def test_store_three_responses(self):
        """测试三个答案会被妥善地存储。"""
        question = "What languags did you learn first learn to speak?"
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'Spanish', 'Mandarin']
        for respons in responses:
            my_survey.store_response(respons)

        for response in responses:
            self.assertIn(respons, my_survey.responses)


if __name__ == '__main__':
    unittest.main()
```

创建一个调查对象`my_survey`，定义一个包含三个不同答案的列表，再对其中每个答案调用`store_response()`。在存储这些答案后，使用一个循环来确认每个答案都包含在`my_survey.responses`中。

运行`test_survey.py`两个测试（只针对单个答案的测试和针对三个答案的测试）都通过了：

```
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```

### 11.2.4 方法 setUp()

在前面的`test_survey.py`中，我们在每个测试方法中都创建了一个`AnonymousSurvey`实例，并在每个方法中都创建了答案。`unittest.TestCase`类中包含的方法`setUp()`让我们只需创建这些对象一次，就能在每个测试方法中使用。如果在`TestCase`类中包含了方法`setUp()`，`Python`将先运行它，再运行各个以`test_`打头的方法。这样，在你编写的每个测试方法中，都可使用在方法`setUp()`中创建的对象。

下面使用`setUp()`来创建一个调查对象和一组答案，供方法`test_store_single_response()`和`test_store_three_responses()`使用：

```python
import unittest
from survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    """针对 AnonymousSurvey 类的测试。"""

    def setUp(self):
        """
        创建一个调查对象和一组答案，供使用的测试方法使用。
        """
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']

    def test_store_single_response(self):
        """测试单个答案会被妥善地存储。"""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        """测试三个答案会被妥善地存储。"""
        for response in self.responses:
            self.my_survey.store_response(response)

        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)


if __name__ == '__main__':
    unittest.main()
```

- 方法`setUp()`做了两件事：创建一个调查对象，以及创建一个答案列表。
  存储这两样东西的变量名包含前缀`self`（即存储在属性中），因此可在这个类的任何地方使用。

再次运行`test_survey.py`，这两个测试都通过了。

方法`setUp()`让测试方法编写起来更加容易：可在`setUp()`方法中创建一系列实例并设置其属性，再在测试方法中直接使用这些实例。相比于在每个测试方法中都创建实例并设置其属性，这要容易得多。

---

> 运行测试用例时，每完成一个单元测试，Python 都打印一个字符：测试通过时打印一个句点，测试引发错误时打印一个 E，而测试导致断言失败时则打印一个 F。这就是你运行测试用例时，在输出的第一行中看到的句点和字符数量各不相同的原因。如果测试用例包含很多单元测试，需要运行很长时间，就可通过观察这些结果来获悉有多少个测试通过了。

## 11.3 小结

在本章中，你学习了：

1. 如何使用模块`unittest`中的工具来为函数和类编写测试；
2. 如何编写继承`unittest.TestCase`的类，以及如何编写测试方法，以核实函数和类的行为符合预期；
3. 如何使用方法`setUp()`来根据类高效地创建实例并设置其属性，以便在类的所有测试方法中使用。
