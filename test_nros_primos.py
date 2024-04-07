import unittest
from nros_primos import is_prime

class TestIsPrime(unittest.TestCase):
    def test_with_1(self):
        result = is_prime(1)
        self.assertFalse(result)
    
    def test_with_2(self):
        result = is_prime(2)
        self.assertTrue(result)
    
    def test_with_3(self):
        result = is_prime(3)
        self.assertTrue(result)
    
    def test_with_4(self):
        result = is_prime(4)
        self.assertFalse(result)
    
    def test_with_5(self):
        result = is_prime(5)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()