def to_farh(temp) -> float :
    temp =  temp * 9/5  + 32
    return temp

def to_cels(temp) -> float :
    temp = 5/9 * (temp - 32)
    return temp

result = int(input("Enter if 1 if you know celsius or 2 if you know fahrenheit\n"))

while (result < 1 or result > 2) :
    print("invalid input, enter 1 or 2")
    result = int(input("Enter if 1 if you know celsius or 2 if you know fahrenheit\n"))

if (result == 1) :
    temp = float(input("what's the temperature in Celsius \n"))
    temp = to_farh(temp)
    print("Temperature in Farhrenheit is:", temp)

else :
    temp = float(input("what's the Farhrenheit temperature \n"))
    temp = to_cels(temp)
    print("Temperature in Celsius is:", temp)



print("Fin")
