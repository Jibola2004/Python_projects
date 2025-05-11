try:
    weight = float(input('Enter weight in kg: '))
    height = float(input('Enter height in cm: '))
    height = height / 100  # Convert cm to meters
    bmi = weight / height**2
    print(f'Your Body Mass Index is: {bmi:.2f}')

    if bmi > 0:
        if bmi <= 16:
            print("You are severely underweight")
        elif bmi <= 18.5:
            print("You are underweight")
        elif bmi <= 25:
            print("You are healthy")
        elif bmi <= 30:
            print("You are overweight")
        else:
            print("You are severely overweight")
    else:
        print("❌ Please enter valid weight and height values.")

except ValueError:
    print("❌ Invalid input! Please enter numerical values for weight and height.")
