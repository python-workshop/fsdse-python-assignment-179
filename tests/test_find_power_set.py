from unittest import TestCase


class TestFind_power_set(TestCase):
    def test_find_power_set(self):
        try:
            from build import find_power_set
        except ImportError:
            self.assertFalse("no function found")

        input_set = ''
        expected = ['']
        result = find_power_set(input_set)
        self.assertEqual(result, expected)
        input_set = 'a'
        expected = ['a', '']
        result = find_power_set(input_set)
        self.assertEqual(result, expected)
        input_set = 'ab'
        expected = ['a', 'ab', 'b', '']
        result = find_power_set(input_set)
        self.assertEqual(result, expected)
        input_set = 'abc'
        expected = ['a', 'ab', 'abc', 'ac',
                    'b', 'bc', 'c', '']
        result = find_power_set(input_set)
        self.assertEqual(result, expected)
        input_set = 'aabc'
        expected = ['a', 'aa', 'aab', 'aabc',
                    'aac', 'ab', 'abc', 'ac',
                    'b', 'bc', 'c', '']
        result = find_power_set(input_set)
        self.assertEqual(result, expected)
