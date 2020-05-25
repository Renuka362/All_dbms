"""The module echo

This is the "echo" module, providing some useless functions!
"""
from .reverse import reverse_sound
from ..filters.equalizer import print_equalizer    

def func1():
    print("echo function func1 has been called!")


def func2():
    print("echo function func2 has been called!")


def func3():
    print("echo function func3 has been called!")


def print_echo():
    print("Echo Echo")
    reverse_sound()
    print_equalizer()

print("Module echo.py has been loaded!")

print_echo()
