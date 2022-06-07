# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagrams(word, anagram):
    # [assignment] Add your code here

	word = word.replace(" ", "")
	anagram = anagram.replace(" ", "")

	return sorted(word) == sorted(anagram)

print("Calling find_anagrams with 'hello' and 'check' ", find_anagrams("hello", "check"))
print("Calling find_anagrams with 'below' and 'elbow' ", find_anagrams("below", "elbow"))
