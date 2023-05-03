[TOC]

# 类

面向对象编程。编写类时，定义一大类对象都有的通用行为。基于类创建对象时，每个对象都自动具备这种通用行为，然后可根据需要赋予每个对象独特的个性。根据类来创建对象称为实例化。

## 9.1 创建和使用类

使用类几乎可以模拟任何东西。

### 9.1.1 创建 Dog 类

根据`Dog`类创建的每个实例都将存储名字和年龄，我们赋予小狗蹲下(`sit()`)和打滚(`roll_over()`)的能力：

```python
class Dog:
    """一次模拟小狗的简单尝试。"""

    def __init__(self, name, age):
        """初始化属性name和age"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗收到命令时蹲下"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """模拟小狗收到命令时打滚"""
        print(f"{self.name} rolled over!")
```

- 定义了一个名为`Dog`的类。
  Python 中，首字母大写的名称指的是类。这个类定义中没有圆括号，因为要从空白创建这个类。

#### 方法`__init__()`

类中的函数称为方法。方法`__init__()`是一个特殊方法，每当你根据`Dog`类==创建新实例时==，`Python`都会自动==运行==它。

在这个方法的名称中，开头和末尾各有两个下划线，这是一种约定，旨在避免`Python`默认方法与普通方法发生名称冲突。务必确保`__init__()`的两边都有两个下划线，否则当你使用类时，将不会自动调用这个方法。

- 方法`__init__()`定义成包含三个形参：`self`、`name`和`age`。
  在方法的定义中，形参`self`必不可少，而且必须位于其他形参的前面。在`Python`调用这个方法创建实例时，将自动传入实参`self`。每个与实例相关联的方法调用都自动传递参数`self`，它是一个指向实例本身的引用，让实例能够访问类中的属性和方法。
  创建`Dog`实例时，`Python`将调用`Dog`类的方法`__init__()`。我们将通过实参向`Dog()`传递名字和年龄，`self`会自动传递，因此不需要传递它。每当根据`Dog`类创建实例时，都只需给最后两个形参（`name`和`age`）提供值。

- 方法`__init__()`处定义的两个变量都有前缀`self`。以`self`为前缀的变量可供类中的所有方法使用，可以通过类的任何实例来访问。`self.name = name`获取与形参`name`相关联的值，并将其赋值给变量`name`，然后该变量被关联到当前创建的实例。`self.age = age`的作用与此类似。像这样可以通过实例访问的变量称为属性。

---

`Dog`类还定义了另外两个方法：`sit()`和`roll_over()`。这些方法执行时不需要额外的信息，因此它们只有一个形参`self`。

### 9.1.2 根据类创建实例

创建表示特定小狗的实例：

```python
class Dog:
    """一次模拟小狗的简单尝试。"""

    def __init__(self, name, age):
        """初始化属性name和age"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗收到命令时蹲下"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """模拟小狗收到命令时打滚"""
        print(f"{self.name} rolled over!")


my_dog = Dog('Willie', 6)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog's is {my_dog.age} years old.")
```

```
My dog's name is Willie.
My dog's is 6 years old.
```

方法`__init__()`创建一个表示特定小狗的实例，并使用提供的值来设置属性`name`和`age`。

1. 访问属性
   要访问实例的属性，可使用句点表示。访问`my_dog`的属性`name`的值：

   ```python
   my_dog.name
   ```

   在`Dog`类中引用这和属性时，使用的是`self.name`。

2. 调用方法
   根据`Dog`类创建实例后，就能使用句点表示法来调用`Dog`类中定义的任何方法。

   ```python
   class Dog:
       --snip--

   my_dog = Dog('Willie', 6)
   my_dog.sit()
   my_dog.roll_over()
   ```

   要调用方法，可指定实例的名称和要调用的方法，并用句点分隔。遇到代码`my_dog.sit()`时，`Python`在类`Dog`中查找方法`sit()`并运行其代码。

   ```
   Willie is now sitting.
   Willie rolled over!
   ```

