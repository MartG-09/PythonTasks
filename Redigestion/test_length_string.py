from unittest import TestCase

import length_string

class TestValidatePrime(TestCase):
    def test_that_function_exist(self):
       length_string.is_prime(2)
    
    def test_that_number_is_prime_number(self):
        is_Valid = length_string.is_prime(2)
        self.assertTrue(is_Valid)

    def test_that_number_is_not_prime_number(self):
        is_Valid = length_string.is_prime(1)
        self.assertFalse(is_Valid)
