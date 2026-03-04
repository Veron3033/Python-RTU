print("Enter temperature:")
temp = float(input())

if float(input()) < 35:
    print("a bit too cold")
elif float(input()) == 35 or float(input()) == 37:
    print("you are all right")
else:    print("possible fever")