import string
alphabet = string.ascii_letters
request = input('write letters ... - ... ')
start = alphabet.index(request[0])
end = alphabet.index(request[-1])
print(alphabet[start:end])