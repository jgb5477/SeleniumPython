import unittest

class AppTesting(unittest.TestCase):

    @unittest.SkipTest
    def test_search(self):
        print("This is Search test")

    @unittest.skip("this is not Ready")
    def test_advanceSearch(self):
        print("This is Advance test")

    def test_signin(self):
        print("This is SignIn Test")

    @unittest.skipIf(1==1,"Numbers are not equal")
    def test_signout(self):
        print("This is SignOut Test")

    def test_prepaid(self):
        print("This is Prepaid Test")

    def test_postpaid(self):
        print("This is Postpaid Test")\

if __name__ == "__main__" :
    unittest.main()