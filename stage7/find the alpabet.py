word = input()

alphabet = ['a']
buf = ord('a')

while alphabet[-1] != 'z' :
    buf += 1
    alphabet.append(chr(buf))

alphabet = {i:word.find(i) for i in alphabet}

count = list(alphabet.values())

for i in count :
    print(i, end=" ")