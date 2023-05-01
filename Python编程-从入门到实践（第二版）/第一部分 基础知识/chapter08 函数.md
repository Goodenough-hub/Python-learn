[TOC]

# 函数

函数是带名字的代码块，用于完成具体的工作。要执行函数定义的特定任务，可调用该函数。需要在程序中多次执行同一项任务时，无需反复编写完成该任务的代码，只需要调用执行该任务的函数，让`Python`运行其中的代码即可。通过使用函数，程序编写、阅读、测试和修复起来都更加容易。

## 8.1 定义函数

使用关键字`def`定义一个函数，向`Python`指出函数名，还可以在圆括号中传递参数。定义以冒号结尾。

要调用函数，可依次指定函数名以及用圆括号括起的必要信息。

```python
def greet_user():
    """显示简单的问候语。"""
    print("Hello!")


greet_user()
```

```
Hello!
```

> `"""显示简单的问候语。"""`是称为文档字符串的注释，描述了函数时做什么的。文档字符串用三引号括起，`Python`使用它们来生成有关程序中函数的文档。

### 8.1.1 向函数传递信息

可以在函数定义的圆括号中传递参数。

```python
def greet_user(username):
    """显示简单的问候语。"""
    print(f"Hello, {username.title()}!")


greet_user('jesse')
```

```
Hello, Jesse!
```

### 8.1.2 实参和形参

在函数定义中，通过圆括号传递的参数是形参，是函数完成工作所需的信息。

在调用函数中，在圆括号内的信息是实参，是调用函数时传递给函数的信息。

## 8.2 传递参数

函数定义中可能包含多个形参，因此函数调用中也可能包含多个实参。

向函数传递实参的方法很多：

1. 位置实参，要求实参的顺序和形参的顺序相同。
2. 关键字实参，其中每个实参都由变量名和值组成。
3. 列表和字典。

### 8.2.1 位置实参

调用函数时，`Python`必须将函数调用中的每个实参都关联到函数定义中的一个形参。关联方式是基于实参的顺序，这种关联方式称为位置实参。

```python
def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet('hamster', 'harry') # 描述一只名为Harry的仓鼠
```

在函数调用中，实参`hamster`被赋给形参`animal_type`，而实参`harry`被赋给形参`pet_name`。

```

I have a hamster.
My hamster's name is Harry.
```

#### 多次调用函数

可以根据需要调用函数任意次。

```python
def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')
```

多次调用函数是一种效率极高的工作方式。只需在函数中编写一次描述宠物的代码，然后每当需要描述新宠物时，都调用该函数并向它提供新宠物的信息。

```

I have a hamster.
My hamster's name is Harry.

I have a dog.
My dog's name is Willie.
```

在函数中，可根据需要使用任意数量的位置实参，`Python`将按顺序将函数调用中的实参关联到函数定义中相应的形参。

#### 位置实参的顺序很重要

如果实参的顺序不正确，结果会出乎意料。

```python
def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet('harry', 'hamster')
```

```
I have a harry.
My harry's name is Hamster.
```

### 8.2.2 关键字实参

关键字实参传递给函数的名称值对。因为直接在实参将名称和值关联起来，所以向函数传递实参时不会混淆。关键字实参让你无需考虑函数调用中的实参顺序，还清楚地指出函数调用中各个值的用途。

```python
def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet(animal_type='hamster', pet_name='harry')
```

函数调用时指定，`Python`明确地指出各个实参对应的形参。

```

I have a hamster.
My hamster's name is Harry.
```

### 8.2.3 默认值

编写函数时，可给每个形参指定默认值。在调用函数中给形参提供了实参时，`Python`将使用指定的实参值；否则，将使用形参的默认值。因此，给形参指定默认值后，可在函数调用中省略相应的实参。

```python
def describe_pet(pet_name, animal_type='dog'): # animal_type默认为dog
    """显示宠物的信息"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet(pet_name='harry')
```

```

I have a dog.
My dog's name is Harry.
```

> 形参指定了默认值，一般放在形参中的右侧。这是因为函数调用过程中依然将实参视为位置实参，传入的第一个实参关联到函数定义中的第一个形参。
>
> 使用默认值，必须先在形参列表中列出没有默认值的形参，再列出有默认值的实参。这让`Python`依然能够正确地解读位置实参。

---

若显式地给出实参，`Python`将忽略这个形参的默认值。

```python
describe_pet(pet_name='harry', animal_type='hamster')
```

