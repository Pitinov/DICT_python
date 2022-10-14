print("Hello! My name is bot_Yarik")
print("I was created in 05.10.2022")
print("Please, remind me your name.")
name = input (">")
print(f"What a great name you have, {name}!")
print("Let me guess your age.")
print("Enter remainders of dividing your age by 3, 5 and 7.")
remainder3 = int(input (">"))
remainder5 = int(input (">"))
remainder7 = int(input (">"))
age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
print(f"Your age is {age} that's a good time to start programming!")
a = int(input("Now I will prove to you that I can count to any number you want.\n"))
for i in range(a + 1):
    print(str(i) + "!")
print("Completed, have a nice day!")
print("Test.")
print("You Human?")
print("1. Yes")
print("2. No")
while True:
    q = int(input(">"))
    if q == 1:
        print("Cool")
        print("Completed, have a nice day!")
        break
    else:
        print("Please try again")
print("Congratulations, have a nice day!")



