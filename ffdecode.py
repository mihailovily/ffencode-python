morse_rev = {
    " @": "A",
    "@   ": "B",
    "@ @ ": "C",
    "@  ": "D",
    " ": "E",
    "  @ ": "F",
    "@@ ": "G",
    "    ": "H",
    "  ": "I",
    " @@@": "J",
    "@ @": "K",
    " @  ": "L",
    "@@": "M",
    "@ ": "N",
    "@@@": "O",
    " @@ ": "P",
    "@@ @": "Q",
    " @ ": "R",
    "   ": "S",
    "@": "T",
    "  @": "U",
    "   @": "V",
    " @@": "W",
    "@  @": "X",
    "@ @@": "Y",
    "@@  ": "Z",
    " @@@@": "1",
    "  @@@": "2",
    "   @@": "3",
    "    @": "4",
    "     ": "5",
    "@    ": "6",
    "@@   ": "7",
    "@@@  ": "8",
    "@@@@ ": "9",
    "@@@@@": "0",
    "@@  @@": ", ",
    " @ @ @": ".",
    "  @@  ": "?",
    "@  @ ": "/",
    "@    @": "-",
    "@ @@ ": "(",
    "@ @@ @": ")",
    "#": " "
}
letters = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
with open('crypted.txt') as f:
    encoded = f.read()
    encoded = encoded.split("/")
result = []
filtered = []
for i in range(len(encoded)):
    word = encoded[i]
    crypted = True
    for j in range(len(word)):
        if word[j] in letters:
            crypted = False
    if crypted:
        filtered.append(word)
for i in filtered:
    if i in morse_rev:
        result.append(morse_rev[i])
print(''.join(result))
with open('decrypted.txt', 'w') as f:
    f.write(''.join(result))