from Controller import Controller


class Hangman:

    def __init__(self):
        Controller().main()


if __name__ == "__main__":
    #TODO read command line db name
    #TODO if letter inputed second time read as error
    Hangman()