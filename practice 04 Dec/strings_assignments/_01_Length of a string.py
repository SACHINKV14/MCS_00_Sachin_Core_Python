

a = '''Lorem ipsum dolor sit amet,
    consectetur adipiscing elit,
    sed do eiusmod tempor incididunt
    ut labore et dolore magna aliqua.'''

print("with special characters",len(a))
numeric_string2=""
for character in a:
    if character.isalpha():
        numeric_string2 +=character
print("without special characters",len(numeric_string2))
