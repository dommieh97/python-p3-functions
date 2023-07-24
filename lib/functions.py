#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")

def greet(name = "Guido"):
    print(f"Hello, {name}!")

def greet_with_default(name='Hello, programmer!'):
    print(f"{name}")


def add(num1 = 45, num2= 55):
    return num1 + num2

def halve(number = 100):
    return number /2
