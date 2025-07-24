def string_reverse(s):
    """
    Task 1
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
    """
    if not isinstance(s, str):
        return None
    return s[::-1]

# Task 2
# Invoke the function "string_reverse" using the following scenarios:
result1 = string_reverse("Hello World")  # This will return "dlroW olleH"
result2 = string_reverse("Python")       # This will return "nohtyP"