### 8.2.4 等效的函数调用

鉴于可混合使用位置实参、关键字实参和默认值，通常有多种等效的函数调用方式。
针对`describe_pet()` 的定义，其中给一个形参提供了默认值：

```python
def describe_pet(pet_name, animal_type='dog'): # animal_type默认为dog
```

以下的函数调用都可行：

```python
# 一条名为Willie的小狗。
describe_pet('willie') # 位置方式
describe_pet(pet_name='willie') #关键字方式

# 一只名为Harry的仓鼠
describe_pet('harry', 'hamster') # 位置方式
describe_pet(pet_name='harry', animal_type='hamster') # 关键字方式
describe_pet(animal_type='hamster', pet_name='harry') # 关键字方式
```

### 8.2.5 避免实参错误

提供的实参个数多于或少于形参个数时，将会出现实参不匹配错误。

```python
def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet()
```

```
Traceback (most recent call last):
  File "d:/git/Python-learn/Python编程-从入门到实践（第二版）/第一部分 基础知识/code/chapter08/pets.py", line 7, in <module>
    describe_pet()
TypeError: describe_pet() missing 2 required positional arguments: 'animal_type' and 'pet_name
```

## 8.3 返回值

在函数中，可使用`return`语句将值返回到调用函数的代码行。可以返回一个或一组值。

### 8.3.1 返回简单值

```python
def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)
```

```
Jimi Hendrix
```

### 8.3.2 让实参变成可选的

可使用默认值来让实参变成可选的。

```python
def get_formatted_name(first_name, last_name, middle_name=''):
    """返回整洁的姓名"""
    if middle_name: # 若middle_name不为空
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)
```

```
Jimi Hendrix
John Lee Hooker
```

### 8.3.3 返回字典

函数可返回任何类型的值，包括列表和字典等较复杂的数据结构。

```python
def build_person(first_name, last_name):
    """返回一个字典，其中包含有关一个人的信息。"""
    person = {'first': first_name, 'last': last_name}
    return person


musician = build_person('jimi', 'hendrix')
print(musician)
```

```
{'first': 'jimi', 'last': 'hendrix'}
```

```python
def build_person(first_name, last_name, age=None):
    """返回一个字典，其中包含有关一个人的信息。"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


musician = build_person('jimi', 'hendrix', age=27)
print(musician)
```

在函数定义中，新增了一个可选参数`age`，并将其默认值设置为特殊值`None`（表示变量没有值）。可将`None`视为占位值。在条件测试中，`None`相当于`False`。如果函数调用中包含形参`age`的值，这个值将被存储到字典中。

```
{'first': 'jimi', 'last': 'hendrix', 'age': 27}
```

### 8.3.4 结合使用函数和 while 循环

```python
def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


# 这是一个无限循环！
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")
```

```
Please tell me your name:
(enter 'q' at any time to quit)
First name: eric
Last name: matthes

Hello, Eric Matthes!

Please tell me your name:
(enter 'q' at any time to quit)
First name: q
```

## 8.4 传递列表

将列表传递给函数后，函数就能直接访问其内容。使用函数能提高处理列表的效率。

```python
def greet_user(names):
    """向列表中的每位用户发出简单的问候。"""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)


usernames = ['hannah', 'ty', 'margot']
greet_user(usernames)
```

`greet_user()`定义为接受一个名字列表，并将其赋值给`names`。这个函数遍历收到的列表，并对其中的每位用户打印一条问候语。

```
Hello, Hannah!
Hello, Ty!
Hello, Margot!
```

### 8.4.1 在函数中修改列表

将列表传递给函数后，函数就可对其进行修改。在函数中对这个列表所做的任何修改都是永久性的。

```python
# 首先创建一个列表，其中包含一些要打印的设计。
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# 模拟打印每个设计
# 打印每个设计，都将其移到列表completed_models中。
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

# 显示打印好的所有模型。
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)
```

```
Printing model: dodecahedron
Printing model: robot pendant
Printing model: phone case

The following models have been printed:
dodecahedron
robot pendant
phone case
```

为组织这些代码，可编写两个函数，每个都做一件具体的工作。第一个函数`print_models()`负责打印设计的工作，第二个函数`show_completed_models()`概述打印了哪些设计。

```python
def print_models(unprinted_designs, completed_models):
    """
    模拟打印每个设计， 直到没有未打印的设计为止。
    打印每个设计，都将其移到列表completed_models中。
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """显示打印好的所有模型。"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
```

