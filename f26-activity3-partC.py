# Complete the TODOs using the Python concepts introduced in class.
# Run this file to check your result.

# DG8002 - F26 - Activity 3
# Author Name: Erfan Sheikh Sajadieh
# Date: September 30, 2026

# SCENARIO
# A group is splitting a restaurant bill, including a tip.
# For this exercise, use these starting values:
# Meal cost (before tip): $80.00
# Tip rate: 18% (store this as 0.18)
# Number of people: 4
# Ignore taxes for this simplified calculation.

# TODO 1: Create variables for the meal cost, tip rate, and number of people.
meal_cost = 80.00
tip_rate = 0.18
number_of_people = 4

# TODO 2: Calculate the dollar amount of the tip.
tip_amount = meal_cost * tip_rate

# TODO 3: Calculate the total bill, including the tip.
total_bill = meal_cost + tip_amount

# TODO 4: Use an if/else statement to check whether the number of people
# is greater than zero.
#   - If it is, calculate the cost per person and print the tip amount,
#     total bill, and cost per person.
#   - Otherwise, print a helpful message explaining why the bill
#     cannot be split.
if number_of_people > 0:
    cost_per_person = total_bill / number_of_people
    print("Tip amount (CAD):", tip_amount)
    print("Total bill (CAD):", total_bill)
    print("Cost per person (CAD):", cost_per_person)
else:
    print("The bill cannot be split because the number of people must be greater than zero.")

# CHECK YOUR WORK
# With the starting values above:
# Tip: $14.40
# Total: $94.40
# Per person: $23.60
# Test again with zero people. Your program should not divide by zero.
