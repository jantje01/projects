morse = {
    "A": "* -",
    "B": "- * * *",
    "C": "- * - *",
    "D": "- * *",
    "E": "*",
    "F": "* * - *",
    "G": "- - *",
    "H": "* * * *",
    "I": "* *",
    "J": "* - - -",
    "K": "- * -",
    "L": "* - * *",
    "M": "- -",
    "N": "- *",
    "O": "- - -",
    "P": "* - - *",
    "Q": "- - * -",
    "R": "* - *",
    "S": "* * *",
    "T": "_",
    "U": "* * -",
    "V": "* * * -",
    "W": "* - -",
    "X": "- * * -",
    "Y": "- * - -",
    "Z": "- - * *",

    "1": "* - - - -",
    "2": "* * - - -",
    "3": "* * * - -",
    "4": "* * * * -",
    "5": "* * * * *",
    "6": "- * * * *",
    "7": "- - * * *",
    "8": "- - - * *",
    "9": "- - - - *",
    "0": "- - - - -"
}

answer = input("Typ the text you would like to convert: ")
answer = answer.upper()

generated_morse = []

for character in answer:
    if character == " ":
        generated_morse.append("/")
    if character in morse.keys():
        generated_morse.append(morse.get(character))
    else:
        pass

print("\n")
print(*generated_morse)
print("\n")

