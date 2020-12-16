# -*- coding: utf-8 -*-

# @FileName: test_scope2.py

import pytest
def testScope2(commonData):
    print(commonData)
    assert commonData == ' 通过conftest.py 共享fixture'
if __name__ == '__main__':
    pytest.main(["-q", "test_scope2.py"])