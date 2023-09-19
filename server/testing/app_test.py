

import unittest
from flask import Flask
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        # Create a test client
        self.app = app.test_client()
        self.app.testing = True

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Python Operations with Flask Routing and Views", response.data)

    def test_print(self):
        response = self.app.get('/print/Hello')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b"Hello")

    def test_count(self):
        response = self.app.get('/count/5')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b"1\n2\n3\n4\n5")

    def test_count_negative(self):
        response = self.app.get('/count/-5')
        self.assertEqual(response.status_code, 400)
        self.assertIn(b"Don't be stupid. We need a positive number.", response.data)

    def test_math_add(self):
        response = self.app.get('/math/2.5/add/3.5')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b"The result of 2.5 add 3.5 is 6.0")

    def test_math_subtract(self):
        response = self.app.get('/math/10.0/subtract/5.0')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b"The result of 10.0 subtract 5.0 is 5.0")

    def test_math_multiply(self):
        response = self.app.get('/math/4.0/multiply/2.5')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b"The result of 4.0 multiply 2.5 is 10.0")

    def test_math_divide(self):
        response = self.app.get('/math/10.0/divide/2.0')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b"The result of 10.0 divide 2.0 is 5.0")

    def test_math_divide_by_zero(self):
        response = self.app.get('/math/5.0/divide/0.0')
        self.assertEqual(response.status_code, 400)
        self.assertIn(b"Division by zero is mathematically impossible.", response.data)

    def test_math_invalid_operation(self):
        response = self.app.get('/math/5.0/unknown/2.0')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b"The operation is improbable.")

if __name__ == '__main__':
    unittest.main()