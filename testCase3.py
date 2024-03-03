import unittest

def setUpModule():
    print("SetUPMODULE")

def tearDownModule():
    print("tearDOWNMODULE")

class AppTesting(unittest.TestCase):
    @classmethod
    def setUp(self):
        print("This is Login Method")

    @classmethod
    def tearDown(self):
        print("This is Logout Method")

    @classmethod
    def setUpClass(cls):
        print("Open Application")

    @classmethod
    def tearDownClass(cls):
        print("Close Application")

    def test_search(self):
        print("This is Search Test Case")

    def test_advancedSearch(self):
        print("This is Advance Search Test Case")

    def test_prepaid(self):
        print("This is prepaid Test Case")

    def test_postpaid(self):
        print("This is postpaid Test Case")

if __name__=="__main__" :
    unittest.main()
