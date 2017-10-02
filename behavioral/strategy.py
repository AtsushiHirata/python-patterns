#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
http://stackoverflow.com/questions/963965/how-is-this-strategy-pattern
WikiPediaに掲載されているPythonで書かれたサンプルコード

他のプログラミング言語のほぼ全てにおいて、Strategy(ストラテジ)パターンは、基本となるstrategyのインターフェイスクラス、あるいはabstractクラスから実装します。そして、そのサブクラスを作ることで、複数の実装のあるstrategyクラスを作るのです。(参照 http://en.wikipedia.org/wiki/Strategy_pattern)しかしながら、Pythonは高階関数をサポートしており、このサンプルコードに示すように、一つのクラスに対して、機能の異なる別の関数を引数として与えて、別の動作をするインスタンスを作ることができます。
"""
import types


class StrategyExample:

    def __init__(self, func=None):
        self.name = 'Strategy Example 0'
        if func is not None:
            self.execute = types.MethodType(func, self)

    def execute(self):
        print(self.name)


def execute_replacement1(self):
    print(self.name + ' from execute 1')


def execute_replacement2(self):
    print(self.name + ' from execute 2')


if __name__ == '__main__':
    strat0 = StrategyExample()

    strat1 = StrategyExample(execute_replacement1)
    strat1.name = 'Strategy Example 1'

    strat2 = StrategyExample(execute_replacement2)
    strat2.name = 'Strategy Example 2'

    strat0.execute()
    strat1.execute()
    strat2.execute()

### OUTPUT ###
# Strategy Example 0
# Strategy Example 1 from execute 1
# Strategy Example 2 from execute 2
