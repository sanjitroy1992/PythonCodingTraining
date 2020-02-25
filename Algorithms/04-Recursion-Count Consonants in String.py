"""Youtube: https://youtu.be/FTOTyTXIX6I?list=PL5tcWHG-UPH1K7oTJgIbWy6rCMc8-8Lfm"""

def iterative_count_consonants():
    string = str(input("Enter the string: ")).lower().replace(" ","")
    vowels = 'aeiou'
    consonants_count = 0
    vowel_count = 0
    for i in range(len(string)):
        if string[i] not in vowels and string[i].isalpha():
            consonants_count += 1
    return [consonants_count]

print(iterative_count_consonants())
