# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    file = open(filename, "r")
    return file


def count_words():
    text = read_file_content("./story.txt")
    tempDict = {}
    resultDict = {}

    for line in text:
        line = line.strip()

        line = line.lower()

        words = line.split(" ")

        for word in words:
            if word in tempDict:
                tempDict[word] = tempDict[word] + 1
            else:
                tempDict[word] = 1

    for key in list(tempDict.keys()):
        resultDict[key] = tempDict[key]

    return resultDict

print(count_words())