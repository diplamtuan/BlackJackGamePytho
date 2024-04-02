#items = ['Tuan','Long','Hung','Dieu']
#itemscopy = items[:] # Copy array
#items.sort(key=str.lower)

# Tuples
# Can't modifile
#sorted(items,key=str.lower) # not modifile origin array
#names = ("Roger","Syd")

#names[0] # Roger
#names.index("Roger") # 0
#len(names) # 2

#print("Roger" in names) #True
#names[0:1] # Roger
#print(names[0:1]) # Roger

# sorted không chỉnh sửa mảng gốc
# Example: sorted(names)

############################################################################################################
# Distionary 
# Example: dog = {"name": "Roger","age":8}

# Truy xuất phần tử 
# Example: dog["name"]

# Truy xuat phan tu bang ham get
# Example: dog.get("name")

# Dat gia tri mat dinh
# Example: dog.get("color","brown")

# Xoa mot phan tu
# Example: dog.pop("name")
# Pop method return value cua dog["name"] : Example : Roger

# Xoa mot phan tu cuoi mang
# Example : dog.popitem()
# popitem return cap key va value cua phann tu cuoi : Example: ('age',8)

# Thay doi gia tri
# Example": dog["name"] = "Sys"

# Kiem tra mot key co ton tai trong object khong
# Example: "name" in dog
# return : true

# Lay danh sach cac key
# Example: dog.keys()
# return  dict_keys(["name","age"])

# Co the convert sang list
# Example: list(dog.keys())
# return ["name","age"]

# Lay danh sach cac value
# Example: dog.values()
# return dict_values(["roger",8])

# Co the convert sang list
# Example: list(dog.values())
# return ["roger",8]

# Lay danh sach (key,value)
# Example: dog.items()
# return [("name","roger"),("age",8)]

# Lay do dai phan tu
# Example: len(dog)
# return 2

# Add phan tu moi vao dictionary
# Example dog["favorite food"] = "Meat"

# Xoa phan tu
# Example del dog["color"]

# Copy ra mot ban sao moi
# Example dogCopy = dog.copy()

#############################################################################################
# Sets
# Concept: Not Ordered

# Example: names = {"Roger", "Syd"}

# In ra diem chung set
# Example: set1= {"Roger","Syd"}
# set2 = {"Roger"}
# intersect = set1 & set2
# print(intersect) => {"Roger"}

#List is a collection which is ordered and changeable. Allows duplicate members.
#Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
#Dictionary is a collection which is ordered** and changeable. No duplicate members.

############################################################################################
#FUNCTION
# Example
# def hello(name="My Friend"):
#   print ("Hello "+ name)
# hello()

# Example 2
#def hello(name,age):
#   print ("Hello "+ name + str(age))
# hello("Tuan",22)

# Example 3
# def change(value):
#   value = 2
# value = 1
# change(value)
# print(value) => 1

# Example 4
# def change(value):
#   value["name"]="Long"
#value={"name":"Tuan"}
#change(value)
#print(value) => {"name":"Long"}
 
# Example 5
#def hello(name):
#   if not name:
#       return
#    print("Hello"+name)
#hello(False) => 
#hello("Tuan") => Hello Tuan

# Example 6
#def hello(name):
#    return name,"Tuan",8
#print(hello("Long")) => ("Long","Tuan",8)

##############################################################################################
# Variable Scope
# Example 1
# age = 8
# def test():
#     print(age)
# print(age) => 8
# test() => 8

##############################################################################################
# Nested Function
# Example 1
# def talk(phrase):
#     def say(word):
#         print(word)
#      words = phrase.split(" ")
#      for word in words:
#          say(word)
# talk("I am a beginner person in Python") =>
# I
# am
# a
# beginner
# person
# in
# Python

# Example 2
# def count():
#     count = 0
#     def increment():
#         nonlocal count
#         count = count + 1
#         print(count)
#     increment()
# count() => 1

####################################################################################################
# Closures
#def count():
#    count = 0

#    def increment():
#        nonlocal count
#        count = count + 1
#        return count
#    return increment
#increment = count()
#print(increment()) #1
#print(increment()) #2
#print(increment()) #3

####################################################################################################\
#Object
# Example 1
# age = 8
# print(age.real) # 8
# print(age.imag) # 0
# print(age.bit_length()) # 4

#####################################################################################################
#Loops
# condition =True
# while condition == True:
#       print("Condition is true")
#       condition = False

# items = [1,2,3,4]
# for item in items:
#      print(item)

# for item in range(10)
#      print(item)
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

# Example 3
# items = [1,2,3,4]
# for index, item in enumerate(items):
#     print(index, item)

# continue in loop
# items = [1,2,3,4]
# for item in items:
#     if item == 2
#        continue
#     print(item)
# result : 1, 3 ,4

# break in loop
# items = [1,2,3,4]
# for item in items:
#     if item == 2
#        break
#     print(item)
# result : 1

#######################################################################################################
# classes

# Example 1
#class Dog:
#    def __init__(self,name,age):
#        self.name = name
#        self.age = age
#    def bark(self):
#        print("Woof!")
#
#tuan = Dog("Tuan",10)
#print(tuan.name)    
#print(tuan.age)    
#tuan.bark#()    

