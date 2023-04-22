[TOC]

# 字典

## 6.1 一个简单的字典

```python
alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])
```

```
green
5
```

## 6.2 使用字典

在`Python`中，字典是一系列键值对。每个键都与一个值相关联，可使用键来访问相关联的值。与键相关联的值可以是数、字符串、列表乃至字典。可以将任何`Python`对象用作字典中的值。
在`Python`中，字典用放在方括号({})中一系列键值对表示。

```python
alien_0 = {'color': 'green', 'points': 5}
```

键值对是两个相关联的值。指定键时，`Python`将返回与之相关联的值。键和值之间用冒号分隔，而键值对之间用逗号分隔。

### 6.2.1 访问字典中的值

要获取与键相关联的值，可依次指定字典名和放在方括号内的键。

```python
alien_0 = {'color': 'green'}

print(alien_0['color'])
```

```
green
```

```python
alien_0 = {'color': 'green', 'points': 5}

new_points = alien_0['points']
print(f"You just earned {new_points} points!")
```

```
You just earned 5 points!
```

### 6.2.2 添加键值对

字典是一种动态结构，可随时在其中添加键值对。要添加键值对，可依次指定字典名、用方括号括起的键和相关联的值。

```python
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
```

```
{'color': 'green', 'points': 5}
{'color': 'green', 'points': 5, 'x_position': 0, 'y_position': 25}
```

> 在`Python`中，字典中元素的排列顺序与定义时相同。如果将字典打印出来或遍历其元素，将发现元素的排列顺序与添加顺序相同。

### 6.2.3 先创建一个空字典

可以使用一对空花括号定义一个字典，再分行添加各个键值对。

```python
alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)
```

```
{'color': 'green', 'points': 5}
```

> 使用字典来存储用户提供的数据或在编写能自动生成大量键值对的代码时，通常需要先定义一个空字典。

### 6.2.4 修改字典中的值

要修改字典中的值，可依次指定字典名、用方括号括起的键，以及与该键相关联的新值。

```python
alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}")

alien_0['color'] = 'yellow'
print(f"The alien is {alien_0['color']}")
```

```
The alien is green
The alien is yellow
```

### 6.2.5 删除键值对

对于字典中不再需要的信息，可使用`del`语句将相应的键值对彻底删除。使用`del`语句时，必须指定字典名和要删除的键。

```python
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)
```

```
{'color': 'green', 'points': 5}
{'color': 'green'}
```

> 删除的键值对会永远消失。

### 6.2.6 由类似对象组成的字典

可以使用字典来存储众多对象的同一种信息。

```python
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite_language is {language}.")
```

```
Sarah's favorite_language is C.
```

### 6.2.7 使用 get()来访问值

使用放在方括号内的键从字典中获取感兴趣的值时，可能会引发问题：如果指定的键不存在就会出错。

```python
alien_0 = {'color': 'green', 'speed': 'slow'}
print(alien_0['points'])
```

```
Traceback (most recent call last):
  File "d:/git/Python-learn/Python编程-从入门到实践（第二版）/第一部分 基础知识/code/chapter06/alien_no_points.py", line 2, in <module>
    print(alien_0['points'])
KeyError: 'points'
```

使用方法`get()`在指定的键不存在时返回一个默认值，从而避免这种错误。

方法`get()`的第一个参数用于指定键，是必不可少的；第二个参数为指定的键不存在时要返回的值，是可选的：

```python
alien_0 = {'color': 'green', 'speed': 'slow'}

point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)
```

```
No point value assigned.
```

如果指定的键可能不存在，应考虑使用方法`get()`，而不要使用方括号表示法。

> 调用`get()`时，如果没有指定第二个参数且指定的键不存在，`Python`将返回值`None`。
>
> - `None`这个特殊值表示没有相应的值。`None`并非表示错误，而是一个表示所需值不存在的特殊值。

## 6.3 遍历字典

### 6.3.1 遍历所有键值对

```python
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")
```

```

Key: username
Value: efermi

Key: first
Value: enrico

Key: last
Value: fermi
```

