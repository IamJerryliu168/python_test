
# coding=utf-8

name = "abcde"

print(name)

value = name.find("cd",0,6)

print(value)


name2 = "AAss张三aaa"

value2 = name2.find("里三",0,len(name2))

print(value2)

value3 = name2.index("张三",0,len(name2))
print(value3)


if name2.find("张三",0,len(name2)) > 0 : 
	print("this person is 张三")
else: 
    print("this person is not 张三")

