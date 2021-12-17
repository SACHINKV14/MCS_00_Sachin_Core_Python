import textwrap
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
# print(a)

txt1=textwrap.dedent(a).strip()
print(textwrap.fill(a,initial_indent='' * 4,subsequent_indent=''*8,width=80,))