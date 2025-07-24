def check_divisibility(num, divisor):
    """
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """
    if not isinstance(num, (int, float)) or not isinstance(divisor, (int, float)):
        return None
    return num % divisor == 0

# Task 2
# Invoke the function "check_divisibility" using the following scenarios:
result1 = check_divisibility(10, 2)  # This will return True
result2 = check_divisibility(7, 3)   # This will return False