# Inheritance
#class Animal:
#   def walk(self):
#        print("Walking...")
#class Dog(Animal):
#    def __init__(self,name,age):
#        self.name = name
#        self.age = age
#    def bark(self):
#        print("Woof!")
#tuan = Dog("Tuan",10)
#tuan.walk()

###############################################################################################################
# Modules
# import dog
# from dog import hello
# hello()

# from lib import dog
# dog.hello()

# from lib.dog import hello
# hello()
#
##############################################################################################
# math for math utilities
# re for regular expressions
# json to work with JSON
# datetime to work with dates
# splite3 to use SQLite
# os for Operating System utilities
# random for random number generation
# statistics for statistics utilities
# requests to perform HTTP network requests
# http to create HTTP servers
# urllib to manage URLS

# Example
# import math
# print(math.sqrt(4))

# Example 2
# from math import sqrt
# print(sqrt(4))

#####################################################################################
# Accepting Arguments

# Example
# import sys
# print(sys.argv)
# commanline => python main.py Tuan 12
# result in commandline => ["main.py", "Tuan", "12"]

####################################################################################
# Lambda functions
# Meanig: Anonymous function
# Example 1
# lambda num : num * 2
# multiply = lambda a,b : a * b
####################################################################################

# map,filter,reduce 

# map example
# numbers = [1,2,3]
# def double(a):
#     return a * 2
# result = map(double,numbers)
# print(list(result)) => [2,4,6]

# example 2
# numbers = [1,2,3]
# double = lambda a : a * 2
# result = map(double,numbers)
# print(list(result)) => [2,4,6]

# example 3
# numbers = [1,2,3]
# result = map(lambda a : a * 2,numbers)
# print(list(result)) => [2,4,6]

# Filter
# Example 1 
# numbers = [1,2,3,4,5,6]
# def isEven(n):
#    return n % 2 == 0
# result = filter(isEven,numbers)
# print(list(result))

# Example 2
#numbers = [1,2,3,4,5,6]
#result = filter(lambda n :n % 2 == 0,numbers)
#print(list(result))

# Without Reduce()
# expenses = [
#    ('Dinner', 80),
#    ('Car repair', 120),
# ]
# sum = 0
# for expense in expenses:
#     sum = sum + expense[1]
# print(sum)

# Using reduce
# from functools import reduce
# expenses = [
#    ('Dinner', 80),
#   ('Car repair', 120),
#]
# sum = reduce(lambda a,b: a[1] + b[1],expenses)
# print(sum)

#######################################################################################
# recursion (de quy)

# def factorial(x):
#    if x == 1: return 1
#   return x * factorial(x-1)

#print(factorial(3)) #6
#print(factorial(4)) #24
#print(factorial(5)) #120

########################################################################################
# decorators

# def logtime(func):
#    def wrapper():
#        print("Before")
#        val = func()
#        print("After")
#        return val
#    return wrapper

# @logtime
# def hello():
#    print("Hello")

# hello()
# CMD : "Before"
# CMD : "Hello"
# CMD : "After"

############################################################################################
# docstrings
# Example
# """ Dip
# Lam
# Tuan """

#############################################################################################
# annotations
# Example
# def increment(n: int) -> int:
#      return n + 1

# Example for variable
# count: int = 0

##############################################################################################
# Exception
# Example
# try:
#   result = 2 / 0
# except ZeroDivisionError:
#    print("Cannot dive by zero")
# finally:
#    result = 1
# print(result) # 1

# Example 2
# try:
#    raise Exception("An Error")
# except Exception as error:
#    print(error)

# class DogNotFoundException(Exception):
#    pass

# try:
#    raise DogNotFoundException()
# except DogNotFoundException:
#    print("Dog not found")

#####################################################################################################
# with

#####################################################################################################
# pip

# Example
# pip install requests

# Upgrade Packages
# Example
# pip install -U requests

# Uninstall Packages
# Example
# pip uninstall requests

# Show information package
# Example
# pip show requests

#######################################################################################################
# list compressions
# create list concise way(ngắn gọn)
# Example list compressions
# numbers = [1,2,3,4,5]
# numbers_power_2 = [n**2 for n in numbers]
# print(numbers_power_2)

# Regular
# numbers_power_2=[]
# for n in numbers:
#    numbers_power_2.append(n**2)

# map method
# numbers_power_2 = list(map(lambda n: n**2,numbers))

###########################################################################################################
# polymorphism(da hinh)

# class Dog:
#    def eat(self):
#       print("Dog eating...")

# class Cat:
#    def eat(self):
#        print("Cat eating...")

# cat = Cat()
# dog = Dog()

# dog.eat()
# cat.eat()
##############################################################################################################
# operator Overloading
# class Dog():
#    def __init__(self,name,age):
#        self.name = name
#        self.age = age
#    def __gt__(self,other):
#        return True if self.age > other.age else False

# Tuan1 = Dog("Tuan",10)
# Tuan2 = Dog("Tuan2",12)
# print(Tuan1 > Tuan2) # False



