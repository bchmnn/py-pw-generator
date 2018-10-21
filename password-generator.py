import sys
import os
from random import randint

# functions
def usage():
    print("USAGE: python " + sys.argv[0] + " <number>")
    print("0 < number < 100")
    sys.exit(0)

def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def gen_rand_chr(lower, upper, specials, numbers):
    while True:
        num = randint(33, 126)
        if not lower and 96 < num and num < 123:
            continue
        elif not upper and 64 < num and num < 91:
            continue
        elif not specials and ( 32 < num and num < 48 ) \
                           or ( 57 < num and num < 65 ) \
                           or ( 90 < num and num < 97 ) \
                           or ( 122 < num and num < 127 ):
            continue
        elif not numbers and 47 < num and num < 58:
            continue
        else:
            return chr(num)

def to_clipb(s):
    os.system("echo " + s + " | clip")

# script
if len(sys.argv) != 2:
    usage()

s = sys.argv[1]
if not is_int(s):
    usage()

length = int(s)
if length < 1 or length > 100:
    usage()


password = ""
shell_password = ""
for i in range(0, length):
    char = gen_rand_chr(True, True, False, True)
    password += char
    shell_password += "^"+char

print(password)
to_clipb(shell_password)
