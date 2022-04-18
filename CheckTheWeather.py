#Very simple weather converter

choice = input("What do you want to convert? Degrees to Celsius or Celsius to Degrees? Type C for the first and D for the second: ")
print(choice, type(choice))

correct = False

def degreesToCelsius(num):
    temp = (num - 32)*.5556
    txt = "It is currently {} celsius"
    print(txt.format(temp))

def celsiusToDegrees(num):
    temp = (num *9/5) + 32
    txt = "It is currently {} degrees"
    print(txt.format(temp))


if choice == "D":
    correct = True
    temperature = input("Input a number: ")
    conversion = int(temperature)
    celsiusToDegrees(conversion)


if choice == "C":
    correct = True
    temperature = input("Input a number: ")
    conversion = int(temperature)
    degreesToCelsius(conversion)



while correct == False:
    print("Invalid answer")
    choose = input("Choose C or D: ")
    if choose == "C" or "D":
        correct = True
        temperature = input("Input a number: ")
        conversion = int(temperature)
        if choose == "C":
            degreesToCelsius(conversion)
        if choose == "D":
            celsiusToDegrees(conversion)






