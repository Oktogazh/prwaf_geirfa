from utils.word_utils import collect_words_of_length, generate_pseudowords_for_length


def main():
    # load content of the file dic/src.dict
    dic = ""
    with open("dic/src.dic") as f:
        dic = f.read()

    real_words = collect_words_of_length(dic, 6)
    pseudo_words = generate_pseudowords_for_length(real_words, 6)
    print("real words count", len(real_words))
    print("pseudo words count", len(pseudo_words))


if __name__ == "__main__":
    main()
