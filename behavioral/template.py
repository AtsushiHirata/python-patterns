#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""http://ginstrom.com/scribbles/2007/10/08/design-patterns-python-style/

Pythonで書いたTemplate(テンプレート)パターンのサンプルコード
Skeletons,Getters,Actionsで二つずつ用意したメソッドを、make_templateメソッドの引数として与えて、動作するメソッドのリストtemplatesを作っている。
最後にそのtemplatesからメソッドをイテレータで取り出し、実行している。
"""

ingredients = "spam eggs apple"
line = '-' * 10


# Skeletons
def iter_elements(getter, action):
    """Template skeleton that iterates items
    要素を順次処理するテンプレートの骨組み"""
    # 引数として受け取ったgetter,actionを使用。
    # getterはグローバル変数ingredientsの文字列をリスト化するメソッド。getter()が実行された結果、リストに置き換わる。
    # このリストから要素を一つづつ「順に」取り出して、elementにセット。
    # 引数actionはelementを表示するアルゴリズムを内包したメソッド。
    # print(line)で画面に区切り線を表示。
    for element in getter():
        action(element)
        print(line)


def rev_elements(getter, action):
    """Template skeleton that iterates items in reverse order
    要素を逆順に処理するテンプレートの骨組み"""
    # 引数として受け取ったgetter,actionを使用。
    # getterはグローバル変数ingredientsの文字列をリスト化するメソッド。getter()が実行された結果、リストに置き換わる。
    # このリストから要素を一つづつ「逆順に」取り出して、elementにセット。
    # 引数actionはelementを表示するアルゴリズムを内包したメソッド。
    # print(line)で画面に区切り線を表示。
    for element in getter()[::-1]:
        action(element)
        print(line)


# Getters
def get_list():
    """リストをスペースで区切って、ワードのリストにして返す"""
    return ingredients.split()


def get_lists():
    """リストを単文字のリストのリストにして返す"""
    return [list(x) for x in ingredients.split()]


# Actions
def print_item(item):
    print(item)


def reverse_item(item):
    print(item[::-1])


# Makes templates
def make_template(skeleton, getter, action):
    """Instantiate a template method with getter and action"""
    def template():
        skeleton(getter, action)
    return template

# Create our template functions
# 面白いのは、関数のリストをイテレートして実行しているところ。
templates = [make_template(s, g, a)
             for g in (get_list, get_lists)
             for a in (print_item, reverse_item)
             for s in (iter_elements, rev_elements)]

# Execute them
for template in templates:
    template()

### OUTPUT ###
# spam          iter_elements(get_list,print_item)
# ----------
# eggs
# ----------
# apple
# ----------
# apple         rev_elements(get_list,print_item)
# ----------
# eggs
# ----------
# spam
# ----------
# maps          iter_elements(get_list,reverse_item)
# ----------
# sgge
# ----------
# elppa
# ----------
# elppa         rev_elements(get_list,reverse_item)
# ----------
# sgge
# ----------
# maps
# ----------
# ['s', 'p', 'a', 'm']    iter_elements(get_lists,print_item)
# ----------
# ['e', 'g', 'g', 's']
# ----------
# ['a', 'p', 'p', 'l', 'e']
# ----------
# ['a', 'p', 'p', 'l', 'e']    rev_elements(get_lists,print_item)
# ----------
# ['e', 'g', 'g', 's']
# ----------
# ['s', 'p', 'a', 'm']
# ----------
# ['m', 'a', 'p', 's']    iter_elements(get_lists,reverse_item)
# ----------
# ['s', 'g', 'g', 'e']
# ----------
# ['e', 'l', 'p', 'p', 'a']
# ----------
# ['e', 'l', 'p', 'p', 'a']    rev_elements(get_lists,reverse_item)
# ----------
# ['s', 'g', 'g', 'e']
# ----------
# ['m', 'a', 'p', 's']
# ----------
