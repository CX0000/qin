#import unittest
#class testdome(unittest.TestCase):
 #   def test_a001(self):
 #       pass
  #  def test_a002(self):
   #     pass
    #def test_a003(self):
     #   pass
#if __name__ == '__main__' :
 #   unittest.main()

import unittest
class TestClass:
    def setUp(self):
        print('这是setUp')
    def teardown(self):
        print('这是teardown')
    def test_one(self):
        print('这是test_one')
    def test_two(self):
        pass
if __name__ == '__main__' :
    unittest.main()
