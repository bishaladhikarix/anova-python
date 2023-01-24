message = input("> ")


def first_function(message):
    word = message.split()
    emoji ={
    ":)":"😁",
    ":(":"😢"
    }
    output = ""
    for each in word:
        output += emoji.get(each, each)
    return output

resut = first_function(message)
print(resut)