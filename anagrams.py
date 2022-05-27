# Check if a word is an anagrams
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


def find_anagrams():
    word1 = input("Please enter your first word: ")
    word2 = input("Please enter your second word: ")
    word1_list = list(word1)
    word1_list.sort()
    word2_list = list(word2)
    word2_list.sort()

    if word1_list == word2_list:
        return True
    else:
        return False


print(find_anagrams())

