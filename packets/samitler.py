
def unique_consonants(text):
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    unique_consonant_set = set()
    for letter in text:
        if letter in consonants:
            unique_consonant_set.add(letter)
    return list(unique_consonant_set)

text = "The hopes die the lastest"
result = unique_consonants(text)
print(result)
