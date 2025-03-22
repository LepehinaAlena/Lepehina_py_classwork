import unittest

import pytest

from suggester import app, Suggester, SUGGEST_FILE


class MyTestCase(unittest.TestCase):

    def test_suggester_initialization(self):
        suggester = Suggester(SUGGEST_FILE)
        assert suggester is not None
        assert len(suggester.words) > 0

    def test_length(self):
        suggester = Suggester(SUGGEST_FILE)
        suggestions = suggester.get('ан')
        assert len(suggestions) <= 10
        for suggestion in suggestions:
            assert suggestion.startswith('ан')

    def test_words(self):
        suggester = Suggester(SUGGEST_FILE)
        suggestions = suggester.get('ана')
        print(suggestions)
        result = ["ана", "анабадуст", "анабазин", "анабазис", "анабаптист", "анабаптистка", "анабас", "анабасис",
                  "анаболизм", "анаболик", "анаболия"]
        assert suggestions == result


if __name__ == '__main__':
    unittest.main()
