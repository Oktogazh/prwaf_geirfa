from utils.word_utils import collect_words_of_length


def main():
    print("Hello, world!")
    # load content of the file dic/src.dict
    dic = ""
    with open("dic/src.dic") as f:
        dic = f.read()

    real_words = collect_words_of_length(dic, 6)
    print(len(real_words))


if __name__ == "__main__":
    main()
