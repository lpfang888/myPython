#!/usr/bin/python3
# coding=utf-8

class MyClass:
    id: int = 1
    name: str = "fanglp"

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def my_function(self):
        return "id:{:d},name:{}".format(self.id, self.name)


# 实例化类
# x = MyClass(2, "xiaoming")
x = MyClass(2, "xiaoming")
print(x.id)
print(x.name)
print(x.my_function())

print("====================================================================")


class Parent:
    def my_method(self):
        print("调用父级方法")


class Child(Parent):
    def my_method(self):
        print("调用子类方法")


c = Child()
c.my_method()

super(Child, c).my_method()
