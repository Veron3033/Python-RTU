text = input("Enter the text (first player): ")

# Build the masked version: asterisks for letters, spaces stay
masked = ""
for ch in text:
    if ch == " ":
        masked += " "
    else:
        masked += "*"

print(masked)

symbol = input("Enter a symbol to guess (second player): ").lower()

# Reveal matching letters
result = ""
for i in range(len(text)):
    if text[i] == " ":
        result += " "
    elif text[i].lower() == symbol:
        result += text[i]
    else:
        result += masked[i]  # keep existing asterisk (or already revealed letter)

print(result)