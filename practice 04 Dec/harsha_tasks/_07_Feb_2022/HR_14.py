def mutate_string(string, position, character):
    a=string[0:position]+character+string[position+1::]
    return a

if __name__ == '__main__':
    s = input("enter string:")
    i, c = input("enter index and characer:").split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)