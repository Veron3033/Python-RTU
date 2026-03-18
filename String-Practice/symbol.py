text = input("Enter the text (first player): ")

masked = ""
for ch in text:
    if ch == " ":
        masked += " "
    else:
        masked += "*"

print(masked)

symbol = input("Enter a symbol to guess (second player): ").lower()

result = ""
for i in range(len(text)):
    if text[i] == " ":
        result += " "
    elif text[i].lower() == symbol:
        result += text[i]
    else:
        result += masked[i]

print(result)