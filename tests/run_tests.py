# Unit tests
import unittest

class SimpleTest(unittest.TestCase):
  
    def test(self):        
        self.assertTrue(True)

    def test_run_stuff(self):
        self.assertEqual(run_stuff(1), 2)
        
if __name__ == '__main__':
  unittest.main()
  test_run_stuff()
