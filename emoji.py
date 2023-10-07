# with function
def emoji_convertor(message):
    msg2 = msg.split(" ")
    emoji = {":(": "😔", ":)": "😊"}
    output = ""
    for line in msg2:
        output += emoji.get(line, line) + " "
    return output


msg = input(">")
result = emoji_convertor(msg)
print(result)
