[TOC]

# 列表简介

## 3.1 列表是什么

[Python 列表(List)](https://www.runoob.com/python/python-lists.html)

列表由一系列按特定顺序排列的元素组成。可以将任何东西加入列表中。

在`Python`中，用方括号([])表示列表，并用逗号分隔其中的元素。

```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
```

`Python`打印列表时，不仅会输出列表的内部表示，也会打印方括号。

```
['trek', 'cannondale', 'redline', 'specialized']
```

### 3.1.1 访问列表元素

列表是有序集合。根据元素的位置（索引）来访问列表元素。

```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])
```

```
trek
```

### 3.1.2 索引从 0 而不是 1 开始

在`Python`中，第一个列表元素的索引为 0，而不是 1。

```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[1])
print(bicycles[1])
```

```
cannondale
specialized
```

`Python`为访问最后一个列表元素提供了一种特殊语法。通过将索引指定为-1，可让`Python`返回最后一个列表元素。

```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[-1])
```

```
specialized
```

同理，索引-2 返回倒数第二个列表元素...

> 这种语法常用于不知道列表长度的情况下访问列表的最后的元素。

### 3.1.3 使用列表中的各个值

可以像使用其他变量一样来使用列表中的各个值。

```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = f"My first bicycles was a {bicycles[0].title()}."

print(message)
```

```
My first bicycles was a Trek.
```

## 3.2 修改、添加和删除元素

### 3.2.1 修改列表元素

可以修改任意列表元素的值。

```python
motocycles = ['honda', 'yamaha', 'suzuki']
print(motocycles)

motocycles[0] = 'ducati'
print(motocycles)
```

```
['honda', 'yamaha', 'suzuki']
['ducati', 'yamaha', 'suzuki']
```

### 3.2.2 在列表中添加元素

1. 在列表末尾添加元素——`append()`方法

   ```python
   motocycles = ['honda', 'yamaha', 'suzuki']
   print(motocycles)

   motocycles.append('ducati')
   print(motocycles)
   ```

   ```
   ['honda', 'yamaha', 'suzuki']
   ['honda', 'yamaha', 'suzuki', 'ducati']
   ```

2. 在列表中插入元素——`insert()`方法
   `insert()`方法可在列表中的任何位置添加新元素。需要指定元素的索引和值。

   ```python
   motocycles = ['honda', 'yamaha', 'suzuki']

   motocycles.insert(0, 'ducati')
   print(motocycles)
   ```

   值`'ducati'`被插入到了列表的开头。方法`insert()`在索引 0 处添加空间，并将值`'ducati'`存储到这个地方。这种操作将列表中既有的每个元素都右移一个位置。

   ```
   ['ducati', 'honda', 'yamaha', 'suzuki']
   ```

### 3.2.3 从列表中删除元素

1. 使用 `del` 语句删除元素
   使用`del`可删除任意位置处的列表元素，条件是知道其索引。

   ```python
   motocycles = ['honda', 'yamaha', 'suzuki']
   print(motocycles)

   del motocycles[0]
   print(motocycles)
   ```

   删除列表`motocycles`中的第一个元素`'honda'`

   ```
   ['honda', 'yamaha', 'suzuki']
   ['yamaha', 'suzuki']
   ```

2. 使用方法 `pop()`删除元素
   方法`pop()`删除列表末尾的元素，并让你能够接着使用它。

   ```python
   motocycles = ['honda', 'yamaha', 'suzuki']
   print(motocycles)

   popped_motocycle = motocycles.pop()
   print(motocycles)
   print(popped_motocycle)
   ```

   ```
   ['honda', 'yamaha', 'suzuki']
   ['honda', 'yamaha']
   suzuki
   ```

3. 弹出列表中任何位置处的元素
   可以使用`pop()`来删除列表中任意位置的元素，只需在圆括号中指定要删除元素的索引。

   ```python
   motocycles = ['honda', 'yamaha', 'suzuki']

   first_owned = motocycles.pop(0)
   print(f"The first motocycle I owned was a {fisrt_owned.title()}.")
   ```

   ```
   The first motocycle I owned was a honda.
   ```

   使用`pop()`时，被弹出的元素就不再列表中了。

   > 使用`del`语句还是`pop()`方法的判断标准：
   >
   > - 若要从列表中删除一个元素，且不再以任何方式使用它，就使用`del`语句。
   > - 若要在删除元素后还能继续使用它，就使用方法`pop()`。

4. 根据值删除元素
   使用方法`remove()`，删除元素的值。

   ```python
   motocycles = ['honda', 'yamaha', 'suzuki', 'ducati']
   print(motocycles)

   motocycles.remove('ducati')
   print(motocycles)
   ```

   ```
   ['honda', 'yamaha', 'suzuki', 'ducati']
   ['honda', 'yamaha', 'suzuki']
   ```

   > 方法`remove()`只删除第一个指定的值。如果要删除的值可能在列表中出现多次，就需要使用循环来确保将每个值都删除。

## 3.3 组织元素

以特定的顺序呈现列表中的信息。

### 3.3.1 使用方法 sort()对列表 1 永久排序

```python
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
```

方法`sort()`永久性地修改列表元素的排列顺序。

```
['audi', 'bmw', 'subaru', 'toyota']
```

---

还可以按与字母顺序相反的顺序排列列表元素，需要向`sort()`方法传递参数`reverse=True`。

```python
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)
```

```
['toyota', 'subaru', 'bmw', 'audi']
```

### 3.3.2 使用函数 sorted()对列表临时排序

要保留列表元素原来的排列顺序，同时以特定的顺序呈现它们，可使用函数`sorted()`。函数`sorted()`让你能够按特定顺序显示列表元素，同时不影响它们在列表中的原始排列顺序。

```python
cars = ['bmw', 'audi', 'toyota', 'subaru']

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

```

```
Here is the original list:
['bmw', 'audi', 'toyota', 'subaru']

Here is the sorted list:
['audi', 'bmw', 'subaru', 'toyota']

Here is the original list again:
['bmw', 'audi', 'toyota', 'subaru']
```

> - 调用函数`sorted()`后，列表元素的排列顺序并没有变。
> - 若要按与字母顺序相反的顺序显示列表，也可以向函数`sort()`传递参数`reverse=True`

### 3.3.3 倒着打印列表

要反转列表元素的排列顺序，可使用方法`reverse()`。

```python
cars = ['bmw', 'audi', 'toyota', 'subaru']

print(cars)

cars.reverse()
print(cars)
```

```
['bmw', 'audi', 'toyota', 'subaru']
['subaru', 'toyota', 'audi', 'bmw']
```

> 方法`reverse()`永久性修改列表元素的排列顺序，可以再次调用`reverse()`恢复原来的排列顺序。

### 3.3.4 确定列表的长度

使用函数`len()`可以快速获得列表的长度。

```python
cars = ['bmw', 'audi', 'toyota', 'subaru']

print(len(cars))
```

```
4
```

## 3.4 使用列表时避免索引错误

鉴于列表索引差一的特征，这种错误很常见。（索引值从 0 开始计数）

```python
cars = ['bmw', 'audi', 'toyota', 'subaru']

print(cars[4])
```

```
Traceback (most recent call last):
  File "d:/git/Python-learn/Python编程-从入门到实践（第二版）/第一部分 基础知识/code/chapter03/cars.py", line 3, in <module>
    print(cars[4])
IndexError: list index out of range
```

> 每当需要访问最后一个列表元素时，都可使用索引-1。这在任何情况下都行之有效。

## 3.5 小结

1. 列表是什么以及如何使用其中的元素；
2. 如何定义列表以及如何增删元素；
3. 如何对列表进行永久性排序，以及如何展示而进行临时排序；
4. 如何确定列表的长度，以及在使用列表时如何避免索引错误。
