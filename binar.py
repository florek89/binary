
# Wprowadzenie danych
while True:
    try:
        x_input = input("Enter a number and -after space- numeral system (2 or 10): ")
        x = x_input.split()
        x2_input = int(x[0])
        x3_input = int(x[1])
        score = ""
        temp = str(x2_input)
        power = 0
        number = 0
        binar_numbers = (1, 0)
        # Sprawdzenie czy podano poprawny system liczbowy
        if x3_input != 2 and x3_input != 10:
                print("Wrong numeral system!")

        else:
            # Konwertowanie z systemu dziesiętnego na binarny
            if x3_input == 10:
                while x2_input > 0:
                        score = str(x2_input % 2) + score
                        x2_input = x2_input // 2

                print(" /------------\ ")
                print(" |", score, "|", 2,  " |")
                print(" \------------/ ")
            # Konwertowanie z systemu binarnego na dziesiętny
            elif x3_input == 2:
                while len(temp) > 0:
                    bit = int(temp[-1])
                    number = number + bit * 2 ** power
                    power += 1
                    temp = temp[:-1]
                print(" /------------\ ")
                print(" |", number, "|", 10, "  |")
                print(" \------------/ ")
    # A kiedy wprowadzisz wszystko inne, oprócz tego o co prosi program:
    except ValueError:
        print("Wrong sign. Use a numbers only next time.")
    except IndexError:
        print("Ooooops! Try again --> NUMBER - SPACE - NUMERAL SYSTEM (2 or 10)")