这个程序的输出与未使用函数的版本相同，但组织更为有序。完成大部分工作的代码都移动到了两个函数中，让主程序更容易理解。相比于没有使用函数的版本，这个程序更容易扩展和维护。

```Printing model: dodecahedron
Printing model: robot pendant
Printing model: phone case

The following models have been printed:
dodecahedron
robot pendant
phone case
```

> 每个函数都应只负责一项具体的工作。编写函数时，如果发现它执行的任务太多，请尝试将这些代码划分到两个函数中。

### 8.4.2 禁止函数修改列表

若要保留原来列表中的数据，可向函数传递列表的副本而非原件。这样，函数所做的任何修改都只影响副本，而原件不受影响。

要将列表的副本传递给函数，可以使用切片：

```python
function_name(list_name[:])
```

切片表示法`[:]`创建列表的副本。

> 向函数传递列表的副本可保留原始列表的内容，但也会花费更多时间和内存创建副本。在处理大型列表时，会导致效率降低。

## 8.5 传递任意数量的实参

有时候，预先不知道函数需要接受多少个实参，`Python`允许函数从调用语句中收集任意数量的实参。

```python
def make_pizza(*toppings):
    """打印顾客点的所有配料。"""
    print(toppings)


make_pizza('pepperoni')
make_pizza('mushroom', 'green peppers', 'extra cheese')
```

形参名`*toppings`中的星号让`Python`创建一个名为`toppings`的空元组，并将收到的所有值都封装到这个元组中。

```
('pepperoni',)
('mushroom', 'green peppers', 'extra cheese')
```

将函数调用`print()`替换为一个循环，遍历配料列表：

```python
def make_pizza(*toppings):
    """概述要制作的披萨"""
    print("\nMaking a pizza with the following toppings: ")
    for topping in toppings:
        print(f"- {topping}")


make_pizza('pepperoni')
make_pizza('mushroom', 'green peppers', 'extra cheese')
```

```

Making a pizza with the following toppings:
- pepperoni

Making a pizza with the following toppings:
- mushroom
- green peppers
- extra cheese
```

不管函数收到的实参是多少个，这种语法都管用。

### 8.5.1 结合使用位置实参和任意数量实参

如果要让函数接受不同类型的实参，必须正在函数定义这种将接纳任意数量实参的形参放在最后。`Python`先匹配位置实参和关键字实参，再将余下的实参都收集到最后一个形参中。

```python
def make_pizza(size, *toppings):
    """概述要制作的披萨"""
    print(f"\nMaking a {size}-inch pizza with the following toppings: ")
    for topping in toppings:
        print(f"- {topping}")


make_pizza(16, 'pepperoni')
make_pizza(12, 'mushroom', 'green peppers', 'extra cheese')
```

```

Making a 16-inch pizza with the following toppings:
- pepperoni

Making a 12-inch pizza with the following toppings:
- mushroom
- green peppers
- extra cheese
```

> 通用形参名`*args`，收集任意数量的位置实参。

### 8.5.2 使用任意数量的关键字实参

需要接受任意数量的实参，但预先不知道传递给函数的会是什么样的信息。这时，可将函数编写成能够接受任意数量的键值对——调用语句提供了多少就接受多少。

```python
def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切。"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physic')
print(user_profile)
```

函数`build_profile()`的定义要求提供名和姓，同时允许根据需要提供任意数量的名称键值对。

形参`**usr_info`中的两个星号让`Python`创建一个名为`user_info`的空字典，并将收到的所有名称键值对都放到在这个字典中。

```
{'location': 'princeton', 'field': 'physic', 'first_name': 'albert', 'last_name': 'einstein'}
```

> 通用形参名`*kwargs`，收集任意数量的关键字实参。

## 8.6 将函数存储在模块中

使用函数的优点之一是可将代码块与主程序分离。通过给函数指定描述性名称，可让主程序容易理解得多。

还可以更进一步，将函数存储在称为模块的独立文件中，再将模块导入到主程序中。`import`语句允许在当前运行的程序文件中使用模块中的代码。

通过将函数存储在独立的文件中，可隐藏程序代码的细节，将重点放在程序的高层逻辑上。这还能让你在众多不同的程序中重用函数。将函数存储正在独立文件后，可与其他程序员共享这些文件而不是整个程序。知道如何导入函数还能让你使用其他程序员编写的函数库。

### 8.6.1 导入整个模块

