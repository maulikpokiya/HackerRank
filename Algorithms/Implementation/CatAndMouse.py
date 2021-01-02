# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    a = abs(x-z)
    b = abs(y-z)
    if a == b:
        return 'Mouse C'
    elif a < b:
        return 'Cat A'
    else:
        return 'Cat B' 
