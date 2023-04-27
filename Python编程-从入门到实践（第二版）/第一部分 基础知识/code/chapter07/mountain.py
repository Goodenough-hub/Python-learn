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
