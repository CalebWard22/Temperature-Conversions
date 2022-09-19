# Hi shane, this is just a simplified version of the temperature thing :)

num = int(input("Enter a temperature: "))
unit = input("What unit is your temperature? ").upper()

if unit == "F":
    tem1 = (num - 32) * 5/9  # F to C
    tem2 = num * 5/9 + 32 + 273.15  # F to K
    output = f"{tem1}°C, {tem2}K"
elif unit == "C":
    tem1 = num * 9/5 + 32  # C to F
    tem2 = num + 273.15  # C to K
    output = f"{tem1}°F, {tem2}K"
else:
    tem1 = num - 273.25 * 9/5 + 32  # K to F
    tem2 = num - 273.15  # K to C
    output = f"{tem1}°F, {tem2}°C"

print(output)
