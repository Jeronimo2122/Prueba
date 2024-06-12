suma = 0
for i in range(101):

    if i % 3 == 0 or i % 5 == 0:
        if suma != 0:
            print(suma)
            suma = 0
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")

    else:
        suma += i
