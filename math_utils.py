def add(a, b):
    """Повертає суму двох чисел"""
    return a + b

def subtract(a, b):
    """Повертає різницю двох чисел"""
    return a - b

def divide(a, b):
    """Ділення з перевіркою ділення на нуль"""
    if b == 0:
        raise ValueError("Ділення на нуль заборонено")
    return a / b
