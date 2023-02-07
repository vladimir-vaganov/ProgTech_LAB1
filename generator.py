import random, string

def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))

f = open("1000000.txt", "w")

for i in range(6000000):
    f.write(randomword(3) + " ")
    if (i % 6 == 5):
        f.write("\n")

f.close()
