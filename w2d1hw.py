#  Exceptional Weather Forcast


while True:
    try:
        temperature = int(input("What is the temperature please? : "))
        print(f"You entered {temperature}!")
        break
    except ValueError:
        print("That was not a number! Try again!")

def temp_conversion():
    while True:
        try:
            temperature = int(input("What is the temperature please? : "))
            celcius = ((temperature - 32) * 5/9)
            # print(f"You entered {temperature}, the celcius value is {celcius}")
            # break
        except ValueError:
            print("That was not a number! Try again!")
        else:
            print(f"You entered {temperature}, the celcius value is {celcius} degrees!")
            break
        finally:
            print("Thank you for using the conversion app!")
    
temp_conversion()
