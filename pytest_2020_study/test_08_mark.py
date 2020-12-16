#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

@pytest.mark.weibo
def test_weibo():
    print("测试微博")

@pytest.mark.toutiao
def test_toutiao():
    print("测试头条")

@pytest.mark.toutiao
def test_toutiao1():
    print("再次测试头条")

@pytest.mark.xinlang
class TestClass:
    def test_method(self):
        print("测试新浪")

def testnoMark():
    print("没有标记测试")



if __name__ == '__main__':
    pytest.main(["-s", "test_08_mark.py",'-m=weibo'])
