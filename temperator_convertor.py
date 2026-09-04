temp = float(input("Enter temperature: "))
unit = input("Enter unit (C/F): ")

if unit == "C":
    fahrenheit = (temp * 9/5) + 32
    print("Temperature in Fahrenheit =", fahrenheit)

elif unit == "F":
    celsius = (temp - 32) * 5/9
    print("Temperature in Celsius =", celsius)

else:
    print("Invalid unit")