import unittest
from app import app

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here
class BasicTestsSetup(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False

        self.app = app.test_client()
        self.assertEqual(app.debug, False)

    # executed after each test
    def tearDown(self):
        pass


class TestCaseExamples(unittest.TestCase):

    def test_login_status(self):
        tester = app.test_client(self)
        response = tester.get('/loginpg', content_type='html/text')
        self.assertEqual(response.status_code, 200)  # pass (test if the page renders successfully)

    def test_random_status(self):
        tester = app.test_client(self)
        response = tester.get('/random', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_random_content(self):
        tester = app.test_client(self)
        response = tester.get('/random', content_type='html/text')
        #self.assertTrue(b'User Account Demo' in response.data)  # passed the test
        # self.assertFalse(b'Administration Demo' in response.data)  # passed the test




if __name__ == '__main__':
    unittest.main()