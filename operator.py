def Distance():
    print("Distance")
    print("--------")
    print("kilometer (1)")
    print("meter (2)")
    print("centimeter (3)")
    print("miles (4)")
    o1 = input("What do you want to convert: ")
    o2 = input("What do you want to convert it to: ")
    if o1 == 1:
        kilometer()
    elif o1 == 2:
        meter()
    elif o1 == 3:
        centimeter()
    elif o1 == 4:
        miles()
    else:
        print("Falsche Eingabe")


def Time():
    print("Time")
    print("--------")
    print("seconds (1)")
    print("minutes (2)")
    print("hours (3)")
    print("days (4)")
    o1 = input("What do you want to convert: ")
    o2 = input("What do you want to convert it to: ")
    if o1 == 1:
        seconds()
    elif o1 == 2:
        minutes()
    elif o1 == 3:
        hours()
    elif o1 == 4:
        days()
    else:
        print("Falsche Eingabe")


def Temperature():
    print("Temperature")
    print("--------")
    print("Celsius (1)")
    print("Fahrenheit (2)")
    print("Kelvin (3)")
    o1 = input("What do you want to convert: ")
    o2 = input("What do you want to convert it to: ")
    if o1 == 1:
        Celsius()
    elif o1 == 2:
        Fahrenheit()
    elif o1 == 3:
        Kelvin()
    else:
        print("Falsche Eingabe")