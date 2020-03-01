def longWordReverse(long_string):
    sentence = str(input(long_string))
    result = sentence.split()
    newSentence = " "

    result.reverse()
    return (newSentence.join(result))

print(longWordReverse("Type in a long sentence: "))
