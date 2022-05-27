# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


#def find_anagram(word, anagram):
    # [assignment] Add your code here
def check(s1, s2):

	if (sorted(s1) == sorted(s2)):
		print("True")
	else:
		print("False")


s1 = "below"
s2 = "elbow"
check(s1, s2)

s1 = "hello"
s2 = "check"
check(s1, s2)

    #return True