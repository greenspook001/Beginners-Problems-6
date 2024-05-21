# The first one I did
def triangleTest(side1, side2, side3):
    sides = sorted([side1, side2, side3])
    return sides[0] + sides[1] > sides[2]

print(triangleTest(3, 4, 5))  
print(triangleTest(1, 2, 3))  

# The second one I did
def greet_morning(name):
    print(f"Good morning, {name}!")

def greet_afternoon(name):
    print(f"Good afternoon, {name}!")

def greet_evening(name):
    print(f"Good evening, {name}!")

def main():
    name = input("What's your name: ")
    time = int(input("What time is it (0-23): "))

    if 0 <= time < 12:
        greet_morning(name)
    elif 12 <= time < 18:
        greet_afternoon(name)
    elif 18 <= time < 24:
        greet_evening(name)
    else:
        print("Invalid time. Please enter a time between 0 and 23.")

main()


# The third one I did
def getEven(numbers):
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers

numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = getEven(numbers_list)

print("Even numbers:", even_numbers)
