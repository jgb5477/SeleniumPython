from selenium import webdriver
import unittest

class Testing(unittest.TestCase):

    def test_search(self):
        self.myweb = webdriver.Chrome('/Users/deepintent/PycharmProjects/SeleniumPython/seleniumdirect/chromedriver')
        self.assertIsNone(self.myweb)
        #self.assertIsNotNone(self.myweb)

if __name__ == "__main__" :
    unittest.main()