3. 创建多个实例
   可按需求根据类创建任意数量的实例。

   ```python
   class Dog:
   """一次模拟小狗的简单尝试。"""

   def __init__(self, name, age):
       """初始化属性name和age"""
       self.name = name
       self.age = age

   def sit(self):
       """模拟小狗收到命令时蹲下"""
       print(f"{self.name} is now sitting.")

   def roll_over(self):
       """模拟小狗收到命令时打滚"""
       print(f"{self.name} rolled over!")


   my_dog = Dog('Willie', 6)
   your_dog = Dog('Lucy', 3)

   print(f"My dog's name is {my_dog.name}.")
   print(f"My dog is {my_dog.age} years old.")
   my_dog.sit()

   print(f"\nYour dog's name is {your_dog.name}.")
   print(f"Your dog is {your_dog.age} years old.")
   your_dog.sit()
   ```

   创建两条小狗，每条小狗都是一个独立的实例，有自己的一组属性，能够执行相同的操作。

   ```
   My dog's name is Willie.
   My dog is 6 years old.
   Willie is now sitting.

   Your dog's name is Lucy.
   Your dog is 3 years old.
   Lucy is now sitting.
   ```

## 9.2 使用类的实例

### 9.2.1 Car 类

```python
class Car:
    """一次模拟汽车的简单尝试。"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性。"""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """返回整洁的描述性信息。"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()


my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
```

```
2019 Audi A4
```

### 9.2.2 给属性指定默认值

创建实例时，有些属性无须通过形参来定义，可在方法`__init()__`中为其指定的默认值。

```python
class Car:
    """一次模拟汽车的简单尝试。"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性。"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性信息。"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车里程的消息。"""
        print(f"This car has {self.odometer_reading} miles on it.")


my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
```

`Python`创建一个名为`odometer_reading`的属性，并将其初始值设置为 0。`read_odometer()`方法打印汽车的里程。

```
2019 Audi A4
This car has 0 miles on it.
```

### 9.2.3 修改属性的值

有三种方式修改属性的值：直接通过实例进行修改，通过方法进行设置，以及通过方法进行递增（增加特定的值）。

#### 1. 直接修改属性的值

要修改属性的值，最简单的方法是通过实例直接访问它。

```python
class Car:
    """一次模拟汽车的简单尝试。"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性。"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性信息。"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车里程的消息。"""
        print(f"This car has {self.odometer_reading} miles on it.")


my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()
```

使用句点表示法直接访问并设置汽车的属性`odometer_reading`。`Python`在实例`my_new_car`中找到属性`odometer_reading`，并将其值设置为 23：

```
2019 Audi A4
This car has 23 miles on it.
```

#### 2. 通过方法修改属性的值

编写对属性进行 1 更新的方法。这样就无须直接访问属性，而可将值传递给方法。

```python
class Car:
    """一次模拟汽车的简单尝试。"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性。"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性信息。"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车里程的消息。"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """将里程表读书设置为指定的值。"""
        self.odometer_reading = mileage


my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(23)
my_new_car.read_odometer()
```

对`Car`类添加了方法`update_odometer()`。这个方法接受一个里程值，并将其赋给`self.odometer_reading`。

```
2019 Audi A4
This car has 23 miles on it.
```

---

可对方法`update_odometer()`进行扩展，使其在修改里程表读数时做些额外的工作。禁止任何人将里程表读数回调：

```python
class Car:
    --snip--

    def update_odometer(self, mileage):
        """
        将里程表读数设置为指定的值。
        禁止将里程表读数往回调。
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
```

`update_odometer()`在修改属性前检查指定的读数是否合理。如何新指定的里程（`mileage`）大于或等于原来的里程（`self.odometer_reading`），就将里程表读数改为新指定的里程；否则发出警告，指出不能将里程表往回调。

#### 3. 通过方法对属性的值进行递增

有时候需要将属性值递增特定的量，而不是将其设置为全新的值。

```python
class Car:
    """一次模拟汽车的简单尝试。"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性。"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性信息。"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车里程的消息。"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """将里程表读书设置为指定的值。"""
        self.odometer_reading = mileage

    def increment_odometer(self, miles):
        """将里程表读数增加指定的量。"""
        self.odometer_reading += miles


my_used_car = Car('subaru', 'outback', 2015)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()
```

```
2015 Subaru Outback
This car has 23500 miles on it.
This car has 23600 miles on it.
```

## 9.3 继承

一个类继承另一个类时，将自动获得另一个类的所有属性和方法。原有的类称为父类，而新类称为子类。子类继承了父类的所有属性和方法，同时还可以定义自己的属性和方法。

### 9.3.1 子类的方法`__init__()`

