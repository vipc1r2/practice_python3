# -*- coding: utf-8 -*-

# @FileName: test_scopeModule.py

'''
fixture为module示例
'''
import pytest


@pytest.fixture(scope='module')
def data():
    return '\nscope为module'


def test1(data):
    print(data)
  




class TestClass(object):
    def test2(self, data):
        print('我在类中了哦，' + data)



if __name__ == '__main__':
    pytest.main(["-q", "test_scopeModule.py"])