# def pwd():
#     print("获取用户名")
#     a = "yygirl"
#     assert a == "yygirl123"
#
#
# def test_1(pwd):
#     assert user == "yygirl"
import pytest


# @pytest.fixture()
# def user():
#     print("获取用户名")
#     a = "yygirl"
#     assert a == "yygirl123"
#     return a
#
#
# def test_1(user):
#     assert user == "yygirl"

# @pytest.fixture()
# def pwd():
#     print("获取密码")
#     a = "yygirl"
#     return a
#
#
# def test_2(pwd):
#     assert pwd == "yygirl123"


# @pytest.fixture()
# def pwd():
#     print("获取密码")
#     a = "polo"
#     return a
#
#
# def test_2(pwd):
#     raise NameError
#     assert pwd == "polo"


# 断言装饰器
@pytest.mark.xfail(raises=ZeroDivisionError)
def test_f():
    1 / 0