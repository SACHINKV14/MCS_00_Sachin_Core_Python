# print("-----method 1--------")
# def swap(string1):
#     start=string1[0]
#     end=string1[-1]
#     swapped_string=end+string1[1:-1]+start
#     print(swapped_string)
#
# # should implement removing special characters
# a = '''Lorem ipsum dolor sit amet,
#     consectetur adipiscing elit,
#     sed do eiusmod tempor incididunt
#     ut labore et dolore magna aliqua.'''
# swap(a)
#
# print("-----method 1-------")

print("-----method 2-------")
string2="sachin.k.v!123"
numeric_string2=""
for character in string2:
    if character.isalpha():
        numeric_string2 +=character
print(numeric_string2)
start=numeric_string2[0]
end=numeric_string2[-1]
swapped_string=end+numeric_string2[1:-1]+start
print(swapped_string)
print("-----method 2-------")