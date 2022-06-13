# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}
import re
def read_file_content(filename):
    f = open(filename, "r")

    file = f.read()
    
    f.close()
    
    return file


txt = read_file_content("./story.txt")
print(txt)


def count_words():
    text = read_file_content("./story.txt")
    words = re.split(r'[;,.?\s]\s*',text)
    numberOfWords = {}

    for i in words:
        if numberOfWords.__contains__(i):

            value = numberOfWords.get(i)
            numberOfWords[i] = value+1
        else:
            numberOfWords[i] =1

    return numberOfWords
print(count_words())
    # return {"as": 10, "would": 20}