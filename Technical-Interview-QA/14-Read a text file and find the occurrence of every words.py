

def find_word_occurrence(file=None):

    with open(file, "r") as f:
        lines = f.readlines()
        dict1 = {}
        for line in lines:
            wordlist = line.replace(",", "").split(" ")
            for i in range(len(wordlist)-1):
                if wordlist[i] in dict1.keys():
                    dict1[wordlist[i]] += 1
                else:
                    dict1[wordlist[i]] = 1
        print(dict1)


find_word_occurrence(file='D:\\file.txt')