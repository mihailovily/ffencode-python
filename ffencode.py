with open('hideme.txt') as f:
    hideme = f.read().upper()
with open('container.txt') as f:
    container = f.read()
    container = container.split()
result = ""
# . = ' '
# - = @
morse = {
    "A": " @",
    "B": "@   ",
    "C": "@ @ ",
    "D": "@  ",
    "E": " ",
    "F": "  @ ",
    "G": "@@ ",
    "H": "    ",
    "I": "  ",
    "J": " @@@",
    "K": "@ @",
    "L": " @  ",
    "M": "@@",
    "N": "@ ",
    "O": "@@@",
    "P": " @@ ",
    "Q": "@@ @",
    "R": " @ ",
    "S": "   ",
    "T": "@",
    "U": "  @",
    "V": "   @",
    "W": " @@",
    "X": "@  @",
    "Y": "@ @@",
    "Z": "@@  ",
    "1": " @@@@",
    "2": "  @@@",
    "3": "   @@",
    "4": "    @",
    "5": "     ",
    "6": "@    ",
    "7": "@@   ",
    "8": "@@@  ",
    "9": "@@@@ ",
    "0": "@@@@@",
    ", ": "@@  @@",
    ".": " @ @ @",
    "?": "  @@  ",
    "/": "@  @ ",
    "-": "@    @",
    "(": "@ @@ ",
    ")": "@ @@ @",
    " ": "#"
}

for i in range(len(container)):
    if (i + 1) <= len(hideme):
        if hideme[i] in morse:
            result += container[i] + "/" + morse[hideme[i]] + "/"
    else:
        result += container[i]
result += "."
with open('crypted.txt', 'w') as f:
    f.write(result)
print(result)
