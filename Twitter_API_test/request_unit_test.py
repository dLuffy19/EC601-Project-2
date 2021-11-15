import unittest
import request

class TestRequest(unittest.TestCase):

    def test_request(self):
        self.assertEqual(request.send_request(), 200)

if __name__ == '__main__':
    unittest.main()