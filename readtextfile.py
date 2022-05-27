# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

#def read_file_content("filename"):
    # [assignment] Add your code here
f = open("story.txt","r")
for x in f:
	print(x)

    
    #return "Hello World"




    
from collections import Counter

def count_words(file_name):
	with open(file_name) as f:
		return Counter(f.read().split())

print("Frequency :",count_words("story.txt"))
    #text = read_file_content("story.txt")
    # [assignment] Add your code here


    #return {"as": 10, "would": 20}