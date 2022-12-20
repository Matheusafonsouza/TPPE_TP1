import pytest


def func(x):
    return x + 1


def exception_func():
    raise SystemExit(1)


def test_answer():
    assert func(4) == 5


def test_mytest():
    with pytest.raises(SystemExit):
        exception_func()
