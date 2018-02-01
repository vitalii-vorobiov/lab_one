def circle_len(R):
    """
    Function which count lenght of circle
    (float) -> float
    """
    import math
    return 2*math.pi*R
def circle_square(R):
    """
    Function which count area of circle
    (float) -> float
    """
    import math
    return math.pi*R*R
def value_input():
    """
    Function which get input and check it.
    It will return False if value is not correct
    () -> (float,list,float)
    """
    try:
        n = int(input("Number of triples "))
        R = float(input("Radius of circle "))
        eps = float(input("Epsilon for counts "))
    except ValueError as error:
        print("Please,input correct value")
        return False
    chocolate_list = []
    for i in range(n):
        try:
            chocolate_i = [int(x) for x in input().split()]
            chocolate_list.append(chocolate_i)
        except ValueError:
            return False
    return R,chocolate_list,eps
def check(R,chocolate,eps):
    """
    Function which check if lenght of ribbon is 
    enough and area of box is enough.
    (float,list,float) -> boolean
    """
    if chocolate[0] < 1.17*circle_len(R) + eps:
        return False
    elif (chocolate[1] > circle_square(R) + eps) and\
         (chocolate[2] > circle_square(R) + eps):
        return False
    else:
        return True
def write_to_file(chocolate):
    """
    Function which write to file
    (list) -> None
    """
    f = open('chocolate.txt','a')
    f.write(str(chocolate[0])+' '+str(chocolate[1])+' '\
            +str(chocolate[2])+'\n')
    f.close()
def main_function():
    """
    Main function
    () -> None
    """
    try:
        R,chocolate_list,eps = value_input()
    except TypeError:
        return None
    for chocolate in chocolate_list:
        if check(R,chocolate,eps):
            write_to_file(chocolate)
main_function()

