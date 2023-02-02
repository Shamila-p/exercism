def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number<=0:
        raise ValueError("Classification is only possible for positive integers.")
    else:
        sum=aliquot_sum(number)
        if sum==number:
            return f'perfect'
        if sum>number:
            return f'abundant'
        if sum<number:
            return f'deficient'
            
def aliquot_sum(number):
    sum=0
    for i in range(1,number):
        if number%i==0:
            sum=sum+i
    return sum