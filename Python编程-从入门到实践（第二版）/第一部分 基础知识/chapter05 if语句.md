[TOC]

# if 语句

## 5.1 一个简单示例

```python
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if (car == 'bmw'):
        print(car.upper())
    else:
        print(car.title())
```

```
Audi
BMW
Subaru
Toyota
```

## 5.2 条件测试

每条`if`语句的核心都是一个值为`True`或`False`的表达式，这种表达式称为条件测试。`Python`根据条件测试的值为`True`还是`False`来决定`if`语句中的代码。如果条件测试的值为`True`，`Python`就执行紧跟在`if`语句后面的代码；如果为`False`，`Python`就忽略这些代码。

### 5.2.1 检查是否相等

大多数测试条件将一个变量的当前值同特定值进行比较。最简单的条件测试检测变量的值是否与特定值相等：

```
>>> car = 'bmw'
>>> car == 'bmw'
True
```

> - 一个等号表示赋值操作。
> - 两个等号表示相等操作，两边的值相等时返回`True`，否则返回`False`。

### 5.2.2 检查是否相等时忽略大小写

在`Python`中检查是否相等时区分大小写。

```
>>> car = 'Audi'
>>> car == 'audi'
False
```

---

若大小写无关紧要，只想检查变量的值，可将变量的值转换为小写，再进行比较：

```
>>> car = 'Audi'
>>> car.lower() == 'audi'
True
>>> car
'Audi'
```

> 方法`lower()`并不会改变原变量的值。

### 5.2.3 检查是否不相等

判断两个值不等，可使用惊叹号和等号（!=）。

```python
requested_topping = 'mushrooms'

if(requested_topping != 'anchovies'):
    print("Hold the anchovies")
```

```
Hold the anchovies
```

### 5.2.4 数值比较

- 检查相等：
  ```
  >>> age = 18
  >>> age == 18
  True
  ```
- 检查不等：

  ```python
  answer = 17

  if answer != 42:
      print("That is not the correct answer. Please try again!")
  ```

  ```
  That is not the correct answer. Please try again!
  ```

- 条件语句中可包含各种数学比较，如小于、小于等于、大于、大于等于：
  ```
  >>> age = 19
  >>> age < 21
  True
  >>> age <= 21
  True
  >>> age > 21
  False
  >>> age >= 21
  False
  ```

### 5.2.5 检查多个条件

同时检查多个条件。

1. 使用 and 检查多个条件
   要检查是否两个条件都为`True`，可使用关键字`and`将两个条件测试合二为一。如果每个测试都通过了，整个表达式就为`True`；如果至少一个测试没有通过，整个表达式就为`False`。

```
>>> age = 19
>>> age < 21
True
>>> age <= 21
True
>>> age > 21
False
>>> age >= 21
False
>>> age_0 = 32
>>> age_1 = 18
>>> age_0 >= 21 and age_1 >= 24
False
>>> age_1 = 22
>>> age_0 >= 21 and age_1 >= 21
True
```

为改善可读性，可将每个测试分别放在一对圆括号内：

```
(age_0 >= 21) and (age_1 >= 21)
```

2. 使用 or 检查多个条件
   关键字`or`也能够检查多个条件，但至少一个条件满足，就能通过整个测试。仅当两个测试都没有通过时，使用`or`的表达式才为`False`。

```
>>> age_0 = 22
>>> age_1 = 18
>>> age_0 >= 21 or age_1 >= 21
True
>>> age_0 = 18
>>> age_0 >= 21 or age_1 >= 21
False
```

### 5.2.6 检查特定值是否包含在列表中

要判断特定的值是否包含在列表中，可使用关键字`in`。

```
>>> requested_toppings = ['mushrooms', 'onions', 'pineapple']
>>> 'mushrooms' in requested_toppings
True
>>> 'pepperoni' in requested_toppings
False
```

### 5.2.7 检查特定值是否不包含在列表中

要判断特定的值是否不包含在列表中，可使用关键字`not in`。

```python
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")
```

```
Marie, you can post a response if you wish.
```

### 5.2.8 布尔表达式

布尔表达式是条件测试的别名。与条件表达式一样，布尔表达式的结果要么为`True`，要么为`False`。布尔值通常用于记录条件。