编写一条`import`语句并在其中指定模块名，就可在程序中使用该模块中的所有函数。若导入名为`module_name.py`的整个模块，就可以使用下面的语法来使用其中任一函数：

```python
module_name.function_name()
```

`pizza.py`中的代码：

```python
def make_pizza(size, *toppings):
    """概述要制作的披萨"""
    print(f"\nMaking a {size}-inch pizza with the following toppings: ")
    for topping in toppings:
        print(f"- {topping}")
```

`making_pizza.py`在`pizza.py`所在的目录中。`Python`读取这个文件时，代码行`import pizza`让`Python`打开文件`pizza.py`，并将其中的所有函数都复制到这个程序中。

要调用被导入模块中的函数，可指定被导入模块的名称`pizza`和函数名`make_pizza()`，并用句点分隔。

```python
import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushroom', 'green peppers', 'extra cheese')
```

```
Making a 16-inch pizza with the following toppings:
- pepperoni

Making a 12-inch pizza with the following toppings:
- mushroom
- green peppers
- extra cheese
```

### 8.6.2 导入特定的函数

可以导入模块中的特定函数：

```python
from module_name import function_name
```

---

通过用逗号分隔函数名，可根据需要从模块中导入任意数量的函数：

```python
from module_name import function_0, function_1, function_2
```

---

使用这种语法时，调用函数时无须使用句点。

上例中的`making_pizza.py`，只导入`make_pizza()`函数。由于`import`语句中显式地导入了函数`make_pizza()`，调用时只需指定其名称即可：

```python
from pizza import make_pizza

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushroom', 'green peppers', 'extra cheese')
```

### 8.6.3 使用 as 给函数指定别名

如果要导入函数的名称可能与程序中现有的名称冲突，或者函数的名称太长，可指定简短而独一无二的别名：函数的另一个名称，类似于外号。要给函数取这种特殊外号，需要在导入它时指定。

关键字`as`将函数重命名为指定的别名。指定别名的通用语法如下：

```python
from module_name import function_name as fn
```

给函数`make_pizza()`指定了别名`mp()`：

```python
from pizza import make_pizza as mp

mp(16, 'pepperoni')
mp(12, 'mushroom', 'green peppers', 'extra cheese')
```

### 8.6.4 使用 as 给模块指定别名

还可以给模块指定别名。通过给模块指定简短的别名，能够更加轻松地调用模块中的函数。

给模块指定别名后，模块中的所有函数名称都没有改变。

```python
import pizza as p

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushroom', 'green peppers', 'extra cheese')
```

### 8.6.5 导入模块中的所有函数

使用星号`（*）`运算符可让`Python`导入模块中所有函数。`import`语句中的星号让`Python`将模块中的每个函数都复制到这个程序文件中。由于导入了每个函数，可通过名称来调用每个函数，而无须使用句点表示法。

```python
from module_name import *
```

`import`语句中的星号让`Python`将模块`pizza`中的每个函数都复制到这个程序文件中：

```python
from pizza import *

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushroom', 'green peppers', 'extra cheese')
```

## 8.7 函数编写指南

编写函数需要牢记的细节：

1. 给函数指定描述性名称。
   - 只在函数名称中使用小写字母和下划线。
   - 描述性名称可帮助你和别人明白代码的功能。
   - 给模块命名也应遵守上述约定。
2. 每个函数都应包含简要地阐述其功能的注释。
   - 注释应紧跟在函数定义后面。
   - 应采用文档字符串格式。
3. 给形参指定默认值时，等号两边不要有空格：
   ```python
   def function_name(parameter_0, parameter_1='default value')
   ```
4. 对于函数调用中的关键字实参，也应该遵守这种约定：
   ```python
   function_name(value_0, parameter='value')
   ```
5. `PEP 8`建议代码行长度不超过 79 字符。
6. 所有`import`语句都应放在文件开头。（唯一的例外是，在文件开头使用了注释来描述整个程序）

## 8.8 小结

在本章中，学习了：

1. 如何编写函数，以及如何传递实参，让函数能够访问其工作所需的信息；
2. 如何使用位置实参和关键字实参，以及如何接受任意数量的实参；
3. 显示输出的函数和返回值的函数；
4. 如何将函数同列表、字典、`if`语句和`while`循环结合起来使用；
5. 如何将函数存储在称为模块的独立文件中，让程序文件更加简单、易于理解；
6. 函数编写指南。
