
print("Distance (1)")
print("Time (2)")
print("Temperature (3)")
a = input("What do you want to convert: ")

if a == 1:
    Distance()
elif a == 2:
    Time()
elif a == 3:
    Temperature()
else:
    print("Falsche Eingabe")

