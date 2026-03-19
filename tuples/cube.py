cubes = []

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

for number in range(start, end + 1):
    cube = number ** 3
    cubes.append(cube)
    print(f"{number} in a cube: {cube}")

print(f"\nAll cubes: {cubes}")