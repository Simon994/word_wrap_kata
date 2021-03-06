import unittest

from word_wrap import Wrapper

class TestWrapper(unittest.TestCase):
    
    def test_wrapper_returns_empty_string(self):
        wrapped_result = Wrapper.wrap('', 1)
        self.assertEqual('', wrapped_result)
        
    def test_wrapper_returns_string_when_shorter_than_column_length(self):
        wrapped_result = Wrapper.wrap('beans', 6)
        self.assertEqual('beans', wrapped_result)
    
    def test_wrapper_returns_string_when_length_is_equal_to_column_length(self):
        wrapped_result = Wrapper.wrap('beans', 5)
        self.assertEqual('beans', wrapped_result)

    def test_wrapper_wraps_string_with_no_spaces_and_longer_than_column_length(self):
        wrapped_result = Wrapper.wrap('bean', 2)
        self.assertEqual('be\nan', wrapped_result)

    def test_wrapper_wraps_another_string_with_no_spaces_and_longer_than_column_length(self):
        wrapped_result = Wrapper.wrap('andgone', 3)
        self.assertEqual('and\ngon\ne', wrapped_result)

    def test_wrapper_wraps_two_words_only_space(self):
        wrapped_result = Wrapper.wrap('fava beans', 6)
        self.assertEqual('fava\nbeans', wrapped_result)
    
    def test_wrapper_wraps_two_more_words_with_only_one_space(self):
        wrapped_result = Wrapper.wrap('bean beangone', 10)
        self.assertEqual('bean\nbeangone', wrapped_result)

    def test_wrapper_wraps_three_words_at_all_spaces(self):
        wrapped_result = Wrapper.wrap('bean bean bean', 6)
        self.assertEqual('bean\nbean\nbean', wrapped_result)
    
    def test_wrapper_wraps_three_words_at_second_space(self):
        wrapped_result = Wrapper.wrap('bean bean gone', 10)
        self.assertEqual('bean bean\ngone', wrapped_result)
    
    def test_wrapper_wraps_two_words_with_second_word_longer_than_column_length(self):
        wrapped_result = Wrapper.wrap('bean beanandgone', 10)
        self.assertEqual('bean beana\nndgone', wrapped_result)
    
    def test_wrapper_wraps_very_long_word_across_multiple_lines(self):
        wrapped_result = Wrapper.wrap('supercalifragilisticexpialidocious', 10)
        self.assertEqual('supercalif\nragilistic\nexpialidoc\nious', wrapped_result)

if __name__ == '__main__':
    unittest.main()
