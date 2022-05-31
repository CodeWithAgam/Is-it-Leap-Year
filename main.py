# Created by Agamdeep Singh / CodeWithAgam
# Youtube: CodeWithAgam
# Github: CodeWithAgam
# Instagram: @coderagam001 / @codewithagam
# Twitter: @CoderAgam001
# Linkdin: Agamdeep Singh

# Print a welcome message

# Get the year from the user
year = int(input("Which year do you want to check? "))

# Check for the conditions
# The Modulo Sign (%) calculates remainder after division of 2 numbers.
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")

else:
    print("Not leap year.") 