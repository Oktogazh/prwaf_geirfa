def collect_words_of_length(input: str, length: int) -> tuple:
    """
    Collects words of a given length from a string of words

    :param input: a string of words
    :param length: the length of the words to collect
    :return: a tuple of words of the given length
    """
    words = input.split("\n")
    return tuple(word for word in words if len(word) == length and word.islower())
