import unittest

import lex

class TestLex(unittest.TestCase):
    def test_lexer_head(self):
        data = '# HEAD1\n## HEAD2'
        lex.lexer.input(data)
        
        tokens = ['HEAD', 'LINE', 'CR',
                'HEAD', 'LINE']
        for token_type in tokens:
            token = lex.lexer.token()
            self.assertEqual(token_type, token.type)
        self.assertIsNone(lex.lexer.token())

    def test_lexer_line(self):
        data = 'foo\nbar\ndah'
        lex.lexer.input(data)

        tokens = ['LINE', 'CR', 'LINE', 'CR', 'LINE']
        for token_type in tokens:
            token = lex.lexer.token()
            self.assertEqual(token_type, token.type)
        self.assertIsNone(lex.lexer.token())

    def test_lexer_quote(self):
        data = '> foo\n> bar\ndah'
        lex.lexer.input(data)

        tokens = ['QUOTE', 'LINE', 'CR',
                'QUOTE', 'LINE', 'CR',
                'LINE']
        for token_type in tokens:
            token = lex.lexer.token()
            self.assertEqual(token_type, token.type)
        self.assertIsNone(lex.lexer.token())

    def test_lexer_olist(self):
        data = '1. foo\n2. bar\n3. dah'
        lex.lexer.input(data)

        tokens = ['OLIST', 'LINE', 'CR',
                'OLIST', 'LINE', 'CR',
                'OLIST', 'LINE']
        for token_type in tokens:
            token = lex.lexer.token()
            self.assertEqual(token_type, token.type)
        self.assertIsNone(lex.lexer.token())

    def test_lexer_olist_with_random_number(self):
        data = '1. foo\n' \
               '233. bar\n' \
               '12345. dah'
        lex.lexer.input(data)

        tokens = ['OLIST', 'LINE', 'CR',
                'OLIST', 'LINE', 'CR',
                'OLIST', 'LINE']
        for token_type in tokens:
            token = lex.lexer.token()
            self.assertEqual(token_type, token.type)
        self.assertIsNone(lex.lexer.token())

    def test_lexer_ulist(self):
        data = '* foo\n' \
               '* bar\n' \
               '* dah'
        lex.lexer.input(data)

        tokens = ['ULIST', 'LINE', 'CR',
                'ULIST', 'LINE', 'CR',
                'ULIST', 'LINE']
        for token_type in tokens:
            token = lex.lexer.token()
            self.assertEqual(token_type, token.type)
        self.assertIsNone(lex.lexer.token())

if __name__ == '__main__':
    unittest.main()
