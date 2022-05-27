# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True
word=input("first_word: ")
anagram=input("second_word: ")

def find_anagram():
    # [assignment] Add your code here
    if sorted(word)== sorted(anagram)                                                                                                                                                                                       :
         return("the anagram is true")
    else:
         return("the anagram is false")

find_anagram()