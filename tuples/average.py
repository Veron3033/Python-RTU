while True:
    user_input = input("Enter a number or 'q' to quit: ")
    if user_input == 'q':
        break
    try:
        number = float(user_input)
        numbers.append(number)
        average = sum(numbers) / len(numbers)

        sorted_numbers = sorted(numbers)
        top3 = sorted_numbers[-3:][::-1]
        bottom3 = sorted_numbers[:3]    

        print(f"Average: {average:.2f}")
        print(f"TOP 3:    {top3}")
        print(f"BOTTOM 3: {bottom3}")
    except ValueError:
        print("Invalid, enter new number: ")