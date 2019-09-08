# Project 4: Word Search
# Author: Ben Clark

import funcs
import unittest

class tests(unittest.TestCase):

    def test_puz_tolist1(self):
        puz = "AAAAAAAAAABBBBBBBBBBCCCCCCCCCCDDDDDDDDDDEEEEEEEEEE"
        puz += "FFFFFFFFFFGGGGGGGGGGHHHHHHHHHHIIIIIIIIIIJJJJJJJJJJ"
        result = ["AAAAAAAAAA", 
        "BBBBBBBBBB", 
        "CCCCCCCCCC", 
        "DDDDDDDDDD", 
        "EEEEEEEEEE",
        "FFFFFFFFFF",
        "GGGGGGGGGG",
        "HHHHHHHHHH",
        "IIIIIIIIII",
        "JJJJJJJJJJ"]
        self.assertEqual(funcs.puzzle_to_list(puz), result)

    def test_check_forward1(self):
        puz = ["AAAAAAAAAA",  
        "FFFCATFFFF",
        "IIIIIIIISAT",
        "JJJJSPATJJ"]
        words = "CAT SAT SPAT".split()
        print("forward words: ", funcs.check_forward(puz, words))
        self.assertEqual(funcs.check_forward(puz, words)['CAT'], (1,3))
    def test_check_forward2(self):
        puz = ["AAAAAAAAAA",  
        "FFFCATFFFF",
        "IIIIIIISAT",
        "JJJJJJJJJJ"]
        words = "CAT SAT SPAT".split()
        self.assertEqual(funcs.check_forward(puz, words)['SAT'], (2,7))

    def test_check_backward1(self):
        puz = ["AAAAAAAAAA",  
        "FFFTACFFFF",
        "IIIIIIIITAS",
        "JJJJJJJJJJ"]
        words = "CAT SAT SPAT".split()
        print("backwards words: ", funcs.check_backward(puz, words))
        self.assertEqual(funcs.check_backward(puz, words)['CAT'], (1,5))
    def test_check_backward2(self):
        puz = ["AAAAAAAAAA",  
        "FFFTACFFFF",
        "IIIIIIITAS",
        "JJJJJJJJJJ"]
        words = "CAT SAT SPAT".split()
        self.assertEqual(funcs.check_backward(puz, words)['SAT'], (2,9))

    def test_back_index1(self):
        self.assertEqual(funcs.backward_index_converter((3,7)), (3,2))
    def test_back_index2(self):
        self.assertEqual(funcs.backward_index_converter((7,4)), (7,5))

    def test_check_down1(self):
        puz = ["AAAAAMAAAA",  
               "FFFFFAFFFF",
               "IAIIINIIII",
               "JNJJJJJJJJ"]
        words = "FAN MAN BAN STAN".split()
        print("downward words: ", funcs.check_down(puz, words))
        self.assertEqual(funcs.check_down(puz, words)['MAN'], (0,5))
    def test_check_down2(self):
        puz = ["AAAAAMAAAA",  
               "FFFFFAFFFF",
               "IAIIINIIII",
               "JNJJJJJJJJ"]
        words = "FAN MAN BAN STAN".split()
        self.assertEqual(funcs.check_down(puz, words)['FAN'], (1,1))

    def test_down_index1(self):
        self.assertEqual(funcs.downward_index_converter((3,7)), (7,3))
    def test_down_index2(self):
        self.assertEqual(funcs.downward_index_converter((4,5)), (5,4))

    def test_check_up1(self):
        puz = ["AAAAANAAAN",  
               "FNFFFAFFFA",
               "IAIIIMIIIT",
               "JFJJJJJJJS",
               "BBBBBBBBBB",
               "CCCCCCCCCC",
               "DDDDDDDDDD",
               "EEEEEEEEEE",
               "GGGGGGGGGG",
               "HHHHHHHHHH"]
        words = "FAN MAN BAN STAN".split()
        print("upward words: ", funcs.check_up(puz, words))
        self.assertEqual(funcs.check_up(puz, words)['STAN'], (3,9))
    def test_check_up2(self):
        puz = ["AAAAANAAAN",  
               "FNFFFAFFFA",
               "IAIIIMIIIT",
               "JFJJJJJJJS",
               "BBBBBBBBBB",
               "CCCCCCCCCC",
               "DDDDDDDDDD",
               "EEEEEEEEEE",
               "GGGGGGGGGG",
               "HHHHHHHHHH"]
        words = "FAN MAN BAN STAN".split()
        self.assertEqual(funcs.check_up(puz, words)['MAN'], (2,5))

    def test_check_diagonal1(self):
        puz = ["AAAAAAAAAA",  
               "FFFFFFFFFF",
               "IIIIIIIIII",
               "JJJJJJJJJJ",
               "BBBBBBBBBB",
               "CCACCCCCCC",
               "DDDNSDDDDD",
               "EEEEETEEEE",
               "GGGGGGAGGG",
               "HHHHHHHNHH"]
        words = "FAN MAN BAN STAN".split()
        print("diagonal words: ", funcs.check_diagonal(puz, words))
        self.assertEqual(funcs.check_diagonal(puz, words)['BAN'], (4,1))
    def test_check_diagonal2(self):
        puz = ["AAAAAAAAAA",  
               "FFFFFFFFFF",
               "IIIIIIIIII",
               "JJJJJJJJJJ",
               "BBBBBBBBBB",
               "CCACCCCCCC",
               "DDDNSDDDDD",
               "EEEEETEEEE",
               "GGGGGGAGGG",
               "HHHHHHHNHH"]
        words = "FAN MAN BAN STAN".split()
        self.assertEqual(funcs.check_diagonal(puz, words)['STAN'], (6,4))

    def test_diag_index1(self):
        self.assertEqual(funcs.diagonal_index_converter((1,7)), (7,8))
    def test_diag_index2(self):
        self.assertEqual(funcs.diagonal_index_converter((8,2)), (2,0))


if __name__=='__main__':
    unittest.main()


