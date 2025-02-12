# chat answer
def get_multiple_of_six():
    """
    return a multiple of 6 that was entered by the user
    :return: int a number
    """
    while True:
        try:
            user_input = input("Enter a multiple of 6: ")
            number = int(user_input)
            if number % 6 == 0:
                return number
            else:
                print("That number is not a multiple of 6. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")



#professor
def get_multiple():
    while True:
        try:
            n = input("Please give me a multiple of 6: ")
            n = int(n)
            if n % 6 == 0:
                return n
            else:
                print("It is not multiple of 6! Try again.")
        except ValueError:
            print("You have not entered a number")

print(get_multiple())