在既有类的基础上编写新类时，通常要调用父类的方法`__init__()`。这将初始化在父类`__init__()`方法中定义的所有属性，从而让子类包含这些属性。

- 创建子类时，父类必须包含在当前文件中，且位于子类的前面。
- 定义子类时，必须在圆括号内指定父类的名称。
- `super()`是一个特殊函数，让你能够调用父类的方法。

```python
class Car:
    """一次模拟汽车的简单尝试。"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性。"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性信息。"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车里程的消息。"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """将里程表读书设置为指定的值。"""
        self.odometer_reading = mileage

    def increment_odometer(self, miles):
        """将里程表读数增加指定的量。"""
        self.odometer_reading += miles


class ElectricCar(Car):
    """电动汽车的独特之处。"""

    def __init__(self, make, model, year):
        """初始化父类的属性。"""
        super().__init__(make, model, year)


my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
```

```
2019 Tesla Model S
```

### 9.3.2 给子类定义属性和方法

让一个类继承另一个类后，就可以添加区分子类和父类所需的新属性和新方法了。

```python
class Car:
    """一次模拟汽车的简单尝试。"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性。"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性信息。"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车里程的消息。"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """将里程表读书设置为指定的值。"""
        self.odometer_reading = mileage

    def increment_odometer(self, miles):
        """将里程表读数增加指定的量。"""
        self.odometer_reading += miles


class ElectricCar(Car):
    """电动汽车的独特之处。"""

    def __init__(self, make, model, year):
        """
        初始化父类的属性。
        再初始化电动汽车特有的属性。
        """
        super().__init__(make, model, year)
        self.battery_size = 75

    def describe_battery(self):
        """打印一条描述电瓶容量的消息。"""
        print(f"This car has a {self.battery_size}-kwh battery.")


my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
```

添加新属性`self.battery_size`，并设置其初始值（75）。根据`ElectricCar`类创建的所有实例都将包含该属性，但所有`Car`实例都不包含它。还添加了一个名为`describe_battery()`的方法，打印有关电瓶的信息。

```
2019 Tesla Model S
This car has a 75-kwh battery.
```

### 9.3.3 重写父类的方法

对于父类的方法，只要它不符合子类模拟的实物的行为，都可以进行重写。使用继承时，可让子类保留从父类那里继承额而来的精华，而剔除不需要的糟粕。
在子类中定义个与要重写的父类方法同名的方法，这样`Python`将不会考虑这个父类方法。

假设`Car`类有一个名为`fill_gas_tank()`的方法，这对电动车毫无意义，可以重写它。

```python
class ElectricCar(Car):
    --snip--

    def fill_gas_tank(self):
        """电动车没有油箱。"""
        print("This car doesn't need a gas tank!")
```

若有人对电动车调用`fill_gas_tank()`这个方法，`Python`将忽略`Car`类中的`full_gas_tank()`方法，执行`ElectricCar`类中的方法。

### 9.3.4 将实例用作属性

可以将大型类拆分成多个协同工作的小类。

```python
class Car:
    """一次模拟汽车的简单尝试。"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性。"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性信息。"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车里程的消息。"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """将里程表读书设置为指定的值。"""
        self.odometer_reading = mileage

    def increment_odometer(self, miles):
        """将里程表读数增加指定的量。"""
        self.odometer_reading += miles


class Battery:
    """一次模拟电动汽车电瓶的简单尝试。"""

    def __init__(self, battery_size=75):
        """初始化电瓶的属性。"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息。"""
        print(f"This car has a {self.battery_size}-kwh battery.")

    def get_range(self):
        """打印一条消息，指出电瓶的续航里程。"""
        if self.battery_size == 75:
            range = 260
        elif self.batter_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge.")


class ElectricCar(Car):
    """电动汽车的独特之处。"""

    def __init__(self, make, model, year):
        """
        初始化父类的属性。
        再初始化电动汽车特有的属性。
        """
        super().__init__(make, model, year)
        self.battery = Battery()

    def describe_battery(self):
        """打印一条描述电瓶容量的消息。"""
        print(f"This car has a {self.battery_size}-kwh battery.")


my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
```

`Battery`这个类是`ElectricCar`类中的一个属性。

```
2019 Tesla Model S
This car has a 75-kwh battery.
This car can go about 260 miles on a full charge.
```

### 9.3.5 模拟实物

对现实世界的建模方法有多种，找出效率最高的表示法。

