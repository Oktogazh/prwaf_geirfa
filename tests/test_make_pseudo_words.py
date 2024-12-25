from utils.word_utils import collect_words_of_length, generate_pseudowords_for_length

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
lenfix
lensix
rensev
sonven
vaneno
"""


def test_collect_words_of_length():
    assert collect_words_of_length(test_string, 6) == (
        "lenfix",
        "lensix",
        "rensev",
        "sonven",
        "vaneno",
    )


def test_make_ngrams_for_length():
    dic = collect_words_of_length(test_string, 6)
    result = generate_pseudowords_for_length(dic, 6)
    expected = {"lensev", "renfix", "rensix"}
    assert set(result) == expected
