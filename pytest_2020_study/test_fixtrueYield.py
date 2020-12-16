# -*- coding: utf-8 -*-

import pytest

@pytest.fixture(scope='module')
def open():
    print("打开浏览器！！！")
    yield
    print('关闭浏览器！！！')


def test01():
    print("\n我是第一个用例")
    raise Exception


def test02(open):
    print("\n我是第二个用例")


if __name__ == '__main__':
    pytest.main(["-q", "test_fixtrueYield.py"])