def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    if b == 0:
        raise ValueError("Denominator cannot be zero.")

    return a / b
print("Calculator functions are ready to use.")
def add(a, b):
    """Returns the sum of a and b."""
    return a + b

def subtract(a, b):
    """Returns the difference of a and b."""
    return a - b

def multiply(a, b):
    """Returns the product of a and b."""
    return a * b

def divide(a, b):
    """Returns the quotient of a and b."""
    if b == 0:
        raise ValueError("Denominator cannot be zero.")
    return a / b

    def greet():
    return "Hello from the greeting module!"