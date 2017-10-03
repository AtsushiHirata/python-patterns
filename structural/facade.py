#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
*What is this pattern about?
*このパターンの目的
The Facade pattern is a way to provide a simpler unified interface to
a more complex system.
Facade(ファサード)パターンは、より複雑なシステムに対して、単純で一本化されたインターフェイスを提供する方法です。
It provides an easier way to access functions
of the underlying system by providing a single entry point.
窓口を一つにすることで、システムの中に組み込まれている見通しの悪い機能群に簡単にアクセスする手段を提供します。
This kind of abstraction is seen in many real life situations.
このような抽象化は、多くの現実世界の状況においても見出せます。
For example, we can turn on a computer by just pressing a button, but in
fact there are many procedures and operations done when that happens
(e.g., loading programs from disk to memory).
例えば、ボタンを一つ、ポンと押すだけでコンピュータを起動できます。でもその裏で実際には、たくさんの手順と操作が行われているのです。（例えば、ハードドライブからメモリへプログラムを読み込むことです。）
In this case, the button serves as an unified interface to all the underlying procedures to turn on a computer.
このコンピュータ起動の例では、電源ボタンはコンピュータを起動するための、システムの内部にある全ての機能群に対する一本化されたインターフェイス、すなわち窓口として働いているのです。

*What does this example do?
*このサンプルコードは何をしているのか
The code defines three classes (TC1, TC2, TC3) that represent complex
parts to be tested.
三つのクラス(TC1,TC2,TC3)を定義するコードです。これらのクラスはテストが必要な複雑な部分を持っているとします。
Instead of testing each class separately, the
TestRunner class acts as the facade to run all tests with only one
call to the method runAll.
個別にテストをする代わりに、TestRunnerクラスがfacadeとして振る舞います。runAllメソッドただ一つを呼ぶことで、全てのテストが実行されます。
By doing that, the client part only needs
to instantiate the class TestRunner and call the runAll method.
Facadeパターンを適用することで、クライアント側に必要なのはTestRunnerクラスを生成し、runAllメソッドを呼ぶことだけです。
As seen in the example, the interface provided by the Facade pattern
is independent from the undrlying implementation.
このサンプルコードに見られるように、Facadeパターンで提供されるインターフェイスはシステム内部の実装からは切り離され独立しています。
Since the client just calls the runAll method, we can modify the classes TC1, TC2 or
TC3 without impact on the way the client uses the system.
これによって、クライアント側は単純にrunAllメソッドを呼ぶだけで良くなります。クライアント側のクラスが複雑なシステムを使う際に、望まない悪影響を生じることなしに、各クラスTC1,TC2,あるいはTC3のコードに変更を加えられるのです。

*Where is the pattern used practically?
*実際にどこでこのデザインパターンが使われているか。
This pattern can be seen in the Python standard library when we use
the isdir function.
このパターンは、Pythonの標準ライブラリ内のisdir関数を使う際に目にすることができます。
Although a user simply uses this function to know
whether a path refers to a directory, the system makes a few
operations and calls other modules (e.g., os.stat) to give the result.
あるファイルパスがどのディレクトリを参照しているのかを知るために、ユーザは単純にこの関数を使います。
しかしながら、求める結果を得るために、システムはいくつかの操作と、いくつかの別のモジュール(例えばos.statです。)を呼んでいるのです。

*References:
*参考情報
https://sourcemaking.com/design_patterns/facade
https://fkromer.github.io/python-pattern-references/design/#facade
http://python-3-patterns-idioms-test.readthedocs.io/en/latest/ChangeInterface.html#facade
"""


from __future__ import print_function
import time

SLEEP = 0.1


# Complex Parts
class TC1:

    def run(self):
        print(u"###### In Test 1 ######")
        time.sleep(SLEEP)
        print(u"Setting up")
        time.sleep(SLEEP)
        print(u"Running test")
        time.sleep(SLEEP)
        print(u"Tearing down")
        time.sleep(SLEEP)
        print(u"Test Finished\n")


class TC2:

    def run(self):
        print(u"###### In Test 2 ######")
        time.sleep(SLEEP)
        print(u"Setting up")
        time.sleep(SLEEP)
        print(u"Running test")
        time.sleep(SLEEP)
        print(u"Tearing down")
        time.sleep(SLEEP)
        print(u"Test Finished\n")


class TC3:

    def run(self):
        print(u"###### In Test 3 ######")
        time.sleep(SLEEP)
        print(u"Setting up")
        time.sleep(SLEEP)
        print(u"Running test")
        time.sleep(SLEEP)
        print(u"Tearing down")
        time.sleep(SLEEP)
        print(u"Test Finished\n")


# Facade
class TestRunner:

    def __init__(self):
        self.tc1 = TC1()
        self.tc2 = TC2()
        self.tc3 = TC3()
        self.tests = [self.tc1, self.tc2, self.tc3]

    def runAll(self):
        [i.run() for i in self.tests]


# Client
if __name__ == '__main__':
    testrunner = TestRunner()
    testrunner.runAll()

### OUTPUT ###
# ###### In Test 1 ######
# Setting up
# Running test
# Tearing down
# Test Finished
#
# ###### In Test 2 ######
# Setting up
# Running test
# Tearing down
# Test Finished
#
# ###### In Test 3 ######
# Setting up
# Running test
# Tearing down
# Test Finished
#
