pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:  # 当列表中有cat则执行循环
    pets.remove('cat')

print(pets)
