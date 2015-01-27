#coding=utf-8
import unittest

from lex import lexer
from yacc import parser

class TestYacc(unittest.TestCase):
    def test_yacc_heading(self):
        data = '# Head1\n## Head2\n### Head3\n'
        result = parser.parse(data)

        self.assertEqual(len(result), 3)

        self.assertEqual(result[0]['type'], 'HEADING')
        self.assertEqual(result[0]['level'], 1)

        self.assertEqual(result[1]['type'], 'HEADING')
        self.assertEqual(result[1]['level'], 2)

        self.assertEqual(result[2]['type'], 'HEADING')
        self.assertEqual(result[2]['level'], 3)

    def test_yacc_cr(self):
        data = '\n\n'
        result = parser.parse(data)

        self.assertEqual(len(result), 2)
        
        self.assertEqual(result[0]['type'], 'CR')
        self.assertEqual(result[1]['type'], 'CR')

    def test_yacc_raw_line(self):
        data = 'foo\nbar\n'
        result = parser.parse(data)
        self.assertEqual(len(result), 2)

        self.assertEqual(result[0][0]['type'], 'RAW')
        self.assertEqual(result[0][0]['line'], 'foo')

        self.assertEqual(result[1][0]['type'], 'RAW')
        self.assertEqual(result[1][0]['line'], 'bar')

    def test_yacc_bold_line(self):
        data = 'foo**bar**dah\n'
        result = parser.parse(data)
        self.assertEqual(len(result), 1)
        self.assertEqual(len(result[0]), 3)

        self.assertEqual(result[0][0]['type'], 'RAW')
        self.assertEqual(result[0][0]['line'], 'foo')

        self.assertEqual(result[0][1]['type'], 'BOLD')
        self.assertEqual(result[0][1]['line'], 'bar')

        self.assertEqual(result[0][2]['type'], 'RAW')
        self.assertEqual(result[0][2]['line'], 'dah')

    def test_yacc_quote(self):
        data = '> foo\n> bar\n\n> dah\n'
        result = parser.parse(data)

        self.assertEqual(len(result), 3)

        self.assertEqual(result[0]['type'], 'QUOTE')
        self.assertEqual(result[0]['line'], ['foo', 'bar'])

        self.assertEqual(result[1]['type'], 'CR')

        self.assertEqual(result[2]['type'], 'QUOTE')
        self.assertEqual(result[2]['line'], ['dah'])

    def test_yacc_olist(self):
        data = '1. foo\n2. bar\n\n3. dah\n'
        result = parser.parse(data)

        self.assertEqual(len(result), 3)

        self.assertEqual(result[0]['type'], 'OLIST')
        self.assertEqual(result[0]['line'], ['foo', 'bar'])

        self.assertEqual(result[1]['type'], 'CR')

        self.assertEqual(result[2]['type'], 'OLIST')
        self.assertEqual(result[2]['line'], ['dah'])

    def test_yacc_ulist(self):
        data = '* foo\n* bar\n\n* dah\n'
        result = parser.parse(data)

        self.assertEqual(len(result), 3)

        self.assertEqual(result[0]['type'], 'ULIST')
        self.assertEqual(result[0]['line'], ['foo', 'bar'])

        self.assertEqual(result[1]['type'], 'CR')

        self.assertEqual(result[2]['type'], 'ULIST')
        self.assertEqual(result[2]['line'], ['dah'])


if __name__ == '__main__':
    unittest.main()
