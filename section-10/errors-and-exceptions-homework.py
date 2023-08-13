# problem 1
try:
    for i in ["a", "b", "c"]:
        print(i**2)
except:
    print("You are trying to do some aritmethic operation on str values")

# problem 2
x = 5
y = 0

try:
    z = x / y
except:
    print("You are trying to divide a number by 0")
finally:
    print("All done")


# problem 3
def ask():
    while True:
        try:
            print(int(input("Please enter a number: ")) ** 2)
        except:
            print("Enter a valid number")
        else:
            break


ask()
