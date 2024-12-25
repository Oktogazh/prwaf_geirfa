import random


def collect_words_of_length(input: str, length: int) -> tuple:
    """
    Collects words of a given length from a string of words

    :param input: a string that is the content of an hunspell dictionary .dic file
    :param length: the length of the words to collect
    :return: a tuple of words of the given length
    """
    words = input.split("\n")
    return tuple(word for word in words if len(word) == length and word.islower())


def generate_pseudowords_for_length(words: tuple, length: int) -> tuple:
    """
    Generates pseudowords of a given length from a tuple of words

    :param words: a tuple of words from .collect_words_of_length
    :param length: the length of the pseudowords to generate
    :return: a tuple of pseudowords of the given length
    """

    ## generate the 3-grams of the words
    three_grams = []
    for i in range(length - 2):
        three_grams_of_index = []
        for word in words:
            three_gram = word[i : i + 3]
            if three_gram not in three_grams_of_index:
                three_grams_of_index.append(three_gram)
        three_grams.append(three_grams_of_index)

    ## generate the pseudowords
    pseudowords = three_grams[0]
    for i in range(len(three_grams[1:])):
        for word in pseudowords:
            for str in three_grams[i + 1]:
                if word[1 + i :] == str[:2]:
                    pseudowords.append(word + str[-1])
        pseudowords = [word for word in pseudowords if len(word) != 3 + i]

    for word in words:
        if word in pseudowords:
            pseudowords.remove(word)

    words_count = len(words)
    if words_count < len(pseudowords):
        ## randomly select words_count pseudowords
        random.shuffle(pseudowords)
        del pseudowords[words_count:]

    return tuple(sorted(pseudowords))
