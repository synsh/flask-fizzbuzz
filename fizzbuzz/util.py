
def fizzbuzzer(limit: int, int1: int, int2: int, str1: str, str2: str) -> str:
    """
    Args:
        limit:  int
        int1:   int
        int2:   int
        str1:   str
        str2:   str    
    """
    if type(limit) != int or int1 < 1:
        raise TypeError('limit must be an integer greater than one')

    if type(int1) != int or int1 < 1:
        raise TypeError('int1 must be an integer greater than one')

    if type(int2) != int or int1 < 1:
        raise TypeError('int2 must be an integer greater than one')

    result = []

    for n in range(1, limit+1):
        if n % int1 == 0 and n % int2 == 0:
            result.append(f'{str1}{str2}')
        elif n % int1 == 0:
            result.append(str1)
        elif n % int2 == 0:
            result.append(str2)
        else:
            result.append(str(n))

    return ','.join(result)

