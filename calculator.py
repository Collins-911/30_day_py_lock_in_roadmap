def add(a,b):
    try:
        return float(a) + float(b)
    except ValueError:
        return None
def subtract(a,b):
    try:
        return float(a) - float(b)
    except ValueError:
        return None
def multiply(a,b):
    try:
        return float(a) * float(b)
    except ValueError:
        return None
def divide(a,b):
    try:
        return float(a) / float(b)
    except ValueError:
        return None
    except ZeroDivisionError:
        return None


