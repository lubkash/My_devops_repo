import unittest
from app import app

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True  # Enable test mode

    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)  # Check if the page loads successfully
        self.assertIn(b'Welcome to the Flask GUI', response.data)  # Check if content is present

if __name__ == '__main__':
    unittest.main()
