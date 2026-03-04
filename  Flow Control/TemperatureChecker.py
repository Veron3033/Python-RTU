print("Enter temperature:")
temp = float(input())

if temp < 35:
    print("a bit too cold")
elif 35 <= temp <= 37:
    print("you are all right")
else:
    print("possible fever")