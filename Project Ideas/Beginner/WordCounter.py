# Objective, to count the numbers of words in an Input
class WordsParser:
    def __init__(self, input):
        words = self.__count_word(input)
        print(words)
    def __count_word(self, input):
        if not isinstance (input , str) :
            return 0
        wordCount=1
        for i in range(len(input)):
            if ((i+1)< len(input)) and (' ' == input[i] or '\n'==input [i]):
                wordCount += 1
        return wordCount
words = WordsParser("""
Hello this is Abhirama Sonny
I am going to count the words in this sentence.
""")