## 9.4 导入类

`Python`允许将类存储在模块中，然后在主程序中导入所需的模块。

### 9.4.1 导入单个类

导入类是一种有效的编程方式。通过将这个类移到一个模块中并导入该模块，依然可以使用其所有功能，但主程序文件变得整洁而易于阅读，还能够将大部分逻辑存储在独立的文件中。

模块`Car.py`，只包含`Car`类的代码：

```python
"""一个可用于表示汽车的类。"""


class Car:
    """一次模拟汽车的简单尝试。"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性。"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性信息。"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车里程的消息。"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        将里程表读书设置为指定的值。
        拒绝将里程表往回调。
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """将里程表读数增加指定的量。"""
        self.odometer_reading += miles
```

在`my_car.py`中导入`Car`类并创建实例：

```python
from car import Car

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()
```

```
2019 Audi A4
This car has 23 miles on it.
```

### 9.4.2 在一个模块中存储多个类

可根据需要在一个模块中存储任意数量的类。

`Battery`类和`ElectricCar`类都可以帮助模拟汽车，将它们都加入模块`car.py`中。

```python
"""一组用于表示燃油车汽车和电动汽车的类。"""


class Car:
    """一次模拟汽车的简单尝试。"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性。"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性信息。"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车里程的消息。"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        将里程表读书设置为指定的值。
        拒绝将里程表往回调。
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """将里程表读数增加指定的量。"""
        self.odometer_reading += miles


class Battery:
    """一次模拟电动汽车电瓶的简单尝试。"""

    def __init__(self, battery_size=75):
        """初始化电瓶的属性。"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息。"""
        print(f"This car has a {self.battery_size}-kwh battery.")

    def get_range(self):
        """打印一条消息，指出电瓶的续航里程。"""
        if self.battery_size == 75:
            range = 260
        elif self.batter_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge.")

class ElectricCar(Car):
    """电动汽车的独特之处。"""

    def __init__(self, make, model, year):
        """
        初始化父类的属性。
        再初始化电动汽车特有的属性。
        """
        super().__init__(make, model, year)
        self.battery = Battery()
```

新建一个名为`my_electric_car.py`的文件，导入`ElectricCar`类，并创建一辆电动汽车。

```python
from car import ElectricCar

my_tesla = ElectricCar('tesla', 'model s', '2019')

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
```

```
2019 Tesla Model S
This car has a 75-kwh battery.
This car can go about 260 miles on a full charge.
```

### 9.4.3 从一个模块中导入多个类

可以根据需要在程序文件中导入任意数量的类。从一个模块中导入多个类时，用逗号分隔各个类。导入必要的类后，就可根据需要创建每个类的任意数量实例。

若要在同一个程序中创建普通汽车和电动汽车，就需要将`Car`类和`ElectricCar`类都导入：

```python
from car import Car, ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())
```

```
2019 Volkswagen Beetle
2019 Tesla Roadster
```

### 9.4.4 导入整个模块

可以导入整个模块，再使用句点表示法访问需要的类。由于创建类实例的代码都包含模块名，所以不会与当前文件使用的任何名称发生冲突。

导入`module_name`，使用语法`moule_name.ClassName`访问需要的类。

```python
import car

my_beetle = car.Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = car.ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())
```

```
2019 Volkswagen Beetle
2019 Tesla Roadster
```

### 9.4.5 导入模块中的所有类

要导入模块中的每个类，可以使用语法：

```python
from module_name import *
```

不推荐这种导入方式：

1. 若能够只看`import`语句就知道程序使用了哪些类，将大有裨益。
2. 这种方式可能会引发名称方面的迷惑。

### 9.4.6 在一个模块中导入另一个模块

有时候需要将类分散到多个模块中，以免模块太大或在同一个模块中存储不相关的类。将类存储在多个模块中，可能会出现一个模块中的类依赖于另一个模块中的类。在这种情况下，可在前一个模块中导入必要的类。

`Car`类存储在`car.py`模块中：

```python
"""一组用于表示燃油车汽车和电动汽车的类。"""


class Car:
    """一次模拟汽车的简单尝试。"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性。"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性信息。"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车里程的消息。"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        将里程表读书设置为指定的值。
        拒绝将里程表往回调。
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """将里程表读数增加指定的量。"""
        self.odometer_reading += miles
```

`electric_car.py`模块中存储`ElectricCar`类和`Battery`类，并将`Car`类导入该模块：

