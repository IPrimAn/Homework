def second_index(text: str, some_str: str):
    first = text.find(some_str)
    if first == -1:
        print(None)
    second = text.find(some_str, first + 1)
    if second != -1:
        print(second)
    else:
        print(None)
second_index(input('write word or sentence:'), input('write symbol iin sentence: '))
