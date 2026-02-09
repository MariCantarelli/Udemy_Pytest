import unittest

def somar(a, b):
    return a + b

class TesteSoma(unittest.TestCase):
    def test_soma(self):
        seft.assertEqual(somar(3, 4), 7)
        seft.assertEqual(somar(5, 5), 10)
        seft.assertEqual(somar(-1, 1), 0)

if __name__ == '__main__'
    unittest.main()

"""
    def somar(a, b):
        return a + b

    def test_soma():
        assert somar(3, 4) == 7
        assert somar(5, 5) == 10
        assert somar(-1, 1) == 0 
"""