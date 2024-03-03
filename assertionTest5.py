import unittest


class Testing(unittest.TestCase):

    def test_search(self):
        # self.assertGreater(100,10)
        # self.assertGreaterEqual(100,200)
        # self.assertLess(10,45)
        self.assertLessEqual(40, 60)


if __name__ == "__main__":
    unittest.main()
