
def samitleri_al(text):
    vowels = "aeiouAEIOU"
    result = ""
    for char in text:
        if char not in vowels:
            result += char
    return result

text = "The hopes die the lastest"
result = samitleri_al(text)
print(result)