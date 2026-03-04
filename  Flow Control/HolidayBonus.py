salary = float(input("Your monthly salary: "))
years_worked = int(input("Number of years worked: "))

if years_worked > 2:
    bonus_years = years_worked - 2
    bonus = salary * 0.15 * bonus_years
    print(f"Your holiday bonus is: {bonus:.2f}")
else:   print("You are not eligible for a holiday bonus.")