# -*- coding: utf-8 -*-

# @FileName: test_Multiplefixture.py

'''
多个fixture使用情况
'''
import pytest
@pytest.fixture()
def username():
    return '软件测试君'
@pytest.fixture()
def password():
    return '123456'
def test_login(username, password):
    print('\n输入用户名：'+username)
    print('输入密码：'+password)
    print('登录成功，传入多个fixture参数成功')