def count_consonants(name):
    #mapping through using dictionaries
    consonants = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7,
                  'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13,
                  'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19,
                  't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25,
                  'z': 26}
   #these variables keep track of maximum consonant and initial or current being calculated
    max_value = 0
    initial_value = 0
   #looping through to iterate over each value character
    for value in name:
        if value in "aeiou":
            max_value = max(max_value, initial_value)
            initial_value = 0
            
        else:
            initial_value += consonants[value]

    return max(max_value, initial_value)

word1 = input("Enter a name: ") 
word2 = input("Enter another name: ")

#printing the output
print(count_consonants(word1))
print(count_consonants(word2))
