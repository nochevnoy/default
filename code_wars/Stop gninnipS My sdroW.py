"""
Write a function that takes in a string of one or more words, 
and returns the same string, but with all five or more letter words reversed 
(Just like the name of this Kata). Strings passed in will consist of only letters and spaces. 
Spaces will be included only when more than one word is present.
"""

def spin_words(sentence):
    r = []
    words = sentence.split()
    for word in words:
        if len(word) >= 5:
            word = word[::-1]
            r.append(word)
        else:
            r.append(word)
    res = ' '.join(r)
    return res
