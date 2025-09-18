# PRIMM: Make Activity (Graded Assignment)
#
# ## Title: Tip Calculator
#
# Problem Description:
# Your task is to create a simple, friendly tip calculator. The program will ask
# the user for a few pieces of information and then calculate how much each person
# in a group should pay.
#
# Program Requirements:
#
# 1.  Welcome the user with a friendly message.
# 2.  Ask the user for the following inputs:
#     * The total bill amount (e.g., `124.56`).
#     * The percentage of tip they would like to give (e.g., `15` for 15%).
#     * The number of people who are splitting the bill (e.g., `5`).
# 3.  Calculate the following values:
#     * The total tip amount.
#     * The total bill including the tip.
#     * The amount that each person should pay.
# 4.  Display the results to the user in a clear and easy-to-read format.
#     Make sure to format the currency to two decimal places.
#
# Example Input/Output:
#
# Welcome to the tip calculator!
# What was the total bill? $124.56
# What percentage tip would you like to give? 15
# How many people to split the bill? 5
#
# Each person should pay: $28.65
#
#
# Hints:
#
# * Remember that the `input()` function returns a string. You will need to
#   convert these inputs into numbers (`float` or `int`) to do the calculations.
# * To calculate the tip, you'll need to convert the percentage (like 15)
#   into a decimal (0.15). You can do this by dividing the percentage by 100.
# * An f-string is a great way to format your final output to show exactly
#   two decimal places. For example: `f"{your_variable:.2f}"`.
#
# Stretch Goals (Optional):
#
# * Can you make the calculator handle a tip percentage with decimals, like `18.5`?
# * What happens if the user enters `0` for the number of people? How might you handle that?

# --- Write Your Code Below ---
