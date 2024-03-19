# Objective: The aim of this assignment is to enhance your understanding of exception 
# handling by creating a weather forecast application that gracefully handles unexpected 
# user input and provides user-friendly error messages.

# Task 1: Start
# Begin by setting up a simple user input loop that asks the user to enter the temperature 
# in Fahrenheit.

# Ensure that your program only accepts numerical input and provides a friendly 
# error message if the user enters something that can't be converted to a number.

while True:
    userTemp = input("Please enter a temperature in Fahrenheit...")
    try: 
        userTempFloat = float(userTemp)
        print(f"Great. You entered {userTempFloat}")
    except ValueError:
        print(f"'{userTemp}' is not a number. Make sure you enter a real number :)")


# Task 2: Temperature Conversion
# Write a function that converts the Fahrenheit temperature to Celsius.
# Remember that the formula is (Fahrenheit - 32) * 5/9.

# Use a try block to catch any potential errors during the conversion 
# process, such as division by zero or overflow errors.



# Task 3: User Experience
# Implement an else block that prints the converted temperature in a user-friendly format.

# Add a finally block that thanks the user for using the weather forecast 
# application, ensuring that this message is displayed regardless of 
# whether an exception was caught or not.


def tempConverter(Temp):
    convertedTemp = 0
    try:
        convertedTemp = round((Temp - 32) * (5/9), 1)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    except OverflowError:
        print("Overflow error! Use a more realistic temperature.")
    else:
        print(f"Successfully converted {userTemp} Fahrenheit to Celcius!")
        print(f"Your converted temperature is: {convertedTemp}")
        return convertedTemp


try:
    userTemp = float(input("Please enter a temperature in Fahrenheit..."))
except ValueError:
    print("Make sure you enter a valid number!")
except ZeroDivisionError:
    print("You can't divide by zero!")
else:
    convertedTemp = tempConverter(userTemp)
finally:
    print("Thanks for using the temperature converter application! :)")
    
