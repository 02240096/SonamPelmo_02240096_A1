import requests


def menu():                                             #prints a menu and asks the user for input.
      print("Menu")
      print("1. Prime Number Sum")
      print("2. Lenght Unit Converter")
      print("3. Consonants Counter ")
      print("4. Min Max Finder")
      print("5. Palindrome Checker")
      print("6. Word Counter")
      print("7. Exit")
      choice = int(input("Enter your choice : "))
      return choice                                       #used to send a value back from a function

choice = menu()

def prime_number_sum_calculator():
    """ Find the sum of prime numbers between the given range. """
    startingnumber = int(input("Enter the starting number: "))
    endingnumber = int(input("Enter the ending number: "))
    sum = 0                                                    #sets sum to zero

    for num in range(startingnumber, endingnumber +1):
        if num > 1:                                #num > 1: checks if num is more than 1.
            for i in range(2, num):
                if num % i == 0:                #num % i gives the remainder of num ÷ i, used to check divisibility
                    break
            else:
                    sum += num                     # sum += adds number one by one
    print("Sum of prime numbers:", sum)
    return sum 

def Length_Unit_Converter():
    """ Convert meters to feet and feet to meters. """
    length = float(input("Enter the length:"))
    direction = input("Enter the length (M for meters to feet, F for feet to meters):")
    if direction == 'M':
          x = length * 3.281                      # 1 meter = 3.281 feet
          y = round(x, 2)
          print("The value in feet is:", y)
    elif direction == 'F':
          x = length / 3.281                      # 1 feet = 0.3048 meters(1/3.281)
          y = round(x, 2)
          print("The value in metre is:", y)
    else: 
          print("Invalid choice!")

def consonant_counter():
    """ Count consonants in a string. """
    text = input("Enter the text: ")
    count = 0                                  # initializes the variable count with a value of 0
    for i in text:
        if i in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ":
               count += 1                      #count += 1 adds a value to the count variable and updates it
    print("The number of consonants in the text is:", count)
    return count 

def min_max_finder(): 
    """ Find the lowest and the highest number. """
    numbers = input("Enter the numbers separated by commas: ").split(',')  #split() divides a string into a list 
    numbers = [int(num.strip()) for num in numbers]                       #strip() removes spaces 
    print("The lowest number is:", min(numbers))
    print("The highest number is:", max(numbers))

def palindrome_checker():
    """ Check if the string is a palindrome. """
    text = input("Enter the text:")
    if text == text[ ::-1]:                               # ::-1 Reverses a string or list.
          print("Its a palindrome. ")
    else: 
         print("Its not a palindrome. ")

def word_counter():
    """Counts occurrences of ['the', 'was', 'and'] in a text file."""
    url = input("Enter the URL of the text file: ")
    try:
        text = requests.get(url).text.lower()
        words = ["the", "was", "and"]
        counts = {word: text.count(word) for word in words}
        print(f"Word counts: {counts}")
    except requests.exceptions.RequestException:
         print("Error fetching the file")

def Exit_program():
    print("Thank you for using the program.")
    return 

while True:
    if choice == 1: 
        prime_number_sum_calculator()
    elif choice == 2:
        Length_Unit_Converter()
    elif choice == 3:
        consonant_counter()
    elif choice == 4:
        min_max_finder()
    elif choice == 5:
        palindrome_checker()
    elif choice == 6:
        word_counter()
    elif choice == 7:
        Exit_program()
        break
    else: 
        print("That does not seem right. Choose again. ")

    x = input("Do you want to continue? (y/n): ")
    if x.lower() == "y":
        choice = menu()
    else:
        Exit_program()
        break                                          #exit a loop
         