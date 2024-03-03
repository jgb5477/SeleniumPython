import unittest

class Testing(unittest.TestCase):

    def test_search(self):
        list1 = ["python","Java","C++"]
        #self.assertIn("python",list1)

        self.assertNotIn("python",list1)


if __name__ == "__main__" :
    unittest.main()