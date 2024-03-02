def main(a):
    """
    Given integer a,  check the following statement "The integer is a five-digit number".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    x=a//10000
    y=a//1000
    z=a//100
    d=a//10
    b=a//1
    return x<y<z<d<b
print(main(12645)) 