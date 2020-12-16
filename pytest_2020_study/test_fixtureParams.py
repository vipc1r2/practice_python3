# -*- coding: utf-8 -*-

# @FileName: test_fixtureParams.py

'''
fixture的params示例
'''
import pytest

seq=[1,2]

@pytest.fixture(params=seq)
def params(request):
    # request用来接收param列表数据
    return request.param


def test_params(params):
    print(params)
    assert 1 == params