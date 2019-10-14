import unittest
# https://docs.python.org/zh-cn/3/library/unittest.html


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def test_add(self):
        # false fail
        # output:
        # FAIL: test_add (__main__.TestStringMethods)
        # ----------------------------------------------------------------------
        # Traceback (most recent call last):
        # File "c:\msys32\home\chenyudong\github\small_code\test\py_unit_test.py", line 21, in test_add
        #     self.assertEqual('a'+'b', 'ac')
        # AssertionError: 'ab' != 'ac'
        # - ab
        # + ac
        self.assertEqual('a'+'b', 'ac')

    def test_sub(self):
        # false fail
        self.assertEqual('a'-'b', 'ab')


if __name__ == '__main__':
    unittest.main()

# or run `py -3 -m unittest py_unit_test.py` in cmdline

# output:

# F..E.
# ======================================================================
# ERROR: test_sub (__main__.TestStringMethods)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "c:\msys32\home\chenyudong\github\small_code\test\py_unit_test.py", line 35, in test_sub
#     self.assertEqual('a'-'b', 'ab')
# TypeError: unsupported operand type(s) for -: 'str' and 'str'

# ======================================================================
# FAIL: test_add (__main__.TestStringMethods)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "c:\msys32\home\chenyudong\github\small_code\test\py_unit_test.py", line 31, in test_add
#     self.assertEqual('a'+'b', 'ac')
# AssertionError: 'ab' != 'ac'
# - ab
# + ac


# ----------------------------------------------------------------------
# Ran 5 tests in 0.009s

# FAILED (failures=1, errors=1)
