a_float=3.14159
b_float=-3.14159
formatted_float_a="{:+.2f}".format(a_float)
print(formatted_float_a)
formatted_float_b="{:+.2f}".format(b_float)
print(formatted_float_b)

#print the following floating numbers with no decimal places
formatted_float_c="{:+.0f}".format(b_float)
print(formatted_float_c)