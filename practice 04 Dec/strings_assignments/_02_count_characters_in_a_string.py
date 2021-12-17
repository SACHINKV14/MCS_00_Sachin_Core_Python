
a = '''Lorem ipsum dolor sit amet,
    consectetur adipiscing elit,
    sed do eiusmod tempor incididunt
    ut labore et dolore magna aliqua.'''
alpha_string2=""
for character in a:
    if character.isalpha():
        alpha_string2 +=character
print(len(alpha_string2))