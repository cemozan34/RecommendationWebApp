from urllib import response
from app import app
import unittest


class FlaskTest(unittest.TestCase):

    # Checking response 200
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get("/")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)


if __name__ == 'main':
    unittest.main()
