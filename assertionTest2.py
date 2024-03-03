from selenium import webdriver
import unittest

class Testing(unittest.TestCase):

    def test_search(self):
        self.myweb = webdriver.Chrome('/Users/deepintent/PycharmProjects/SeleniumPython/seleniumdirect/chromedriver')
        self.myweb.get("https://www.google.com/")
        titleOfPage= self.myweb.title

        #self.assertTrue("Google"==titleOfPage)
        self.assertFalse("Google123"==titleOfPage)


if __name__ == "__main__" :
    unittest.main()