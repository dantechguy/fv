import unittest
from fvar import fv
import math

class TestFVFunctions(unittest.TestCase):
	def test_initialising_values(self):
		a = fv(1)
		a = fv(-5)
		a = fv(1.2)
		a = fv(-9999.4523)
		a = fv('Infinity')
		a = fv('-Infinity')
		a = fv('infinity')
		a = fv('NaN')
		a = fv('nan')
		a = fv('A string!')
		a = fv('')
		a = fv([])
		a = fv([1,2,3])
		a = fv(['hey', 2.3, -1])
		with self.assertRaises(TypeError):
			a = fv({'a':3, 'b':5})
		with self.assertRaises(TypeError):
			a = fv(set(1,2,3))

	def test_conversion(self):
		self.assertTrue (fv(123).is_number())
		self.assertFalse(fv(123).is_string())
		self.assertFalse(fv(123).is_list())
		self.assertFalse(fv(123).is_infinite())
		self.assertFalse(fv(123).is_nan())

		self.assertTrue (fv('Infinity').is_number())
		self.assertFalse(fv('Infinity').is_string())
		self.assertFalse(fv('Infinity').is_list())
		self.assertTrue (fv('Infinity').is_infinite())
		self.assertFalse(fv('Infinity').is_nan())

		self.assertTrue (fv('-Infinity').is_number())
		self.assertFalse(fv('-Infinity').is_string())
		self.assertFalse(fv('-Infinity').is_list())
		self.assertTrue (fv('-Infinity').is_infinite())
		self.assertFalse(fv('-Infinity').is_nan())

		self.assertFalse(fv('infinity').is_number())
		self.assertTrue (fv('infinity').is_string())
		self.assertFalse(fv('infinity').is_list())
		self.assertFalse(fv('infinity').is_infinite())
		self.assertFalse(fv('infinity').is_nan())

		self.assertFalse(fv('-infinity').is_number())
		self.assertTrue (fv('-infinity').is_string())
		self.assertFalse(fv('-infinity').is_list())
		self.assertFalse(fv('-infinity').is_infinite())
		self.assertFalse(fv('-infinity').is_nan())

		self.assertFalse(fv('inf').is_number())
		self.assertTrue(fv('inf').is_string())
		self.assertFalse(fv('inf').is_list())
		self.assertFalse(fv('inf').is_infinite())
		self.assertFalse(fv('inf').is_nan())

		self.assertFalse(fv('-inf').is_number())
		self.assertTrue (fv('-inf').is_string())
		self.assertFalse(fv('-inf').is_list())
		self.assertFalse(fv('-inf').is_infinite())
		self.assertFalse(fv('-inf').is_nan())

		self.assertTrue (fv('NaN').is_number())
		self.assertFalse(fv('NaN').is_string())
		self.assertFalse(fv('NaN').is_list())
		self.assertFalse(fv('NaN').is_infinite())
		self.assertTrue (fv('NaN').is_nan())

		self.assertFalse(fv('nan').is_number())
		self.assertTrue (fv('nan').is_string())
		self.assertFalse(fv('nan').is_list())
		self.assertFalse(fv('nan').is_infinite())
		self.assertFalse(fv('nan').is_nan())

		self.assertFalse(fv('test string').is_number())
		self.assertTrue (fv('test string').is_string())
		self.assertFalse(fv('test string').is_list())
		self.assertFalse(fv('test string').is_infinite())
		self.assertFalse(fv('test string').is_nan())

		self.assertFalse(fv([1,2]).is_number())
		self.assertFalse(fv([1,2]).is_string())
		self.assertTrue (fv([1,2]).is_list())
		self.assertFalse(fv([1,2]).is_infinite())
		self.assertFalse(fv([1,2]).is_nan())

		self.assertEqual(len(fv(123456)), 6)
		self.assertEqual(len(fv('hello!')), 6)
		self.assertEqual(len(fv('')), 0)
		self.assertEqual(len(fv([1,2])), 2)
		self.assertEqual(len(fv([])), 0)

		self.assertTrue (fv('2') in fv('123'))
		self.assertFalse(fv('4') in fv('123'))
		self.assertTrue (fv(2) in fv(123))
		self.assertFalse(fv(4) in fv(123))
		self.assertTrue (fv(2) in fv([1,2,3]))
		self.assertFalse(fv(4) in fv([1,2,3]))

	def test_sign(self):
		self.assertEqual(fv(-5), -fv(5))
		self.assertEqual(fv(5), -fv(-5))
		self.assertEqual(fv(-5.7), -fv(5.7))
		self.assertEqual(fv(-0), -fv(0))
		self.assertEqual(fv(0), fv(-0))
		self.assertEqual(fv(0), -fv(0))
		self.assertEqual(fv('-Infinity'), -fv('Infinity'))
		self.assertEqual(fv('NaN'), -fv('NaN'))
		self.assertEqual(-fv('hello'), fv(0))
		self.assertEqual(fv('-12'), -fv('12'))

		self.assertEqual(abs(fv(-5)), fv(5))
		self.assertEqual(abs(fv(5)), fv(5))
		self.assertEqual(abs(fv(-5.7)), fv(5.7))
		self.assertEqual(abs(fv(5.7)), fv(5.7))
		self.assertEqual(abs(fv('-Infinity')), fv('Infinity'))
		self.assertEqual(abs(fv('Infinity')), fv('Infinity'))
		self.assertEqual(abs(fv('-12')), fv('12'))
		self.assertEqual(abs(fv('12')), fv('12'))

	def test_math(self):
		self.assertEqual(fv(5) + fv(3), fv(8))
		self.assertEqual(fv('5') + fv(3), fv('8'))
		self.assertEqual(fv('Infinity') + fv(3), fv('Infinity'))
		self.assertEqual(fv('Infinity') + fv('Infinity'), fv('Infinity'))
		self.assertEqual(fv('-Infinity') + fv(3), fv('-Infinity'))

		self.assertEqual(fv(5) - fv(3), fv(2))
		self.assertEqual(fv('5') - fv(3), fv('2'))
		self.assertEqual(fv('Infinity') - fv(3), fv('Infinity'))
		self.assertEqual(fv('Infinity') - fv('Infinity'), fv('NaN'))
		self.assertEqual(fv('3') - fv('Infinity'), fv('-Infinity'))

		self.assertEqual(fv(5) * fv(3), fv(15))
		self.assertEqual(fv('5') * fv(3), fv('15'))
		self.assertEqual(fv('Infinity') * fv(3), fv('Infinity'))
		self.assertEqual(fv('-Infinity') * fv(3), fv('-Infinity'))
		self.assertEqual(fv('Infinity') * fv(0), fv('NaN'))

		self.assertEqual(fv(15) / fv(3), fv(5))
		self.assertEqual(fv('15') / fv(3), fv('5'))
		self.assertEqual(fv('Infinity') / fv(3), fv('Infinity'))
		self.assertEqual(fv(3) / fv('Infinity'), fv(0))
		self.assertEqual(fv(0) / fv('Infinity'), fv(0))
		self.assertEqual(fv('Infinity') / fv(0), fv('Infinity'))
		self.assertEqual(fv(3) / fv(0), fv('Infinity'))
		self.assertEqual(fv(0) / fv(0), fv('NaN'))

		self.assertEqual(fv(10) // fv(3), fv(3))
		self.assertEqual(fv('10') // fv(3), fv('3'))
		self.assertEqual(fv('Infinity') // fv(3), fv('Infinity'))
		self.assertEqual(fv(3) // fv('Infinity'), fv(0))
		self.assertEqual(fv(0) // fv('Infinity'), fv(0))
		self.assertEqual(fv('Infinity') // fv(0), fv('Infinity'))
		self.assertEqual(fv(3) // fv(0), fv('Infinity'))
		self.assertEqual(fv(0) // fv(0), fv('NaN'))

		self.assertEqual(fv(10) % fv(3), fv(1))
		self.assertEqual(fv('10') % fv(3), fv('1'))
		self.assertEqual(fv('Infinity') % fv(3), fv('NaN'))
		self.assertEqual(fv(3) % fv('Infinity'), fv(3))
		self.assertEqual(fv(3) % fv('-Infinity'), fv(3))

	def test_rounding(self):
		self.assertEqual(round(fv(1.5)), fv(2))
		self.assertEqual(round(fv(-1.5)), fv(-2))
		self.assertEqual(round(fv('Infinity')), fv('Infinity'))
		self.assertEqual(round(fv('-Infinity')), fv('-Infinity'))
		self.assertEqual(round(fv('NaN')), fv('NaN'))
		self.assertEqual(round(fv('abc')), fv(0))

		self.assertEqual(math.floor(fv(1.5)), fv(1))
		self.assertEqual(math.floor(fv(-1.5)), fv(-2))
		self.assertEqual(math.floor(fv('Infinity')), fv('Infinity'))
		self.assertEqual(math.floor(fv('-Infinity')), fv('-Infinity'))
		self.assertEqual(math.floor(fv('NaN')), fv('NaN'))
		self.assertEqual(math.floor(fv('abc')), fv(0))

		self.assertEqual(math.ceil(fv(1.5)), fv(2))
		self.assertEqual(math.ceil(fv(-1.5)), fv(-1))
		self.assertEqual(math.ceil(fv('Infinity')), fv('Infinity'))
		self.assertEqual(math.ceil(fv('-Infinity')), fv('-Infinity'))
		self.assertEqual(math.ceil(fv('NaN')), fv('NaN'))
		self.assertEqual(math.ceil(fv('abc')), fv(0))

		self.assertEqual(math.trunc(fv(1.5)), fv(1))
		self.assertEqual(math.trunc(fv(-1.5)), fv(-1))
		self.assertEqual(math.trunc(fv('Infinity')), fv('Infinity'))
		self.assertEqual(math.trunc(fv('-Infinity')), fv('-Infinity'))
		self.assertEqual(math.trunc(fv('NaN')), fv('NaN'))
		self.assertEqual(math.trunc(fv('abc')), fv(0))

		self.assertEqual(type(int(fv(1.5))), int)
		self.assertEqual(int(fv(1.5)), 1)
		self.assertEqual(int(fv(-1.5)), -1)
		self.assertEqual(int(fv('Infinity')), 0)
		self.assertEqual(int(fv('-Infinity')), 0)
		self.assertEqual(int(fv('NaN')), 0)
		self.assertEqual(int(fv('abc')), 0)

		self.assertEqual(type(float(fv(1.5))), float)
		self.assertEqual(float(fv(1.5)), 1.5)
		self.assertEqual(float(fv(-1.5)), -1.5)
		self.assertEqual(float(fv('Infinity')), float('inf'))
		self.assertEqual(float(fv('-Infinity')), float('-inf'))
		self.assertTrue (math.isnan(float(fv('NaN'))))
		self.assertEqual(float(fv('abc')), 0.0)

	def test_comparison(self):
		self.assertTrue (fv(3) > fv(2))
		self.assertFalse(fv(3) > fv(5))
		self.assertTrue (fv(3) > fv('2'))
		self.assertTrue (fv('bb') > fv('aaa'))
		self.assertTrue (fv('bbb') > fv('bb'))
		self.assertTrue (fv('Infinity') > fv(3))
		self.assertTrue (fv(3) > fv('-Infinity'))

		self.assertFalse(fv(3) < fv(2))
		self.assertTrue (fv(3) < fv(5))
		self.assertFalse(fv(3) < fv('2'))
		self.assertFalse(fv('bb') < fv('aaa'))
		self.assertFalse(fv('bbb') < fv('bb'))
		self.assertFalse(fv('Infinity') < fv(3))
		self.assertFalse(fv(3) < fv('-Infinity'))

		self.assertTrue (fv(5) == 5)
		self.assertTrue (fv(5) == fv(5))
		self.assertFalse(fv(5) == fv('3'))
		self.assertTrue (fv([1, '2', 3]) == fv(['1', 2, '3']))
		self.assertFalse(fv([1,'2']) == fv(['1', 2, '3']))
		self.assertTrue (fv('Infinity') == fv('Infinity'))
		self.assertFalse(fv('Infinity') == fv('-Infinity'))
		self.assertTrue (fv('NaN') == fv('NaN'))

	def test_string_and_index(self):
		self.assertEqual(fv('abc').join(fv('def')), fv('abcdef'))
		self.assertEqual(fv('abc').join(fv(123)), fv('abc123'))
		self.assertEqual(fv(123).join(fv(456)), fv(123456))

		self.assertEqual(fv('abc')[1], fv('b'))
		self.assertEqual(fv('abc')[-1], fv(''))
		self.assertEqual(fv(123)[1], fv(2))
		self.assertEqual(fv(123)[-1], fv(''))
		self.assertEqual(fv([1,2,3])[1], fv(2))
		self.assertEqual(fv([1,2,3])[-1], fv(''))

		a = fv([1,2,3])
		a.add(4)
		self.assertEqual(a, fv([1,2,3,4]))

		self.assertEqual(fv([]).add(1).add(2).add(3).add(4), fv([1,2,3,4]))

		a = fv([1,2,3])
		a[1] = 'b'
		self.assertEqual(a, fv([1, 'b', 3]))

		a = fv([1,2,3])
		a[3] = 'b'

		a = fv([1,2,3])
		del a[1]
		self.assertEqual(a, fv([1,3]))

		a = fv([1,3])
		a.insert(1, 2)
		self.assertEqual(a, fv([1,2,3]))

		self.assertEqual(fv([1, 4]).insert(1, 2).insert(2, 3), fv([1,2,3,4]))

		self.assertEqual(fv([1,2,3]).item_number(2), 1)

		self.assertEqual(fv([1,2,3]).item_number(4), 0)

if __name__ == "__main__":
	unittest.main()