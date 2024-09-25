
# Lesson 23: Emoji Converter
# This program converts text to emoji

def emoji_converter(message):
    words = message.split(' ')
    emojis = {
        ":)": "😊",
        ":(": "😢"
    }
    result = ""
    for word in words:
        result += emojis.get(word, word) + " "
    return result

message = input("Enter a message: ")
print(emoji_converter(message))
