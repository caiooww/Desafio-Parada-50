import collections

# def count_vowels(file_name):
#     vowels = 'aeiouáéíóúãõ'
#     with open(file_name, 'r') as f:
#         text = f.read().lower()
#         vowel_count = {vowel: text.count(vowel) for vowel in vowels}
#     return vowel_count

# print(count_vowels('exagerado_letra.txt'))

#* or



def count_vowels(file_name):
    vowels = 'aeiouáéíóúãõ'
    with open(file_name, 'r') as f:
        text = f.read().lower()
        vowel_count = collections.Counter(c for c in text if c in vowels)
    return vowel_count

print(count_vowels('exagerado_letra.txt'))

#o código debaixo da erro se rodar como "run python file", mas como terminal dedicado ele funciona