def long_word_reverse(long_string):
    sentence = str(input(long_string))
    result = sentence.split()
    new_sentence = " "

    result.reverse()
    return (new_sentence.join(result))

print(long_word_reverse("Type in a long sentence: "))
