# utf-8
import pytest
# https://docs.pytest.org/en/latest/


def my_inc(x):
    return x + 1

def test_inc():
    assert my_inc(3) == 5


if __name__ == '__main__':
    pytest.main(['c:\\msys32\\home\\chenyudong\\github\\small_code\\test\\py_test.py'])


# pytest will run all files of the form test_*.py or *_test.py in the current directory and its subdirectories. 
# More generally, it follows standard test discovery rules.
# specific: https://docs.pytest.org/en/latest/usage.html#cmdline
# just run pytest, the output:

# $ pytest
# ============================= test session starts =============================
# platform win32 -- Python 2.7.16, pytest-4.6.6, py-1.8.0, pluggy-0.13.0
# rootdir: c:\msys32\home\chenyudong\github\small_code
# collected 1 item                                                               

# test\py_test.py F                                                        [100%]

# ================================== FAILURES ===================================
# __________________________________ test_inc ___________________________________

#     def test_inc():
# >       assert my_inc(3) == 5
# E       assert 4 == 5
# E        +  where 4 = my_inc(3)

# test\py_test.py:9: AssertionError
# ========================== 1 failed in 0.28 seconds ===========================