```python
"""一组可用于表示电动汽车的类。"""


from car import Car


class Battery:
    """一次模拟电动汽车电瓶的简单尝试。"""

    def __init__(self, battery_size=75):
        """初始化电瓶的属性。"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息。"""
        print(f"This car has a {self.battery_size}-kwh battery.")

    def get_range(self):
        """打印一条消息，指出电瓶的续航里程。"""
        if self.battery_size == 75:
            range = 260
        elif self.batter_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge.")


class ElectricCar(Car):
    """电动汽车的独特之处。"""

    def __init__(self, make, model, year):
        """
        初始化父类的属性。
        再初始化电动汽车特有的属性。
        """
        super().__init__(make, model, year)
        self.battery = Battery()

    def describe_battery(self):
        """打印一条描述电瓶容量的消息。"""
        print(f"This car has a {self.battery_size}-kwh battery.")
```

分别从每个模块中导入类，根据需要创建任何类型的汽车：

```python
from car import Car
from electric_car import ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())
```

```
2019 Volkswagen Beetle
2019 Tesla Roadster
```

### 9.4.7 使用别名

在`chapter08`中，可以给模块指定别名。导入类时，也可以使用`as`关键字指定别名。

在`import`语句中给`ElectricCar`指定别名：

```python
from electic_car import ElectricCar as EC
```

当需要创建电动汽车实例时，都可以使用这个别名：

```python
my_tesla = EC('tesla', 'roadster', 2019)
```

### 9.4.8 自定义工作流程

先尽可能在一个文件中完成所有工作，确定一切都能正确运行后，再将类移到独立的模块中。

若喜欢模块和文件的交互方式，可在项目开始时就尝试将类存储到模块中。

## 9.5 Python 标准库

[`Python`标准库](https://docs.python.org/zh-cn/3/library/index.html)是一组模块，我们安装的`Python`都包含它。可以使用标准库中的任何函数和类，只需在程序开头包含一条简单的`import`语句即可。

[模块`random`](https://docs.python.org/zh-cn/3/library/random.html):

- 函数`randint()`:
  将两个整数作为参数，并随机返回一个位于这两个整数之间（含）的整数。
  ```python
  >>> from random import randint
  >>> randint(1, 6)
  4
  ```
- 函数`choice()`：
  它将一个列表或元组作为参数，并随机返回其中一个元素。
  ```python
  >>> from random import choice
  >>> players = ['charles', 'martina', 'michael', 'florence', 'eli']
  >>> first_up = choice(players)
  >>> first_up
  'michael'
  ```

创建与安全相关的应用程序时，请不要使用模块`random`，但该模块可以很好地用于创建众多有趣的项目。

> 还可以从其他地方下载外部模块。第二部分的每个项目都需要使用外部模块。

## 9.6 类编码风格

类名采用驼峰命名法，即将类名中的每个单词的首字母都大写，而不使用下划线。实例名和模块名都采用小写格式，并在单词之间加上下划线。

对于每个类，都紧跟在类定义后面包含一个文档字符串。这种文档字符串简要地描述类的功能，并遵循编写函数的文档字符串时采用的格式约定。每个模块也都应包含一个文档字符串，对其中的类可用于做什么进行描述。

可使用空行来组织代码，但不要滥用。在类中，可使用一个空行来分隔方法；而在模块中，可使用两个空行来分隔类。

需要同时导入标准库中的模块和你编写的模块时，先编写导入的标准库模块的`import`语句，再添加空行，然后编写导入你自己编写的模块的`import`语句。在包含多条`import`语句的程序中，这种做法让人更容易明白程序使用的各个模块都来自何处。

## 9.7 小结

在本章中，学习了：

1. 如何编写类；
2. 如何使用属性在类中存储信息，以及如何编写方法，以让类具备所需的行为；
3. 如何编写方法`__init__()`，以便根据类创建包含所需属性的实例；
4. 如何修改实例的属性，包括直接修改以及通过方法进行修改；
5. 使用继承可简化相关类的创建工作，以及将一个类的实例用作另一个类的属性可让类更加简洁；
6. 通过将类存储在模块中，并在需要使用这些类的文件中导入它们，可让项目组织有序；
7. 学习了`Python`标准库，并见识了一个使用模块`random`的示例；
8. 学习了编写类时应遵循的`Python`约定。
