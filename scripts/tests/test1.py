import unittest


class MyTest(unittest.TestCase):

	def test_that_works(self):
		self.assertTrue(True)
		self.assertTrue(1 == 1)
		self.assertFlase(1 == 2)



	def test_that_fails(self):
		self.assertTrue(False)


	def test_equal(self):
		self.assertEqual(1,1)


	def test_equal_fails(self):
		self.assertEqual(1,2)
