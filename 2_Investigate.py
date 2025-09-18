# PRIMM: Investigate Activity
#
# Instructions: Now, let's investigate the code from the first Predict activity.
# Run this file and then answer the questions in the comments below.

# Variables for calculation
num_items = 15
price_per_item = 4.50
shipping_cost = 10

# Calculate the results
result_1 = num_items * price_per_item + shipping_cost
result_2 = num_items * (price_per_item + shipping_cost)

print(f"Result 1 is: {result_1}, Type: {type(result_1)}")
print(f"Result 2 is: {result_2}, Type: {type(result_2)}")


# --- Answer the following questions ---
#
# 1.  In the calculation for `result_1`, which operation happens first:
#     the multiplication (`*`) or the addition (`+`)? Why does Python
#     choose this order? (This is called "operator precedence").
#
#     Your Answer:
#
# 2.  What is the data type of `result_1`? Why is it that type, even though
#     `num_items` and `shipping_cost` are integers?
#
#     Your Answer:
#
# 3.  How do the parentheses `()` in the calculation for `result_2` change
#     the order of operations compared to `result_1`?
#
#     Your Answer:


# PRIMM: Investigate Activity
#
# Instructions: Let's investigate a program that calculates the area of a circle.
# Run this file and then answer the questions in the comments below.

import math

radius = 7
area = math.pi * radius ** 2

print(f"The area of a circle with radius {radius} is {area}")


# --- Answer the following questions ---
#
# 1.  What does the `import math` line do? What do you predict would happen
#     if you deleted that line and tried to run the code?
#
#     Your Answer:
#
# 2.  What is `math.pi`? Based on how it's used, do you think it is a
#     function or a variable defined inside the `math` module?
#
#     Your Answer:
#
# 3.  In the expression `math.pi * radius ** 2`, which operation happens first:
#     the multiplication (`*`) or the exponentiation (`**`)? How could you confirm this?
#
#     Your Answer:
