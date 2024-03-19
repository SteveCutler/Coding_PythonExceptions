# Objective: The aim of this assignment is to create a program that adjusts 
# the quantities of a recipe based on the number of servings, handling any 
# type of arithmetic errors or user input exceptions.

# Task 1: Start
# Ask the user for the number of servings the recipe is originally for and 
# the number of servings they wish to make.

# Ensure that the user inputs are valid numbers and handle any ValueError 
# that arises from improper input.

try:
    originalServings = int(input("How many servings does this recipe make?"))
except ValueError:
    print("Please make sure you enter a valid integer!")
except ZeroDivisionError:
    print("You cannot divide by zero!")
else:
    print(f"Great, the recipe makes {originalServings} servings!")

try:
    userServings = int(input("How many servings are you looking to make with this recipe?"))
except ValueError:
    print("Please make sure you enter a valid integer!")
else:
    print(f"Great, you want to make {userServings} servings!")



# Task 2: Quantity Calculation
# Calculate the adjustment factor by dividing the desired servings by the original servings.

# Use a try block to catch any arithmetic errors that may occur during the calculation.
    


# Task 3: Serving Success
# If the calculation is successful, display the adjusted recipe quantities to the user.

# Use a finally block to print a message encouraging the user to enjoy their 
# cooking, regardless of the outcome of the calculation.
    
try:
    adjustmentFactor = userServings/originalServings
except ZeroDivisionError:
    print("You can't make zero servings! Please enter a real number.")
except OverflowError:
    print("Please enter a realistic number!")
else:
    print(f"Great! You need to adjust the recipe by a factor of: {adjustmentFactor}")
finally:
    print("Thanks for using the recipe factor calculation app! :)")