```
game_active = True
can_edit = False
```

> 在跟踪程序状态或程序中重要的条件方面，布尔值提供了一种高效的方式。

## 5.3 if 语句

### 5.3.1 简单的 if 语句

最简单的`if`语句只有一个测试和一个操作：

```
if conditional_test:
    do something
```

```python
age = 19
if age >= 18:
    print("You are old enough to vate!")
```

```
You are old enough to vate!
```

### 5.3.2 if-else 语句

在条件测试通过时执行一个操作，在没有操作时执行另一个操作。

```python
age = 17
if age >= 18:
    print("You are old enough to vate!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please registered to vote as soon turn 18!")
```

```
Sorry, you are too young to vote.
Please registered to vote as soon turn 18!
```

### 5.3.3 if-elif-else 结构

检查超过两个的情形。依次检查每个条件测试，直到遇到通过了的条件测试。

```python
age = 12

if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admisson cost is $25.")
else:
    print("Your admission cost is $40.")
```

```
Your admission cost is $40.
```

修订代码：

```python
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40
print(f"Your admission cost is ${price}.")
```

### 5.3.4 使用多个 elif 代码块

可根据需要使用任意数量的`elif`代码。

```python
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20

print(f"Your admission cost is ${price}.")
```

```
Your admission cost is $25.
```

### 5.3.5 省略 else 代码块

`Python`并不要求`if-else`结构必须有`else`代码块。在一些情况下，使用`elif`语句代替`else`代码块来处理特定的情形更加清晰。

```python
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20

print(f"Your admission cost is ${price}.")
```

```
Your admission cost is $25.
```

### 5.3.6 测试多个条件

`if-elif-else`结构功能强大，但仅适合用于只有一个条件满足的条件：遇到通过了的测试后，`Python`就==跳过余下的测试==。这种行为效率高，能够测试一个特定的条件。
然而，有些时候必须检查你关心的所有条件。在这种情况下，应使用一系列不包含`elif`和`else`代码块的简单`if`语句。在可能有多个条件为`True`且需要在每个条件为`True`时都采取相应措施时，适合使用这种方法。

```python
requested_topping = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_topping: # 蘑菇
    print("Adding mushrooms.")
if 'pepperoni' in requested_topping: # 辣香肠
    print("Adding pepperoni.")
if 'extra cheese' in requested_topping: # 多加芝士
    print("Adding extra cheese.")

print("\nFinished making your pizza!")
```

```
Adding mushrooms.
Adding extra cheese.

Finished making your pizza!
```

## 5.4 使用 if 语句处理列表

### 5.4.1 检查特殊元素

```python
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!")
```

```
Adding mushrooms.
Sorry, we are out of green peppers right now.
Adding extra cheese.

Finished making your pizza!
```

### 5.4.2 确定列表不是空的

在`if`语句中将列表名用作条件表达式时，`Python`将在列表至少包含一个元素时返回`True`，并在列表为空时返回`False`。

```python
requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")
```

```
Are you sure you want a plain pizza?
```

### 5.4.3 使用多个列表

```python
available_toppings = ['mushrooms', 'olives',
                      'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {ResourceWarning}.")

print("\nFinished making your pizza!")
```

```
Adding mushrooms.
Sorry, we don't have <class 'ResourceWarning'>.
Adding extra cheese.

Finished making your pizza!
```

## 5.5 设置 if 语句的格式

在条件测试的格式设置方面，`PEP 8`提供的唯一建议是，在诸如`==`、`>=`、`<=`等比较运算符两边各添加一个空格。

```
if age < 4:
```

空格不会影响`Python`对代码的解读，而只是让代码阅读起来更加容易。

## 5.6 小结

本章学习了：

1. 如何编写结果要么为`True`要么为`False`的条件测试；
2. 如何编写简单的 `if` 语句、`if-else` 语句和 `if-elif-else` 语句，并且在程序中使用这些结构来测试特定的条件，以确定这些条件是否满足；
3. 如何在利用高效的 `for` 循环的同时，以不同于其他元素的方式对特定的列表元素进行处理。
4. 再次学习了`Python`就代码格式提出的建议，保证代码易于阅读。
