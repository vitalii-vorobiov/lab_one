def Heron_area(a,b,c):
    """
    Function which counts area of triangle 
    using Heron's formula
    (float,float,float) -> float
    """
    import math
    p = (a + b + c)/2
    area = math.sqrt(p*(p-a)*(p-b)*(p-c))
    return area
def read_input():
    """
    Function to read input
    retuns three sides and accuracy
    () -> (float,float,float,float)

    """
    try:
        a = float(input("Enter triangle bottom side "))
        b = float(input("Enter other sides lenght "))
        c = b
        e = float(input("Enter accuracy "))
        assert (a>0) and (b>0) and (c>0) and (e>0)
    except ValueError or AssertionError:
        print("Invalid values")
    return a,b,c,e
def check_triangle(a,b,c):
    """
    Function to check if triangle exist
    (float,float,float) -> boolean
    """
    if (a + b < c) or (b + c < a) or (c + a < b):
        return False
    return True
def found(a,b,c,x,e):
    """
    Function which check if we found right value.
    Request three sides,square side and epsilon
    (float,float,float,float,float) -> string
    """
    import math
    #formula to count sum of all areas
    sum_of_areas = x*x + x*(a-x)/2 + x*(math.sqrt(b**2 - (a**2)/4) - x)/2
    if abs(Heron_area(a,b,c) - sum_of_areas) <= e:
        return "ok"
    elif Heron_area(a,b,c) > sum_of_areas + e:
        return "smaller"
    else:
        return "bigger"
def main():
    """
    Main function where binar search works
    """
    a,b,c,e = read_input()
    if check_triangle(a,b,c):
        left = 0
        right = a
        while True:
            x = (left + right)/2
            if found(a,b,c,x,e) == 'ok':
                break
            elif found(a,b,c,x,e) == "smaller":
                left = x
            else:
                right = x
        print(x)
main()
