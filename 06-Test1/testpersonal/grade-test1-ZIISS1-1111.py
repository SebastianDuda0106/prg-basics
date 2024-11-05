'''
1. Download your programs from Moodle.
1. Put this grading program in a folder with your programs.
2. Run this grading program.
3. Read your test results from results.txt file.
'''

import sys
import unittest

class Test(unittest.TestCase):
    def test_p1(self):
        import p1
        self.assertEqual(p1.f(160),True)
        self.assertEqual(p1.f(150),False)

    def test_p2(self):
        import p2
        self.assertEqual(p2.f(11,11),1)
        self.assertEqual(p2.f(-11,11),2)
        self.assertEqual(p2.f(-11,-11),3)
        self.assertEqual(p2.f(11,-11),4)

    def test_p3(self):
        import p3
        self.assertEqual(p3.f("1236"),True)
        self.assertEqual(p3.f("3215"),False)

    def test_p4(self):
        import p4
        self.assertEqual(p4.f(3),"123")
        self.assertEqual(p4.f(12),"123456789101112")
        self.assertEqual(p4.f(0),"")

    def test_p5(self):
        import p5
        self.assertEqual(p5.f(1,6),9)
        self.assertEqual(p5.f(10,20),45)

    def test_p6(self):
        import p6
        self.assertEqual(p6.f("3,3,4,5","4,3"),1)
        self.assertEqual(p6.f("3,3,4,5,5","5,5,5,2"),2)
        self.assertEqual(p6.f("3,3","5,2,2"),0)

    def test_p7(self):
        import p7
        self.assertEqual(p7.f(144),True)
        self.assertEqual(p7.f(143),False)

    def test_p8(self):
        import p8
        self.assertEqual(p8.f(72,20),True)
        self.assertEqual(p8.f(75,20),False)

    def test_p9(self):
        import p9
        self.assertEqual(p9.f("L","M"),1)
        self.assertEqual(p9.f("S","M"),2)
        self.assertEqual(p9.f("M","M"),0)

    def test_p10(self):
        import p10
        self.assertEqual(p10.f("13:06","13:03"),"13:03")
        self.assertEqual(p10.f("13:06","1:03pm"),"1:03pm")
        self.assertEqual(p10.f("13:06","1:06pm"),"13:06")


if __name__ == '__main__':
    sys.stderr = open('results.txt', 'w', encoding="utf-8")
    unittest.main(verbosity=2)
