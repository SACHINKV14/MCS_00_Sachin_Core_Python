"""
Sample Input 0

Ross
Taylor
Sample Output 0

Hello Ross Taylor! You just delved into python.
"""

def print_full_name(first, last):
    print(f'Hello {first} {last}! You just delved into python.')
    # Write your code here

if __name__ == '__main__':
    first_name = "Ross"
    last_name = "Taylor"
    print_full_name(first_name, last_name)