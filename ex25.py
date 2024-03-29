def break_words(stuff):
    """This function will break words for us"""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sort this words"""
    return sorted(words)

def print_first_word(words):
    """Printing the first word after popping it off"""
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """Print the last word after popping it off"""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """Takes in a full sentence and returns sorted words"""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Printing the first and the last sentence"""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words and then prints the first and the last"""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

###sentence = "All good things come to those who wait."
#words = break_words(sentence)
#print(words)
#sorted_words = sort_words(words)
#print(sorted_words)
#print_first_word(words)
#print_last_word(words)
#print(words)
#print_first_word(sorted_words)
#print_last_word(sorted_words)
#print(sorted_words)
#sorted_words = sort_sentence(sentence)
#print(sorted_words)
#print_first_and_last(sentence)
#print_first_and_last_sorted(sentence)
