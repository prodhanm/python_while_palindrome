import unittest

class TestPalindromes(unittest.TestCase):
    def true_palindrome(self):
        word = "abba"
        for w in range(len(word)//2):
            if word[w] == word[len(word)-w-1]:
                self.assertTrue(word)

if __name__ == "__main__":
    unittest.main()

'''
for w in range(len(word)//2):
            self.assertEqual(word[w], word[len(word)-w-1])
'''