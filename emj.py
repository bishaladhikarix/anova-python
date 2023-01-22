message = input("> ")
word = message.split()
emoji = {
    ":)":"😁",
    ":(":"😢"
}
output = ""
for each in word:
    output += emoji.get(each, each)
print(output)