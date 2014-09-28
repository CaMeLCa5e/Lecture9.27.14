import unittest

def juice_maker(fruit):
	if fruit.startswith('a'):
		return 'apple'
	if fruit.startswith('b'):
		return 'banana'
	return fruit + " juice"
	
class JuiceMakerTestCase(unittest.TestCase):
	def setUp()
		print('set up db')
		
	def test_juice_maker(self):
		fruit = "apple"
		result = juice_maker(fruit)
		self.assertEqual(result == fruit + 'juice')
		pass
		
	def test_juice_maker_a(self):
		fruit = 'appler'
		result = juice_maker(fruit)
		self.assertEqual(result, 'apple')
		
	def test_juice_maker_all_else(self):
		fruit = 'orange'
		result = juice_maker(fruit)
		self.assertEqual(result, fruit + 'juice')
		
	def hopscotch(self):
		pass
if __name__ == "__main__":
	unittest.main()
	