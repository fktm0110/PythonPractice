temperature = float(input("Enter temperature : "))
convert = input("Covert to (F)ahrenheit or (C)elsius? ")

if convert == "F":
    result=(9/5)*temperature+32
    unit = "C"

elif convert == "C":
    result=(5/9)*(temperature-32)
    unit = "F"

print("{}{} = {}{}".format(temperature,unit, result, convert))