import unittest

from word_wrap import Wrapper

class TestWrapper(unittest.TestCase):
    # create an instance of Wrapper, stored in self.wrapper
    def setUp(self):
        self.wrapper = Wrapper()
    
    def test_wrapper_returns_empty_string(self):
        wrapped_result = self.wrapper.wrap('', 1)
        self.assertEqual('', wrapped_result)
    
    def test_wrapper_returns_string_when_shorter_than_column_length(self):
        wrapped_result = self.wrapper.wrap('beans', 6)
        self.assertEqual('beans', wrapped_result)

if __name__ == '__main__':
    unittest.main()
