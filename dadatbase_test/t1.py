#!/usr/bin/env python3

import unittest
from prog import name_function

class NameTest (unittest.TestCase):
    def test_name1(self):
        result = name_function('Nune')
        self.assertEqual(result, 'Nune')
    
#    def ank(self):
#        result = name_function('Anna')
#        self.assertEqual(result, 'Anna')
    
    def test_name2(self):
        result = name_function('nune')
        self.assertEqual(result, 0)
        result2 = name_function('nune')
        self.assertEqual(result2, 0)
    
    def test_name3(self):
        result = name_function('nune')
        self.assertEqual(result, 0)
        result2 = name_function('12')
        self.assertEqual(result2, 0)

    def test_name4(self):
        result = name_function('nune')
        self.assertEqual(result, 0)
        result2 = name_function('12name')
        self.assertEqual(result2, 0)
    
    def test_name5(self):
        result = name_function('name')
        self.assertEqual(result, 0)
        result2 = name_function('Nune')
        self.assertEqual(result2, 'Nune')

    def test_name6(self):
        result = name_function('name')
        self.assertEqual(result, 0)
        result2 = name_function('')
        self.assertEqual(result2, 0)

    def test_name7(self):
        result = name_function('')
        self.assertEqual(result, 0)
        result2 = name_function('')
        self.assertEqual(result, 0)

    def test_name8(self):
        result = name_function('')
        self.assertEqual(result, 0)
        result2 = name_function('nune')
        self.assertEqual(result, 0)

    def test_name9(self):
        result = name_function('')
        self.assertEqual(result, 0)
        result2 = name_function('12')
        self.assertEqual(result, 0)

    def test_name10(self):
        result = name_function('')
        self.assertEqual(result, 0)
        result2 = name_function('Nune')
        self.assertEqual(result2,'Nune')
    
    def test_name11(self):
        result = name_function('')
        self.assertEqual(result, 0)
        result2 = name_function('12nune')
        self.assertEqual(result2, 0)

    def test_name12(self):
        result = name_function('12')
        self.assertEqual(result, 0)
        result2 = name_function('Nune')
        self.assertEqual(result2, 'Nune')
    
    def test_name13(self):
        result = name_function('12')
        self.assertEqual(result, 0)
        result2 = name_function('nune')
        self.assertEqual(result2, 0)

    def test_name14(self):
        result = name_function('12')
        self.assertEqual(result, 0)
        result2 = name_function('12')
        self.assertEqual(result2, 0)

    def test_name15(self):
        result = name_function('12')
        self.assertEqual(result, 0)
        result2 = name_function('')
        self.assertEqual(result2, 0)
    
    def test_name16(self):
        result = name_function('12')
        self.assertEqual(result, 0)
        result2 = name_function('12nune')
        self.assertEqual(result2, 0)

    def test_name17(self):
        result = name_function('..')
        self.assertEqual(result, 0)
        result2 = name_function('..')
        self.assertEqual(result2, 0)
    
    def test_name18(self):
        result = name_function('..')
        self.assertEqual(result, 0)
        result2 = name_function('Nune')
        self.assertEqual(result2, 'Nune')

    def test_name19(self):
        result = name_function('..')
        self.assertEqual(result, 0)
        result2 = name_function('nune')
        self.assertEqual(result2, 0)

    def test_name20(self):
        result = name_function('..')
        self.assertEqual(result, 0)
        result2 = name_function('12')
        self.assertEqual(result2, 0)

    def test_name21(self):
        result = name_function('..')
        self.assertEqual(result, 0)
        result2 = name_function('..nune')
        self.assertEqual(result2, 0)

    def test_name22(self):
        result = name_function('..')
        self.assertEqual(result, 0)
        result2 = name_function('12nune')
        self.assertEqual(result2, 0)

    def test_name23(self):
        result = name_function(' ')
        self.assertEqual(result, 0)
        result2 = name_function('Nune')
        self.assertEqual(result2,'Nune')
    
#`    
#`    def test_error(self):
#`        self.assertRaises(IndexError)
#`

if __name__ == '__main__' :
    unittest.main()