`for`语句中包含字典名和方法`items()`，它返回一个键值对列表。

循环中可以不使用`key`和`value`这两个变量名。

```python
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite_language is {language.title()}.")
```

```
Jen's favorite_language is Python.
Sarah's favorite_language is C.
Edward's favorite_language is Ruby.
Phil's favorite_language is Python.
```

### 6.3.2 遍历字典中的所有键

不需要使用字典中的值，可以使用方法`keys()`遍历字典中的所有键。

```python
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name in favorite_languages.keys():
    print(name.title())
```

```
Jen
Sarah
Edward
Phil
```

> - 遍历字典时，会默认遍历所有的键。显示地使用方法`keys()`可让代码更容易理解。
> - 方法`keys()`返回一个列表，其中包含字典中的所有键。

### 6.3.3 按特定顺序遍历字典中的所有键

要以特定顺序返回元素，可以在`for`循环中对返回的键进行排序。

```python
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")
```

```
Edward, thank you for taking the poll.
Jen, thank you for taking the poll.
Phil, thank you for taking the poll.
Sarah, thank you for taking the poll.
```

### 6.3.4 遍历字典中的所有值

方法`values()`返回一个值列表，不包含任何键。

```python
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print("The following languages have been mentioned:")

for language in favorite_languages.values():
    print(language.title())
```

```
The following languages have been mentioned:
Python
C
Ruby
Python
```

这种提取字典中所有的值，并没有考虑到是否重复。为剔除重复项，可使用集合(set)。==集合中的每个元素都必须是独一无二的。==

```python
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print("The following languages have been mentioned:")

for language in set(favorite_languages.values()):
    print(language.title())
```

```
The following languages have been mentioned:
Python
Ruby
C
```

---

#### 集合

1. 使用一对花括号直接创建结合，并在其中用逗号分隔元素：

```
  >>> languages = {'python', 'ruby', 'python', 'c'}
  >>> languages
  {'c', 'python', 'ruby'}
```

2. 集合和字典都是用花括号定义的。字典中是键值对，集合中不是键值对。

3. 不同与列表和字典，集合不会以特定的顺序存储元素。

## 6.4 嵌套

将一系列字典存储在列表中，获将列表作为值存储在字典中，称为嵌套。

### 6.4.1 字典列表

列表中嵌套字典。

```python
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)
```

```
{'color': 'green', 'points': 5}
{'color': 'yellow', 'points': 10}
{'color': 'red', 'points': 15}
```

### 6.4.2 在字典中存储列表

将列表存储在字典中。

```python
# 存储所点的比萨的信息。
pizza = {
    'crust': 'thick',  # 外皮类型
    'toppings': ['mushrooms', 'extra cheese'],  # 配料列表
}

# 概述所点的比萨。
print(
    f"You ordered a {pizza['crust']}-crust pizza "
    "with the following toppings: ")

for topping in pizza['toppings']:
    print("\t" + topping)
```

```
You ordered a thick-crust pizza with the following toppings:
        mushrooms
        extra cheese
```

每当需要在字典中将一个键关联到多个值时，都可以在字典中嵌套一个列表。

> 如果函数调用`print()`中的字符串很长，可以在合适的位置分行。只需要在每行末尾都加上引号，同时对于第一行以外的其他各行，都在行首加上引号并缩进。这样，`Python`将自动合并圆括号内的所有字符串。

### 6.4.3 在字典中存储字典

可以在字典中嵌套字典，但这样会导致代码比较复杂。

```python
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']}{user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
```

```
Username: aeinstein
        Full name: Alberteinstein
        Location: Princeton

Username: mcurie
        Full name: Mariecurie
        Location: Paris
```

若字典中的字典结构不同，`for`循环内部的代码会比较复杂。

## 6.5 小结

学习了：

1. 如何定义字典，以及如何使用存储在字典中的信息；
2. 如何访问和修改字典中的元素，以及如何遍历字典中的所有信息；
3. 如何遍历字典中所有的键值对、所有的键和所有的值；
4. 如何在列表中嵌套字典、在字典中嵌套列表以及在列表中嵌套字典。
