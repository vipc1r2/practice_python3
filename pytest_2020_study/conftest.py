# -*- coding: utf-8 -*-

# @FileName: conftest.py

import pytest
@pytest.fixture(scope='session')
def commonData():
    str = ' 通过conftest.py 共享fixture'
    print('获取到%s' % str)
    return str