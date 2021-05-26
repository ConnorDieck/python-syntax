words = ["hello", "hey", "goodbye", "yo", "yes"]

# for word in words:
#     new_word = ""
#     for char in word:
#         new_word += char.capitalize()
#     print(new_word)

def print_upper_words(words, must_start_with):
    """Returns a list of words in all caps"""

    for word in words:
        # print(word)
        new_word = ""
        for letter in must_start_with:
            # print(word[0])
            # print(letter)
            # print(letter.capitalize())
            # print(word[0] == letter or word[0] == letter.capitalize())

            if word[0] == letter or word[0] == letter.capitalize():
                for char in word:
                    new_word += char.capitalize()
        print(new_word)

print_upper_words(words, {"h", "y"})