text = input("Enter text: ")

phrase = "not bad"

if phrase in text:
    index = text.find(phrase)
    text = text[:index] + "good" + text[index + len(phrase):]

print(text)