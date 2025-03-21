sentence = str(input('write something: '))
def check():
    sentence2 = sentence.capitalize()
    if sentence2[-1] != ".":
        new_sentence = sentence2.__add__(".")
        print(new_sentence)
    else:
        print(sentence2)
check()


