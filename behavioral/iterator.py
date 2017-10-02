#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
http://ginstrom.com/scribbles/2007/10/08/design-patterns-python-style/
Implementation of the iterator pattern with a generator
ジェネレータを用いたiterator(イテレータ)パターンの例
"""

from __future__ import print_function


def count_to(count):
    """数を名前で数え上げます。最大で５(five)までです。
       この関数の型がgenerator型です。"""
    numbers = ["one", "two", "three", "four", "five"]
    for number in numbers[:count]:
        yield number

# generatorを試します。
count_to_two = lambda: count_to(2)
count_to_five = lambda: count_to(5)

print('Counting to two...')
for number in count_to_two():
    print(number, end=' ')

print()

print('Counting to five...')
for number in count_to_five():
    print(number, end=' ')

print()

# それぞれの関数呼び出しの型が何かを確認しましょう。
print("count_to_two        type is " + str(type(count_to_two)))
print("lambda: count_to(2) type is " + str(type(lambda: count_to(2))))
print("count_to(2)         type is " + str(type(count_to(2))))


### OUTPUT ###
# Counting to two...
# one two
# Counting to five...
# one two three four five
# count_to_two        type is <class 'function'>
# lambda: count_to(2) type is <class 'function'>
# count_to(2)         type is <class 'generator'>
