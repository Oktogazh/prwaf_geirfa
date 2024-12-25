from utils.word_utils import collect_words_of_length

"""
TODO:
test that the function collects words of length 6 in an tuple
test that the function make dictionary of n-grams returns a dictionary of n-grams
test that the function make pseudo words returns a list of pseudo words
test that no pseudo word is similar to a real word
"""

test_string = """
word
Sixlen
lensix
rensev
sonven
vaneno
"""


def test_collect_words_of_length():
    assert collect_words_of_length(test_string, 6) == (
        "lensix",
        "rensev",
        "sonven",
        "vaneno",
    )
