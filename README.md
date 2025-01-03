# Uncommon Python Bug: Silent Failure on Non-Numeric Input

This repository demonstrates a subtle bug in a Python function designed to calculate the average of a list of numbers. While the function correctly handles empty lists, it silently fails when provided with non-numeric input, leading to unexpected results and making debugging more challenging.

## Bug Description:
The `calculate_average` function uses the `sum()` function which will implicitly try to convert non-numeric input to numbers. If this fails, it will throw an error, however the type error could be very difficult to track down since the call looks perfectly valid.

## Solution:
The improved version includes explicit type checking to ensure all inputs are numbers, thus preventing silent failures and improving the robustness of the function.  It raises a `TypeError` for non-numeric inputs, offering more informative error handling.
