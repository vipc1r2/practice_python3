import pytest

@pytest.fixture(scope="module")
def test_addfinalizer(request):
    # 前置操作setup
    print("==再次打开浏览器==")
    test = "test_addfinalizer"

    def fin():
        # 后置操作teardown
        print("==再次关闭浏览器==")

    request.addfinalizer(fin)
    # 返回前置操作的变量
    return test


def test_anthor(test_addfinalizer):
    print("==最新用例==", test_addfinalizer)