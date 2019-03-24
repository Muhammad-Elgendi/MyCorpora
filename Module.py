from os import listdir
from os.path import join
from collections import Counter

path = input("What is your directory? ")

# get files paths from the given path
filesPaths = [join(path,f) for f in listdir(path)]
print("This directory has the following : ",filesPaths)
numberOfWords =int(input("We can get the most repeated word in the dictionary , How many word you want ? "))
content = ""

# open files
for file in filesPaths:
    fileHandle = open(file)
    content+=" "+fileHandle.read()
    fileHandle.close()

# A Counter is a dict subclass for counting hashable objects. 
# It is a collection where elements are stored as dictionary keys 
# and their counts are stored as dictionary values.
wordcounts = Counter(content.split())

# get n of the most repeated words
for i in range(numberOfWords):
    print("word :",max(wordcounts, key=wordcounts.get),"count :",wordcounts[max(wordcounts, key=wordcounts.get)],"\n")
    # remove the most repeated word
    wordcounts.pop(max(wordcounts, key=wordcounts.get),None)