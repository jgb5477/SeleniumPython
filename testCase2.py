import unittest
from selenium import webdriver

class searchEngine(unittest.TestCase):
    def test_google(self):
        self.myweb = webdriver.Chrome('/Users/deepintent/PycharmProjects/SeleniumPython/seleniumdirect/chromedriver')
        self.myweb.get("https://www.google.com/")
        print(f"Title Page of {self.myweb.title}")
        self.myweb.close()

    def test_amazon(self):
        self.myweb = webdriver.Chrome('/Users/deepintent/PycharmProjects/SeleniumPython/seleniumdirect/chromedriver')
        self.myweb.get("https://www.amazon.in/")
        print(f"Title Page of {self.myweb.title}")
        self.myweb.close()

if __name__=="__main__" :
   unittest.main()
